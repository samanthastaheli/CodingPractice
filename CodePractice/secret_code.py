from random import randint

code_count = 0

def generate_code(options):
    # function that generates 4 digit codes
    code = ""
    for i in range(4):
        n = options[randint(0,9)]
        code += str(n)
        update_count()
    return code

def match(target, option):
    # function that compares actual code with others
    if target == option:
        return True
    else:
        return False

def update_count():
    global code_count
    code_count += 1
    return code_count

def main(target, options, found):
    global code_count
    correct_code = ""
    while found == False:
        code = generate_code(options)
        # print(code)
        if match(target, code) == True:
            correct_code = code
            found = True
        else:
            pass

    print(f'secret code: {target}')
    print(f'code found: {correct_code}')
    print(f'code count: {code_count}')

main("1234", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False)