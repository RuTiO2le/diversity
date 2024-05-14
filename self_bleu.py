import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from collections import Counter
import numpy as np

from tokenize_japanese import tokenize_japanese


# Function to calculate Self-BLEU
def self_bleu(sentences):
    bleu_scores = []

    for i, sentence in enumerate(sentences):
        references = [tokenize_japanese(s) for j, s in enumerate(sentences) if i != j]
        candidate = tokenize_japanese(sentence)
        if not references:
            continue
        bleu_score = sentence_bleu(references, candidate, smoothing_function=SmoothingFunction().method1)
        bleu_scores.append(bleu_score)

    if not bleu_scores:
        return 0.0

    return np.mean(bleu_scores)


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


# Calculate Self-BLEU
for i in range(2, len(sentences)+1, 5):
    self_bleu_score = self_bleu(sentences[:i])
    print(f"Self-BLEU (up to {i} sentences): {self_bleu_score}")
# self_bleu_score = self_bleu(sentences)
# print(f"Self-BLEU: {self_bleu_score}")