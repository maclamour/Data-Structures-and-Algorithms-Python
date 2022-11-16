class Solution(object):
    def HousesFighting(N):
        result = str('')
        if N % 3 == 0:
            result = 'Me and E'
        elif N % 3 == 1:
            result =  'E and D'
        elif N % 3 == 2:
            result = 'D and M'

    Y = int(raw_input())


    HousesFighting(Y)