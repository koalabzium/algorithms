


def encode(code):
    memo = {}
    if not code[0]:
        return 0
    code += '.'
    if code[1] != '.':
        code = code[:-1]
        counter = countCodes(code[0],code[1:],memo) + countCodes(code[0:2],code[2:],memo)
    else:
        return 1
    return counter


def countCodes(beg, code, memo):
    key = beg + ': ' + code
    if int(beg) > 26:
        return 0
    if not code:
        return 1
    if key in memo:
        return memo[key]
    code += '.'
    if code[1] != '.':
        code = code[:-1]
        to_return = countCodes(code[0], code[1:], memo) + countCodes(code[0:2],code[2:],memo)
    else:
        to_return = 1
    memo[key] = to_return
    return to_return

print(encode('12613'))


