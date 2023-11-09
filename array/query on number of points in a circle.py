# https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/









class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        r=[0]*len(queries)
        for i in range(len(r)) :
            for j in range(len(points)) :
                if ((points[j][0]-queries[i][0]) ** 2) + ((points[j][1]-queries[i][1]) ** 2) <= (queries[i][2] ** 2) :
                    r[i]+=1
        return r

        


