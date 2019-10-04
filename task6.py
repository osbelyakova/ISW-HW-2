#!/usr/bin/env python3
"""Network delay time"""
def get_graph(edge_num=0):
    """Make a matrix with weight of the edge on intersection"""
    graph_matrix = []
    str_with_tops = input("times = ")
    str_with_tops = str_with_tops.replace(' ','')
    str_with_tops = str_with_tops.replace(',',' ')
    str_with_tops = str_with_tops.replace('[','')
    str_with_tops = str_with_tops.replace(']','')
    list_with_tops = str_with_tops.split(' ')
    k = 0
    while k < len(list_with_tops) - 2:
        first_top = int(list_with_tops[k])
        k += 1
        second_top = int(list_with_tops[k])
        k += 1
        edge_weight = int(list_with_tops[k])
        k += 1
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
        graph_matrix[first_top][second_top] = edge_weight
    return graph_matrix

class Graph:
    """Graph"""
    def __init__(self):
        self.graph_matrix = get_graph()

    def search_way(self, visited_arr, nodeStart=0, nodeEnd=0, best_way=0):
        """Best way by matching tops which were visited"""
        if nodeStart == nodeEnd:
            return 0
        elif self.graph_matrix[nodeStart][nodeEnd] != 0:
            return self.graph_matrix[nodeStart][nodeEnd]
        else:
            mas = []
            for j in range(0, len(self.graph_matrix)):
                if (self.graph_matrix[nodeStart][j] != 0) and (visited_arr[j] == 0):
                    visited_arr[nodeStart] = 1
                    k = self.search_way(visited_arr, j, nodeEnd, best_way)
                    if k >= 0:
                        mas.append([k + self.graph_matrix[nodeStart][j], j])
            if mas == []:
                visited_arr[nodeStart] = 1
                return -1
            minimum = -2
            for i in range(0, len(mas)):
                if mas[i][0] < minimum or minimum < 0:
                    minimum = mas[i][0]
            best_way += minimum
            return best_way

    def print_graph(self):
        """Print the graph in matrix-style"""
        for i in range(0, len(self.graph_matrix)):
            print(self.graph_matrix[i])

times_graph = Graph()
N = int(input("N = "))
if N > 100 or N < 1:
    print("Error")
else:
    #try_graph.print_graph()
    X = int(input("X = "))
    if X > N or X < 1:
        print("Error")
    else:
        visited_arr = []
        length = -1
        for i in range(0, len(times_graph.graph_matrix)):
            visited_arr.append(0)
        for i in range(1, N + 1):
            for j in range(0, len(times_graph.graph_matrix)):
                visited_arr[j] = 0
            new_way = times_graph.search_way(visited_arr, X, i)
            #print("Р Р°СЃСЃС‚РѕСЏРЅРёРµ РјРµР¶РґСѓ {} Рё {}: {}".format(X, i, new_way))
            if new_way == -1:
                length = -1
                break
            if (length < new_way) and (X != i):
                length = new_way
        print("The answer: {}".format(length))
