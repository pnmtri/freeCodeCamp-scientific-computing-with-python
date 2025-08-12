def arithmetic_arranger(problems, show_answers=False):
    
    # First constraint
    if len(problems) > 5:
        return 'Error: Too many problems.'
        
    # BREAKING DOWN THE FORMAT 
    first_operands = [first_operand.split()[0] for first_operand in problems]    # List of first operands
    operators = [operator.split()[1] for operator in problems]  # List of operators
    second_operands = [second_operand.split()[2] for second_operand in problems]  # List of second operands
    
    # Constraints for input 
    for i in range(len(problems)):
        if operators[i] not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        if not first_operands[i].isdigit() or not second_operands[i].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(first_operands[i]) > 4 or len(second_operands[i]) > 4 or len(first_operands[i]) < 1 or len(second_operands[i]) < 1:
            return 'Error: Numbers cannot be more than four digits.'
    
# BREAKING DOWN ELEMENTS OF EACH PROBLEM
    answers = [(int(first_operands[i]) + int(second_operands[i])) if operators[i] == '+' else (int(first_operands[i]) - int(second_operands[i])) for i in range(len(problems))] # List of answers
    width = [max(len(first_operands[i]), len(second_operands[i])) for i in range(len(problems))]    # Width of each problem block when formatting
    dashes = ['-'*(width[i] + 2) for i in range(len(problems))]   # List of dashes used for formatting
    
    # MODIFYING LIST1 AND LIST2 
    # Space multipliers for each line presented
    space_l1 = []   # List of space multipliers for list 1
    space_l2 = []   # List of space multipliers for line 2
    space_al = []   # List of space multipliers for answer line
    for i in range(len(problems)):
        space_l1.append(len(dashes[i]) - len(first_operands[i]))
        space_l2.append(len(dashes[i]) - len(second_operands[i]) - 1)
        space_al.append(len(dashes[i]) - len(str(answers[i])))
    
    #LINES OF OPERATIONS
    line_1 = [(' '*space_l1[i]) + first_operands[i] for i in range(len(problems))] # First operands
    line_2 = [operators[i] + (" " * space_l2[i]) + second_operands[i] for i in range(len(problems))] # Operators and second operands
    answer_line = [(" " * space_al[i]) + str(answers[i]) for i in range(len(problems))]
    
    # FORMATTING THE PROBLEMS
    # Format without answers
    arranged_format = ("    ".join(line_1) + "\n" +
                "    ".join(line_2) + "\n" +
                "    ".join(dashes)
    )
    # Format with answers included
    if show_answers:
        return arranged_format + "\n" + "    ".join(answer_line)
    else:
        return arranged_format

# TESTING CALLS
#print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
#print(arithmetic_arranger(["1 + 2", "1 - 9380"]))
#print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
#print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))
#print(arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]))
#print(arithmetic_arranger(["3 + 855", "988 + 40"], True))
#print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))





