def gcd(self,a,b):
    if(b==0):
        return a
    else:
        return self.gcd(b,a%b)

def maxPoints(self, points):
    """
    :type points: List[Point]
    :rtype: int
    """
    maxNumOfPoints = 0
    for i in range(len(points)):
        table = {'90' : 1}
        samePoint = 0
        for j in range(i+1, len(points)):
            if(points[i].x == points[j].x and points[i].y == points[j].y):
                samePoint += 1
                continue
            if(points[i].x == points[j].x):
                angle = '90'
            else:
                temp = self.gcd(points[i].y-points[j].y, points[i].x-points[j].x)
                angle = ((points[i].y-points[j].y)/temp, (points[i].x-points[j].x)/temp)
                #angle = (points[i].y-points[j].y) * 1.0 /(points[i].x-points[j].x)
            if(not table.has_key(angle)):
                table[angle] = 1
            table[angle] += 1
        maxNumOfPoints = max(maxNumOfPoints, max(table.values()) + samePoint)
    if(len(points) == 0):
        return 0
    #print table
    return maxNumOfPoints





class Solution:
    def maxPoints(self, points) -> int:
        res = 0
        for i in range(len(points)):
            xi, yi = points[i]
            same = 0
            s = {"i":1}
            for j in range(i+1, len(points)):
                xj, yj = points[j]
                if xi == xj and yi == yj:
                    same += 1
                elif xi == xj:
                    s["i"] += 1
                else:
                    slope = (yj-yi) / (xj-xi)
                    s[slope] = s.get(slope, 1) + 1
            res = max(res, max(s.values()) +same)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maxPoints([[0,0]]))
    print(s.maxPoints([[1,1],[2,2],[3,3]]))
    print(s.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
    print(s.maxPoints([[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]]))
