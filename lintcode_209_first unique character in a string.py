Description
Given a string and find the first unique character in a given string. You can assume that there is at least 
one unique character in the string.

Example
Example 1:
	Input: "abaccdeff"
	Output:  'b'
	
	Explanation:
	There is only one 'b' and it is the first one.


Example 2:
	Input: "aabccd"
	Output:  'b'
	
	Explanation:
	'b' is the first one.




>>> class Solution:
    
    def firstUniqChar(self, s):
        
        dummy = ListNode(None); tail = dummy
        tab, invalid = {}, object()
        for c in s:
            
            if c not in tab:
                node = ListNode(c)
                tab[c], tail.next, tail = tail, node, node
            else:
                if tab[c] is invalid:
                    continue
                prv, nxt = tab[c], tab[c].next.next
                prv.next = nxt 
                if nxt:
                    tab[nxt.val] = prv
                else:
                    tail = prv
                tab[c] = invalid
            
        return dummy.next.val if dummy.next else '0'