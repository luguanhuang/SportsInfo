
from services.http.server import htttp_start
from utils.task import task
import datetime 
import asyncio

def start():
    # 启动http服务
    # htttp_start()
    task.add_job(htttp_start, "date", run_date=datetime.datetime.now() + datetime.timedelta(seconds=1))
    asyncio.get_event_loop().run_forever()

if __name__ == "__main__":
    start()