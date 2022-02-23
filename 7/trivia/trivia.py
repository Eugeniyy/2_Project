# Викторина
# Игра на выбор правильного ответа
# вопросы которой читаются из текстового файла
import sys, pickle
def the_scores(name, scores):
    the_scores1 = open("the_scores.dat", "ab")
    the_scores2 = open("the_scores.txt", "a")
    scores = str(scores)
    pickle.dump(name+ " " + scores, the_scores1)
    the_scores2.write("\n" + name+ " " + scores)
    return the_scores1, the_scores2
def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf8')
    except IOError as e:
        print("Невозможно открыть файл" , file_name , ". Работа будет завершена\n" , e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file
def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/" , "\n")
    return line
def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    score = next_line(the_file)
    if score:
        score = int(score[0])
    category = []
    category.append(next_line(the_file))
    category.append("Количество баллов за этот вопрос -")
    category.append(score)
    category.append("балл(а)!")
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    return category, question, answers, correct, explanation, score
def welcome(title):
    """Приветствует игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру 'Викторина'!\n")
    print("\t\t", title, "\n")
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    scores = 0
    name = input("Введите Ваше имя: ")
    # извлечение первого блока
    category, question, answers, correct, explanation, score = next_block(trivia_file)
    while question:
        # вывод вопроса на экран
        print(category[0], category[1], category[2], category[3])
        print(question)
        for i in range(4):
            print("\t", i + 1, "-" , answers[i])
        # получание ответа
        answer = input("Ваш ответ: ")
        # проверка ответа
        if answer == correct:
            print("\nДа!", end=" ")
            scores += score
        else:
            print("\nНет.", end=" ")
        print(correct, explanation)
        print("Счет:", scores, "\n\n")
        # переход к следующему вопросу
        category, question, answers, correct, explanation, score = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашему счету", scores)
    the_scores(name, scores)
    f = open("the_scores.dat" , "rb")
    string = pickle.load(f)
    print("Вот список рекордов:\n", string)
    while string:
        try:
            string = pickle.load(f)
            print(string)
        except EOFError:
            break
    f.close()
main()
input("\n\nНажмите Enter, чтобы выйти.")
