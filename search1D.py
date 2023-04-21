import cells
import time
import os
import IPython.display

class OneDimSearch:
    """Parent class having the attributes of any one dimensional search."""
    def __init__(self, nums: list(), target: int, waiting_time = 0.75):
        self.nums = nums
        self.target = target
        self.waiting_time = waiting_time
    
    def print_state(self, visited = [], actual = None, 
                    left = None, right = None):
        """Prints to screen the actual state of an explored array.
        Only works when there are no duplicates."""
        targetCell  = cells.Target(self.target)
        notVisitedCell = cells.NotVisited() 
        os.system('clear')
        IPython.display.clear_output(wait = True)
        print("1D SEARCH INITIALIZED: \n")
        for j in self.nums:
            if j == self.target:
                targetCell.print_to_screen()
            elif j == left:
                leftCell = cells.LeftPointer(left)
                leftCell.print_to_screen()
            elif j == right:
                rightCell = cells.RightPointer(right)
                rightCell.print_to_screen()
            elif j in visited:
                visitedCell = cells.Visited(j)
                visitedCell.print_to_screen()
            elif j == actual:
                actualCell = cells.Actual(j)
                actualCell.print_to_screen()
            else:
                notVisitedCell.print_to_screen()
        print("\n")
        time.sleep(self.waiting_time)
    
    def print_visited_indices(self, visited = [], actual = None, 
                            left = None, right = None):
        """Prints to screen the actual state of an explored array.
        Inputs here should represent indices."""
        targetCell  = cells.Target(self.target)
        notVisitedCell = cells.NotVisited() 
        os.system('clear')
        IPython.display.clear_output(wait = True)
        print("1D SEARCH INITIALIZED: \n")
        for j,val in enumerate(self.nums):
            if val == self.target:
                targetCell.print_to_screen()
            elif j == left:
                leftCell = cells.LeftPointer(val)
                leftCell.print_to_screen()
            elif j == right:
                rightCell = cells.RightPointer(val)
                rightCell.print_to_screen()
            elif j in visited:
                visitedCell = cells.Visited(j)
                visitedCell.print_to_screen()
            elif j == actual:
                actualCell = cells.Actual(j)
                actualCell.print_to_screen()
            else:
                notVisitedCell.print_to_screen()
        print("\n")
        time.sleep(self.waiting_time)

class LinearSearch(OneDimSearch):
    """Represents an un/sorted 1D array to be linearly searched O(N)."""        
    def visualize_it(self):
        """Runs the algorithm while printing each step."""
        steps, visited = 0, []
        for i in self.nums:
            self.print_state(visited, i)
            visited.append(i)
            if i == self.target:
                print(f"Target found. It required {steps + 1} steps. \n")
                time.sleep(1.5)
                break
            steps += 1

class BinarySearch(OneDimSearch):
    """Represents a sorted 1D array to be searched with a binary algorithm."""
    def visualize_it(self):
        """Runs the algorithm while printing each step."""
        if self.nums != sorted(self.nums):
            print("The list must be first sorted.")
            time.sleep(1)
            return
        
        steps, visited = 0, []
        left, right = 0, len(self.nums)-1
        while left <= right:
            middle_point = (left + right)//2
            self.print_state(visited, self.nums[middle_point], 
                            self.nums[left], self.nums[right])
            visited.append(self.nums[middle_point])
            if self.nums[middle_point] == self.target:
                print(f"Target found. It required {steps + 1} steps. \n")
                time.sleep(1.5)
                break
            steps += 1
            if self.nums[middle_point] < self.target:
                left = middle_point + 1
            else:
                right = middle_point - 1

def main():
    """Examples:"""
    search1 = LinearSearch( sorted([3,7,1,4,8,2,15,30,22,0,11,9,13,20,10,5]), 20 )
    search1.visualize_it()

    search2 = BinarySearch( sorted([3,7,1,4,8,2,15,30,22,0,11,9,13,20,10,5]), 10, 1.5 )
    search2.visualize_it()

if __name__ == '__main__':
    main()
