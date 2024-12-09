def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator."

        operand1, operator, operands2 = parts

        if not operand1.isdigit() or not operands2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(operand1) > 4 or len(operands2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        result = 0

        if operator == "+":
            result = int(operand1) + int(operands2)
        elif operator == "-":
            result = int(operand1) - int(operands2)

        width = max(len(operand1), len(operands2)) + 2

        first_line.append(operand1.rjust(width))
        second_line.append(operator + " " + operands2.rjust(width - 2))

        dashes_line.append("-" * width)

        if show_answers:
            answers_line.append(str(result).rjust(width))

    arranged = (
        "    ".join(first_line)
        + "\n"
        + "    ".join(second_line)
        + "\n"
        + "    ".join(dashes_line)
    )

    if show_answers:
        arranged += "\n" + "    ".join(answers_line)

    return arranged


# print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
print(f'\n{arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])}')
print(
    f'\n{arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])}'
    f'\n{arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])}'
    f'\n{arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])}'
    f'\n{arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])}'
    f'\n{arithmetic_arranger(["3 + 855", "988 + 40"], True)}'
    f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}'
)
