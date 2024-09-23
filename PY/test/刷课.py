import os
import tkinter as tk
from tkinter import messagebox


def set_java_home(jdk_version):
    # 默认 JDK 安装路径，根据实际情况修改
    jdk_base_path = "C:\\Program Files\\Java\\"

    if jdk_version == "17":
        jdk_path = os.path.join(jdk_base_path, "jdk-17")
    elif jdk_version == "21":
        jdk_path = os.path.join(jdk_base_path, "jdk-21")
    else:
        messagebox.showerror("Error", f"Unsupported JDK version: {jdk_version}")
        return False

    # 设置 JAVA_HOME 环境变量
    os.system(f'setx /M JAVA_HOME "{jdk_path}"')

    # 添加 JDK 的 bin 目录到系统 PATH 变量（可选）
    os.system(f'setx /M PATH "%PATH%;{jdk_path}\\bin"')

    messagebox.showinfo("Success", f"Successfully set JAVA_HOME to {jdk_path}")
    return True


def set_jdk_17():
    success = set_java_home("17")
    if success:
        label.config(text="Current JDK: JDK 17")


def set_jdk_21():
    success = set_java_home("21")
    if success:
        label.config(text="Current JDK: JDK 21")


# 创建主窗口
root = tk.Tk()
root.title("JDK Environment Setter")

# 添加标签显示当前 JDK 版本
label = tk.Label(root, text="Current JDK: None", pady=10)
label.pack()

# 添加按钮切换到 JDK 17 和 JDK 21
btn_jdk17 = tk.Button(root, text="Set JDK 17", command=set_jdk_17)
btn_jdk17.pack(pady=5)

btn_jdk21 = tk.Button(root, text="Set JDK 21", command=set_jdk_21)
btn_jdk21.pack(pady=5)

# 运行主循环
root.mainloop()
