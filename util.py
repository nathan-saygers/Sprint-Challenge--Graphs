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
        self.vertices[vertex_id] = [
            {'n': '?', 's': '?', 'w': '?', 'e': '?'}, set()]

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1][1].add(v2)
        else:
            raise IndexError("Vertex does not exist in graph")

    def get_parents(self, vertex_id):
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        # Depth first traversal:

        s = Stack()
        s.push(starting_vertex)
        result = []

        # Keep track of visited nodes
        visited = set()

        # Repeat until stack is empty
        while s.size() > 0:
            # Pop first vert
            v = s.pop()

            # If it's not been visisted
            if v not in visited:
                result.append(v)

                # Mark as visited
                visited.add(v)

                # add to the stack the neighbors of the popped vertex
                for next_vert in self.get_parents(v):
                    s.push(next_vert)

        return result
