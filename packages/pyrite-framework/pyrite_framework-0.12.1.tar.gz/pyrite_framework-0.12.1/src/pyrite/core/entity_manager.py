from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from weakref import WeakSet

from ..types.entity import Entity

if TYPE_CHECKING:
    from ..types._base_type import _BaseType

import pygame


class EntityManager(ABC):

    @abstractmethod
    def enable(self, item: _BaseType) -> None:
        """
        Adds an entity to the collection of active entities.

        Does nothing if the passed item is not an Entity.

        :param item: Object being enabled. Objects that are not entities will be
        skipped.
        """
        pass

    @abstractmethod
    def disable(self, item: _BaseType) -> None:
        """
        Removes an entity from the collection of active entities.

        Does nothing if the passed item is not an Entity.

        :param item: Object being enabled. Objects that are not entities will be
        skipped.
        """
        pass

    @abstractmethod
    def flush_buffer(self):
        """
        Used to allow the entity manager to update its entity collection safely,
        without modifying it while iterating over it.

        Called at the beginning of the loop, before event handling.
        """
        pass

    # Update Methods

    @abstractmethod
    def pre_update(self, delta_time: float):
        """
        Runs the pre_update phase for active entities.

        :param delta_time: Time passed since last frame
        """
        pass

    @abstractmethod
    def update(self, delta_time: float):
        """
        Runs the update phase for active entities.

        :param delta_time: Time passed since last frame
        """
        pass

    @abstractmethod
    def post_update(self, delta_time: float):
        """
        Runs the post_update phase for active entities.

        :param delta_time: Time passed since last frame
        """
        pass

    @abstractmethod
    def const_update(self, timestep: float):
        """
        Runs the const_update phase for active entities.

        :param timestep: Length of the simulated step
        """
        pass

    @abstractmethod
    def handle_event(self, event: pygame.Event):
        """
        Passes the event down to all active entities.

        :param event: A pygame event.
        """
        pass

    # Profiling methods

    @abstractmethod
    def get_number_entities(self) -> int:
        """
        Returns the number ot active entities managed by the entity manager.
        """
        pass

    @staticmethod
    def get_entity_manager(**kwds) -> EntityManager:
        """
        Extracts an entity manager from keyword arguments.
        Gives the default entity manager if no entity manager is supplied.

        Used for getting an entity manager for a new game instance
        """
        if (entity_manager := kwds.get("entity_manager", None)) is None:
            manager_type = get_default_entity_manager_type()
            entity_manager = manager_type()
        return entity_manager


class DefaultEntityManager(EntityManager):

    def __init__(self) -> None:
        self.entities: WeakSet[Entity] = WeakSet()
        self._added_buffer: set[Entity] = set()
        self._disabled_buffer: set[Entity] = set()

    def enable(self, item: _BaseType) -> None:
        if isinstance(item, Entity):
            self._added_buffer.add(item)

    def disable(self, item: _BaseType) -> None:
        if isinstance(item, Entity):
            self._disabled_buffer.add(item)

    def flush_buffer(self):
        self.entities |= self._added_buffer

        self.entities -= self._disabled_buffer

        self._added_buffer = set()
        self._disabled_buffer = set()

    def pre_update(self, delta_time: float):
        for entity in self.entities:
            entity.pre_update(delta_time)

    def update(self, delta_time: float):
        for entity in self.entities:
            entity.update(delta_time)

    def post_update(self, delta_time: float):
        for entity in self.entities:
            entity.post_update(delta_time)

    def const_update(self, timestep: float):
        for entity in self.entities:
            entity.const_update(timestep)

    def handle_event(self, event: pygame.Event):
        for entity in self.entities:
            entity.on_event(event)

    def get_number_entities(self) -> int:
        return len(self.entities)


_default_entity_manager_type = DefaultEntityManager


def get_default_entity_manager_type() -> type[EntityManager]:
    return _default_entity_manager_type


def set_default_entity_manager_type(manager_type: type[EntityManager]):
    global _default_entity_manager_type
    _default_entity_manager_type = manager_type
