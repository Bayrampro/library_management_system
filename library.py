import json
import os
from typing import List, Dict

DATA_FILE = "storage.json"

class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self) -> List[Dict]:
        """Загружает книги из JSON-файла."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    print("Ошибка чтения данных из файла. Файл повреждён или пуст.")
                    return []
        else:
            print("Файл данных не найден, создаём новый.")
            return []

    def save_books(self):
        """Сохраняет книги в JSON-файл."""
        with open(DATA_FILE, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title: str, author: str, year: int) -> None:
        """Добавляет новую книгу в библиотеку."""
        new_book = {
            "id": len(self.books) + 1,
            "title": title,
            "author": author,
            "year": year,
            "status": "в наличии",
        }
        self.books.append(new_book)
        self.save_books()
        print(f"Книга '{title}' добавлена с ID {new_book['id']}.")

    def delete_book(self, book_id: int) -> None:
        """Удаляет книгу по ID."""
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                self.save_books()
                print(f"Книга с ID {book_id} удалена.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    def search_books(self, field: str, value: str) -> list:
        """
         Поиск книг по указанному полю и значению.

         """
        results = [book for book in self.books if str(book.get(field, '')).lower() == value.lower()]
        return results

    def list_books(self):
        """Выводит список всех книг."""
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(self.format_book(book))

    def update_status(self, book_id, status):
        """Обновляет статус книги."""
        if status not in ["в наличии", "выдана"]:
            print("Неверный статус. Допустимые значения: 'в наличии', 'выдана'.")
            return
        for book in self.books:
            if book["id"] == book_id:
                book["status"] = status
                self.save_books()
                print(f"Статус книги с ID {book_id} обновлен на '{status}'.")
                return
        print(f"Книга с ID {book_id} не найдена.")

    @staticmethod
    def format_book(book):
        """Форматирует вывод информации о книге."""
        return f"[ID: {book['id']}] {book['title']} - {book['author']} ({book['year']}) [{book['status']}]"
