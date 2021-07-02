# try:
from app.lib.utils import is_isbn
from app.lib.helper import HttpHelper
# except:
# from utils import is_isbn
# from helper import HttpHelper
from flask import jsonify
from fisher import app


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    只支持isbn搜索 （因为鱼书api不可用）
    :param q:
    :param page:
    :return:
    """
    if is_isbn(q):
        return jsonify(HttpHelper.get(q))
