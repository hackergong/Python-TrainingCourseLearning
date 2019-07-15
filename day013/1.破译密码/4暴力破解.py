import itertools
import time

passwd =  ("".join(x) for x in itertools.product("0123456789",repeat=3))

while True:
    try:
        str = next(passwd)
        time.sleep(0.5)
        print(str)
    except StopIteration as e:
        break


