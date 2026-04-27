# marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# print(marks)
# print(len(marks))
# print(marks[0])
# print(marks[1])

# student = ["Karan" , 95.4,17,"Delhi"]
# print(student[0])
# student[0] = "arjun"
# print(student)

#list slicing
marks = [85, 94, 76, 63,48]
print(marks[-3:-1])
 
list = [ 2, 1, 3]
print(list.append(4))
print(list.sort())
print(list)

# sort 
list = ['a' , 'b' ,'c' , 'd', 'e']
print(list.sort())
print(list)
# reerse
list = ['a' , 'b' ,'c' , 'd', 'e']
list.reverse()
print(list)
# insert
list = [2,1,3]
list.insert(1,5)
print(list)

#remove
list = [2,1,3]
list.pop(2)
print(list)
#tuple
tup = (1,2,3,4)
print(tup)
print(type(tup))
# insert 
tup = (1,2,3,4)
print(tup.index(2))
#count
tup = (1,2,3,4,2,2)
print(tup.count(2))