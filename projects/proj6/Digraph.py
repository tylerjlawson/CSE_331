# Project 6 - Directed Graph
# Uses python lists in order to implement a directed graph
# Dijkstra's Algorith was used in order to find shortest path

import math # used for infinity attribute

class Digraph:
    def __init__(self, n):
        """
        Constructor
        :param n: Number of vertices
        """
        self.order = n
        self.size = 0
        # You may put any required initialization code here
        self.weights = [[] for e in range(n)] # tracks the weights or each arc
                                              # both indexed by the start vertices
        self.dests = [[] for e in range(n)]   # saves the destinations fron source

    def insert_arc(self, s, d, w):
        """
        Inserts an arc with a weight to the directed graph
        parameters are source, destination and weight
        """
        if self.order <= d or self.order <= s: # Error check
            raise IndexError
        if d < 0 or s < 0:
            raise IndexError

        if d not in self.dests[s]: # if there is not already an arc 
            self.weights[s].append(w)  # add the weight
            self.dests[s].append(d)    # add the destination
            self.size += 1             # update size
        else:  # if it is an overwrite
            self.weights[s][self.dests[s].index(d)] = w

    def out_degree(self, v):  
        # return the outdegree of a vertex
        # parameter is a vertex
        return len(self.dests[v])

    def are_connected(self, s, d):
        # Parameters source and destination vertex
        if self.order <= d or self.order <= s: # Error Check
            raise IndexError
        if d < 0 or s < 0:
            raise IndexError
        return d in self.dests[s] # return True if there is a connection

    def is_path_valid(self, path):
        for i in path:
            if i >= self.order or i < 0: # error check
                raise IndexError

        for i in range(len(path)-1): # go through all connections
            if not self.are_connected(path[i],path[i+1]):
                return False
        return True # all connections were true

    def arc_weight(self, s, d): # finds the weight  of an arc
        if not self.are_connected(s,d): # error check sort of
            return math.inf
        return self.weights[s][self.dests[s].index(d)] # gets corresponding index for list

    def path_weight(self, path): # finds total weight of a path list
        if not self.is_path_valid(path): # error check
            return math.inf
        num = 0 # counter
        for i in range(len(path)-1): # go through path
            num += self.arc_weight(path[i],path[i+1]) # adds each arc weight
        return num

    def does_path_exist(self, s, d):
        # check if path exists
        if self.order <= d or self.order <= s: # error check
            raise IndexError
        if d < 0 or s < 0:
            raise IndexError

        V = [False] * self.order # variables
        search = [s]
        V[s] = True 
        while search: # go till search done
            tmp = search.pop(0) # remove the front
            if tmp == d:         # if found end return true
                return True
            for i in self.dests[tmp]:   # visited and add next vertex to list
                search.append(i)
                V[i] = True
        return False  # not found

    def find_min_weight_path(self, s, d):
        '''
        Dijkstra's Algorithm for smallest weight path
        parameters start and destination
        '''
        if not self.does_path_exist(s,d): # error check
            raise ValueError
        if self.size == 0:
            return 0

        dist = [math.inf] * self.order   # distances list
        dist[s] = 0  # start vertex distance 0
        visited = [] # visited list
        unvisited = [i for i in range(self.order)] # unvisited list
        parent = [None] * self.order # previous node in path
        while d not in visited: # visit siblings to find min weight path
            u = unvisited[dist.index(min(dist))] # neighbor node
            for v in self.dests[u]: # for each of its neighbors
                if v not in visited: # test visited
                    if dist[u] + self.arc_weight(u,v) < dist[v]: # distance calc
                        dist[v] = dist[u] + self.arc_weight(u,v) # update if need be
                        parent[v] = u # update parent
            visited.append(u) # update lists
            unvisited.remove(u)

        path = [d]
        while path[0] != s: # build the result path
            path = [parent[path[0]]] + path
            
        return path
        