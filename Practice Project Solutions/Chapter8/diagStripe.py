import time
og_list = []
new_list =[]
for i in range(50):
    exp = i*'O'
    og_list.append(exp.rjust(i , '.') + (50 -i)*'.')
for i in range(50):
    newexp = i * 'O'
    new_list.append((50-i)*'.' + newexp.rjust(i , '.'))
og_list = og_list
new_list = new_list
reversed_list = list(reversed(new_list))
while True:
    for i in og_list:
        print(i)
        time.sleep(0.01)
    for j in reversed_list:
        print(j)
        time.sleep(0.01)