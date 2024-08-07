from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # result = 0
        # start = [0] * n
        # parents = [0] * n
        children = [[] for _ in range(n)]

        for a, b in relations:
            a -= 1
            b -= 1
            # parents[b] += 1
            children[a].append(b)

        cache = [None] * n

        def dfs(node):
            if cache[node] is not None:
                return cache[node]

            res = time[node]

            child_max = 0
            for child in children[node]:
                child_time = dfs(child)
                if child_time > child_max:
                    child_max = child_time

            res += child_max

            cache[node] = res
            return res

        return max(dfs(i) for i in range(n))

        # stack = [i for i, val in enumerate(parents) if val == 0]

        # while stack:
        #     node = stack.pop()
        #     end = start[node] + time[node]
        #     if end > result:
        #         result = end

        #     for child in children[node]:
        #         if start[child] < end:
        #             start[child] = end
        #         parents[child] -= 1
        #         if parents[child] == 0:
        #             stack.append(child)

        # return result

if __name__=="__main__":
    n =3
    relations =[[1,3],[2,3]]
    time =[3,2,5]
    s=Solution()
    print(s.minimumTime(n,relations,time))