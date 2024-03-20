import subprocess
from time import sleep


#这一行导入了 Python 内置的 subprocess 模块。
# 该模块允许 Python 与系统 shell 进行交互，从而可以在 Python 中运行外部命令。


def get_audit_logs():
    command = ['/home/zzl/Desktop/log_parse/auparse']
    # subprocess.Popen 函数来启动一个新的进程，并运行 command 列表中的命令。
    # 该函数会返回一个 Popen 对象，该对象代表了新的进程。
    # command = ["stdbuf", "-oL"] + command
    process = subprocess.Popen(command, stdout=subprocess.PIPE ,encoding="utf-8",bufsize=512)
    print(process.pid)

    try:
        # 持续读取子进程的标准输出数据
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:
                break
            if output:
                print(output,end="")


    except KeyboardInterrupt:
        # 用户按下 Ctrl+C 时停止处理数据
        process.terminate()


# 调用函数获取审计日志
logs = get_audit_logs()

