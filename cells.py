class OneDimCell:
    """Represents a cell or element in an array. It has BKG and TXT colors."""
    BKG_COLOR = {'RESET' : '\u001b[0m', 
                'BLACK' : '\u001b[40m', 
                'WHITE' : '\u001b[47m',    
                'LIGHT_WHITE' : '\u001b[47;1m', 
                'CYAN' : '\u001b[46;1m',
                'MAGENTA' : '\u001b[45;1m'
                }
    TXT_COLOR = {'WHITE' : '\u001b[37;1m', 
                'BLACK' : '\u001b[30;1m', 
                'RED' : '\u001b[31;1m'
                }

class Target(OneDimCell): 
    """Represents the target cell in an array. It requires a value."""  
    def __init__(self, target_value):
        self.target_value = target_value
    
    def print_to_screen(self):
        print(f"{Target.BKG_COLOR['CYAN']}{Target.TXT_COLOR['WHITE']} {self.target_value} "
            + f"{Target.BKG_COLOR['RESET']}", end = ' '
            )

class NotVisited(OneDimCell):
    """Represents any unknown cell that has not been visited."""
    def print_to_screen(self):
        print(f"{NotVisited.BKG_COLOR['BLACK']}{NotVisited.TXT_COLOR['WHITE']}   "
            + f"{NotVisited.BKG_COLOR['RESET']}", end = ' '
            )

class Visited(OneDimCell):
    """Represents all the visited elements of an array before reaching the target.
        It needs a value.
    """
    def __init__(self, visited_value):
        self.visited_value = visited_value
    
    def print_to_screen(self):
        print(f"{Visited.BKG_COLOR['WHITE']}{Visited.TXT_COLOR['BLACK']} {self.visited_value} "
            + f"{Visited.BKG_COLOR['RESET']}", end = ' '
            )

class Actual(OneDimCell):
    """Represents the present cell while looping the array. It needs a value."""
    def __init__(self, visited_value):
        self.visited_value = visited_value
    
    def print_to_screen(self):
        print(f"{Actual.BKG_COLOR['MAGENTA']}{Actual.TXT_COLOR['BLACK']} {self.visited_value} "
            + f"{Actual.BKG_COLOR['RESET']}", end = ' '
            )

def main():
    tCell = Target('T')
    tCell.print_to_screen()

    nVCell = NotVisited()
    nVCell.print_to_screen()

    vCell = Visited('V')
    vCell.print_to_screen()

    aCell = Actual('A')
    aCell.print_to_screen()

if __name__ == '__main__':
    main()