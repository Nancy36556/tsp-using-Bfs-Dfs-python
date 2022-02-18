            #       1
            #     /  \
            #    /    \ 
            #   2      3
            #   \      \
            #    \      5 
            #     \    /
            #       4    
            
import queue
graph={"1":["2","3"],
        "2":["4","1"],
        "3":["1","5"],
        "4":["2","5"],
        "5":["4","3"]
}
def recursive_DFS(graph ,start, visited=[ ]):
    visited.append(start)
    for next in set(graph [start])-set(visited):
        recursive_DFS(graph , next, visited)
    return visited
print("TSP USEING DFS  ")
print(recursive_DFS(graph,"1"))
queue=[]
visited=[]
def bfs(graph, node):
  visited.append(node)
  queue.append(node)

  while queue:         
    m = queue.pop(0) 
    print (m, end = " ") 

    for n in graph[m]:
      if n not in visited:
        visited.append(n)
        queue.append(n)

# Driver Code
print("TSP USNIG BFS")
bfs( graph, '1')
