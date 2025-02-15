class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {}
        for idx, char in enumerate(order):
            mapping[char] = idx

        def compare(w1: str, w2: str) -> bool:
            '''
            Returns true if w2 > w1
            '''
            l = 0
            r = 0

            while l < len(w1) and r < len(w2):
                if w1[l] == w2[r]:
                    l += 1
                    r += 1
                    continue
                elif mapping[w1[l]] < mapping[w2[r]]:
                    l += 1
                    r += 1
                    return True
                else:
                    l += 1
                    r += 1
                    return False
            
            # if we reach here, we have a case like "abcert" and "abce", in this case the shorter one comes before
            if len(w2) < len(w1):
                return False
            return True

        
        for i in range(len(words) - 1):
            cmp1 = words[i]
            cmp2 = words[i + 1]

            # true if cmp2 is after cmp1
            if compare(cmp1, cmp2):
                continue
            else:
                return False
        
        return True
