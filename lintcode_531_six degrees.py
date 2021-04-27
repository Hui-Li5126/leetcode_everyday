Python 3.8.3 (default, May 19 2020, 06:50:17) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
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