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
    map_graph.add_vertex(player.current_room.id)
    # check to see which directions the player can move (get_exits returns an array of available exits)
    exits = player.current_room.get_exits()
    # choose a random direction from the exits
    direction = random.choice(exits)
    # save current room as previous room
    prev_room_id = player.current_room.id
    # move the player into an available room (add the direction to the tracking list)
    player.travel(direction)
    # update the path with the direction traveled
    path.append(direction)
    # update the current room's vertex value
    map_graph.vertices[prev_room_id][0][direction] = player.current_room.id
    print('Graph:', map_graph.vertices, 'Path:', path,
          'Current Room:', player.current_room)

    ####### DEPTH FIRST TRAVERSE #######
    while len(exits) > 1:
        # Add current room to graph
        map_graph.add_vertex(player.current_room.id)
        # Create edge
        map_graph.add_edge(player.current_room.id, prev_room_id)
        # update current room's vertex value with previous direction
        map_graph.vertices[player.current_room.id][0][opposite[direction]
                                                      ] = prev_room_id
        # check to see which directions the player can move (get_exits returns an array of available exits)
        exits = player.current_room.get_exits()
        # choose a random direction from the exits
        direction = random.choice(exits)
        # save current room as previous room
        prev_room_id = player.current_room.id
        # move the player into an available room (add the direction to the tracking list)
        player.travel(direction)
        # update the path with the direction traveled
        path.append(direction)
        print('Graph:', map_graph.vertices, 'Path:', path,
              'Current Room:', player.current_room)

    return path
