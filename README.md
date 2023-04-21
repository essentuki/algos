# ALGOS
Python library to visualize data structures and ALGOrithmS. It can be used at any terminal and also in Jupyter Notebooks.

Aside from any understanding that one could have, about data structures and search algorithms, 
possessing the chance of visualizing what our code is actually doing helps deepen our
understanding and sometimes even finding bugs.

1) EXAMPLE: 
The following is a LeetCode problem (No. 5). It is called the Last Stone Weight and it is considered easy. 
The statement goes as follows:

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:
- If x == y, both stones are destroyed, and
- If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.
Return the weight of the last remaining stone. If there are no stones left, return 0.

2) How to implement ALGOS?

This is the original code solution:

    def lastStoneWeight(stones):
            while len(stones) > 1:
                stones.sort()
                y, x = stones[-1], stones[-2]
                stones.pop()
                stones.pop()
                if y-x:
                    stones.append(y-x)
            if stones: 
                return stones[0]
            return 0

Implementing ALGOS looks like this:

    import search1D
    def lastStoneWeight(stones):
            while len(stones) > 1:
                stones.sort()

                # --------- ALGOS starts here ---------
                state = search1D.OneDimSearch(stones, None, 1)
                state.print_visited_indices(range(len(stones)), None, len(stones)-2, len(stones)-1)
                # --------- ALGOS  ends here  ---------

                y, x = stones[-1], stones[-2]
                stones.pop()
                stones.pop()
                if y-x:
                    stones.append(y-x)

                # --------- ALGOS starts here ---------
                state = search1D.OneDimSearch(stones, None, 1)
                state.print_visited_indices(range(len(stones)), None, len(stones)-2, len(stones)-1)
                # --------- ALGOS  ends here  ---------

            if stones: 
                return stones[0]
            return 0

Each moment ALGOS is called is to take a "picture" of the current state of our array. Here is been called twice
as we first identify the position of the last two numbers and after removing them we append their difference.

LeetCode offers the following explanation for their example:

Input: stones = [2,7,4,1,8,1]

Output: 1

Explanation: 

We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,

we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,

we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,

we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

By implementing ALGOS the user can see the following process:

https://user-images.githubusercontent.com/11930196/233712166-be55e749-4dfe-414d-a63e-a56e642591ee.mp4

which shows the same reduction process.
