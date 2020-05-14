"""
Traversal for simple (cross) map
"""

from .room import Room
from .player import Player

# PSR == player start room


def cross_traverse(psr):
    # instantiate a visited dictionary
    visited = {}
    # Mark starting room as visited
    visited[psr.id] = True
    # check to see which directions the player can move (get_exits returns an array of available exits)
    exits = psr.get_exits()
    # move the player into an available room (store the direction you went)
    if 'n' in exits:
        player.travel('n')
        prev_dir = 'n'
    elif 's' in exits:
        player.travel('s')
        prev_dir = 's'
    elif 'e' in exits:
        player.travel('e')
        prev_dir = 'e'
    elif 'w' in exits:
        player.travel('w')
        prev_dir = 'w'

        # WHILE the room you've moved into is not ONLY OPPOSITE the available room
        # check to see which directions the player can move
        # move the player into an available room (store the direction you went)

    pass
