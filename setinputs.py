set1_input=input("Enter integers for the first set, separated by spaces: ").split()

set1 =set(map(int,set1_input))

set2_input=input("Enter integers for the second set, separated by spaces: ").split()
set2 =set(map(int,set2_input))

common_set =set1 & set2
print("The common elements between the two sets are:", common_set)