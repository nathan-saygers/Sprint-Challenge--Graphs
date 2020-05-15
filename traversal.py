"""
Traversal for simple (cross) map
"""

from room import Room
from player import Player
from util import Graph, Queue, Stack
import random

# PSR == player start room


def cross_traverse(player):
    # instantiate a graph, to track rooms
    map_graph = Graph()
    # instantiate a list, to track movement
    path = []
    # instantiate opposites dictionary
    opposite = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

    ####### FIRST ROOM #######
    # Add the starting room to the graph.  Vertexes will have the room number as their id
    # directional object as value
    # check to see which directions the player can move (get_exits returns an array of available exits
    # choose a random direction from the exits
    # save current room as previous room
    # move the player into an available room (add the direction to the tracking list)
    # update the path with the direction traveled
    # update the current room's vertex value

    ####### DEPTH FIRST TRAVERSE #######
    # while length of verteces is less than 500
    # Add current room to graph
    # Create edge
    # update current room's vertex value with previous direction
    # check to see which directions the player can move (get_exits returns an array of available exits)
    # choose a random direction from the exits
    # save current room as previous room
    # move the player into an available room (add the direction to the tracking list)
    # update the path with the direction traveled

    return path
