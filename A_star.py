from sliding3 import Puzzle
import argparse
from heap import heap

class Node:
    def __init__(self,state, move = None, parent = None):
        self.state = state
        self.parent = parent
        self.direction = move
        self.h = self.state.get_heuristic()
        if(self.parent != None):
            self.g = self.parent.g + 1#assume unit cost
        else:
            self.g = 0

    def __lt__(self, other): #this is less than function
        if self.f_value() < other.f_value(): 
            return True
        elif self.f_value() == other.f_value() and self.get_h() < other.get_h():
            return True
        else: 
            return False 

    def __hash__(self):
        return hash(self.state.get_state())

    def __eq__(self, other):
        return not other is None and self.state.get_state() == other.state.get_state()

    def __repr__(self):
        return str(self.g) + " " + str(self.h) + " " + str(self.f_value()) + " " + str(self.state.get_state())

    def g_value(self):
        return self.g

    def get_h(self):
        return self.h

    def f_value(self):
        return (self.h + self.g) 
   
    def get_puzzle(self):
        return self.state.get_state()

    def get_action(self):
        return self.direction

    def solved_state(self):
        return self.state.solved()

    def moves(self):
        return self.state.children()

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

def A_star_algorithm(state):
    current = Node(state) 
    lst = []
    pq = heap(lst)
    pq.push(current)
    table = {}
    nodes_generated = 1
    nodes_expanded = 0
    duplicates = 0
    table.update({current.get_puzzle():current})
    while pq.is_empty() == False:
        parent = pq.pop()
        table.update({parent.get_puzzle():parent})
        nodes_expanded += 1
        if parent.solved_state() == True:
            return (parent.path(current), "Number of Nodes generated:" + " " +  str(nodes_generated), "Number of Nodes expanded:" + " " + str(nodes_expanded), "Number of Duplicates:" + " " + str(duplicates))              
        for child in parent.moves():
            if child != None:
                child_node = Node(child[0], child[1], parent)
                if child_node.get_puzzle() not in table:
                    if child_node in pq:
                        dup = pq[child_node]
                        duplicates += 1
                        if child_node.g_value() < dup.g_value():
                            pq[child_node] = child_node
                            duplicates += 1
                    else:
                        pq.push(child_node)
                        nodes_generated += 1 

    #Would using f values as the main element in our closed list increase the speed and optimality of our algorithm (The heuristic computation then becomes a table lookup )
    #If we were to add the starting state and it's children to our open list and check the first two states poped from our queue could that possibly double the speed of our time.


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='A star algorithm')
    parser.add_argument('-s','--state', nargs = "+", type=int, help='input state we need', required=True)
    parser.add_argument('-l','--height', type=int, help='height of grid', required=True)
    parser.add_argument('-w','--width', type=int, help='width.grid', required=True)
    args = parser.parse_args()

    my_tuple = tuple(args.state)
    state = Puzzle(args.height,args.width, my_tuple) #85   
    results = A_star_algorithm(state)
    for i in results:
        print(i)
        print("\n")
    """res = A_star_algorithm(state)
    state = Puzzle((14 1 9 6 4 8 12 5 7 2 3 0 10 11 13 15))  #12
    inst = 12
    sol_len = 45
    print("solved "+str(inst)+" "+["incorrectly", "correctly"][res[1] == str(sol_len)+" moves"])
    state = Puzzle((4 5 7 2 9 14 12 13 0 3 6 11 8 1 15 10))  #42
    res = A_star_algorithm(state)
    inst = 42
    sol_len = 42
    print("solved "+str(inst)+" "+["incorrectly", "correctly"][res[1] == str(sol_len)+" moves"])
    state = Puzzle((13 8 14 3 9 1 0 7 15 5 4 10 12 2 6 11))  #55  
    res = A_star_algorithm(state)
    inst = 55
    sol_len = 41
    print("solved "+str(inst)+" "+["incorrectly", "correctly"][res[1] == str(sol_len)+" moves"])
    state = Puzzle((0 1 9 7 11 13 5 3 14 12 4 2 8 6 10 15))   #79
    res = A_star_algorithm(state)
    inst = 79
    sol_len = 42
    print("solved "+str(inst)+" "+["incorrectly", "correctly"][res[1] == str(sol_len)+" moves"])
    state = Puzzle((4 7 13 10 1 2 9 6 12 8 14 5 3 0 11 15)) #85
    res = A_star_algorithm(state)
    inst = 85
    sol_len = 44
    print("solved "+str(inst)+" "+["incorrectly", "correctly"][res[1] == str(sol_len)+" moves"])
    state = Puzzle((12, 3, 9, 1, 4, 5, 10, 2, 6, 11, 15, 0, 14, 7, 13, 8)) #83
    res = A_star_algorithm(state)
    inst = 85
    sol_len = 44
    print("solved "+str(inst)+" "+["incorrectly", "correctly"][res[1] == str(sol_len)+" moves"])"""

    #print(A_star_algorithm(state))
    




    
