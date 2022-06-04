import threading
from random import randint

code_count = 0
thread_count = 0
found = False

def generate_code(options):
    # function that generates 4 digit codes
    code = ""
    for i in range(4):
        n = options[randint(0,9)]
        code += str(n)
        update_code_count()
    return code

def match(target, option):
    # function that compares actual code with others
    if target == option:
        return True
    else:
        return False

def update_code_count():
    global code_count
    code_count += 1
    return code_count

def update_thread_count():
    global thread_count
    thread_count += 1
    return thread_count

# class use_thread(threading.Thread):
#     def __init__(self):
#         self.target = "1234"
#         self.code = ""
#         self.correct_code = ""
#         # self.found = False
#         self.options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#     def run(self):
#         global found
#         self.code = generate_code()
#         if match(self.target, self.code) == True:
#             self.correct_code = self.code
#             found = True
#             return self.correct_code

def run_thread(target, options):
    global code_count
    global thread_count
    global found
    correct_code = ""

    update_thread_count()

    while found == False:
        code = generate_code(options)
        # print(code)
        if match(target, code) == True:
            correct_code = code
            found = True
        else:
            pass

def main():
    global code_count
    global thread_count
    global found

    target = "1234"
    options = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
    while found == False:
        # thread = use_thread()
        # update_thread_count()
        t = threading.Thread(target=run_thread, args=(target, options))
        t.start()
        t.join()

    print(f'secret code: {t.target}')
    print(f'code found: {t.correct_code}')
    print(f'code count: {code_count}')

if __name__ == "__main__":
    main()