from werkzeug.local import LocalStack
from werkzeug.local import LocalStack, LocalProxy
from threading import Thread, current_thread



stack = LocalStack()
stack.push(3)


def push_num():
    stack.push(4)
    print(current_thread().ident)


t = Thread(target=push_num, name='child thread')

t.start()
print(1)







