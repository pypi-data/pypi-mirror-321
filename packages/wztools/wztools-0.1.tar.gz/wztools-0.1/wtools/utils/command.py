import subprocess
import sys


def run_cmd(command: list, run_path: str = "."):
    try:
        with subprocess.Popen(
            command,
            cwd=run_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        ) as process:
            print("=" * 20 + "正在运行" + "=" * 20)
            print("以下命令正在执行 -->")
            print(f"{''.join(command)}")
            # 实时输出命令的输出到控制台
            for line in process.stdout:
                print(line, end="")  # 使用 end='' 来避免双重换行
                sys.stdout.flush()  # 刷新输出缓冲区，确保实时输出

            # 等待命令执行完成
            process.wait()

            # 检查命令的返回状态
            if process.returncode == 0:
                print("命令执行成功")
            else:
                print(f"命令执行失败，返回状态码: {process.returncode}")
            print("=" * 20 + "运行完成" + "=" * 20)
    except Exception as e:
        print(e)
    finally:
        pass
