#Challenge 30
shopping_list = []
while True:
    item = input('Enter the item: ')
    if item != 'done':
        shopping_list += item
    else:
        shopping_list+=item


#challenge 31
newlist = []
for i in range(5):
    ask = int(input('Number: '))
    newlist += ask
print(newlist)
print(sum(newlist))
print(min(newlist))
print(max(newlist))
print(sum(newlist)/len(newlist))
