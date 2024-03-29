#!/usr/bin/env python3
"""BFS and DFS"""
def get_graph(edge_num=0):
    """Make a matrix with 1 on intersection"""
    graph_matrix = []
    str_with_tops = input()
    str_with_tops = str_with_tops.replace(' ','')
    str_with_tops = str_with_tops.replace(',',' ')
    str_with_tops = str_with_tops.replace('[','')
    str_with_tops = str_with_tops.replace(']','')
    list_with_tops = str_with_tops.split(' ')
    k = 0
    while k < len(list_with_tops) - 1:
        first_top = int(list_with_tops[k])
        k += 1
        second_top = int(list_with_tops[k])
        k += 1
        if (first_top == second_top):
            continue
        if edge_num == 0:
            for i in range(edge_num, max(first_top, second_top) + 1):
                graph_matrix.append(0)
                graph_matrix[i] = []
            for i in range(0, edge_num + 1):
                for j in range(edge_num, max(first_top, second_top) + 1):
                    graph_matrix[i].append(0)
            for i in range(edge_num + 1, max(first_top, second_top) + 1):
                for j in range(0, max(first_top, second_top) + 1):
                    graph_matrix[i].append(0)
            edge_num = max(first_top, second_top)
        elif edge_num < max(first_top, second_top):
            for i in range(edge_num + 1, max(first_top, second_top) + 1):
                graph_matrix.append(0)
                graph_matrix[i] = []
            for i in range(0, edge_num + 1):
                for j in range(edge_num, max(first_top, second_top)):
                    graph_matrix[i].append(0)
            for i in range(edge_num + 1, max(first_top, second_top) + 1):
                for j in range(0, max(first_top, second_top) + 1):
                    graph_matrix[i].append(0)
            edge_num = max(first_top, second_top)
        graph_matrix[first_top][second_top] = 1
        graph_matrix[second_top][first_top] = 1
    return graph_matrix

class Graph:
    """Graph"""
    def __init__(self):
        self.graph_matrix = get_graph()

    def bfs(self, i=0):
        """BFS"""
        visited_arr = [None] * (len(self.graph_matrix) + 1)
        visited_arr[i] = 0
        top_queue = [i]
        while i < len(top_queue):
            u = top_queue[i]
            i += 1
            for j in range(0, len(self.graph_matrix)):
                if (self.graph_matrix[u][j] != 0) and (visited_arr[j] is None):
                    visited_arr[j] = visited_arr[u] + 1
                    top_queue.append(j)
        for i in range(0, len(top_queue)):
            print(top_queue[i])
        return 0

    def dfs(self, visited_arr, i=0):
        """DFS"""
        visited_arr[i] = 1
        print(i)
        if i == len(self.graph_matrix) - 1 or sum(self.graph_matrix[i]) == 0:
            return 0
        for j in range(0, len(self.graph_matrix)):
            if (self.graph_matrix[i][j] != 0) and (visited_arr[j] is None):
                self.dfs(visited_arr, j)
                print(i)
        return 1

    def print_graph(self):
        """Print the graph in matrix-style"""
        for i in range(0, len(self.graph_matrix)):
            print(self.graph_matrix[i])
try_graph = Graph()
#try_graph.print_graph()
print("BFS: ")
try_graph.bfs(0)

print("")
visited_arr = []
for i in range(0, len(try_graph.graph_matrix)):
    visited_arr.append(None)
print("DFS: ")
try_graph.dfs(visited_arr, 0)
