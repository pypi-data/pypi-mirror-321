from flask import Flask
from automock25  import logset
from automock25  import recordJob
from   automock25 import controller  # 导入 controller.py 文件
app = Flask(__name__)


def main():
    # 设置日志
    logger = logset.setup_logging()
    logger.info("Starting App")
    # 启动定时任务
    recordJob.jobStart()
    # 初始化路由
    controller.init_routes(app)
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    main()







