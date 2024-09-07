n = int(input('Enter a number of todo tasks you want : '))
task = []
for i in range(0,n):
    tasks = input('Enter the task ' + str(i+1) + ': ')
    task.append(tasks)
for i in range(0,len(task)):
    print(str(i+1)+" "+task[i])
