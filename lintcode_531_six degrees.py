
Description
Six degrees of separation is a philosophical problem, which means that everyone and everything can be connected through 
six steps or less.

Now give you a friendship, calculate how many steps two people can be connected through, if not, return -1.

Example
Example1

Input: {1,2,3#2,1,4#3,1,4#4,2,3} and s = 1, t = 4 
Output: 2
Explanation:
    1------2-----4
     \          /
      \        /
       \--3--/
Example2

Input: {1#2,4#3,4#4,2,3} and s = 1, t = 4
Output: -1
Explanation:
    1      2-----4
                 /
               /
              3



>>> # Definition for Undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
import queue

class Solution:

    '''

    @param {UndirectedGraphNode[]} graph a list of Undirectevisited graph node

    @param {UndirectedGraphNode} s, t two Undirectevisited graph nodes

    @return {int} an integer

    '''

    def sixDegrees(self, graph, s, t):

        # Write your code here

        visited = {}

        q = queue.Queue(maxsize = len(graph))

        q.put(s)

        visited[s] = 0

        while not q.empty():

            x = q.get()

            if x == t:

                return visited[x]

            for y in x.neighbors:

                if y not in visited:

                    visited[y] = visited[x] + 1

                    q.put(y)

        return -1