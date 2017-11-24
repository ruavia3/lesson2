answers = {
    "привет": "Привет!",
    "как дела": "Отлично, а у тебя как?",
    "Пока!": "Еще увидимся"
    }
    
def get_answer(question, answers):
    return answers.get(question)
    
def ask_user(answers):
    
    #while True:
        try:
            user_input = input ("Скажи что-нибудь?\n")
            answer = get_answer(user_input,answers)
            if answer == None:
                print ("ну-ну")
            else:
                print(answer)
        #if user_input == "Пока!":
        #    break
        except KeyError:
            print ("даже не знаю, что сказать")
        except KeyboardInterrupt:
            print("через Ctrl-Z не выходит")
        
        ask_user(answers)

ask_user(answers)