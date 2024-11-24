from library import Library


def main():
    library = Library()

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания: "))
                library.add_book(title, author, year)
            except ValueError:
                print("Ошибка: Год должен быть числом.")

        elif choice == "2":
            try:
                book_id = int(input("Введите ID книги для удаления: "))
                library.delete_book(book_id)
            except ValueError:
                print("Ошибка: ID книги должен быть числом.")

        elif choice == "3":
            field = input("Введите поле для поиска (title, author, year): ").lower()
            if field not in ["title", "author", "year"]:
                print("Ошибка: Некорректное поле поиска. Доступные поля: title, author, year.")
                continue
            value = input("Введите значение для поиска: ")
            results = library.search_books(field, value)
            if results:
                for book in results:
                    print(library.format_book(book))
            else:
                print("Книги не найдены.")

        elif choice == "4":
            library.list_books()

        elif choice == "5":
            try:
                book_id = int(input("Введите ID книги: "))
                status = input("Введите новый статус (в наличии/выдана): ").lower()
                library.update_status(book_id, status)
            except ValueError:
                print("Ошибка: ID книги должен быть числом.")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
