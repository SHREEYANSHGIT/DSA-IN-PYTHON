class Solution(object):
    def replaceWords(self, dictionary, sentence):
        maxl = max(len(w) for w in dictionary)
        hm = {}

        for w in dictionary:
            hm[w] = w
        
        sarr = sentence.split()

        for i in range(len(sarr)):
            for j in range(1 , min(len(sarr[i]),maxl) +1 ):
                x = sarr[i][:j] 
                if x in hm:
                    sarr[i] = x
                    break
        
        return " ".join(sarr)



        