my_list =[]
my_list.append(10)
my_list.append(20)
my_list.append(40)
my_list.append(30)

my_list.insert(1,15)

another_list =[50,60,70]

my_list.extend(another_list)

my_list.pop()

my_list.sort()

index_of_30=my_list.index(30)


print(f"list values: ",my_list)

print(f"Index of 30 is ", index_of_30)