import schedule
import time
from main import main


schedule.every(5).seconds.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
