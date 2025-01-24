import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from uuid import uuid4
import shutil

def init_logger(logger, file_name, use_console=True):
    """Initialize a logger with a FileHandler."""
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(message)s - %(levelname)s (%(lineno)d) - %(asctime)s - %(name)s - (%(filename)s:%(funcName)s)"
    )

    # 检查是否已经有文件处理器
    has_file_handler = any(isinstance(h, logging.FileHandler) for h in logger.handlers)
    if not has_file_handler:
        # 创建一个文件处理器
        file_handler = RotatingFileHandler(
            str(file_name) + ".log", maxBytes=3 * 1024 * 1024, backupCount = 2
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    if use_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)


class Clog:
    def __init__(self, file_name: str, log_dir: str="./logs") -> None:
        """ 创建日志，提供子日志创建功能，防止多任务日志混乱，确保同一任务日志连续性 """
        self.file_name = file_name
        self.logger = logging.getLogger(file_name)

        # Initialize main logger
        self.log_dir = Path(log_dir, file_name)
        self.sub_log_dir = self.log_dir / "tmp"

        self.log_dir.mkdir(exist_ok=True, parents=True)
        
        init_logger(self.logger, self.log_dir / file_name, use_console=False)


    def create_sub_logger(self) -> logging.Logger:
        """Create a sub logger that writes to a separate log file."""

        self.sub_log_dir.mkdir(exist_ok=True, parents=True)
        sub_file_name = f"sub_logger-{uuid4()}"
        sub_logger = logging.getLogger(sub_file_name)
        init_logger(sub_logger, self.sub_log_dir / sub_file_name)

        sub_logger.info(f"### 子日志创建: {sub_file_name}")
        return sub_logger

    def merge_file(self, sub_logger):
        """Merge all sub-log files into the main log file."""
        for handler in sub_logger.handlers:
            if isinstance(handler, logging.FileHandler):
                sub_log_file_path = Path(handler.baseFilename)
                break
        else:
            raise ValueError("No FileHandler found in sub_logger")
        
        with sub_log_file_path.open('r', encoding='utf-8') as f_in:
            log_sub = f_in.read().strip()
            self.logger.info(f"{log_sub}\n{'*'*50}")  # Write sub-log content to main log
        sub_log_file_path.unlink()  # Delete the temporary log file
        sub_logger.handlers.clear()  # 移除所有处理器
        self.delete_tmp_logs()

    def clean_tmp_dir(self):
        try:
            shutil.rmtree(self.sub_log_dir)
        except Exception as e:
            print(e)

    def delete_tmp_logs(self):
        if self.sub_log_dir.exists() and len(list(self.sub_log_dir.iterdir())) == 0: # 空文件夹
            self.sub_log_dir.rmdir()


