import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                            .lower()
                            .split()
                        if word not in banned]

counter = collections.Counter(words)
print(counter.most_common(1)[0][0])