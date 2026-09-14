class Solution(object):
    def largestRectangleArea(self, heights):
        n = len(heights)

        left = [-1] * n
        right = [n] * n

        st = []
        
        for i in range(n - 1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                right[i] = st[-1]

            st.append(i)

        st = []

        for j in range(n):
            while st and heights[st[-1]] >= heights[j]:
                st.pop()

            if st:
                left[j] = st[-1]

            st.append(j)

        ans = 0

        for k in range(n):
            width = right[k] - left[k] - 1
            area = heights[k] * width
            ans = max(ans, area)

        return ans
    def maximalRectangle(self, matrix):
        n = len(matrix[0])
        m = len(matrix)
        heights = [0]*n
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    heights[j] = 0
                else:
                    heights[j] += 1
            x = self.largestRectangleArea(heights) 
            ans = max(x, ans)
        
        return ans  
