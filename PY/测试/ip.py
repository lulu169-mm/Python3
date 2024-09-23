import os
import subprocess
import threading

# base_ip = "192.168.71."
base_ip = input("请输入需要生成的起始ip地址(例如192.168.71.*):")
last_num = int(base_ip.rsplit('.', 1)[-1])  # 获取最后一个数字 *
base_ip = base_ip.rsplit('.', 1)[0] + '.'  # 获取除了最后一个数字的部分 192.168.71.
ips = [base_ip + str(i) for i in range(last_num, 255)]
# 写入文件
with open("C:/Users/24937/Desktop/ip.txt", "w") as f:
    for ip in ips:
        print(ip)
        # f.write(ip + "\n")
print('写入成功!!!')
#
# print(subprocess.run("ipconfig", capture_output=True, encoding='gbk'))
os.system("nmap -iL C:\\Users\\24937\\Desktop\\ip.txt -p 80,8080,22,3306,6379,3389,1433,445 -sV -O")
os.system("fscan.exe -hf C:\\Users\\24937\\Desktop\\ip.txt -p 80,8080,22,3306,6379,3389,1433,445")

os.system('sqlmap -u "www.baidu.com" --batch --random-agent --threads 10 --level 3 --risk 3 --banner --dbs --batch')

os.system("D:\\naabu\\naabu.exe -host 192.168.71.21 -p 1-65535")
os.system("D:\\masscan\\masscan.exe --ports 1-65535 192.168.71.21")


