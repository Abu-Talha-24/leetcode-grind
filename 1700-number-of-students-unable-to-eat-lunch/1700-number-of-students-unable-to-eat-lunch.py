class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        
        while students and sandwiches:
            if sandwiches[0] not in students:
                return len(students)
            
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                students.append(students.pop(0))
        
        return 0