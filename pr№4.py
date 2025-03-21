import threading
import time
import os
import json


users_file = "users.json"
notes_file = "notes.json"
current_user = None
last_activity_time = time.time()
activity_timeout = 60

def check_user_activity():
    global last_activity_time
    while True:
        time.sleep(10)
        if time.time() - last_activity_time > activity_timeout:
            print("\nВы были неактивны слишком долго. Программа завершается.")
            save_notes_to_file()
            exit()


def update_last_activity():
    global last_activity_time
    last_activity_time = time.time()


def load_users():
    if os.path.exists(users_file):
        with open(users_file, "r") as file:
            return json.load(file)
    return {}

def save_users(users):
    with open(users_file, "w") as file:
        json.dump(users, file)


def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    return {}


def save_notes_to_file():
    global current_user
    notes = load_notes()
    if current_user and current_user in notes:
        with open(notes_file, "w") as file:
            json.dump(notes, file)


def auto_save_notes():
    while True:
        time.sleep(30)
        save_notes_to_file()


def register():
    users = load_users()
    username = input("Введите имя пользователя: ")
    if username in users:
        print("Пользователь уже существует.")
        return False
    password = input("Введите пароль: ")
    users[username] = password
    save_users(users)
    print("Регистрация успешна.")
    return True


def login():
    global current_user
    users = load_users()
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if username in users and users[username] == password:
        current_user = username
        print(f"Добро пожаловать, {username}!")
        return True
    print("Неверное имя пользователя или пароль.")
    return False


def add_note(notes):
    update_last_activity()
    note = input("Введите текст заметки: ")
    if current_user not in notes:
        notes[current_user] = []
    notes[current_user].append(note)
    print("Заметка добавлена.")


def view_notes(notes):
    update_last_activity()
    if current_user in notes and notes[current_user]:
        print("Ваши заметки:")
        for i, note in enumerate(notes[current_user], 1):
            print(f"{i}. {note}")
    else:
        print("У вас пока нет заметок.")


def main():
    global current_user
    threading.Thread(target=check_user_activity, daemon=True).start()
    threading.Thread(target=auto_save_notes, daemon=True).start()

    notes = load_notes()

    while True:
        if not current_user:
            print("\n1. Регистрация\n2. Авторизация\n3. Выход")
            choice = input("Выберите действие: ")
            if choice == "1":
                register()
            elif choice == "2":
                if login():
                    continue
            elif choice == "3":
                print("До свидания!")
                break
            else:
                print("Неверный выбор.")
        else:
            print("\n1. Добавить заметку\n2. Просмотреть заметки\n3. Выход")
            choice = input("Выберите действие: ")
            if choice == "1":
                add_note(notes)
            elif choice == "2":
                view_notes(notes)
            elif choice == "3":
                print("До свидания!")
                save_notes_to_file()
                break
            else:
                print("Неверный выбор.")

if __name__ == "__main__":
    main()