from __future__ import annotations

from dataclasses import dataclass

import pygame


@dataclass
class GameData:
    """
    A collection of data about a game.
    """

    title: str = "Game"
    """
    The title of the game.
    """
    caption: str = None
    """
    Text displayed by the title bar. Defaults to the game's title.
    """
    icon: pygame.Surface | None = None
    """
    Icon displayed in the title bar. 'None' uses the default pygame icon. Changes will
    only go into effect when the window is recreated.
    """

    @staticmethod
    def get_game_data(**kwds) -> GameData:
        """
        Creates a GameData object from external arguments.
        Used for generating game data from arguments passed into Game init.
        """
        metadata: GameData | None = kwds.get("game_data", None)
        if metadata is None:
            # If no metadata object is supplied, create one.
            keys: set = {"title", "caption", "icon"}
            params: dict = {key: kwds[key] for key in keys if key in kwds}
            metadata = GameData(**params)
        return metadata
