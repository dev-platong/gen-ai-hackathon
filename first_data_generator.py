import logging
from openai import OpenAI
from domain.shogi.kishi import kishi_list
from domain.shogi.strategies import strategies
from dotenv import dotenv_values
import json

config = dotenv_values(".env")

logging.basicConfig(level=logging.DEBUG)

message = f"""
渡された全ての将棋の棋士の得意な戦略を教えてください。回答は以下のような形式とします。余計な補足等が入らないようにしてください。
出力例：
藤井聡太の得意とする戦略は居飛車力戦です。
近藤正和の得意とする戦略はゴキゲン中飛車です。
以下、渡された棋士の人数分続く

棋士は以下
{",".join(kishi_list)}
棋士終わり

戦略は以下から選択してください。
{strategies}
戦略終わり
"""

model_gpt3 = "gpt-3.5-turbo"
model_gpt4 = "gpt-4-0125-preview"

client = OpenAI(api_key=config["OPENAI_API_KEY"])
response = client.chat.completions.create(
    model=model_gpt4,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message},
    ],
)

with open('tmp.json', 'w', encoding="utf8") as f:
    lines: list[str] = response.choices[0].message.content.split("\n")
    json.dump(lines, f, ensure_ascii=False)