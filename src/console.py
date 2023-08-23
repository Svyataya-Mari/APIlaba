import requests


# Перед запуском этой программы запустить main.py!
if __name__ == '__main__':
    HOST = "localhost"
    PORT = 8080

    inWork = True
    print("Консольный клиент к сервису: \n Выберите команду -  \n"
          "1) Прочитать заметку \n"
          "2) Создать заметку\n"
          "3) Получить информацию о заметке\n"
          "4) Удалить заметку\n"
          "5) Обновить заметку\n"
          "6) Получить список заметок\n"
          "7) Остановить программу\n")
    while inWork:
        choice = int(input("Введите команду: "))
        if choice == 1:
                text = input("Введите текст заметки: ")
                token = input("Введите Ваш токен: ")
                response = requests.post(f"http://{HOST}:{PORT}" + "/createNote", params={"text": text, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 2:
                note_id = int(input("Введите id заметки: "))
                token = input("Введите Ваш токен: ")
                response = requests.get(f"http://{HOST}:{PORT}" + "/getNoteText", params={"id": note_id, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 3:
                note_id = int(input("Введите id заметки: "))
                token = input("Введите Ваш токен: ")
                response = requests.get(f"http://{HOST}:{PORT}" + "/getNoteInfo", params={"note_id": note_id, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 4:
                note_id = int(input("Введите id заметки: "))
                token = input("Введите Ваш токен: ")
                response = requests.delete(f"http://{HOST}:{PORT}" + "/removeNote", params={"note_id": note_id, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 5:
                note_id = int(input("Введите id заметки: "))
                text = input("Введите текст заметки: ")
                token = input("Введите Ваш токен: ")
                response = requests.patch(f"http://{HOST}:{PORT}" + "/updateNote", params={"note_id": note_id, "text": text, "token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 6:
                token = input("Введите Ваш токен: ")
                response = requests.get(f"http://{HOST}:{PORT}" + "/getNotesList", params={"token": token})
                print(f"Status code: {response.status_code}")
                print(f"Response body: {response.text}")
        elif choice == 7:
                inWork = False
        else:
            print("Ошибка! Недопустимое значение. Вводите числа от  1 до 7.")