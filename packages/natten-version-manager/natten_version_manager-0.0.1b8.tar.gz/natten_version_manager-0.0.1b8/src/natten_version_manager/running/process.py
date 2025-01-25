import psutil


def is_process_alive(pid):
    try:
        process = psutil.Process(pid)
        process_status = process.status()
        return process_status != psutil.STATUS_ZOMBIE
    except psutil.NoSuchProcess:
        return False