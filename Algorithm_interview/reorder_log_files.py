logs = ["dig1 8 1 5 1", "let1 art can", "dig 2 3 6", "let2 own kit dig", "let3 art zero"]
digits = []
letters = []

for log in logs:
    if log.split()[1].isdigit():
        digits.append(log)
    else:
        letters.append(log)

# letters lambda 정렬
letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(letters + digits)
