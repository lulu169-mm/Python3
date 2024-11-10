import os
import re
from colorama import Fore, Style, init

# 初始化 colorama
init()
# 获取当前目录
current_directory = os.getcwd()

# 介绍文本
intro_text = """

░█▀▀▄░█░▒█░▀█▀░▄▀▀▄░░░▀▀█▀▀░█▀▀▄░█▀▄▀█░▄▀▀▄░█▀▀░█▀▀▄
▒█▄▄█░█░▒█░░█░░█░░█░░░░▒█░░░█▄▄█░█░▀░█░█▄▄█░█▀▀░█▄▄▀
▒█░▒█░░▀▀▀░░▀░░░▀▀░░░░░▒█░░░▀░░▀░▀░░▒▀░█░░░░▀▀▀░▀░▀▀

AutoTamper 是一个使用 SQLMap 进行自动 Tamper 测试的工具。它允许你输入带有注入点的目标 URL
以及一组 SQLMap 命令选项。该工具会运行 SQLMap 并使用各种 tamper 脚本，帮助你识别最适合目标的 tamper 脚本。

"""

# 居中显示介绍文本
intro_lines = intro_text.strip().split('\n')
max_line_length = max(len(line) for line in intro_lines)
centered_intro = "\n".join(line.center(max_line_length) for line in intro_lines)
print("\n\n\n" + centered_intro + "\n\n\n")

# 获取用户输入
my_url = input(f"{Fore.YELLOW}请输入带有注入点的 URL (例如: https://sample.com/index.php?id=1*): {Style.RESET_ALL}")
my_command = input(f"{Fore.YELLOW}请输入 SQLMap 命令 (例如: --batch --current-db --dbs --level 5 --risk 3 --dbms mysql): {Style.RESET_ALL}")

# 构建 SQLMap 命令
command = f'sqlmap -u "{my_url}" {my_command}'

# 使用正则表达式提取目标网址的主机名
my_target_match = re.search(r'//(.*?)/', my_url)
i = '0'

if my_target_match:
    my_target = my_target_match.group(1)

    # 将目标名中的非法字符替换为下划线，生成合法的文件夹名称
    my_target_sanitized = re.sub(r'[:/]', '_', my_target)

    print(f"\n{Fore.GREEN}目标 URL: {my_url}")
    print(f"SQLMap 命令: {command}\n")
    print(f"{Fore.CYAN}正在运行 SQLMap...{Style.RESET_ALL}")

    # 获取 tamper 脚本和输出目录
    tamper_directory = os.path.join(current_directory, "tamper")
    output_directory = os.path.join(current_directory, "output")

    # 获取 tamper 目录中的所有脚本
    entries = os.listdir(tamper_directory)

    for entry in entries:
        # 运行 SQLMap，并指定输出目录和 tamper 脚本
        os.system(f"{command} --output-dir={output_directory} --tamper {os.path.join(tamper_directory, entry)}")

        # 使用经过清理的目标名作为输出目录路径
        output_dir_path = os.path.join(output_directory, my_target_sanitized)

        try:
            # 打开 SQLMap 生成的日志文件
            with open(os.path.join(output_dir_path, 'log')) as f:
                line = f.readline()
                while line:
                    line = f.readline()
                    if 'web server operating system' in line:
                        if 'web application technology' in line:
                            if 'available databases' in line:
                                print(f"\n{Fore.GREEN}找到适用的 Tamper 脚本: {entry}{Style.RESET_ALL}")
                                i = '1'
                                break
                    line = f.readline()
            if i == '1':
                break
        except FileNotFoundError:
            print(f"\n{Fore.RED}未找到日志文件，Tamper 脚本: {entry}{Style.RESET_ALL}")
        except OSError as e:
            print(f"\n{Fore.RED}读取日志文件时出错: {e}{Style.RESET_ALL}")

    if i == '0':
        print(f"\n{Fore.YELLOW}未找到适用的 Tamper 脚本。{Style.RESET_ALL}")
else:
    print(f"\n{Fore.RED}URL 格式无效。{Style.RESET_ALL}")
