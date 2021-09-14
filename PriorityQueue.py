from sliding3 import Puzzle
import heapq
    

class Node:
    def __init__(self,state, move = None, parent = None):
        self.state = state
        self.parent = parent
        self.direction = move
        if self.parent != None:
            self.g = self.parent.get_state().get_cost() #assume unit cost
        else:
            self.g = 0
        self.f = self.state.get_heuristic() + self.g
        self.node_children = self.state.children()

    def __lt__(self, other):
        if self.f_value() < other.f_value(): 
            return True
        elif self.f_value() == other.f_value() and self.get_heuristic() < other.get_heuristic():
            return True
        else: 
            return False 

    def f_value(self):
        return self.f

    def get_heuristic(self):
        return self.state.get_heuristic()

    def get_parent(self):
        return self.parent 

    def set_state(self,new_state):
        self = new_state
   
    def get_puzzle(self):
        if self.state != None:
            return self.state.get_state()
        else:
            return None

    def get_action(self):
        return self.direction

    def get_state(self):
        if self != None:
            return self.state
        else:
            return None

    def solved_state(self):
        return self.state.solved()

    def moves(self):
        return self.node_children

    def path(self,start):
        reverse_path = []
        current = self
        count = 0
        while current.get_puzzle() != start.get_puzzle():
            reverse_path.append(current.get_action())
            current = current.parent
            count += 1
        reverse_path.reverse()
        return (reverse_path, str(count) + " moves")

class PriorityQueue:
            
    def __init__(self):
        self._P = []
        heapq.heapify(self._P)
        self._n = 0 
        
    def __len__(self):
        return self._n 
    
    def push(self, Node):
        heapq.heappush(self._P, (Node.f_value(),Node,))                 
        self._n += 1
    
    def pop(self):
        poped = heapq.heappop(self._P)
        self._n -= 1
        return poped
        
    def iterate(self):
        for i in self._P:
            yield i

    def __getitem__(self, v):
        return self.P[v]

if __name__ == "__main__":
    my_puzzle = Puzzle((2,1,0,3))
    parent = Puzzle((1,0,2,3))
    solver = Node(my_puzzle)
    solver.path()
    print(solver.moves())
    print(solver.solved())

