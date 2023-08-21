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

file = "notes.json"
def vvod():
    vizov = int (input('Введите команду: \n1 - Вывод всех данных \n2 - Добавление заметки \n3 - Поиск заметки \n4 - Удаление заметки \n5 - Редактировние заметки \n:'))
    return vizov

def vivod_dannih(file):
    with open(file, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
        # print (type(json_data))
        # print(json_data["notes"])
        for item in json_data["notes"]:
            print (f'{item["id"]}; {item["header"]:>8}; {item["body"]:>20}; {item["noteData"]:>15} {item["noteTime"]:>10}')
    f.close()
    return True

def add_note(file):
    input_id = input('Введите идентификатор id: ')
    input_header = input('Заголовок заметки: ')
    input_body = input('Тело заметки: ')
    input_noteData = strftime("%Y.%m.%d") # 2017.04.05
    input_noteTime = strftime("%H:%M:%S") # 00:18:00
    new_data = {"id": input_id, "header": input_header, "body": input_body, "noteData": input_noteData, "noteTime": input_noteTime}
    with open(file, mode='r', encoding='UTF-8') as f:
        data = json.load(f)
        data["notes"].append(new_data)
        with open(file, mode='w', encoding= 'UTF-8') as f:
            json.dump(data, f, ensure_ascii= False, indent=2)
        print("Запись успешно добавлена")
    f.close()
    return True

def search_note(file):
    with open(file, mode='r', encoding='UTF-8') as f:
        data = json.load(f)
        poisk = input('Введите данные для поиска: ')
        for item in data["notes"]:
            if (str(item ["noteData"]).__contains__(poisk)):
                print(item)
    f.close()
    return True

def del_data (file):
    with open(file, mode='r', encoding='UTF-8') as f:
        data = json.load(f)
        poisk = input('Введите id записи для удаления: ')
        vvod_param = int (input('Подтвердите удаление записи: \n1 - Подтвердить \n2 - Отменить \n'))
        if vvod_param == 1:
            for item in data["notes"]:
                if (str(item ["id"])==(poisk)):
                    print(f'Выбрана запись для удаления: \n {item["id"]}; {item["header"]:>8}; {item["body"]:>15}; {item["noteData"]}; {item["noteTime"]}')
                    # del item["header"]
                    # del item["body"]
                    # del item["noteData"]
                    # del item["noteTime"]
                    del item
                    print (data)
            with open(file, mode='w', encoding= 'UTF-8') as f:
                json.dump(data, f, ensure_ascii= False, indent=2)
                print (f'Удалена заметка с id = {poisk}')
    f.close()
    return True

def edit_data (file):
    with open(file, 'r', encoding='UTF-8') as f:
        json_data = json.load(f)
        vvod_id = int (input('Введите id записи для редактирования: '))
        for item in json_data["notes"]:
            # print(item["id"])
            if vvod_id == int(item["id"]):
                print (f'Выбрана запись для изменения: \n {item["id"]}; {item["header"]:>8}; {item["body"]:>15}; {item["noteData"]}')
                vvod_param = int (input('Введите параметр записи для редактирования: \n1 - id заметки \n2 - Заголовок заметки \n3 - Тело заметки \n'))
                if vvod_param == 1:
                    print (item["id"])

                elif vvod_param == 2:
                    print (item ["header"])
    print("Заметка успешно изменена")
    f.close()
    return True


input_ = vvod()

if input_ ==1:
    vivod_dannih(file)
elif input_ ==2:
    add_note(file)
elif input_ ==3:
    search_note(file)
elif input_ ==4:
    del_data(file)
elif input_ ==5:
    edit_data(file)
else:
    print("Выбран недопустимый параметр! Попробуйте снова! ")

