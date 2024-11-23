user_inputs =input("Enter a list of integers separated by spaces: ")

input_list = [int(x) for x in user_inputs.split()]

total_sum=sum(input_list)

print(f"The sum of the integers is:", total_sum)