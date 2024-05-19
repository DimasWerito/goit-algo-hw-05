import timeit

# Реалізація алгоритму Боєра-Мура
def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    char_table = make_char_table(pattern)
    offset_table = make_offset_table(pattern)
    i = m - 1
    while i < n:
        j = m - 1
        while pattern[j] == text[i]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        i += max(offset_table[m - 1 - j], char_table.get(text[i], m))
    return -1

def make_char_table(pattern):
    table = {}
    for i in range(len(pattern) - 1):
        table[pattern[i]] = len(pattern) - 1 - i
    return table

def make_offset_table(pattern):
    table = []
    last_prefix_position = len(pattern)
    for i in range(len(pattern) - 1, -1, -1):
        if is_prefix(pattern, i + 1):
            last_prefix_position = i + 1
        table.append(last_prefix_position - i + len(pattern) - 1)
    for i in range(len(pattern) - 1):
        slen = suffix_length(pattern, i)
        table[slen] = len(pattern) - 1 - i + slen
    return table

def is_prefix(pattern, p):
    j = 0
    for i in range(p, len(pattern)):
        if pattern[i] != pattern[j]:
            return False
        j += 1
    return True

def suffix_length(pattern, p):
    length = 0
    j = len(pattern) - 1
    i = p
    while i >= 0 and pattern[i] == pattern[j]:
        length += 1
        i -= 1
        j -= 1
    return length

# Реалізація алгоритму Кнута-Морріса-Пратта
def knuth_morris_pratt(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Реалізація алгоритму Рабіна-Карпа
def rabin_karp(text, pattern, d=256, q=101):
    M = len(pattern)
    N = len(text)
    i = 0
    j = 0
    p = 0  # hash value for pattern
    t = 0  # hash value for text
    h = 1

    for i in range(M-1):
        h = (h * d) % q

    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            else:
                return i
        if i < N - M:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q
    return -1

# Визначимо текст статті
text1 = """
ВИКОРИСТАННЯ АЛГОРИТМІВ У БІБЛІОТЕКАХ МОВ ПРОГРАМУВАННЯ
Автори публiкації: Коваленко О.О., Корягіна Д.О. Вінницький національний технічний університет
Анотація: У данній статті було розглянуто використання алгоритмів у бібліотеках мов програмування. Ключові слова: алгоритми, сортування, лінійний пошук, двійковий пошук, пошук стрибками, інтерполяційний пошук, експоненціальний пошук, жадібний алгоритм.
Стаття
За всю історію комп'ютерних наук склалося розуміння, які алгоритми та структури даних (способи їх зберігання) потрібні для вирішення практичних завдань, певний набір, який повинен знати кожен розробник. Наприклад, сортування: товари в магазині сортують за вартістю або терміну придатності, а ресторани – за віддаленістю або рейтингу. Хеш-таблиці допомагають перевірити коректність пароля та не зберігати його на сайті у відкритому вигляді, графи – знаходити найкоротший шлях і зберігати зв'язки між користувач...
Алгоритми – це послідовність точно визначених дій, які призводять до вирішення поставленої задачі чи певного завдання і на сьогодні уже створено величезну кількість алгоритмів для вирішення важких задач, що полегшують написання коду будь-якому програмісту, особливо початківцям.
Метою роботи є виявлення найбільш популярних алгоритмів у бібліотеках мов програмування.
"""

text2 = """
За всю історію комп'ютерних наук склалося розуміння, які алгоритми та структури даних (способи їх зберігання) потрібні для вирішення практичних завдань, певний набір, який повинен знати кожен розробник. Наприклад, сортування: товари в магазині сортують за вартістю або терміну придатності, а ресторани – за віддаленістю або рейтингу. Хеш-таблиці допомагають перевірити коректність пароля та не зберігати його на сайті у відкритому вигляді, графи – знаходити найкоротший шлях і зберігати зв'язки між користувач...
Алгоритми – це послідовність точно визначених дій, які призводять до вирішення поставленої задачі чи певного завдання і на сьогодні уже створено величезну кількість алгоритмів для вирішення важких задач, що полегшують написання коду будь-якому програмісту, особливо початківцям.
Метою роботи є виявлення найбільш популярних алгоритмів у бібліотеках мов програмування.
"""

# Вибір підрядків для пошуку
existing_substring = "структури даних"
fake_substring = "невідомий елемент"

# Функція для вимірювання часу виконання
def measure_time(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=10)

# Вимірюємо час для кожного алгоритму
results = {}
for text, label in [(text1, "Text1"), (text2, "Text2")]:
    results[label] = {}
    for algorithm, func in [("Boyer-Moore", boyer_moore_search), 
                            ("Knuth-Morris-Pratt", knuth_morris_pratt), 
                            ("Rabin-Karp", rabin_karp)]:
        results[label][algorithm] = {
            "existing": measure_time(func, text, existing_substring),
            "fake": measure_time(func, text, fake_substring)
        }

# Виводимо результати
results


print(results)