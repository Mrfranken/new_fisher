from flask import jsonify, request, render_template, flash
import json
from ..lib.utils import is_isbn, get_logger
from ..web import web
from ..forms.book import SearchForm
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
    books = BookCollection()
    if form.validate():
        # q = request.args['q']
        # page = request.args['page']
        q = str(form.q.data).strip()
        page = str(form.page.data).strip()

        fish_book = FisherBook()
        if is_isbn(q) == 'isbn':
            logger.debug('q is isbn')
            fish_book.search_by_isbn(isbn=q)
        else:
            logger.debug('q is not isbn')
            fish_book.search_by_keyword(keyword=q)

        books.collect_book(fish_book, q)
        # return jsonify({k: v.__dict__ for k, v in enumerate(books.books)})
        # return json.dumps(books, default=lambda x: x.__dict__)

    else:
        flash('搜索的keyword不符合要求')
        # return jsonify({'msg': form.q.errors})
    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    fish_book = FisherBook()
    fish_book.search_by_isbn(isbn)

    if fish_book.first:
        book = BookViewModel(fish_book.first)
        return render_template('book_detail.html', book=book, wishes=[], gifts=[])
    else:
        flash('找不到符合{}的书籍'.format(isbn))
        return render_template('search_result.html', books=[])
