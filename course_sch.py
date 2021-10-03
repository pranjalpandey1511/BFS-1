# course_sch
# time complexity: O(E+V)
# space complexity: O(E+V)
# Did this code successfully run on Leetcode : NA
# Any problem you faced while coding this : NA

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {}
        graph = defaultdict(list)
        for i in range(numCourses):
            indegree[i] = 0
        
        for elem in prerequisites:
            current_course, prev_course = elem[0], elem[1]
            graph[current_course].append(prev_course)
            indegree[prev_course] += 1
        
        sources = deque()
        
        for element in indegree:
            if indegree[element] == 0:
                sources.append(element)
        
        visited = 0
        
        while sources:
            vertex = sources.popleft()
            visited += 1
            for child in graph[vertex]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources.append(child)
        
        return visited == numCourses