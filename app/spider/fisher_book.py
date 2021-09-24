from ..lib.helper import HttpHelper
from ..models.book import Book
from ..lib.utils import get_logger

logger = get_logger()


class FisherBook(object):
    def __init__(self):
        self.total = 0
        self.books = []

    def _cut_book_data(self, d):
        book = dict(isbn=d.get('isbn'),
                    title=d.get('title'),
                    author=d.get('author', ''),
                    binding=d.get('binding', ''),
                    image=d.get('pic', ''),
                    page=d.get('page') or 0,
                    price=d.get('price', ''),
                    pubdate=d.get('pubdate', ''),
                    publisher=d.get('publisher', ''),
                    summary=d.get('summary', ''))
        return book

    def _get_single_book_from_api(self, raw_data):
        if raw_data and raw_data['msg'] == 'ok':
            self.total = 1
            book = raw_data['result']
            b = self._cut_book_data(book)
            Book.write_book(b)
            self.books = [b]
        else:
            logger.debug('can not find book by isbn')

    def search_by_isbn(self, isbn):
        single_book = Book.query.filter_by(isbn=isbn).all()
        if single_book:
            self.total = 1
            self.books = self._extract_dict_from_instance(single_book[0])
        else:
            raw_data = HttpHelper.get(isbn)
            self._get_single_book_from_api(raw_data)

    def search_by_keyword(self, keyword):
        """
        only from database but not api
        """
        books = Book.query.filter(Book.author.like('%{}%'.format(keyword))).all()
        if not books:
            books = Book.query.filter(Book.title.like('%{}%'.format(keyword))).all()

        data = []
        for book in books:
            data.extend(self._extract_dict_from_instance(book))
        self.total = len(data)
        self.books = data

    @staticmethod
    def _extract_dict_from_instance(class_name):
        outcome = {}
        for name in class_name.__dict__:
            if not name.startswith('_') and name != 'id':
                outcome.update({name: getattr(class_name, name) or ''})
        return [outcome]

    @property
    def first(self):
        return self.books[0] if self.books else []
