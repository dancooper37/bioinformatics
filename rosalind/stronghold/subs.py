with open("../test_data/subs.txt", "r") as f:
    s = f.readline().rstrip()  # Uses rstrip() to remove any newline chars
    t = f.readline().rstrip()

print(s + "\n" + t)


def findSubstring(fullStr, sub):
    start = 0
    while True:
        start = fullStr.find(sub, start)
        if start == -1:
            return
        yield start
        start += 1


print(" ".join([str(i + 1) for i in list(findSubstring(s, t))]))


