import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {distance[x][y]}')
            break

        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < n:
                new_cost = cost + graph[next_x][next_y]

                if new_cost < distance[next_x][next_y]:
                    distance[next_x][next_y] = new_cost
                    heapq.heappush(q, (new_cost, next_x, next_y))


cnt = 1

while True:
    n = int(input())
    if n == 0:
        break
    graph = []
    distance = []
    for _ in range(n):
        distance.append([INF]*n)
        graph.append(list(map(int,input().split())))

    dijkstra()
    cnt += 1