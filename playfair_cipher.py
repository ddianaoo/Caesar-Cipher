def generate_playfair_table(key):
    # Формируем таблицу 5x5 из ключа
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
    table = []
    used_chars = set()

    # Добавляем символы из ключа
    for char in key.upper():
        if char not in used_chars and char in alphabet:
            table.append(char)
            used_chars.add(char)
    
    # Добавляем оставшиеся буквы
    for char in alphabet:
        if char not in used_chars:
            table.append(char)
    
    return [table[i:i + 5] for i in range(0, 25, 5)]  # Формируем 5 строк по 5 элементов

def preprocess_text(text):
    # Оставляем только буквы, заменяем 'J' на 'I'
    text = ''.join([char for char in text.upper() if char.isalpha()]).replace("J", "I")
    result = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        if i + 1 < len(text):
            char2 = text[i + 1]
            if char1 == char2:
                result += char1 + 'X'  # Вставляем X между одинаковыми буквами
                i += 1
            else:
                result += char1 + char2
                i += 2
        else:
            result += char1 + 'X'  # Добавляем X в конце, если нечетное количество символов
            i += 1
    return result

def find_position(table, char):
    for row in range(5):
        for col in range(5):
            if table[row][col] == char:
                return row, col
    return None, None

def playfair_cipher(text, key, mode='encode'):
    table = generate_playfair_table(key)
    text = preprocess_text(text)
    result = []

    for i in range(0, len(text), 2):
        row1, col1 = find_position(table, text[i])
        row2, col2 = find_position(table, text[i + 1])

        # Пропускаем пары, если символ не найден в таблице
        if row1 is None or col1 is None or row2 is None or col2 is None:
            continue

        if row1 == row2:  # В одной строке
            if mode == 'encode':
                result.append(table[row1][(col1 + 1) % 5])
                result.append(table[row2][(col2 + 1) % 5])
            else:
                result.append(table[row1][(col1 - 1) % 5])
                result.append(table[row2][(col2 - 1) % 5])
        elif col1 == col2:  # В одном столбце
            if mode == 'encode':
                result.append(table[(row1 + 1) % 5][col1])
                result.append(table[(row2 + 1) % 5][col2])
            else:
                result.append(table[(row1 - 1) % 5][col1])
                result.append(table[(row2 - 1) % 5][col2])
        else:  # Прямоугольник
            result.append(table[row1][col2])
            result.append(table[row2][col1])

    return ''.join(result)
