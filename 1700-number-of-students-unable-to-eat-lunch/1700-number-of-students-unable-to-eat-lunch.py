class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        
        # rotate students queue:
        while students and sandwiches:
        
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            elif sandwiches[0] not in students:
                break
            else:
                students.append(students.pop(0))
        
        return len(students)