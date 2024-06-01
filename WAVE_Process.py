import wave
import pyaudio
import os

from openai import OpenAI
from ChatGPT import GPT
from Voicevox import Voice


class CreateWave():
    def __init__(self, WHISPER):
        self.chunk = 1024
        self.sample_format = pyaudio.paInt16  # 樣本格式
        self.channels = 2  # 聲道數量
        self.fs = 44100  # 取樣頻率
        self.seconds = 3  # 錄音秒數
        self.filename = "Record.wav"  # 錄音檔名
        self.frames = []
        self.text = ''
        self.p = pyaudio.PyAudio()
        self.WHISPER = WHISPER

    def Record(self):

        print("麥克風開啟...")
        # 開啟錄音串流
        stream = self.p.open(format=self.sample_format, channels=self.channels, rate=self.fs, frames_per_buffer=self.chunk, input=True)

        for i in range(0, int(self.fs / self.chunk * self.seconds)):
            data = stream.read(self.chunk)
            self.frames.append(data)  # 將聲音記錄到串列中

        print("停止錄音")
        stream.stop_stream()  # 停止錄音
        stream.close()  # 關閉串流
        self.p.terminate()

    def SaveWaveFile(self):
        print('Save File...')
        wf = wave.open(self.filename, 'wb')  # 開啟聲音記錄檔
        wf.setnchannels(self.channels)  # 設定聲道
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))  # 設定格式
        wf.setframerate(self.fs)  # 設定取樣頻率
        wf.writeframes(b''.join(self.frames))  # 存檔
        wf.close()

    def SendToWhisper(self):
        client = OpenAI(
            api_key=self.WHISPER,
        )

        audio_file = open(self.filename, "rb")  # 打開錄音檔
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
        self.text = transcription.to_dict()['text']
        print("您說：", self.text)
        return self.text

class AudioFile():
    def __init__(self, file):
        """ Init audio stream """
        self.chunk = 1024
        self.wf = wave.open(file, 'rb')
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format = self.p.get_format_from_width(self.wf.getsampwidth()),
            channels = self.wf.getnchannels(),
            rate = self.wf.getframerate(),
            output = True
        )

    def play(self):
        """ Play entire file """
        data = self.wf.readframes(self.chunk)
        while data != b'':
            self.stream.write(data)
            data = self.wf.readframes(self.chunk)

    def close(self):
        """ Graceful shutdown """
        self.stream.close()
        self.p.terminate()




