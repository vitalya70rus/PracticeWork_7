strs = ["abc", "def", "ghi"]
finally_len = 0
for str in strs:
    finally_len += len(str)
print(finally_len)