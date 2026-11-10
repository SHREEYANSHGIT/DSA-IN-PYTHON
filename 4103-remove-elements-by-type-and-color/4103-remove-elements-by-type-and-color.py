class Solution(object):
    def canRemoveAll(self, types, colors, groupSize):
        n = len(colors)
        st = []
        for i in range(n):
            t = types[i]
            c = colors[i]
            if st and st[-1][0] == t and st[-1][1] == c:
                st[-1][2] +=1

            else:
                st.append([t,c,1])

            if st[-1][2] ==  groupSize[t]:
                st.pop()
        
        if not st:
            return True
        else:
            return False
    
