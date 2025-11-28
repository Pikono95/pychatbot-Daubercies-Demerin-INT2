def ask_text(text):
    a = 0
    while a == 0 or a == None or a == '':
        a = input(text)
    return a.strip()
def ask_choice(message, option):
    a = 0
    while a == 0:
        print(message, end='\n')
        for i in range(len(option)):
            print(str(i+1)+". "+option[i])
        a = int(input()) 
    return option[a-1]
