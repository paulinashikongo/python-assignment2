my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)

my_list.extend([50, 60, 70])

my_list.pop()

my_list.sort()

index_of_30 = my_list.index(30)

print("Final list:", my_list)
print("Index of 30:", index_of_30)
PS C:\Users\user\Desktop\PLP Codes\PLP_Python>  & 'c:\Users\user\AppData\Local\Programs\Python\Python313\python.exe' 'c:\Users\user\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '50481' '--' 'c:\Users\user\Desktop\PLP Codes\PLP_Python\Assignmenttwo.py' 
Final list: [10, 15, 20, 30, 40, 50, 60]
Index of 30: 3

