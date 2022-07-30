class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count=100**3+1
        test=strs[0]
        for i in strs[1:]:
            currn=0
            for a in range(len(min(test,i,key=len))):
                if(test[a]==i[a]):
                    currn+=1
                else:
                    break
            count=min(currn,count)
            
        return test[:count]