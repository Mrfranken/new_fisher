from flask import jsonify, request
from app.lib.utils import is_isbn, get_logger
from app.lib.helper import HttpHelper
from app.web import web

logger = get_logger()


@web.route('/book/search/')
def search():
    """
    只支持isbn搜索 （因为鱼书api不可用）
    :param q:
    :param page:
    :return:
    """
    q = request.args['q']
    page = request.args['page']
    logger.debug('q is %s, page is %s', q, page)
    if is_isbn(q):
        return jsonify(HttpHelper.get(q))
