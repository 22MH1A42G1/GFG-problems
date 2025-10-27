import heapq
class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        n1,n2=len(arr1),len(arr2)
        pq=[]
        pq.append((arr1[0]+arr2[0],0,0))
        count=0
        visited={(0,0)}
        ans=[]
        while count<k and pq:
            _,i,j=heapq.heappop(pq)
            ans.append((arr1[i],arr2[j]))
            count+=1
            if i+1<n1 and (i+1,j) not in visited:
                heapq.heappush(pq,(arr1[i+1]+arr2[j],i+1,j))
                visited.add((i+1,j))
            if j+1<n2 and (i,j+1) not in visited:
                heapq.heappush(pq,(arr1[i]+arr2[j+1],i,j+1))
                visited.add((i,j+1))
        return ans