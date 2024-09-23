import subprocess
import win32api
import win32process
import win32con

# ToDesk 的路径（确保路径是正确的）
todesk_path = r"E:\todessk\ToDesk\ToDesk.exe"

# 创建进程启动信息
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
startupinfo.wShowWindow = win32con.SW_HIDE

# 启动 ToDesk 程序并将输出重定向到 devnull
process = subprocess.Popen(
    todesk_path,
    stdout=subprocess.DEVNULL,
    stderr=subprocess.DEVNULL,
    startupinfo=startupinfo
)
