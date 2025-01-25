from __future__ import annotations

import asyncio
import logging
from types import TracebackType
from typing import Self, TYPE_CHECKING

from .core.display_settings import DisplaySettings
from .core.entity_manager import EntityManager
from .core.game_data import GameData
from .core.renderer import Renderer, RenderManager
from .core.rate_settings import RateSettings

from ._helper import defaults

if TYPE_CHECKING:
    from .types.entity import Entity
    from .types.renderable import Renderable


import pygame

logger = logging.getLogger(__name__)

_active_instance = None


def get_game_instance() -> Game | None:
    return _active_instance


def set_game_instance(instance: Game):
    global _active_instance
    _active_instance = instance


defaults._default_container_getter = get_game_instance


class Game:
    """
    Base Game object to serve as a parent for your game.
    Holds onto data required for generating the window and performing the main loop.
    Only one game instance may be running at a time. Attempting to start a new instance
    will stop the previous instance.
    """

    def __new__(cls, *args, **kwds) -> Self:
        active_instance = get_game_instance()
        if active_instance is not None:
            active_instance.is_running = False
            logger.info(
                f"Stopping {active_instance}, only one game may be running at a time."
            )
        logger.info("Starting new game instance.")
        active_instance = super().__new__(cls)
        set_game_instance(active_instance)
        return active_instance

    def __init__(self, **kwds) -> None:

        self.container = self  # To satisfy Container protocol

        suppress_init: bool = kwds.get("suppress_init", False)
        self.debug_mode: bool = kwds.get("debug_mode", False)
        self.suppress_context_errors: bool = kwds.get("suppress_context_errors", False)
        """
        Whether errors generated during context manager function should be suppressed.
        """

        if not suppress_init:
            pygame.init()

        self.is_running = True
        self.clock = pygame.time.Clock()

        # Extract various settings and game data from keyword arguments.
        # Creates defaults if none are provided.
        self.display_settings = DisplaySettings.get_display_settings(**kwds)
        self.game_data = GameData.get_game_data(**kwds)
        self.rate_settings = RateSettings.get_rate_settings(**kwds)

        # Entity manager is responsible for holding and updating all entities.
        # Renderer is responsible for holding and drawing all renderables.
        # Both have a default version that will be spawned if none is provided.
        self.entity_manager: EntityManager = EntityManager.get_entity_manager(**kwds)
        self.render_manager = RenderManager.get_render_manager(**kwds)
        self.renderer = Renderer.get_renderer(**kwds)

        # Create a placeholder for the window, and the create the actual window
        self.window: pygame.Surface = None
        self.create_window()

    def __enter__(self) -> Self:
        """
        Basicmost __enter__ implementation.
        """
        return self

    def __exit__(
        self,
        exception_type: type[Exception] | None,
        exception_value: Exception | None,
        traceback: TracebackType | None,
    ):
        """
        Context manager exit. Starts the game when closing, unless an error occurs.
        """
        if exception_value is None or self.suppress_context_errors:
            # suppress_context_errors allows us to start regardless of any errors,
            # and hides them from the output.
            self.main()
        return self.suppress_context_errors

    def enable(self, item: Entity | Renderable) -> None:
        self.entity_manager.enable(item)
        self.render_manager.enable(item)

    def disable(self, item: Entity | Renderable) -> None:
        self.entity_manager.disable(item)
        self.render_manager.disable(item)

    def create_window(self):
        """
        Generates a window from current display settings.
        Updates the icon, if possible.
        The game's window and display settings are updated to reflect the new window.
        """
        if self.game_data.icon is not None:
            pygame.display.set_icon(self.game_data.icon)
        self.window, self.display_settings = DisplaySettings.create_window(
            self.display_settings
        )

    def main(self):
        """
        The main entry point for the game. By default, calls start_game(), but can be
        overridden to have more complex starting logic.

        For example, a function could be called to create a special early loop for
        loading in resources before calling the main game loop.
        """
        self.create_window()
        self.start_game()

    def start_game(self) -> None:
        """
        Begins the main game loop, calling the update methods and the render methods.
        """

        accumulated_time: float = 0.0

        while self.is_running:
            accumulated_time = self._main_loop_body(accumulated_time)

    def _main_loop_body(self, accumulated_time: float) -> float:
        """
        Body of the main loop. Handles the accumulated time used by const_update.

        :param accumulated_time: Time taken since last const_update call
        :return: Residual accumulated_time
        """

        delta_time, accumulated_time = self._get_frame_time(
            self.rate_settings.fps_cap, accumulated_time
        )

        # This will ensure new entities are processed properly for the new frame.
        self.entity_manager.flush_buffer()

        self.process_events(pygame.event.get())

        if self.rate_settings.tick_rate > 0:
            accumulated_time = self._fixed_update_block(
                self.rate_settings.fixed_timestep, accumulated_time
            )

        self._update_block(delta_time)

        if not (caption := self.game_data.caption):
            caption = self.game_data.title
        pygame.display.set_caption(caption)
        self._render_block(self.window, delta_time)

        return accumulated_time

    def _get_frame_time(
        self, fps_cap: int, accumulated_time: float = 0
    ) -> tuple[float, float]:
        """
        Runs the clock delay, returning the passed time and adding it to the
        accumulated time.

        :param fps_cap: Maximum frame rate, 0 is uncapped.
        :param accumulated_time: Time since last const_update, passed from the main loop
        :return: Tuple containing delta_time and the modified accumulated time.
        """
        delta_time = self.clock.tick(fps_cap) / 1000
        accumulated_time += delta_time
        return (delta_time, accumulated_time)

    def pre_update(self, delta_time: float) -> None:
        """
        Early update function. Used for game logic that needs to run _before_ the main
        update phase.

        :param delta_time: Actual time passed since last frame, in seconds.
        """
        pass

    def update(self, delta_time: float) -> None:
        """
        Main update function. Used for coordinating most of the game state changes
        required.

        :param delta_time: Actual time passed since last frame, in seconds.
        """
        pass

    def post_update(self, delta_time: float) -> None:
        """
        Late update function. Used for game logic that needs to run _after_ the main
        update phase.

        :param delta_time: Actual time passed since last frame, in seconds.
        """
        pass

    def const_update(self, timestep: float) -> None:
        """
        Update function that runs at a constant rate. Useful for anything that is
        sensitive to variations in frame time, such as physics.

        This is a basic, naïve implementation of a fixed timestep, and can be a bit
        jittery, especially when the tick rate and frame rate are not multiples of
        eachother.

        For more info, see Glenn Fiedler's "Fix Your Timestep!"

        :param timestep: Simulated time passed since last update. Passed in from the
        game's rate_settings.
        """
        pass

    def _update_block(self, delta_time: float) -> None:
        """
        Calls all of the update phases, in order.

        :param delta_time: Actual time passed since last frame, in seconds.
        """

        self.pre_update(delta_time)
        self.entity_manager.pre_update(delta_time)
        self.update(delta_time)
        self.entity_manager.update(delta_time)
        self.post_update(delta_time)
        self.entity_manager.post_update(delta_time)

    def _fixed_update_block(self, timestep: float, accumulated_time: float) -> float:
        """
        Runs const_update so long as accumulated time is greater than the timestep.

        CAUTION: If const_update takes longer to run than the timestep, your game will
        fall into a death spiral, as each frame takes longer and longer to compute!

        For more info, see Glenn Fiedler's "Fix Your Timestep!"

        :param timestep: Length of the time step, in seconds. Passed from
        rate_settings.
        :param accumulated_time: Time passed since last const_update.
        :return: Remaining accumulated time.
        """
        while accumulated_time > timestep:
            self.const_update(timestep)
            self.entity_manager.const_update(timestep)
            accumulated_time -= timestep
        return accumulated_time

    def render(self, window: pygame.Surface, delta_time: float) -> None:
        """
        Main drawing phase. Used for rendering active game objects to the screen.

        :param window: The main display window.
        :param delta_time: Time passed since last frame, in seconds.
        """
        pass

    def _render_block(self, window: pygame.Surface, delta_time: float) -> None:
        """
        Calls the render functions, and updates the display.

        :param window: The main display window.
        :param delta_time: Time passed since last frame, in seconds.
        """
        # Redundant if no cameras, but cameras could cause this to be needed.
        window.fill(pygame.Color("black"))

        render_queue = self.render_manager.generate_render_queue()
        self.renderer.render(window, delta_time, render_queue)

        self.render(window, delta_time)

        pygame.display.flip()

    def quit(self) -> None:
        """
        Ends the game loop.
        """
        self.is_running = False

    def quit_called(self) -> None:
        """
        Hook for attaching behavior to the pygame.QUIT event. By default, quits the
        game.
        """
        self.quit()

    def process_events(self, events: list[pygame.Event]) -> None:
        """
        Takes the list of events generated, and processes them.
        by default, the events are passed on to handle_event and the entity manager.
        Pygame.QUIT is specifically checked.

        :param events: List of events since last frame.
        """
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_called()

            self.entity_manager.handle_event(event)
            self.handle_event(event)

    def handle_event(self, event: pygame.Event) -> None:
        """
        Method hook for event behavior.

        Recommendation: Use https://pypi.org/project/pygame-simple-events/ for handling
        events (Shameless plug!)

        :param event: Event to be handled.
        """
        pass


class AsyncGame(Game):
    """
    Variant of Game that runs in async mode.
    Supports pygbag.
    """

    async def start_game(self):
        """
        Begins the game loop in async mode.
        Identical to Base game version, except with an asyncio sleep attached for
        thread handoff required for tools like pygbag.
        """

        accumulated_time: float = 0.0

        # Minimum duplication to get desired results.
        while self.is_running:
            accumulated_time = self._main_loop_body(accumulated_time)
            await asyncio.sleep(0)

    def main(self):
        """
        Main entry point for the game. By default, starts a thread from start_game().
        """
        self.create_window()
        asyncio.run(self.start_game())
