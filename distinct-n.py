import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from collections import Counter
import numpy as np

from tokenize_japanese import tokenize_japanese


# Function to calculate Distinct-N
def distinct_n(sentences, n):
    ngrams = Counter()
    total_ngrams = 0

    for sentence in sentences:
        tokens = tokenize_japanese(sentence)
        sentence_ngrams = list(nltk.ngrams(tokens, n))
        ngrams.update(sentence_ngrams)
        total_ngrams += len(sentence_ngrams)

    if total_ngrams == 0:
        return 0.0

    distinct_ngrams = len(ngrams)
    distinct_score = distinct_ngrams / total_ngrams
    return distinct_score


# sentences = [
#     "this is a test sentence",
#     "this test sentence is a sample",
#     "sample test sentence for evaluation"
# ]
sentences = [
    "グアムへ行こう！絶景と美食を満喫。今すぐ予約！",
    "グアム旅行ならお得なプランが盛りだくさん！",
    "グアムでの贅沢な休暇を体験しよう！",
    "グアムの魅力を存分に楽しむ旅。予約受付中！",
    "グアム旅行で心も体もリフレッシュ！",
    "グアムの楽園へ。お得な旅行プランをチェック！",
    "グアムでの素敵な思い出を作ろう！",
    "グアム旅行で非日常体験を。今すぐ予約！",
    "グアムの美しいビーチでリラックス。予約開始！",
    "グアム旅行で最高の休暇を過ごそう！",
    "グアムへの旅行をお手頃価格で実現！",
    "グアムでの贅沢な休暇を予約しよう！",
    "グアム旅行で夢のような時間を。予約受付中！",
    "グアムの魅力を存分に楽しむ旅行プラン！",
    "グアム旅行で心も体もリフレッシュしよう！",
    "グアムの楽園へ。お得な旅行プランをチェック！",
    "グアムでの素敵な思い出を作る旅。予約受付中！",
    "グアム旅行で非日常体験を。今すぐ予約！",
    "グアムの美しいビーチでリラックス。予約開始！",
    "グアム旅行で最高の休暇を過ごそう！",
    "グアムへの旅行をお手頃価格で実現！",
    "グアムでの贅沢な休暇を予約しよう！",
    "グアム旅行で夢のような時間を。予約受付中！",
    "グアムの魅力を存分に楽しむ旅行プラン！",
    "グアム旅行で心も体もリフレッシュしよう！",
    "グアムの楽園へ。お得な旅行プランをチェック！",
    "グアムでの素敵な思い出を作る旅。予約受付中！",
    "グアム旅行で非日常体験を。今すぐ予約！",
    "グアムの美しいビーチでリラックス。予約開始！",
    "グアム旅行で最高の休暇を過ごそう！"
]
# sentences = sentences[:10]


# Calculate Distinct-1 and Distinct-2
for n in range(1,5):
    distinct_n_value = distinct_n(sentences, n)
    print(f"Distinct-{n}: {distinct_n_value}")

