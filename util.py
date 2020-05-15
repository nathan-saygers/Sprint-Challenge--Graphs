class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = [
                {'n': '?', 's': '?', 'w': '?', 'e': '?'}, set(), vertex_id]

    def add_edge(self, v1, v2):
        if v2 not in self.vertices[v1][1]:
            if v1 in self.vertices and v2 in self.vertices:
                self.vertices[v1][1].add(v2)
            else:
                raise IndexError("Vertex does not exist in graph")

    def get_adjacent_vertices(self, vertex_id):
        return self.vertices[vertex_id][1]

    def bfs(self, starting_vertex_id):
        # Breadth first traversal
        q = Queue()
        q.enqueue(self.vertices[starting_vertex_id])
        print('haaalllp', self.vertices[starting_vertex_id])

        # Keep track of visited nodes
        visited = set()

        # Repeat until queue is empty
        while q.size() > 0:
            # Dqueue first vert
            current_vertex = q.dequeue()

            # If it's not been visited
            if current_vertex[2] not in visited:
                # Mark visited
                visited.add(current_vertex[2])
                print("visited", visited)
                # Queue up the neighbors of the dequeued / visited vertex
                print("yo", '?' in current_vertex[0].values())
                if '?' in current_vertex[0].values():
                    break
                print(current_vertex[0].values())
                for next_vert in self.get_adjacent_vertices(current_vertex[2]):
                    q.enqueue(next_vert)
        return list(visited)
