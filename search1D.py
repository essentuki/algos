import cells

import os
import time
import IPython.display

class OneDimSearch:
    """Parent class having the attributes of any one dimensional search."""
    def __init__(self, nums: list(), target: int, waiting_time = 0.75):
        self.nums = nums
        self.target = target
        self.waiting_time = waiting_time
        
    def print_cell(self, idx = None, visited = [], actual = None, 
                left = None, right = None):
        """Prints a cell with certain characteristics depending on its nature."""           
        if self.nums[idx] == self.target:
            targetCell  = cells.Target(self.target)
            targetCell.print_to_screen()
        elif idx == left:
            leftCell = cells.LeftPointer(self.nums[idx])
            leftCell.print_to_screen()
        elif idx == right:
            rightCell = cells.RightPointer(self.nums[idx])
            rightCell.print_to_screen()
        elif idx in visited:
            visitedCell = cells.Visited(self.nums[idx])
            visitedCell.print_to_screen()
        elif idx == actual:
            actualCell = cells.Actual(self.nums[idx])
            actualCell.print_to_screen()
        else:
            notVisitedCell = cells.NotVisited()
            notVisitedCell.print_to_screen()
    
    def print_state(self, visited = [], actual = None, 
                    left = None, right = None):
        """Prints to screen the actual state of an explored array."""
        os.system('clear')
        IPython.display.clear_output(wait = True)
        print("1D SEARCH INITIALIZED: \n")
        for j in range(len(self.nums)):
            self.print_cell(j, visited, actual, left, right)
        print("\n")
        time.sleep(self.waiting_time)

class LinearSearch(OneDimSearch):
    """Represents an un/sorted 1D array to be linearly searched O(N)."""        
    def visualize_it(self):
        """Runs the algorithm while printing each step."""
        steps, visited = 0, []
        for i in range(len(self.nums)):
            self.print_state(visited, i)
            visited.append(i)
            if self.nums[i] == self.target:
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
            self.print_state(visited, middle_point, left, right)
            visited.append(middle_point)
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
    search1 = LinearSearch( sorted([3,7,1,4,8,2,15,30,22,0,11,9,13,20,10,5]), 30 )
    search1.visualize_it()

    search2 = BinarySearch( sorted([3,7,1,4,8,2,15,30,22,0,11,9,13,20,10,5]), 10, 1.5 )
    search2.visualize_it()

if __name__ == '__main__':
    main()
