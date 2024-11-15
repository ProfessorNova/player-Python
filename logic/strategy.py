from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction


def decide(gameState: GameState) -> List[PlayerAction]:

    print(gameState)

    return [PlayerAction(0, 0, 0)]
