import MeCab
from collections import Counter
import numpy as np

from tokenize_japanese import tokenize_japanese


# Function to calculate Hill numbers
def hill_number(sentences, q):
    # Tokenize all sentences and count frequencies of tokens
    all_tokens = []
    for sentence in sentences:
        tokens = tokenize_japanese(sentence)
        all_tokens.extend(tokens)
    
    token_counts = Counter(all_tokens)
    total_tokens = sum(token_counts.values())
    
    # Calculate relative frequencies
    relative_frequencies = np.array([count / total_tokens for count in token_counts.values()])
    
    if q == 1:
        # Hill number for q = 1 is the exponential of Shannon entropy
        entropy = -sum(relative_frequencies * np.log(relative_frequencies))
        return np.exp(entropy)
    else:
        # General case for Hill number
        return (sum(relative_frequencies ** q)) ** (1 / (1 - q))


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


# Calculate Hill numbers for different orders
hill_0 = hill_number(sentences, 0)  # Species richness (number of unique tokens)
hill_1 = hill_number(sentences, 1)  # Exponential of Shannon entropy
hill_2 = hill_number(sentences, 2)  # Inverse Simpson index

print(f"Hill number (q=0): {hill_0}")
print(f"Hill number (q=1): {hill_1}")
print(f"Hill number (q=2): {hill_2}")

for i in range(3, 11):
    hill_q = hill_number(sentences, i)
    print(f"Hill number (q={i}): {hill_q}")