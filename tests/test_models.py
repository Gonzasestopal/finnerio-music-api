import unittest

from src.models import Genre


class GenreTestCase(unittest.TestCase):

    def test_as_dict(self):
        genre = Genre(name='Rock')

        genre_info = genre.as_dict

        self.assertEqual(genre_info['name'], 'Rock')

if __name__ == '__main__':
    unittest.main()
