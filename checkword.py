from uzwords import words
from difflib import get_close_matches
from isasci import to_crill
from isasci import to_latin  # bu siz yaratgan lotinga o'tkazish funksiyasi


def checkWord(word, words=words):
    original_word = word  # foydalanuvchi asl yozgan so'zni saqlaymiz
    word_crill = to_crill(word)  # lotincha bo'lsa krillga o'tkazamiz
    word_crill = word_crill.lower()  # hamma harflarni kichik qilamiz

    matches = list(get_close_matches(word_crill, words, n=5))
    available = False

    # Agar so'z to'g'ri bo'lsa
    if word_crill in matches:
        available = True
        matches = [word_crill]
    else:
        # "ҳ" va "х" o'xshashligini tekshiramiz
        if "ҳ" in word_crill:
            word_crill = word_crill.replace("ҳ", "х")
            matches += get_close_matches(word_crill, words, n=5)
        elif "х" in word_crill:
            word_crill = word_crill.replace("х", "ҳ")
            matches += get_close_matches(word_crill, words, n=5)

    # Takroriylarni olib tashlaymiz va faqat 5 ta variant
    matches = list(dict.fromkeys(matches))[:5]

    # Javobni foydalanuvchi yozuvi turiga qarab qaytarish
    matches_output = []
    if original_word.isascii():
        matches_output = [to_latin(m) for m in matches]  # lotincha
    else:
        matches_output = matches  # krilcha

    return {"available": available, "matches": matches_output, "original": original_word}



if __name__ == "__main__":
    test_words = ["salom", "ҳат", "kitob", "maktab"]
    for w in test_words:
        print(checkWord(w))
