class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        if not words:
            return ""

        char_graph = { c : set() for word in words for c in word}
        in_degree = {char : 0 for char in char_graph}
        # createa a graph

        def add_edge(s1: str, s2:str) -> bool:

            i = j = 0
            while i<len(s1) and i<len(s2) and s1[i] == s2[j]:
                i += 1
                j += 1
            
            if i != len(s1) and j == len(s2):
                return False
            
            if i != len(s1) and j != len(s2) and s2[j] not in char_graph[s1[i]]:
                char_graph[s1[i]].add(s2[j])
                in_degree[s2[j]] += 1
            
            return True

        for i in range(len(words) - 1):
            if not add_edge(words[i], words[i+1]):
                return ""

        print(char_graph)
        print(in_degree)
        queue = deque(char for char in char_graph if in_degree[char] == 0)

        res = []
        while queue:
            cur = queue.popleft()
            res.append(cur)

            for next_char in char_graph[cur]:
                    in_degree[next_char] -= 1
                    if in_degree[next_char] == 0:
                        queue.append(next_char)


        return  "" if len(res) != len(char_graph) else "".join(res)



