from typing import Dict
from datetime import datetime

from src.config import Config
from src.game import Game

games: Dict[Game] = dict()


def handle_connection(connection, address):
    pass


def garbage_collect_games(hard=False):
    """
    Looks through and deletes stale games from the games dict based on HARD limits
    If the game is older than TTL seconds, delete
    If the game hasn't been interacted with for TIMEOUT seconds, delete
    :param hard: Also delete games based on the SOFT limit, used when the games dict is full and space is needed
    :return: Amount of games that were deleted
    """
    games_to_delete = list()
    now = datetime.now()
    for key in games:
        game = games[key]
        game_age = (now - game.created_time).total_seconds()
        game_interact_age = (now - game.created_time).total_seconds()
        if game_age > Config.GAME_TTL_HARD or game_interact_age > Config.GAME_TIMEOUT_HARD:
            games_to_delete.append(key)
            continue
        if hard and (game_age > Config.GAME_TTL_SOFT or game_interact_age > Config.GAME_TIMEOUT_SOFT):
            games_to_delete.append(key)
    for key in games_to_delete:
        del games[key]
    return len(games_to_delete)
