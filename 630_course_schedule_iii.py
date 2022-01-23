def scheduleCourse(self, A):
    pq = []
    start = 0
    for t, end in sorted(A, key = lambda (t, end): end):
        start += t
        heapq.heappush(pq, -t)
        while start > end:
            start += heapq.heappop(pq)
    return len(pq)





class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        res = 0
        courses = [course for course in courses if course[0] <= course[1]]
        courses.sort(key= lambda course: course[1])
        s = [[course[0], 1] for course in courses]
        for i in range(len(courses)):
            duration, lastday = courses[i]
            for j in range(0, i):
                if lastday-duration >= s[j][0]:
                    if s[j][1]+1 > s[i][1] or (s[j][1]+1 == s[i][1] and s[j][0]+duration < s[i][0]):
                        s[i][0] = s[j][0] + duration
                        s[i][1] = s[j][1] + 1
            res = max(res, s[i][1])
        return res
