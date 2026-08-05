class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return True

        # create adgecenly list.
        graph = defaultdict(list)
        for src, des in edges:
            graph[src].append(des)
            graph[des].append(src)
            
        print(graph)
        #trace is_visited
        is_visited = set()
        # constrcut dfs with current and paret

        def dfs(current, parent):
            nonlocal is_visited
            is_visited.add(current)

            is_valid = True
            for neighbor in graph[current]:
                if neighbor not in is_visited:
                    is_valid = is_valid and dfs(neighbor,current)
                else:
                    if neighbor != parent:
                        return False
            return is_valid

        # do dfs of 0  to ce we can vist all the edges
        if not dfs(0,-1):
            return False

        # if is_visited coutn doesnt match with the count of adgecently ist teh return fase
        # this repiresent the disconnected graphs
        
        return len(is_visited) == len(graph)