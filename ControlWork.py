# Необходимо написать проект, содержащий функционал работы с заметками.
# Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.
# ***Для сдачи проекта необходимо создать отдельный общедоступный репозиторий (Github, gitlub, или Bitbucket).
# Разработку вести в этом репозитории, использовать пул реквесты на изменения.
# Приложение должно:
# * запускаться без ошибок,
# * должно уметь сохранять данные в файл,
# * уметь читать данные из файла,
# * делать выборку по дате,
# * выводить на экран выбранную запись,
# * выводить на экран весь список записок,
# * добавлять записку, редактировать ее и удалять.
# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки.
# Сохранение заметок необходимо сделать в формате json или csv формат
# (разделение полей рекомендуется делать через точку с запятой).

import datetime
from time import strftime
import json

file_path = "notes.json"
def vvod():
    vizov = int (input('Введите команду: \n1 - Вывод всех данных \n2 - Добавление заметки \n3 - Поиск заметки \n4 - Удаление заметки \n5 - Редактировние заметки \n:'))
    return vizov

def vivod_dannih(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
        # print (type(json_data))
        # print(json_data["notes"])
        for item in json_data["notes"]:
            print (f'{item["id"]}; {item["header"]:>8}; {item["body"]:>15}; {item["noteData"]}')
    return True

def add_contact(file_path):
    with open(file_path, 'a', encoding='UTF-8') as f:
        id = input('Введите идентификатор id: ')
        header = input('Заголовок заметки: ')
        body = input('Тело заметки: ')
        noteData = strftime("%Y-%m-%d-%H.%M.%S") # 2017-04-05-00.18.00
        print(f'Контакт успешно добавлен --> {id} {header} {body} {noteData}')
        f.write ('\n' + f'{id};{header};{body};{noteData}')
    return True

def search_cont(file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        poisk = input('Введите данные контакта: ')
        for line in f:
            if poisk in line:
                mass = line.strip().split(';')
                for i in range(len(mass)):
                    print(mass[i], end=" ")
                print("")
        f.read()
    return True

def del_data (file_path):
    with open(file_path, 'r', encoding='UTF-8') as fi:
        lines = fi.readlines()
        fi.close()
    with open(file_path, 'w', encoding='UTF-8') as f:
        poisk = input('Введите данные заметки для удаления: ')
        for line in lines:
            if poisk not in line:
                f.write(line)
        f.close()
    print("Заметка успешно удалена")
    return True

def edit_data (file_path):
    with open(file_path, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
        vvod_id = int (input('Введите id записи для редактирования: '))
        for item in json_data["notes"]:
            # print(item["id"])
            if vvod_id == int(item["id"]):
                print (f'Выбрана запись для изменения: \n {item["id"]}; {item["header"]:>8}; {item["body"]:>15}; {item["noteData"]}')
                vvod_param = int (input('Введите параметр записи для редактирования: \n1 - id заметки \n2 - Заголовок заметки \n3 - Тело заметки \n'))
                if vvod_param == 1:
                    print (item["id"])
    print("Заметка успешно изменена")
    return True


input_ = vvod()

if input_ ==1:
    vivod_dannih(file_path)
elif input_ ==2:
    add_contact(file_path)
elif input_ ==3:
    search_cont(file_path)
elif input_ ==4:
    del_data(file_path)
elif input_ ==5:
    edit_data(file_path)
else:
    print("Выбран недопустимый параметр! Попробуйте снова! ")

