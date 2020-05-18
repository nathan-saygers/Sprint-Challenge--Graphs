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
    # update vertex directions with missing exits
    update_vertex_exits(exits, map_graph, player)
    # choose a random direction from the exits
    direction = random.choice(exits)
    # Set player origin based on direction
    player.origin = opposite[direction]
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
    while len(map_graph.vertices) < 500:
        print(len(map_graph.vertices))
        # Add current room to graph
        map_graph.add_vertex(player.current_room.id)
        # Create edge
        map_graph.add_edge(player.current_room.id, prev_room_id)
        # update current room's vertex value with previous direction
        map_graph.vertices[player.current_room.id][0][player.origin] = prev_room_id
        map_graph.vertices[prev_room_id][0][direction] = player.current_room.id
        print('vertex directions after origin set',
              map_graph.vertices[player.current_room.id][0])
        # check to see which directions the player can move (get_exits returns an array of available exits)
        exits = player.current_room.get_exits(player.origin)
        # update vertex directions with missing exits
        update_vertex_exits(exits, map_graph, player)

        if len(exits) == 0:
            path_to_unexplored_room_ids = map_graph.bfs(
                player.current_room.id)
            path_to_unexplored_room = []
            for id in path_to_unexplored_room_ids:
                if map_graph.vertices[player.current_room.id][0]['n'] == id:
                    path_to_unexplored_room.append('n')
                    continue
                elif map_graph.vertices[player.current_room.id][0]['s'] == id:

                    path_to_unexplored_room.append('s')
                    continue
                elif map_graph.vertices[player.current_room.id][0]['e'] == id:

                    path_to_unexplored_room.append('e')
                    continue
                elif map_graph.vertices[player.current_room.id][0]['w'] == id:
                    path_to_unexplored_room.append('w')
                    continue
            for path_direction in path_to_unexplored_room:
                path.append(path_direction)
                player.origin = opposite[path_direction]
                prev_room_id = player.current_room.id
                player.travel(path_direction)

            continue
        # choose a random direction from the exits
        print('ORIGIN', player.origin)

        direction = next_direction(unexplored_exits(
            exits, map_graph.vertices[player.current_room.id][0]), exits, map_graph.vertices[player.current_room.id][0], map_graph)

        # direction = random.choice(exits)

        # save current room as previous room
        prev_room_id = player.current_room.id
        # Set player origin based on direction
        player.origin = opposite[direction]
        # move the player into an available room (add the direction to the tracking list)
        player.travel(direction)
        # update the path with the direction traveled
        path.append(direction)
        # print('Graph:', map_graph.vertices, 'Path:', path,
        #       'Current Room:', player.current_room)

    return path


def update_vertex_exits(exits, graph, player):
    if player.origin != '':
        exits.append(player.origin)
    if 'n' not in exits:
        graph.vertices[player.current_room.id][0]['n'] = None
    if 's' not in exits:
        graph.vertices[player.current_room.id][0]['s'] = None
    if 'e' not in exits:
        graph.vertices[player.current_room.id][0]['e'] = None
    if 'w' not in exits:
        graph.vertices[player.current_room.id][0]['w'] = None
    if player.origin != '':
        exits.remove(player.origin)


def next_direction(unexplored_exits, exits, graph_room, map_graph):
    if len(unexplored_exits) == 0:
        path_arrays = []
        shortest_path = []
        if 'w' in exits:
            path_arrays.append(((map_graph.bfs(
                graph_room['w'])), 'w'))
        if 'n' in exits:
            path_arrays.append(((map_graph.bfs(
                graph_room['n'])), 'n'))
        if 'e' in exits:
            path_arrays.append(((map_graph.bfs(
                graph_room['e'])), 'e'))
        if 's' in exits:
            path_arrays.append(((map_graph.bfs(
                graph_room['s'])), 's'))
        for path_array in path_arrays:
            if len(shortest_path) == 0:
                shortest_path = path_array
            if len(path_array[0]) < len(shortest_path[0]):
                shortest_path = path_array
        return shortest_path[1]
    elif 'w' in unexplored_exits:
        return 'w'
    elif 'n' in unexplored_exits:
        return 'n'
    elif 'e' in unexplored_exits:
        return 'e'
    elif 's' in unexplored_exits:
        return 's'


def unexplored_exits(exits, graph_room):
    print("GRAF ROO", graph_room, "exits", exits)
    unexplored_exits = []
    if 'n' in exits and graph_room['n'] == '?':
        unexplored_exits.append('n')
    if 's' in exits and graph_room['s'] == '?':
        unexplored_exits.append('s')
    if 'e' in exits and graph_room['e'] == '?':
        unexplored_exits.append('e')
    if 'w' in exits and graph_room['w'] == '?':
        unexplored_exits.append('w')
    return unexplored_exits
