from openai import OpenAI
from colorama import init, Fore

# 初始化 colorama
init(autoreset=True)

# 配置 API
API_KEY = "sk-****"
BASE_URL = "https://api.lkeap.cloud.tencent.com/v1"

# 构造 client
client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


def ask_deepseek(prompt):
    print(f"{Fore.YELLOW}DeepSeek 正在思考...\n")

    # 发送流式请求
    chat_completion = client.chat.completions.create(
        model="deepseek-r1",
        messages=[{"role": "user", "content": prompt}],
        stream=True  # 关键：流式输出
    )

    for chunk in chat_completion:
        if hasattr(chunk.choices[0].delta, 'content'):
            content = chunk.choices[0].delta.content
            if content:
                print(f"{Fore.CYAN}{content}", end="", flush=True)

    print("\n")  # 换行


def chat():
    print(f"{Fore.MAGENTA}欢迎使用 DeepSeek R1 对话机器人！输入 'exit' 退出。")

    while True:
        prompt = input(f"\n{Fore.BLUE}请输入您的问题：")

        if prompt.lower() == "exit":
            print(f"{Fore.RED}退出对话。")
            break

        ask_deepseek(prompt)


# 运行对话
chat()
