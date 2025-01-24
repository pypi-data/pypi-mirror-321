from matrices import Matrix

def __decodeEquation__(equation: str) -> list:
    equation1 = equation.replace(' ', '')
    attributes = []

    sum = float(equation1.split('=')[1].strip())
    attributes.append(sum)

    equation_sub = equation1.split('=')[0]

    breakdown = []
    current = []

    for char in equation_sub:
        if char == '+' or char == '-':
            if current:
                breakdown.append(current)
            breakdown.append(char)
            current = []
        else:
            current.append(char)

    breakdown.append(current)

    for i in range(len(breakdown)):
        if i == 0 and breakdown[0] != '-':
            if len(breakdown[0]) == 1:
                attributes.append([f'{breakdown[0][-1]}', 1.0])
            else:
                attributes.append([f'{breakdown[0][-1]}', float(''.join(breakdown[0])[:-1])])
        elif breakdown[i] == '+' or breakdown[i] == '-':
            continue
        else:
            if len(breakdown[i]) == 1:
                attributes.append([f'{breakdown[i][-1]}', 1.0 if breakdown[i-1] == '+' else -1.0])
            else:
                attributes.append([f'{breakdown[i][-1]}', (float(''.join(breakdown[i])[:-1])*1 if breakdown[i-1] == '+' else float(''.join(breakdown[i])[:-1])*-1)])
    
    return attributes


# deesired decoded output [2, ['x', 2], ['y', 5]]

def solveSim(*equations):
    lines = []
    linesB = []
    vars = []
    for equation in equations:
        attributes = __decodeEquation__(equation)

        if not vars:
            for i in range(len(attributes)-1):
                vars.append(attributes[i+1][0])

        line = []
        for i in range(len(attributes)-1):
            line.append(attributes[i+1][1])
        
        lines.append(line)
        linesB.append([attributes[0]])

    A = Matrix(lines)
    B = Matrix(linesB)
    A_INVERSE = A.inverse()
    X_MATRIX = A_INVERSE*B

    solution = []
    for i in range(len(vars)):
        solution.append({vars[i]: round(X_MATRIX.matrix[i][0],2)})
    
    return solution

