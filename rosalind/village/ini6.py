from collections import Counter

s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in " \
    "my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let" \
    " it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in" \
    " the world agree There will be an answer let it be For though they may be parted there is still a chance " \
    "that they will see There will be an answer let it be Let it be let it be let it be let it be There will b" \
    "e an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be" \
    " let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is st" \
    "ill a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary " \
    "comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be" \
    " an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
words = []

for word in s.split(" "):
    words.append(word)

occurences = Counter(words)

for key, value in occurences.items():
    print(key + " " + str(value))
