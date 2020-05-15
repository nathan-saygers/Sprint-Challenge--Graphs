"""
Strategies when reaching dead end:
    - bfs to find ?s
    - keep track of current path and back track checking each room for ?s
    - recursion does this automatically (but you need to track your backtracks)

DFT and tracking backtrack should be enough to get MVP

runtime is irrelevan

"""

test = {0: {'n': 2, 's': '?', 'w': '?', 'e': '?'}}

print(test[0]['n'])
