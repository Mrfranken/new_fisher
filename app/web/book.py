from flask import jsonify, request
from ..lib.utils import is_isbn, get_logger
from ..lib.helper import HttpHelper
from ..web import web
from ..forms.book import SearchForm
from ..models.book import db, Book
from ..view_model.book_view_model import BookViewModel

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

        if is_isbn(q) == 'isbn':
            single_book = Book.query.filter_by(isbn=q).all()
            if single_book:
                logger.debug('isbn {} exists in database'.format(q))
                result = BookViewModel.get_single_book_from_database(single_book[0], q)
            else:
                logger.debug('there is no book by isbn {}'.format(q))
                raw_data = HttpHelper.get(q)
                result = BookViewModel.pack_single(raw_data, q)
            return jsonify(result)
        else:
            logger.debug('kw {} searching'.format(q))
            return jsonify(BookViewModel.pack_collection(q))

    else:
        return jsonify({'msg': form.q.errors})
