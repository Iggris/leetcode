class Solution(object):
    def maximumDetonation(self, bombs):
        n = len(bombs)
        
        graph = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                xj, yj, _ = bombs[j]
                if (xi - xj)**2 + (yi - yj)**2 <= ri**2:
                    graph[i].append(j)

        def dfs(start):
            seen = set()
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in seen:
                    seen.add(node)
                    for neighbor in graph[node]:
                        if neighbor not in seen:
                            stack.append(neighbor)
            return len(seen)

        max_detonated = 0
        for i in range(n):
            max_detonated = max(max_detonated, dfs(i))
        
        return max_detonated



        
