import csv
import random
import webbrowser
import tkinter as tk

def random_song(csv_file):
    # 读取 CSV 文件
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # 将 CSV 数据转为列表
        songs = [row for row in reader]

        # 从列表中随机选择一行数据
        selected_song = random.choice(songs)
        return selected_song

def play_random_song():
    selected_song = random_song("音乐热歌榜单.csv")
    song_info_label.config(text=f"歌名: {selected_song['歌名']}  歌手: {selected_song['歌手']}  时长: {selected_song['时长']}")
    webbrowser.open(selected_song['歌曲地址'])

# 创建主窗口
window = tk.Tk()
window.title("随机音乐播放器")

# 显示歌曲信息的标签
song_info_label = tk.Label(window, text="随机播放的歌曲信息：", font=("Arial", 12))
song_info_label.pack(pady=10)

# 创建切歌按钮
next_song_button = tk.Button(window, text="切歌", width=10, height=2, command=play_random_song)
next_song_button.pack(pady=10)

# 初始化播放第一首歌曲
play_random_song()

# 运行主循环
window.mainloop()
