from __future__ import annotations

from collections.abc import Iterable, Sequence
from typing import TYPE_CHECKING

from pygame.typing import Point

from .enums import Layer, RenderLayers
from .entity import Entity
from .renderable import Renderable
from .surface_sector import SurfaceSector

import pygame
from pygame import Vector2

if TYPE_CHECKING:
    from . import Container, HasPosition


class CameraBase:
    """
    Defines the important attributes of a camera for the sake of drawing onto its
    surface.

    Can be constructed from the window.
    """

    def __init__(
        self,
        surface: pygame.Surface,
        layer_mask: tuple[Layer] = None,
    ) -> None:
        self.surface = surface
        if layer_mask is None:
            layer_mask = ()
        self.layer_mask = layer_mask

    def clear(self):
        """
        Overwrite the surface to allow new drawing on top.
        Default fill is solid black.
        """
        self.surface.fill((0, 0, 0, 0))

    def cull(self, items: Iterable[Renderable]) -> Iterable[Renderable]:
        """
        Removes any renderables that do not fall within view of the camera.

        :param items: Any iterable containing the renderable to be culled.
        :return: A generator containing only renderables in view of the camera's
        viewport.
        """
        return (item for item in items if self._in_view(item.get_rect()))

    def _in_view(self, rect: pygame.Rect) -> bool:
        return self.surface.get_rect().colliderect(rect)

    def to_local(self, point: pygame.typing.Point) -> Vector2:
        """
        Converts a point in world space to local space (The camera'ssurface)

        :param point: A point, in world space
        :return: The local space equivalent of _point_
        """
        return Vector2(point)

    def to_world(self, point: pygame.typing.Point) -> Vector2:
        """
        Converts a point in local space (The camera's surface) to world space.

        :param point: A point, in local space
        :return: The world space equivalent of _point_
        """

        return Vector2(point)

    def screen_to_world(self, point: Point, sector_index: int = 0) -> Vector2:

        return Vector2(point)

    def screen_to_world_clamped(
        self, point: Point, sector_index: int = 0
    ) -> Vector2 | None:

        return Vector2(point)


class Camera(CameraBase, Renderable):
    """
    Basic form of a camera that is capable of rendering to the screen.
    """

    def __init__(
        self,
        max_size: pygame.typing.Point,
        position: pygame.typing.Point = None,
        surface_sectors: SurfaceSector | Sequence[SurfaceSector] = None,
        viewport: pygame.Rect = None,
        layer_mask: tuple[Layer] = None,
        container: Container = None,
        enabled=True,
        draw_index: int = 0,
    ) -> None:
        """
        Basic form of a camera that is capable of rendering to the screen.

        :param max_size: Largest, most zoomed out size of the camera.
        :param position: Position of the center of the camera surface, defaults to None
        None will give the center of the viewport.
        :param surface_sectors: Defines sections of the screen to render to. If multiple
        surface sectors are used, the camera will be rendered and scaled to each of
        them.
        :param viewport: A rectangle representing the actual viewable area of the
        camera, defaults to None.
        None will give the center of the viewport.
        :param layer_mask: Layers that the camera will exclude from rendering,
        defaults to None
        :param container: The instance of the game to which the rengerable belongs,
        defaults to None. See Renderable.
        :param enabled: Whether the Renderable will be drawn to the screen,
        defaults to True
        :param draw_index: Index determining draw order within a layer, defaults to 0
        """
        self.max_size = Vector2(max_size)
        surface = pygame.Surface(self.max_size)
        if viewport is None:
            viewport = surface.get_rect()
        self.viewport = viewport
        """
        A rectangle representing the actual viewable area of the camera
        """
        if position is None:
            position = self.viewport.center
        self.position = Vector2(position)
        if surface_sectors is None:
            surface_sectors = [SurfaceSector()]
        if not isinstance(surface_sectors, Sequence):
            surface_sectors = [surface_sectors]
        self.surface_sectors: Sequence[SurfaceSector] = surface_sectors
        self._zoom_level: float = 1
        CameraBase.__init__(self, surface=surface, layer_mask=layer_mask)
        Renderable.__init__(
            self,
            container=container,
            enabled=enabled,
            layer=RenderLayers.CAMERA,
            draw_index=draw_index,
        )

    def clear(self):
        """
        Overwrite the surface to allow new drawing on top.
        Basic camera fills with transparent black.
        """
        self.surface.fill((0, 0, 0, 255))

    def _in_view(self, rect: pygame.Rect) -> bool:
        return self.get_viewport_rect().colliderect(rect)

    def get_surface_rect(self) -> pygame.Rect:
        """
        Gets the rect of the camera's surface, in worldspace, centered on the position.

        :return: A Rectangle matching the size of the camera surface, in worldspace.
        """
        return self.surface.get_rect(center=self.position)

    def get_viewport_rect(self) -> pygame.Rect:
        """
        Gives the viewport converted to worldspace.

        :return: A Rectangle matching the size of the viewport, with worldspace
        coordinates.
        """
        return pygame.Rect(
            self.to_world(self.viewport.topleft),
            self.viewport.size,
        )

    def get_rect(self) -> pygame.Rect:
        return self.viewport.move_to(topleft=(0, 0))

    def render(self, delta_time: float) -> pygame.Surface:
        return self.surface.subsurface(self.viewport)

    def to_local(self, point: pygame.typing.Point) -> Vector2:
        point = Vector2(point)

        return point - Vector2(self.get_surface_rect().topleft)

    def to_world(self, point: pygame.typing.Point) -> Vector2:
        point = Vector2(point)

        return point + Vector2(self.get_surface_rect().topleft)

    def screen_to_world(self, point: Point, sector_index: int = 0) -> Vector2:
        """
        Converts a screen coordinate into world coordinates.
        If the screen coordinate is outside the surface sector, it will extrapolate to
        find the equivalent space.

        :param point: A location in screen space, usually pygame.mouse.get_pos()
        :param sector_index: Index of the sector to compare against, defaults to 0.
        :raises IndexError: If the sector_index is larger than the camera's
        number of sectors.
        :return: The screen position, in world space relative to the camera
        """
        sector = self.surface_sectors[sector_index]
        sector_rect = self._get_sector_rect(sector)

        viewport_world = self.get_viewport_rect()

        viewport_space_position = self._screen_to_viewport(
            point, sector_rect, Vector2(viewport_world.size)
        )

        return viewport_space_position.elementwise() + viewport_world.topleft

    def screen_to_world_clamped(
        self, point: Point, sector_index: int = 0
    ) -> Vector2 | None:
        """
        Variant of screen_to_world.
        Converts a screen coordinate into world coordinates.
        If the screen coordinate is outside the surface sector, it will instead return
        None.

        Use this when it needs to be clear that the mouse is outside the camera
        view.

        :param point: A location in screen space, usually pygame.mouse.get_pos()
        :param sector_index: Index of the sector to compare against, defaults to 0.
        :raises IndexError: If the sector_index is larger than the camera's
        number of sectors.
        :return: The screen position, in world space relative to the camera
        """
        sector = self.surface_sectors[sector_index]
        sector_rect = self._get_sector_rect(sector)

        if not sector_rect.collidepoint(point):
            return None

        viewport_world = self.get_viewport_rect()

        viewport_space_position = self._screen_to_viewport(
            point, sector_rect, Vector2(viewport_world.size)
        )

        return viewport_space_position.elementwise() + viewport_world.topleft

    def _screen_to_viewport(
        self, point: Point, sector_rect: pygame.Rect, viewport_size: Vector2
    ) -> Vector2:
        relative_pos = pygame.Vector2(point) - pygame.Vector2(sector_rect.topleft)
        scale_x, scale_y = (
            pygame.Vector2(sector_rect.size).elementwise() / viewport_size
        )
        viewport_space_position: pygame.Vector2 = relative_pos.elementwise() / (
            scale_x,
            scale_y,
        )
        return viewport_space_position

    def _get_sector_rect(self, sector: SurfaceSector) -> pygame.Rect:
        return sector.get_rect(pygame.display.get_surface())

    def zoom(self, zoom_level: float):
        """
        Adjusts the viewport size to match the zoom level.
        Viewport size is scaled in terms of max_size/zoom_level,
        so overall size is 1/zoom_level^2.
        (i.e. zoom_level 2 means half width and half height, 1/4 overall size)

        If the viewport is off center, and the new zoom size would push the viewport
        out of bounds, the viewport is adjusted to fit in the surface. Full zoom out
        will center the viewport.

        :param zoom_level: Integer value indicating zoom level
        :raises ValueError: Raised if zoom level is greater than one
        """
        if zoom_level < 1:
            raise ValueError("Cannot zoom out beyond zoom_level 1")
        self._zoom_level = zoom_level

        center = self.viewport.center

        # Race condition (possibly?) means we can't assign to viewport directly without
        # a potential crash from pushing viewport out of bounds
        # So, we create a new rect to calculate with and assign it to viewport later.
        # This ensures a valid subsurface can always be taken from viewport
        new_view = pygame.Rect(self.viewport)
        new_view.size = self.max_size / zoom_level
        new_view.center = center

        top = new_view.top
        left = new_view.left

        # Clamp viewport to stay in bounds
        new_view.top = max(0, min(top, new_view.height + top))
        new_view.left = max(0, min(left, new_view.width + left))

        # Overwrite the viewport with the new (valid) rect
        self.viewport = new_view


class ChaseCamera(Camera, Entity):
    """
    A camera sub-type that can chase a target with a controllable easing factor and
    maximum distance.
    """

    def __init__(
        self,
        max_size: pygame.typing.Point,
        position: pygame.typing.Point = None,
        container=None,
        surface_sectors: SurfaceSector | Sequence[SurfaceSector] = None,
        enabled=True,
        draw_index=0,
        target: HasPosition = None,
        ease_factor: float = 8.0,
        max_distance: float = -1,
        relative_lag: bool = False,
    ) -> None:
        """
        A camera that is capable of chasing a target.

        :param max_size: Largest, most zoomed out size of the camera.
        :param position: Position of the center of the camera surface, defaults to None
        None will give the center of the viewport.
        :param surface_sectors: Defines sections of the screen to render to. If multiple
        surface sectors are used, the camera will be rendered and scaled to each of
        them.
        :param viewport: A rectangle representing the actual viewable area of the
        camera, defaults to None.
        None will give the center of the viewport.
        :param layer_mask: Layers that the camera will exclude from rendering,
        defaults to None
        :param container: The instance of the game to which the rengerable belongs,
        defaults to None. See Renderable.
        :param enabled: Whether the Renderable will be drawn to the screen,
        defaults to True
        :param draw_index: Index determining draw order within a layer, defaults to 0
        :param target: Object with a position to chase.
        :param ease_factor: Determines the rate at which the camera pursues the target.
        Larger = slower.
        :param max_distance: Maximum distance, in world space, that the target may be
        from the camera. Camera will "speed up" to maintain this distance.
        Negative numbers will disable.
        :param relative_lag: Bool determining if the max distance is relative to zoom
        level. If true, the max distance will be consistent within screen space.
        """
        if target and position is None:
            position = target.position
        Camera.__init__(
            self,
            max_size=max_size,
            position=position,
            surface_sectors=surface_sectors,
            container=container,
            enabled=enabled,
            draw_index=draw_index,
        )
        self.target = target
        self.ease_factor = ease_factor
        self.max_distance = max_distance
        """
        Maximum distance the camera may be from the target.
        Negative numbers will disable.
        """
        self.clamp_magnitude = (
            self._clamp_magnitude_invariant
            if not relative_lag
            else self._clamp_magnitude_scaled
        )

    def post_update(self, delta_time: float) -> None:
        if not self.target:
            return
        delta = self.calculate_ease(self.position - self.target.position, delta_time)
        if self.max_distance >= 0:
            delta = self.clamp_magnitude(delta)
        self.position: Vector2 = self.target.position + delta

    def calculate_ease(self, delta: Vector2, delta_time: float) -> Vector2:
        distance = delta.magnitude()
        if distance == 0:
            return delta
        delta_normalized = delta.normalize()
        distance_adjustment = distance / self.ease_factor
        distance_adjustment *= 60 * delta_time
        distance -= distance_adjustment

        return delta_normalized * distance

    def clamp_magnitude(self, delta: Vector2) -> Vector2:
        pass

    def _clamp_magnitude_invariant(self, delta: Vector2) -> Vector2:
        return delta.clamp_magnitude(0, self.max_distance)

    def _clamp_magnitude_scaled(self, delta: Vector2) -> Vector2:
        return delta.clamp_magnitude(0, self.max_distance / self._zoom_level)
