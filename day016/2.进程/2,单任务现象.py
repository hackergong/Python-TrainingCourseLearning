from time import sleep

def run():
    while True:
        print("tracy is a nice man")



if __name__ == "__main__":
    while True:
        print("tracy is a good man")
        sleep(1)

    #不会执行到run方法，只有上面的while循环结束才执行
    run()