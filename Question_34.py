#Sort a dictionary by its values.

data = {"apple": 40, "banana": 10, "cherry": 30, "date": 20}
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
print("Ascending:", sorted_data)
sorted_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
print("Descending:", sorted_desc)
