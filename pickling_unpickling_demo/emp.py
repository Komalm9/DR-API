class Emp:
    def __init__(self, eid, ename, esalary):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary

    def display(self):
        print(f'Employee Id : {self.eid} \nEmployee Name : {self.ename}\nEmployee Salary: {self.esalary}\n\n')

