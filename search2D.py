import cells
import search1D

import os
import time
import IPython.display

class TwoDimSearch(search1D.LinearSearch):
    """Parent class having the attributes of any two dimensional search."""  
    def print_cell(self, idx = tuple(), visited = [], actual = None, 
                left = None, right = None):  
        """Prints a cell with certain characteristics depending on its nature."""
        val = self.nums[idx[0]][idx[1]]        
        if  val == self.target:
            targetCell  = cells.Target(self.target)
            targetCell.print_to_screen()
        elif idx == left:
            leftCell = cells.LeftPointer(val)
            leftCell.print_to_screen()
        elif idx == right:
            rightCell = cells.RightPointer(val)
            rightCell.print_to_screen()
        elif idx in visited:
            visitedCell = cells.Visited(val)
            visitedCell.print_to_screen()
        elif idx == actual:
            actualCell = cells.Actual(val)
            actualCell.print_to_screen()
        else:
            notVisitedCell = cells.NotVisited()
            notVisitedCell.print_to_screen()

    def print_state(self, visited: list(), actual: None, 
                    left = None, right = None):
        """Prints to screen the actual state of an explored grid."""
        os.system('clear')
        IPython.display.clear_output(wait = True)
        print("2D SEARCH INITIALIZED: \n")
        for i in range(len(self.nums)):
            for j in range(len(self.nums[0])):
                self.print_cell((i,j), visited, actual, left, right)
            print("\n")
        time.sleep(self.waiting_time)

class SequentialSearch(TwoDimSearch):
    """Represents an un/sorted grid to be sequentially searched O(N**2)."""        
    def visualize_it(self):
        """Runs the algorithm while printing each step."""
        steps, visited = 0, []
        for i,row in enumerate(self.nums):
            for j,entry in enumerate(row):
                self.print_state(visited, (i,j))
                visited.append((i,j))
                if entry == self.target:
                    print(f"Target found. It required {steps + 1} steps. \n")
                    time.sleep(1.5)
                    break
                steps += 1
            else:
                continue
            break

def main():
    """Examples:"""
    search1 = SequentialSearch( [[1,1,3,4],[5,6,7,8],[2,4,6,11]], 11)
    search1.visualize_it()

if __name__ == '__main__':
    main()