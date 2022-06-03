def bsearch(arr1,key):
        while(start<=end):
            mid=(start+end)//2
            if(arr1[mid]<key):
                start=mid+1
            elif(arr[mid]>key):
                end=mid-1
            else:
                return arr[mid]
        return None
    
    arr.sort()
    for i in range(len(arr)):
        numi=arr.pop(i)
        fin=bsearch(arr,k-numi)
        if(fin):
            return (numi,fin)
        arr.append(numi)
        arr.sort()