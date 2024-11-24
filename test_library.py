import unittest
from library import Library


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """
        Настраивает библиотеку перед каждым тестом.
        """
        self.library = Library()
        self.library.books = []  # Очищаем список книг для каждого теста

    def test_add_book(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        self.assertEqual(len(self.library.books), 1)

    def test_delete_book(self):
        self.library.add_book("Test Book", "Test Author", 2024)
        book_id = self.library.books[0]["id"]
        self.library.delete_book(book_id)
        self.assertEqual(len(self.library.books), 0)

    def test_search_books(self):
        """
        Тест поиска книги по различным полям.
        """
        # Добавляем несколько книг
        self.library.add_book("Test Book", "Test Author", 2024)
        self.library.add_book("Another Book", "Another Author", 2023)

        # Ищем книгу по названию
        results = self.library.search_books("title", "Test Book")
        print(f"Результаты поиска по названию 'Test Book': {results}")  # Вывод результатов
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Test Book")

        # Ищем книгу по автору
        results = self.library.search_books("author", "Another Author")
        print(f"Результаты поиска по автору 'Another Author': {results}")  # Вывод результатов
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["author"], "Another Author")

        # Ищем книгу по году
        results = self.library.search_books("year", "2024")
        print(f"Результаты поиска по году '2024': {results}")  # Вывод результатов
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["year"], 2024)

        # Пустой результат
        results = self.library.search_books("title", "Nonexistent Book")
        print(f"Результаты поиска по несуществующей книге: {results}")  # Вывод пустого результата
        self.assertEqual(len(results), 0)


if __name__ == '__main__':
    unittest.main()
