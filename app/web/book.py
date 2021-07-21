from flask import jsonify, request
from ..lib.utils import is_isbn, get_logger
# from app.lib.book_spider import BookSpider
from ..web import web
from ..forms.book import SearchForm
from ..models.book import Book
from ..view_model.book_view_model import BookViewModel, BookCollection
from ..spider.fisher_book import FisherBook
logger = get_logger()


@web.route('/book/search/')
def search():
    """
    只支持isbn搜索 （因为鱼书api不可用）
    :param q:
    :param page:

    1. 如果搜索的isbn数据库中没有，那就访问api，然后再存入数据库中
    2. 如果搜索的是关键字，只从数据库中读取，因为api不支持关键字搜索
    """
    form = SearchForm(request.args)
    if form.validate():
        # q = request.args['q']
        # page = request.args['page']
        q = str(form.q.data).strip()
        page = str(form.page.data).strip()
        fish_book = FisherBook()
        books = BookCollection()

        if is_isbn(q) == 'isbn':
            fish_book.search_by_isbn(isbn=q)
        else:
            fish_book.search_by_keyword(keyword=q)
        books.collect_book(fish_book, q)
        return jsonify({k: v.__dict__ for k, v in enumerate(books.books)})
    else:
        return jsonify({'msg': form.q.errors})
