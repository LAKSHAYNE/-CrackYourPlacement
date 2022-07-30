class Solution:
    def convertToTitle(self, coln: int) -> str:
        count=0
        s=''
        while(coln>=26):
            temp=coln
            count=0
            while(temp>26):
                if(temp%26==0):
                    temp=temp//26-1
                else:
                    temp=temp//26
                count+=1
            coln=coln-((26**count)*temp)
            s+=chr((int(temp)+64))
        if(coln>0):
            s+=chr(64+(coln%26))
        return(s)