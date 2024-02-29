import json
import re

with open('tmp.json', 'r', encoding='utf-8') as f:
    data: list[str] = json.load(f)

def extract_name(text: str) -> str:
    pattern = r"^(.*?)の得意とする戦略"
    match = re.search(pattern, text)
    if match:
        return match.group(1)
    else:
        ""

def generate_line(text: str) -> str:
    question = extract_name(text) + "の得意な戦型は？"
    return f'{{"messages": [{{"role": "user", "content": "{question}"}}, {{"role": "assistant", "content": "{text}"}}]}}'

lines: list[str] = [generate_line(x) for x in data]

with open('data.jsonl', 'w', encoding="utf8") as f:
    f.write('\n'.join(lines))