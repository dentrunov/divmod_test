from tkinter import *
import tkinter.font as tkFont
from random import choice, randint

from config import NUM

def get_tasks(num):
    """Легкие задания вида x // y"""
    tasks = [f"{randint(10,100)} {choice(OPERATIONS)} {randint(2,20)} =" for i in range(num)]
    answers = [eval(task.replace("=", "")) for task in tasks]
    return tasks, answers

def get_hard_tasks():
    """Сложные задания вида x % y // m - TODO реализовать"""

def check():
    """Функция проверки"""
    counter = 0
    for i in range(NUM):
        if entries[i].get() == str(answers[i]):
            entries[i]["bg"] = "GREEN"
            counter += 1
        else:
            entries[i]["bg"] = "RED"
    mark = counter // 5 + 1

    result_label1["text"] = f"Правильных ответов: {counter}"
    result_label1["bg"] = MARK_COLORS[mark]
    result_label2["text"] = f"Ваша оценка: {mark}"
    result_label2["bg"] = MARK_COLORS[mark]

def put_answer(event):
    for i in range(NUM):
        if entries[i].get():
            checking[i] = 1
    if sum(checking) == NUM:
        check_button["state"] = "active"
    
def start():
    root.geometry("400x900")
    
COLORS = ["GREEN", "YELLOW", "WHITE", "GREEN", "BLUE", "PINK", "GREY"]
COLOR = choice(COLORS)
MARK_COLORS = {5: "GREEN", 4: "YELLOW", 3: "ORANGE", 2: "RED", 1: "GREY"}
OPERATIONS = ["//", "%"]
checking = [0] * NUM

root = Tk()
root.geometry("400x100")
root.title("Тестирование по целочисленному делению Python")
root.configure(background=COLOR)
root.resizable(False, False)

fontObj = tkFont.Font(size=16)


# создаем вопросы и поля для них
tasks, answers = get_tasks(NUM)
name_label = Label(text="Ваше имя и фамилия", bg=COLOR)
name_entry = Entry(width=15, font=fontObj)
button_start = Button(text="Начать", width=10, command=start)
labels = [Label(text=f"{i+1}. {tasks[i]}", width=15, font=fontObj, bg=COLOR) for i in range(NUM)]
entries = [Entry(width=10, font=fontObj) for i in range(NUM)]
check_button = Button(text="Проверить", width=10, font=fontObj, state="disabled", command=check)
result_label1= Label(width=20, font=fontObj)
result_label2= Label(width=20, font=fontObj)

# проверка заполняемости всех полей ответов
checking = [0] * NUM
for i in range(NUM):
    entries[i].bind("<ButtonRelease-1>", put_answer)

# выставляем виджеты на окно
name_label.grid(row=0, column=0, columnspan=2)
name_entry.grid(row=1, column=0, columnspan=2)
button_start.grid(row=2, column=0, columnspan=2, pady=20)

for row in range(NUM):
    labels[row].grid(row=row+3, column=0)
    entries[row].grid(row=row+3, column=1)

check_button.grid(row=NUM + 4, column=0, columnspan=2)
result_label1.grid(row=NUM + 5, column=0, columnspan=2)
result_label2.grid(row=NUM + 6, column=0, columnspan=2)

# запускаем программу
root.mainloop()


