from django.shortcuts import render
import re


def calculate(request):
    context = {}
    context['digit'] = ''
    context['previous'] = ''
    ans = '0'

    if 'pre' in request.POST:
        str_previous = request.POST['pre']
    else:
        ans = '0'
        str_previous = '#0'

    if 'number' in request.POST:
        str_num = request.POST['number']
        if str_previous[0] == '#':
            str_previous = ''
        if str_previous == 'MathError!' or str_previous == '#MathError!':
            str_previous = ''

        str_previous += str_num

        expression = re.split(r'[+\-×÷]', str_previous)
        if str_previous[0] == '-':
            if len(expression) == 3:
                ans = expression[2]
            else:
                ans = expression[1]
        else:
            if len(expression) == 2:
                ans = expression[1]
            else:
                ans = expression[0]

    if 'operator' in request.POST:
        str_operator = request.POST['operator']

        if str_previous == 'MathError!' or str_previous == '#MathError!':
            str_previous = '0'
            ans = '0'
        if str_previous[0] == '#':
            ans = str_previous[1:len(str_previous)]
            str_previous = ans + str_operator
        else:
            if str_previous[0] == '-':
                if str_previous[len(str_previous) - 1] == '+' or str_previous[len(str_previous) - 1] == '-' or  str_previous[len(str_previous) - 1] == '×' or  str_previous[len(str_previous) - 1] == '÷':
                    ans = str_previous[1:(len(str_previous) - 1)]
                    str_previous = ans + str_operator
                elif ('+' in str_previous[1:len(str_previous)]) or ('-' in str_previous[1:len(str_previous)]) or ('×' in str_previous[1:len(str_previous)]) or ('÷' in str_previous[1:len(str_previous)]):
                    ans = getResult(str_previous)
                    str_previous = ans + str_operator
                else:
                    ans = str_previous
                    str_previous = ans + str_operator
            else:
                if str_previous[len(str_previous) - 1] == '+' or str_previous[len(str_previous) - 1] == '-' or  str_previous[len(str_previous) - 1] == '×' or  str_previous[len(str_previous) - 1] == '÷':
                    ans = str_previous[0:(len(str_previous) - 1)]
                    str_previous = ans + str_operator
                elif ('+' in str_previous) or ('-' in str_previous) or ('×' in str_previous) or ('÷' in str_previous):
                    ans = getResult(str_previous)
                    str_previous = ans + str_operator
                else:
                    ans = str_previous
                    str_previous = ans + str_operator

    if 'equal' in request.POST:
        if str_previous[0] == '#':
            # str_previous is unchanged
            str_previous = str_previous
            ans = str_previous[1:len(str_previous)]
        else:
            if str_previous[0] == '-':
                if str_previous[len(str_previous) - 1] == '+' or str_previous[len(str_previous) - 1] == '-' or str_previous[len(str_previous) - 1] == '×' or str_previous[len(str_previous) - 1] == '÷':
                    ans = str_previous[0:(len(str_previous) - 1)]
                    str_previous = '#' + ans
                elif ('+' in str_previous[1:len(str_previous)]) or ('-' in str_previous[1:len(str_previous)]) or ('×' in str_previous[1:len(str_previous)]) or ('÷' in str_previous[1:len(str_previous)]):
                    ans = getResult(str_previous)
                    str_previous = '#' + ans
                else:
                    ans = str_previous
                    str_previous = '#' + ans
            else:
                if str_previous[len(str_previous) - 1] == '+' or str_previous[len(str_previous) - 1] == '-' or  str_previous[len(str_previous) - 1] == '×' or  str_previous[len(str_previous) - 1] == '÷':
                    ans = str_previous[1:(len(str_previous) - 1)]
                    str_previous = '#' + ans
                elif ('+' in str_previous) or ('-' in str_previous) or ('×' in str_previous) or ('÷' in str_previous):
                    ans = getResult(str_previous)
                    str_previous = '#' + ans
                else:
                    ans = str_previous
                    str_previous = '#' + ans

    context['digit'] = ans
    context['previous'] = str_previous
    return render(request, "CalculatorFrame.html", context)


def getResult(str_previous):
    expression = re.split(r'[+ \- ×÷]', str_previous)
    operator = ''

    i = len(str_previous) - 1
    flag = True
    while i >= 0 and flag:
        i = i - 1
        if str_previous[i] == '+' or str_previous[i] == '-' or str_previous[i] == '×' or str_previous[i] == '÷':
            operator = str_previous[i]
            flag = False

    if len(expression) == 3:
        firstNum = '-' + expression[1]
        secondNum = expression[2]
    elif len(expression) == 2:
        firstNum = expression[0]
        secondNum = expression[1]
    else:
        return '0'

    if operator == '+':
        return str(int(float(firstNum) + float(secondNum)))
    elif operator == '-':
        return str(int(float(firstNum) - float(secondNum)))
    elif operator == '×':
        return str(int(float(firstNum) * float(secondNum)))
    else:
        if float(secondNum) == 0:
            return 'MathError!'
        return str(int(float(firstNum) / float(secondNum)))

