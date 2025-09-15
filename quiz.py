
quiz_questions = {
    "What is the capital of France?": "Paris",
    "Who wrote the play 'Romeo and Juliet'?": "Shakespeare",
    "What is 9 x 9?": "81",
    "Which planet is known as the Red Planet?": "Mars",
    "Who painted the Mona Lisa?": "Da Vinci",
    "What is the largest mammal in the world?": "Blue Whale",
    "What year did World War II end?": "1945",
    "Which gas do plants absorb from the atmosphere?": "Carbon Dioxide",
    "Who is known as the Father of Computers?": "Charles Babbage",
    "What is the boiling point of water in Celsius?": "100"
}
questions_tuple=(tuple(quiz_questions.keys()))
answers_tuple=(tuple(quiz_questions.values()))
count =0
while True:
    user_option = str(input('Do you want to play ? (y/n)  ')).lower()
    if user_option == 'y'or user_option == 'yes':
        for q,a in zip(questions_tuple, answers_tuple):
            # print(q)
            while True:
                count11 = 0

                answer = str(input(q + ":"))
                if answer.strip().lower() == a.lower():
                    print(f'Correct! {q} is {a}')
                    count += 1
                    print(f'your streak is {count}🔥')
                    break
                else:
                    while True:

                        print(f'Incorrect!')
                        answer = str(input(q + ":"))
                        count11 += 1
                        if count11 >= 2:
                            help = str(input(f'want answer type help :')).strip().lower()
                            if help == 'help':
                                print(f' {q} is {a}')
                                break


                        continue
            continue


    elif user_option == 'n' or user_option == 'no':
        print('Thank you for playing!')
        break
#