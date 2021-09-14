import sys
import math

def swop(state, zero_index, index):
        if zero_index < index:
            swapped = state[:zero_index] + (state[index],) + state[zero_index + 1:index] + (0,) + state[index + 1:]
        else:
            swapped = state[:index] + (0,) + state[index + 1:zero_index] + (state[index],) + state[zero_index + 1:]
        return swapped


class Puzzle:
    
    def __init__(self, width, height, state): 
        self.state = state          
        for i in range(len(state)):
            if state[i] == 0:
                self.source = i
        self._n = len(state)
        self.width = width
        self.height = height
        self.heuristic = 0
        for i in range(self._n):
            row = i//self.width
            goalrow = self.state[i]//self.width
            col = i%self.width
            goalcol = self.state[i]%self.width
            if self.state[i] != 0:
                    self.heuristic += (abs(row - goalrow) + abs(col - goalcol))

    def get_state(self):
        return self.state

    def get_source(self):
        return self.source

    def get_cost(self):
        return self.cost

    def get_heuristic(self):
        return int(self.heuristic)

    def move_up(self):
        if self.source >= self.width:
            child = swop(self.state, self.source, self.source - int(self.width))       
            new_state = Puzzle(self.height, self.width,child) 
            return (new_state, "UP")

    def move_down(self):  
        if (self._n - self.source) > self.width:
            child = swop(self.state, self.source, self.source + int(self.width))
            new_state = Puzzle(self.height, self.width,child) 
            return (new_state, "DOWN")

    def move_right(self):   
        if (self.source + 1) % self.height != 0 or 0 < self.source < self.height - 1:
            child = swop(self.state, self.source, self.source + 1)
            new_state = Puzzle(self.height, self.width,child) 
            return (new_state, "RIGHT")

    def move_left(self):      
        if (self.source % self.height != 0 or  0 < self.source < self.height):
            child = swop(self.state, self.source, self.source - 1)
            new_state = Puzzle(self.height, self.width,child) 
            return (new_state, "LEFT")
    
    def children(self):
        return (self.move_right(), self.move_up(), self.move_down(), self.move_left())

    def print_puzzle(self):
        display = []
        start = 0
        end = int(self.width)
        for i in range(int(self.width)):
            display.append(self.state[start:end])
            start += int(self.width)
            end += int(self.width)
        for j in display:
            print(j)

    def solved(self):
        solved_list = ()
        for i in range(self._n):
            solved_list += (i,)
        if self.state == solved_list:
            return True
        else:
            return False



if __name__ == "__main__":
    #my_puzzle = Puzzle((12,11,10,15,0,7,8,3,13,6,14,4,5,1,9,2))
    state = Puzzle((3,2,5,0,4,8,6,1,7))
    state = Puzzle((0,1,2,3,4,5,6,7,8))
    print(state.solved())
