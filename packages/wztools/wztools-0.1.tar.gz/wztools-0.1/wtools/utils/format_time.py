import time

def format_time(seconds: float) -> str:
    days = seconds // 86400
    seconds %= 86400
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    result = []
    if days > 0:
        result.append(f"{int(days)}天")
    if hours > 0:
        result.append(f"{int(hours)}小时")
    if minutes > 0:
        result.append(f"{int(minutes)}分钟")
    if seconds > 0 or len(result) == 0:  # 如果有秒数或者没有其他单位，显示秒数
        result.append(f"{seconds:.2f}秒")

    return ' '.join(result)

def runtime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 执行函数
        end_time = time.time()  # 记录结束时间
        elapsed_time = end_time - start_time  # 计算运行时间
        formatted_time = format_time(elapsed_time)  # 格式化时间
        print(f"函数 {func.__name__} 运行时间: {formatted_time}")
        return result
    return wrapper

