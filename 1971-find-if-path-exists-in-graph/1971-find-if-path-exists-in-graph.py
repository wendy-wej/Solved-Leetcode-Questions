class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int, ) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for i in edges:
            a,b = i
            graph[a].append(b)
            graph[b].append(a)
            
        def findPath(vertex):
            if vertex == destination:
                return True
            
            for new_vertex in graph[vertex]:
                if new_vertex not in visited:
                    visited.add(new_vertex)
                    if findPath(new_vertex):
                        return True
        return findPath(source)
    
        
#         def buildGraph(edges):
#             graph = {}
#             for i in edges:
#                 a,b = i
#                 if a not in graph:
#                     graph[a] = []
#                 if b not in graph:
#                     graph[b] = []
#                 graph[a].append(b)
#                 graph[b].append(a)
#             return graph
    
#         undirectedGraph = buildGraph(edges)
#         stack = [source]
#         visited = set()
        
        
#         while stack:
#             current = stack.pop()
#             if current in visited:
#                 return False
#             if current == destination:
#                 return True
#             else:
#                 visited.add(current)
#                 for nei in undirectedGraph[current]:
#                     stack.append(nei)
#         return False