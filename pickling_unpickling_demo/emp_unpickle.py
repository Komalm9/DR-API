import emp, pickle
f = open('emp.csv','rb')
print('Employee Details : \n')

while(1):
    try:
        x1 = pickle.load(f)
        x1.display()
    except EOFError:
        print('End of file reached---')
        break

f.close()    

