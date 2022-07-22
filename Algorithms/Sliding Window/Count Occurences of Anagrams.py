'''

Count Occurences of Anagrams
https://practice.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1

'''

class Solution:
	def search(self, pat, txt):
	    ans = 0
	    l = len(pat)
	    to_match = {}
	    for i in pat:
	        if i not in to_match:
	            to_match[i] = 1
	        else:
	            to_match[i] += 1
	    
      curr = {}      
      for i in range(l):
          if txt[i] not in curr:
              curr[txt[i]] = 1
          else:
              curr[txt[i]] += 1

      if curr == to_match: ans += 1
      
      for i in range(l, len(txt)):
          if txt[i] in curr:
             curr[txt[i]] += 1
          else:
             curr[txt[i]] = 1
          curr[txt[i-l]] -= 1
          if curr[txt[i-l]] == 0:
              curr.pop(txt[i-l])
          if curr == to_match: ans += 1
            
        return ans
	       
                
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
