class Solution:
    def __init__(self):
        self.ans=[]
        
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj=dict()
        for i in adjacentPairs:
            if(i[0] in adj):
                adj[i[0]].append(i[1])
            else:
                adj[i[0]]=[i[1]]
            if(i[1] in adj):
                adj[i[1]].append(i[0])
            else:
                adj[i[1]]=[i[0]]
            
        
        terminal=0
        for i in adj.keys():
            if(len(adj[i])==1):
                terminal=i
                break
        
        
        visi=dict()
        for i in adj.keys():
            visi[i]=0
        
        def dfs(node):
            visi[node]=1
            self.ans.append(node)
            for i in adj[node]:
                if(not visi[i]):
                    dfs(i)
        
        dfs(terminal)
        return self.ans