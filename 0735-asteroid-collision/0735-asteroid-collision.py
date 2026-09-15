class Solution(object):
    def asteroidCollision(self, asteroids):
        st = []

        for i in range(len(asteroids)):
            while st and asteroids[i] < 0 and st[-1] > 0:

                if abs(st[-1]) < abs(asteroids[i]):
                    st.pop()

                elif abs(st[-1]) == abs(asteroids[i]):
                    st.pop()
                    break

                else:
                    break

            else:
                st.append(asteroids[i])

        return st