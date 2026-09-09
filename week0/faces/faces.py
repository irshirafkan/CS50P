def convert(text):
     text = text.replace(":)", "🙂")
     text = text.replace(":(", "🙁")
     return text

def main(): 
    user_input = input() 
    output = convert(user_input) 
    print(output)

main()    