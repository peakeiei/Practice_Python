# while loop
i = 1
while i < 5 :
    print (i)
    i += 1
print('stop')

#for loop
for i in range(5):
    print(i)

#for loop
name = 'peak'
for letter in name:
    print (letter)

#for loop []
name = ['peak','kub']
for i in name:
    print (i)

#nested for loop python
adjs = ['peak','kub','pub']
surname = ['kalayapichet','1','2']

for adj in adjs:
    for i in surname:
        print (adj,i)

#for loop with if and break
word_list = ['peak','paknonkit','kalayapichet']
for i in word_list:
    print(i)
    if i == 'peak':
        break
print('love u')