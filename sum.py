student_scores =[10,20,30,60,200,50,94,95,100]

total_exam_score =sum(student_scores)

max_exam_score =max(student_scores)

print(total_exam_score)
print(max_exam_score)

sum = 0
for score in student_scores:
    sum +=score
    print(f"Total Sum: {sum}")

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)