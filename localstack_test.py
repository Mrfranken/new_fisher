from werkzeug.local import LocalStack
from werkzeug.local import LocalStack, LocalProxy
from flask import _app_ctx_stack


class P(object):
    def __init__(self):
        self.age = 29

    def push(self):
        _app_ctx_stack.push(self)


if __name__ == '__main__':
    p = P()
    p.push()
    print(_app_ctx_stack.top)

    ls = LocalStack()
    # ls.push({'abc': '123'})
    # ls.push({'abc': '1234'})
    print(ls.top)
    ls.push(23)
    print(ls.pop())
    print(1)

    test_stack = LocalStack()
    test_stack.push({'abc': '123'})
    test_stack.push({'abc': '1234'})


    def pop_item():
        return test_stack.pop()


    item = LocalProxy(pop_item)

    print(item['abc'])
    print(item['abc'])
