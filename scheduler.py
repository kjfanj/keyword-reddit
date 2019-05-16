import schedule
import time
from get_post import look_up_loop


def main():
    schedule.every(5).seconds.do(look_up_loop)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
