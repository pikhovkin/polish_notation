#-------------------------------------------------------------------------------
# Name:        polish_notation
# Purpose:
#
# Author:      Sergey Pikhovkin
#
# Created:     01.04.2011
#-------------------------------------------------------------------------------

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

class CorrectExpressionError(Exception):
    pass

def compute_polish_notation(polish_notation):
    elements = polish_notation.split()
    operators = '*/+-'
    stack = []
    expression = None
    for elem in elements:
        if elem in operators:
            if not stack:
                raise CorrectExpressionError
            elif expression is None:
                expression = stack.pop()
        else:
            try:
                f = float(elem)
            except ValueError:
                raise CorrectExpressionError
            stack.append(int(f) if f.is_integer() else f)
            continue

        try:
            if '*' == elem:
                expression *= stack.pop()
            elif '/' == elem:
                expression /= float(stack.pop())
            elif '+' == elem:
                expression += stack.pop()
            elif '-' == elem:
                expression -= stack.pop()
        except IndexError:
            raise CorrectExpressionError

    if stack:
        raise CorrectExpressionError

    return expression

def main():
    try:
        print(compute_polish_notation('5 8 3 + *'))
    except CorrectExpressionError:
        print('Enter the correct expression')

if __name__ == '__main__':
    main()
