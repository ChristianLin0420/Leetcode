"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {}

        for e in employees:
            employee_map[e.id] = e
        
        def dfs(employee: 'Employee') -> int:
            
            if len(employee.subordinates) == 0:
                return employee.importance
            
            subords = employee.subordinates
            tot_importance = 0
            
            for subord in subords:
                tot_importance +=dfs(employee_map[subord])
            
            return tot_importance + employee.importance
        
        employee = employee_map[id]
        
        return dfs(employee)