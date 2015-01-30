##Wildcard Matching
Source: https://oj.leetcode.com/problems/wildcard-matching  
###Description

                
Implement wildcard pattern matching with support for   
'?'  
 and   
'*'  
.  


  

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the   
entire  
 input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") â false
isMatch("aa","aa") â true
isMatch("aaa","aa") â false
isMatch("aa", "*") â true
isMatch("aa", "a*") â true
isMatch("ab", "?*") â true
isMatch("aab", "c*a*b") â false  
###Tags
Dynamic Programming, Backtracking, Greedy, String  
###Solutions