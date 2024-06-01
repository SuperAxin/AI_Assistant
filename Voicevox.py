import requests

class Voice:
    def __init__(self, TEXT):
        self.TEXT = TEXT
        self.URL = "http://localhost:50021/audio_query?text=" + TEXT +"&speaker=8"

    def POST(self):
        r = requests.post(self.URL)
        payload = r.json()

        api_url_2 = 'http://localhost:50021/synthesis?speaker=8'
        r = requests.post(api_url_2, json=payload)

        # 處理回應
        if r.status_code == 200:
            with open("output.wav", "wb") as f:
                f.write(r.content)
        else:
            print("请求失败: ", r.status_code)
        return 'OK'

