#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from graphviz import Graph
import string


class AdjListGraph:
    def __init__(self):
        self.adj = list()  # Список смежности
        self.attributes = list()  # Список атрибутов вершин, list of dict

    def add_vertices(self, n):
        for i in range(n):
            self.adj.append(list())
            self.attributes.append(dict())

    def remove_vertex(self, v):
        self.adj.pop(v)
        self.attributes.pop(v)

    def number_of_vertices(self):
        return len(self.adj)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def remove_edge(self, u, v):
        self.adj[u].remove(v)
        self.adj[v].remove(u)

    def number_of_edges(self):
        cnt=0
        for i in self.adj:
            for j in i:
                cnt+=1
        return cnt//2

    def neighbors(self, v):
        return list(self.adj[v])

    def draw(self, filename='test.gv'):
        """
        Отрисовывает граф используя библиотеку Graphviz. Больше примеров:
        https://graphviz.readthedocs.io/en/stable/examples.html
        """
        g = Graph('G', filename=filename, engine='sfdp')

        for v, attr in enumerate(self.attributes):
            if 'color' in attr:
                g.attr('node', style='filled', fillcolor=attr['color'])
                if attr['color'] == 'black':
                    g.attr('node', fontcolor='white')
            else:
                g.attr('node', style='', color='', fontcolor='', fillcolor='')

            if 'name' in attr:
                g.node(str(v), label='{} ({})'.format(attr['name'], v))
            else:
                g.node(str(v))

        for i in range(self.number_of_vertices()):
            for j in self.adj[i]:
                if i < j:
                    g.edge(str(i), str(j))

        g.view()


def main():
    g = AdjListGraph()
    g.add_vertices(5)
    for i, c in zip(range(5), string.ascii_lowercase):
        g.attributes[i]['name'] = c

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.remove_edge(1, 2)
    print(g.number_of_edges())
    print(g.number_of_vertices())
    print(g.neighbors(1))
    g.draw()


if __name__ == "__main__":
    main()
