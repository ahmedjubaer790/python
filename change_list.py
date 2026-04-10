thelist=["apple","banana","orange"]
#print the specific value of list
print(thelist[1])

#change the value of list
thelist[2]="Magura"
print(thelist)

#value change range
thelist[1:2]=["Mango","Grapes"]
print('After changing the value of list',thelist)

#insert the value in list
thelist.insert(1,"watermelon")
print('After inserting the value in list',thelist)

#append the value in list
thelist.append(input("Enter the value to append in list: "))
print('After appending the value in list',thelist)

#index of list
indlist=thelist.index(input("Enter the value to find index: "))
print('Index of list',indlist)

#print the list index
print(list(range(len(thelist))))

#remove the value from list
thelist.remove("apple")
print('after removing the value from the list',thelist)