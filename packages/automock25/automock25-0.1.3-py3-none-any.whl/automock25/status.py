import configparser


def get_config_params():
    # 读取 config.ini 文件
    config = configparser.ConfigParser()
    config_file_path = 'config.ini'

    try:
        with open(config_file_path, 'r', encoding='utf-8') as config_file:
            config.read_file(config_file)

        config_params = dict(config['DEFAULT'])
        return config_params
    except FileNotFoundError:
        print(f"Error: {config_file_path} not found.")
        return {}
    except Exception as e:
        print(f"Error reading {config_file_path}: {e}")
        return {}


def get_job_status():
    # 这里假设 job_running 是一个全局变量，可以通过某种方式获取
    # 为了简化示例，我们使用一个固定的值
    # 实际应用中，可以通过某种机制（如文件、数据库等）来跟踪 job 的状态
    from recordJob import job_running
    return "Running" if job_running else "Stopped"
