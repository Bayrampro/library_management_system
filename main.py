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
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)

        elif choice == "2":
            book_id = int(input("Введите ID книги для удаления: "))
            library.delete_book(book_id)

        elif choice == "3":
            field = input("Введите поле для поиска (title, author, year): ").lower()
            value = input("Введите значение для поиска: ")
            library.search_books(field, value)

        elif choice == "4":
            library.list_books()

        elif choice == "5":
            book_id = int(input("Введите ID книги: "))
            status = input("Введите новый статус (в наличии/выдана): ")
            library.update_status(book_id, status)

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
