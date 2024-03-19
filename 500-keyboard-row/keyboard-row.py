class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        # rows = [''.join(sorted(i)) for i in rows]
        
        # for word in words:
        #     temp = ''.join(set(word.lower()))
        #     for c in temp:
        #         if c not in rows

        l1="qwertyuiop"
        l2="asdfghjkl"
        l3="zxcvbnm"
        res=[]

        for word in words:
            w = word.lower()
            if len(set(l1 + w)) == len(l1) or len(set(l2 + w)) == len(l2) or len(set(l3 + w)) == len(l3):
                res.append(word)

        return res

