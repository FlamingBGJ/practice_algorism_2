# -*- coding: utf-8 -*-
"""그래프1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l-wVR-E04bhefd4MCD9652Fg4FTTGoRk
"""

## 함수
class Graph():
  def __init__(self, size):
    self.graph = [[0 for _ in range(size)] for _ in range(size)]

## 메인
G1 = Graph(4)

G1.graph[0][1] = 1
G1.graph[0][2] = 1
G1.graph[0][3] = 1
G1.graph[1][0] = 1
G1.graph[1][2] = 1
G1.graph[1][3] = 0
G1.graph[2][0] = 1
G1.graph[2][1] = 1
G1.graph[2][3] = 1
G1.graph[3][0] = 1
G1.graph[3][1] = 0
G1.graph[3][2] = 1

for row in range(4):
  for col in range(4):
    print(G1.graph[row][col], end=" ")
  print()

