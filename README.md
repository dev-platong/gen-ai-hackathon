# GEN AI HACKATHON

将棋のような一手一手進むたびに何度も問い合わせる必要がある場合はGPT-4を毎回呼ぶのではなく、GPT-4とRAGでfine tuningのデータを作成してGPT-3.5 turboを使うほうが早いし安くていいのではないかというそんな発想で作ったもの
ファインチューン用のデータをRAGとGPT-4のデータを使って作成する。（RAG部分未実装）

## 実際問題

将棋の戦型の概念とかはほとんど誤りに近い実装になってしまったが、追加で直接的な得意戦法の駒版の状態なんかを与えればできるとは思う。
ただそこまでいくと特化しすぎるので生成AIでやらせるべきかは疑問。

# Installation

```shell
brew install poetry
poetry install
```

# HOW TO USE

```shell
poetry run python first_data_generator.py
poetry run python finetune_data_generator.py
poetry run python finetune.py
poetry run python question.py
```

1. first_data_generator でファインチューンデータの解答側を作成する
2. finetune_data_generator でファインチューン用の質問と回答形式のjsonlを作成する
3. finetune.py でファインチューニングして、IDを取得する
4. 与えられたIDを使ってGPT-3.5 turboで特定の領域の問題に回答する

# TIPS

To update whisper, please run
```shell
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git
```
