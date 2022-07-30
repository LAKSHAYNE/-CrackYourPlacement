import collections
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent=[]
        rank=[0]*(len(edges)+1)
        for i in range(len(edges)+1):
            parent.append(i)
            
        def findpar(parent,node):
            if(node==parent[node]):
                return node
            else:
                parent[node]=findpar(parent,parent[node])
                return parent[node]

        def union(parent,rank,edge):
            u=findpar(parent,edge[0])
            v=findpar(parent,edge[1])
            if(u==v):
                return edge
            if(rank[u]==rank[v]):
                rank[u]+=1
                parent[v]=u
            elif(rank[u]>rank[v]):
                parent[v]=u
            else:
                parent[v]=u
            
        
        for ed in edges:
            a=union(parent,rank,ed)
            if(a!=None):
                return ed
                