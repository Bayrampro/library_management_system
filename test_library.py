import unittest
import os
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        # Удаление файла перед каждым тестом
        if os.path.exists('storage.json'):
            os.remove('storage.json')

        # Инициализация новой библиотеки
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        books = self.library.books
        self.assertEqual(len(books), 1)

    def test_delete_book(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        self.library.delete_book(1)
        books = self.library.books
        self.assertEqual(len(books), 0)

    def test_search_books(self):
        """Тест поиска книги по различным полям."""
        # Добавляем несколько книг
        self.library.add_book("Test Book", "Author 1", 2000)
        self.library.add_book("Another Book", "Author 2", 2001)
        self.library.add_book("Some Book", "Author 1", 2000)

        # Выполняем поиск по полю title
        results = self.library.search_books("title", "Test Book")
        self.assertTrue(len(results) > 0, "Книги не найдены по данному заголовку")

        # Проверяем, что результат соответствует ожиданиям
        self.assertEqual(results[0]["title"], "Test Book")

        # Выполняем поиск по автору
        results = self.library.search_books("author", "Author 1")
        self.assertTrue(len(results) > 0, "Книги не найдены по данному автору")

        # Проверяем, что в результатах есть книги с этим автором
        self.assertEqual(results[0]["author"], "Author 1")

        # Выполняем поиск по году
        results = self.library.search_books("year", "2000")
        self.assertTrue(len(results) > 0, "Книги не найдены по данному году")

        # Проверяем, что в результатах есть книга с нужным годом
        self.assertEqual(results[0]["year"], 2000)


if __name__ == "__main__":
    unittest.main()
