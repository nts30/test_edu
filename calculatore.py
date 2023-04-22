def calculate(expression):
    """Выполняет 1 математическую операцию +,-,*,/ над 2-мя значениями

    :param expression: выражение
    :return: результат
    """
    allowed = ('+', '-', '*', '/')
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Выражение должно содержать один из арифмитических знаков: {" ".join(allowed)}')

    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)

                # if sign == '*':
                #    return left * right
                # elif sign == '+':
                #    return left + right
                # elif sign == '-':
                #    return left - right
                # elif sign == '/':
                #    return left / right

                result = {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a * b,
                }
                return result[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError('Выражение должно содержать 2 целых числа и 1 знак')


calculate('2 * 5')
