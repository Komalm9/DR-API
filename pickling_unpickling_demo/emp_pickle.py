import emp, pickle
f = open('emp.dat','wb')
no_of_employees = int(input("Enter the number of employees ? "))

for n in range(no_of_employees):
    eid = int(input('Enter employee Id : '))
    ename = input('Enter employee name : ')
    esalary = int(input('Enter employee salary : '))

    e = emp.Emp(eid, ename, esalary)
    x = pickle.dump(e,f)

f.close()   
 
