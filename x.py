def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    seen = set()
    matrix = []

    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    return [matrix[i*5:(i+1)*5] for i in range(5)]

def preprocess_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i + 1 < len(text) else 'X'

        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + b
            i += 2

    if len(result) % 2 != 0:
        result += 'X'
    return result

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None, None

def playfair_encrypt(text, matrix):
    result = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # cùng hàng
            result += matrix[row1][(col1 + 1) % 5]
            result += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # cùng cột
            result += matrix[(row1 + 1) % 5][col1]
            result += matrix[(row2 + 1) % 5][col2]
        else:  # hình chữ nhật
            result += matrix[row1][col2]
            result += matrix[row2][col1]
    return result

def main():
    try:
        input_path = 'C:/Users/COMPUTER/Documents/HoVanCuong/Nhom6/AES/Bai1/input.txt'
        output_path = 'C:/Users/COMPUTER/Documents/HoVanCuong/Nhom6/AES/Bai1/output.txt'

        with open(input_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        if not lines or not lines[0].startswith('KEY='):
            raise ValueError("File input.txt phải bắt đầu bằng 'KEY='")

        key = lines[0].strip().split('=')[1]
        text = ''.join(lines[1:]).strip()

        matrix = generate_key_matrix(key)
        clean_text = preprocess_text(text)
        cipher_text = playfair_encrypt(clean_text, matrix)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(cipher_text)

        print("Mã hóa Playfair thành công. Kết quả được lưu vào output.txt.")
    except Exception as e:
        print(" Lỗi:", e)

if __name__ == '__main__':
    main()
