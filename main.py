
from UI import menu

if __name__ == '__main__':
    # 需向openai聲請兩組API
    whisper = ''
    GPT_API = ''
    x = menu(whisper, GPT_API)
    x.start()