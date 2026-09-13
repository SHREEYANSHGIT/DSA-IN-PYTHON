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