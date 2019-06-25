class Solution:
    def countAndSay(self, n: int) -> str:

        assert n <= 30, "Input exceeded valid range."

        count = 1
        say = "1"

        d = {}

        while count <= n:
            d[count] = say
            count += 1

            for c, v in enumerate(say):
                # TODO: pass

            say = temp

        return d[n]