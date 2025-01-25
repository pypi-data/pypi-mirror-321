import time
from record import get_order
from excuteOrder import charge
import threading
import logset

# 记录连续失败的次数
failure_count = 0
MAX_FAILURES = 3

# 全局变量来跟踪 job 的运行状态
job_running = True

logger = logset.setup_logging()

def job():
    global failure_count, job_running
    try:
        order_data = get_order()
        if order_data:
            charge(order_data)
            failure_count = 0  # 重置失败计数器



    except Exception as e:
        failure_count += 1
        logger.error(f"Error in job: {e}", exc_info=True)
        if failure_count >= MAX_FAILURES:
            job_running = False
            # 停止定时任务
            global job_thread
            #job_thread.stop()
            #logger.info(f"失败 {failure_count} 次后 线程关闭 ----")

def run_job():
    global job_thread, job_running
    while job_running and not job_thread.stopped():
        job()
        if failure_count >= MAX_FAILURES:
            break
        time.sleep(10)

class StoppableThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop_event = threading.Event()

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

def jobStart():
    # 启动定时任务线程
    global job_thread, job_running
    job_thread = StoppableThread(target=run_job)
    job_thread.daemon = True  # 设置为守护线程，主线程结束时自动退出
    job_thread.start()
    logger.info("线程启动 ----")

def jobRun():
    global job_running
    job_running = True
    logger.info("线程恢复 ----")

def jobPause():
    global job_running
    job_running = False
    logger.info("线程暂停 ----")




