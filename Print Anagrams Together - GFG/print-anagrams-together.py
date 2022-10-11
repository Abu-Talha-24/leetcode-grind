class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        result=[]
        for i in range(n):
            if words[i] == "-1": # if already added skip
                continue
            group = [words[i]]
            
            for j in range(i+1, n): # find anagrams
                if words[j] != "-1":
                    if set(words[i]) == set(words[j]):
            
                        group.append(words[j])
                        words[j] = "-1" # marked as added
                        
            result.append(group)
        
            
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n= int(input())
        words=input().split()
        
        ob = Solution()
        ans = ob.Anagrams(words,n)
        
        for grp in sorted(ans):
            for word in grp:
                print(word,end=' ')
            print()

# } Driver Code Ends