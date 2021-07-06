from flask import jsonify, request
from app.lib.utils import is_isbn, get_logger
from app.lib.helper import HttpHelper
from app.web import web
from app.forms.book import SearchForm

logger = get_logger()


@web.route('/book/search/')
def search():
    """
    只支持isbn搜索 （因为鱼书api不可用）
    :param q:
    :param page:
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        # q = request.args['q']
        # page = request.args['page']
        q = str(form.q.data).strip()
        page = str(form.page.data).strip()
        logger.debug('q is %s, page is %s', q, page)
        if is_isbn(q):
            return jsonify(HttpHelper.get(q))
    else:
        return jsonify({'msg': form.q.errors})
