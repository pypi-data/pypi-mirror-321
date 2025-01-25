from flask import render_template
from status import get_config_params, get_job_status
from automock25.logset import setup_logging
# 设置日志
logger = setup_logging
def init_routes(app):


    @app.route('/')
    def index():
        logger.info("Index page accessed")
        return "Flask App is running with job running in the background."

    @app.route('/status')
    def status():
        logger.info("Status page accessed")
        config_params = get_config_params()
        job_status = get_job_status()
        return render_template('status.html', config_params=config_params, job_status=job_status)
