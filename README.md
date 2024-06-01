## 寫一個自己的AI女僕>< ##
我是超人阿信，是一位致力於金融分析和喜愛二次元文化的肥宅，今天想跟大家介紹我如何利用Python搭配ChatGPT, TTS以及語音包來開發自己的AI女僕，以下是我在開發前認為必須要有的功能。

1.雙方必須能用語音對話

2.女僕會說日文而且聲音很可愛

3.能夠以Live2D的方式呈現 (技術問題目前只有.JPG)

安裝說明：
注意：如果電腦沒有裝Python的話要先下載

1.先到 OpenAI 申請兩組API Key (一組給ChatGPT, 一組給Whisper)

2.下載 AI_Maid 並解壓縮

3.下載 VOICEVOX ENGINE   (語音包)  後解壓縮到 AI_Maid 的資料夾內

4.接著打開 cmd 並切換至 AI_maid 的資料夾

5.輸入以下指令 "pipinstall -r requirements.txt" 安裝模組

6.點開VOICEVOX進到windows-directml之後開啟run.exe ( 一定要開Voicevox才可以使用不然會出問題 )

7.回到cmd介面輸入"python main.py" 就可以打開軟體囉

8.軟體打開之後會要求你輸入API Keys，之後按住底下的按鈕就可以透過麥克風跟女僕對話囉！！
