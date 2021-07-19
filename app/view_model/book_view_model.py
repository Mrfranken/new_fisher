from ..models.book import Book
from ..models.book import Book
from ..lib.utils import is_isbn, get_logger

logger = get_logger()


class BookViewModel(object):
    """
    处理原始数据
    """

    @classmethod
    def pack_single(cls, raw_data, keyword):
        returned = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if raw_data and raw_data['msg'] == 'ok':
            returned['total'] = 1

            book_info = cls._cut_book_data(raw_data['result'])
            Book.write_book(book_info)  # write data to database
            logger.debug('write one book info to database')

            returned['books'] = [book_info]
        return returned

    @classmethod
    def pack_collection(cls, keyword):
        """
        raw_data only from database
        """
        books = Book.query.filter(Book.author.like('%{}%'.format(keyword))).all()
        data = []
        outcome = {}
        for book in books:
            data.extend(cls._extract_dict_from_instance(book))
        outcome['books'] = data
        outcome['total'] = len(data)
        outcome['keyword'] = keyword
        return outcome

    @classmethod
    def _cut_book_data(cls, d):
        book = dict(isbn=d.get('isbn'),
                    title=d.get('title'),
                    author=d.get('author', ''),
                    binding=d.get('binding', None),
                    image=d.get('pic', None),
                    page=d.get('page', None),
                    price=d.get('price', None),
                    pubdate=d.get('pubdate', None),
                    publisher=d.get('publisher', None),
                    summary=d.get('summary', None))
        return book

    @staticmethod
    def _extract_dict_from_instance(class_name):
        outcome = {}
        for name in class_name.__dict__:
            if not name.startswith('_') and name != 'id':
                outcome.update({name: getattr(class_name, name)})
        return [outcome]

    @classmethod
    def get_single_book_from_database(cls, book, q):
        outcome = {}
        value = cls._extract_dict_from_instance(book)
        outcome['books'] = value
        outcome['total'] = 1
        outcome['keyword'] = q
        return outcome
