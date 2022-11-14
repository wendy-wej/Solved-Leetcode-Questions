from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stud = deque(students)
        while stud and sandwiches:
            if sandwiches[0] in stud:
                if stud[0] == sandwiches[0]:
                    sandwiches.pop(0)
                    stud.popleft()
                else:
                    stud.append(stud.popleft())
            else:
                return len(stud)
        return len(stud)
        