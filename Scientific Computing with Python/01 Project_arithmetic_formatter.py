def arithmetic_arranger(problems, show_answers=False):
    # Declare lists for formatting
    arranged_problems = []
    top_row = []
    bottom_row = []
    dashes = []
    answers = []
    
    # If there are too many problems supplied to the function. The limit is five.
    # Check limit number of problems to five
    if len(problems) > 5:
        return "Error: Too many problems."

    # Check every problem part and format
    for problem in problems:
        # Split the problem into parts
        parts = problem.split()
        
        num1 = parts[0]
        operator = parts[1]
        num2 = parts[2]

        # Checking for appropriate operators
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Checking each number (operand) should only contain digits
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."


        # Checking each operand has a max of four digits in width
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculating width of the problem for format
        # A single space between the operator and the longest of the two operands
        width = max(len(num1), len(num2)) + 2
        
        # Format rows. Numbers should be right-aligned.
        top_row.append(num1.rjust(width))
        # A single space between the operator and the longest of the two operands
        bottom_row.append(operator + num2.rjust(width - 1))
        # There should be dashes at the bottom of each problem.
        dashes.append('-' * width)

        # Calculate answer if show_answers=True
        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers.append(answer.rjust(width))

    # Combine rows. There should be four spaces between each problem.
    arranged_problems = '    '.join(top_row) + '\n' + \
                        '    '.join(bottom_row) + '\n' + \
                        '    '.join(dashes)

    # When the second argument is set to True, the answers should be displayed
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

# Test the function
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print("\n")
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))