import time, sys
def my_sleep(miliseconds):
    time.sleep(miliseconds/1000.0)
print('__name__ ==', __name__)
if __name__ == "__main__":
    print('Start waiting')
    my_sleep(int(sys.argv[1]))
    print('End waiting')