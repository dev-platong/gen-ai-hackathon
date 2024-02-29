import os
import whisper
from pytube import YouTube
import streamlit as st
from datetime import datetime
import csv
import logging

logging.basicConfig(level=logging.DEBUG)

st.title("将棋デモ")
youtube = YouTube("https://www.youtube.com/watch?v=BJlUFpl2Uvs") # 【無料プレミア公開】第31期 銀河戦 本戦Hブロック 最終戦 藤井聡太銀河 vs 羽生善治九段
audio = youtube.streams.get_audio_only()

filename = youtube.streams.first().title + ".mp3"
output_path = "dist"
file_path = os.path.join(output_path, filename)

# ファイルが存在しない場合のみダウンロード
if not os.path.exists(file_path):
    audio.download(output_path=output_path, filename=filename)

model = whisper.load_model("base")
trans_result = model.transcribe(file_path)

trans_result["text"]

from datetime import datetime
texts = []
for segment in trans_result["segments"]:
    # リスト内にタイムスタンプとテキストを一組として格納
    texts.append([datetime.fromtimestamp(segment["start"]).strftime("%H:%M:%S"), segment["text"]])

# ファイル名を指定
filename = "output.csv"
file_path = os.path.join(output_path, filename)

# 'w'は書き込みモードを意味します
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # writerowsメソッドでリストのリストをCSVに書き出し
    writer.writerows(texts)