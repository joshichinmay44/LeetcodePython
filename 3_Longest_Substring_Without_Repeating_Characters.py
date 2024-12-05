class Solution(object):
    def lengthOfLongestSubstring(self, s):
        substr=[]
        max_len=0
        cnt=0
        if len(s)==0 :
            return 0
        else :
            for i in s:
                if i not in substr:
                    substr.append(i) 
                    print(substr)
                    
                else:
                    substr=substr[substr.index(i)+1:]
                    substr.append(i)
                    print(substr)
                max_len=max(max_len,len(substr))
        return max_len
        
