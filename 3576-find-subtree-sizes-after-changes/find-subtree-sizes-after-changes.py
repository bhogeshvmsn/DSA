class Solution:
    def findSubtreeSizes(self, parent: list[int], s: str) -> list[int]:
        n = len(parent)

        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)

        newTree = [[] for _ in range(n)]
        last = {}

        def dfs(u):
            ch = s[u]
            prev = last.get(ch, -1)

            p = prev if prev != -1 else parent[u]

            if u != 0:
                newTree[p].append(u)

            last[ch] = u

            for v in tree[u]:
                dfs(v)

            if prev == -1:
                del last[ch]
            else:
                last[ch] = prev

        dfs(0)

        ans = [0] * n

        def calc(u):
            ans[u] = 1

            for v in newTree[u]:
                ans[u] += calc(v)

            return ans[u]

        calc(0)
        return ans