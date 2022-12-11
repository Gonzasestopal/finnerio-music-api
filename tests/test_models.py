import unittest

from src.models import Genre


class GenreTestCase(unittest.TestCase):

    def test_as_dict(self):
        genre = Genre(name='Rock', href="http://sample.com")

        genre_info = genre.as_dict

        self.assertEqual(genre_info['name'], 'Rock')
        self.assertEqual(genre_info['href'], 'http://sample.com')

if __name__ == '__main__':
    unittest.main()
