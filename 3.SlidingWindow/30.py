def minWindow(s, t):
    if not s or not t:
        return ""

    # Tạo từ điển tần số cho t
    dict_t = {}
    for char in t:
        if char in dict_t:
            dict_t[char] += 1
        else:
            dict_t[char] = 1

    required = len(dict_t)

    # Con trỏ trái và phải của cửa sổ
    l, r = 0, 0

    # formed dùng để theo dõi số ký tự độc nhất trong t hiện tại đã có đủ số lần xuất hiện cần thiết trong cửa sổ
    formed = 0

    # Dictionary dùng để đếm số ký tự trong cửa sổ hiện tại
    window_counts = {}

    # Kết quả lưu trữ dạng (độ dài cửa sổ, chỉ số trái, chỉ số phải)
    ans = float("inf"), None, None

    while r < len(s):
        # Thêm một ký tự từ bên phải vào cửa sổ
        character = s[r]
        if character in window_counts:
            window_counts[character] += 1
        else:
            window_counts[character] = 1

        # Nếu tần số của ký tự này trong cửa sổ bằng với tần số cần thiết trong t thì tăng biến formed lên
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Cố gắng thu nhỏ cửa sổ khi có đủ các ký tự cần thiết
        while l <= r and formed == required:
            character = s[l]

            # Lưu kết quả nếu cửa sổ hiện tại nhỏ hơn cửa sổ đã lưu trước đó
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # Loại bỏ ký tự từ bên trái của cửa sổ
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Di chuyển con trỏ trái để thu nhỏ cửa sổ
            l += 1

        # Tiếp tục mở rộng cửa sổ bằng cách di chuyển con trỏ phải
        r += 1

    return "" if ans[1] is None else s[ans[1] : ans[2] + 1]

# Ví dụ sử dụng:
s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))  # Output: "BANC"
