import cells
import os
import time
import IPython.display

class TwoDimSearch:
    """Parent class having the attributes of any two dimensional search."""
    def __init__(self, grid: list(), target: int, waiting_time = 0.75):
        self.grid = grid
        self.target = target
        self.waiting_time = waiting_time
    
    def print_state(self, visited: list(), actual: int):
        """Prints to screen the actual state of an explored grid.
        Only works when there are no duplicates. Inputs here are values."""
        targetCell = cells.Target(self.target)
        notVisitedCell = cells.NotVisited()
        os.system('clear')
        IPython.display.clear_output(wait = True)
        print("2D SEARCH INITIALIZED: \n")
        for row in self.grid:
            for entry in row:
                if entry == self.target:
                    targetCell.print_to_screen()
                elif entry in visited:
                    visitedCell = cells.Visited(entry)
                    visitedCell.print_to_screen()
                elif entry == actual:
                    actualCell = cells.Actual(entry)
                    actualCell.print_to_screen()
                else:
                    notVisitedCell.print_to_screen()
            print("\n")
        time.sleep(self.waiting_time)
    
    def print_visited_indeces(self, visited: list(), actual: tuple()):
        """Prints to screen the actual state of an explored grid.
        Inputs here should only represent indeces not values."""
        targetCell = cells.Target(self.target)
        notVisitedCell = cells.NotVisited()
        os.system('clear')
        IPython.display.clear_output(wait = True)
        print("2D SEARCH INITIALIZED: \n")
        for i,row in enumerate(self.grid):
            for j,entry in enumerate(row):
                if entry == self.target:
                    targetCell.print_to_screen()
                elif (i,j) in visited:
                    visitedCell = cells.Visited(entry)
                    visitedCell.print_to_screen()
                elif (i,j) == actual:
                    actualCell = cells.Actual(entry)
                    actualCell.print_to_screen()
                else:
                    notVisitedCell.print_to_screen()
            print("\n")
        time.sleep(self.waiting_time)

class SequentialSearch(TwoDimSearch):
    """Represents an unsorted/sorted grid that can be sequentially searched O(N**2)."""        
    def visualize_it(self):
        """Runs the algorithm while printing each step."""
        steps, visited = 0, []
        for i,row in enumerate(self.grid):
            for j,entry in enumerate(row):
                self.print_visited_indeces(visited, (i,j))
                visited.append((i,j))
                if entry == self.target:
                    print(f"Target found. It required {steps + 1} steps. \n")
                    time.sleep(1.5)
                    break
                steps += 1

def main():
    search1 = SequentialSearch( [[1,1,3,4],[5,6,7,8]], 8)
    search1.visualize_it()

if __name__ == '__main__':
    main()