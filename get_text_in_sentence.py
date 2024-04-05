import re

from pathlib import Path

from tibcleaner.tokenizer import bo_sent_tokenizer

def preprocess_text(text):
    patterns = [
        ['〔.+〕', ''],
        ['\{D.+\}', ''],
        ['#', '']

    ]

    for pattern in patterns:
        text = re.sub(pattern[0], pattern[1], text)
    if text[-1] == "༄":
        text = text[:-1]
    return text

def get_text_in_sentence(text):
    clean_text = preprocess_text(text)
    tokenized_text = bo_sent_tokenizer(clean_text)
    return tokenized_text

if __name__ == "__main__":
    text_paths = list(Path('./data/tengyur_text').iterdir())
    text_paths.sort()
    for text_path in text_paths:
        text_id = text_path.stem
        text = text_path.read_text(encoding='utf-8')
        sentence_wise_text = get_text_in_sentence(text)
        Path(f'./data/sentence_wise/{text_id}.txt').write_text(sentence_wise_text, encoding='utf-8')