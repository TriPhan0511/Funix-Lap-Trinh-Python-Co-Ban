# #
# lab 16_1

# Đề bài :
# Ở bài toán dưới đây, bạn được cung cấp danh sách các quốc gia ở mảng country và
# danh sách số lương huy chương vàng của từng quốc gia.
# Bạn cần hoàn thành đoạn code để lấy danh sách huy chương vàng theo các quốc gia ở mảng country,
# nếu như không có dữ liệu ở biến gold thì hãy trả về "Did not get gold". Ví dụ như sau:

# gold = {"US": 46, "Fiji": 1, "Great Britain": 27, "Cuba": 5, "Thailand": 2, "China": 26, "France": 10}
# country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]

# Thì kết quả sẽ là:

# [1, 'Did not get gold', 'Did not get gold', 10, 'Did not get gold', 46]
#


gold = {"US": 46, "Fiji": 1, "Great Britain": 27,
        "Cuba": 5, "Thailand": 2, "China": 26, "France": 10}
country = ["Fiji", "Chile", "Mexico", "France", "Norway", "US"]
country_gold = []

# Solution 1:
for x in country:
    try:
        country_gold.append(gold[x])
    except KeyError:
        country_gold.append('Did not get gold')

print(country_gold)


# # Solution 2:
# for x in country:
#     country_gold.append(gold.get(x, 'Did not get gold'))

# print(country_gold)
