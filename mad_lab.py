# import re
# story = "Today, I went to the (place) to see what the scientists were working onWhen I walked in, I saw a (adjective) (animal) running around the room.One scientist shouted, “Quick! Grab the (noun) before it knocks over the (plural noun)!”I tried to help by using a (tool), but instead I slipped on a puddle of (liquid).Everyone laughed so hard that their (body part, plural) started to hurt.Finally, the head scientist announced, “Don’t worry, we have created the world’s first (adjective) (invention)!”The entire lab cheered, and I celebrated by eating a giant bowl of (food).It was the most (adjective) day ever"
# words = set()
# dic = {}
# words = re.findall(r"\(.*?\)", story)
#
# for word in words:
#     dic[word] = input("enter the replacement for word " + word + ": ")
# for word,
# story = story.replace(word, dic[word])
# print(story)
import re

story = "Today, I went to the (place) to see what the scientists were working on. When I walked in, I saw a (adjective) (animal) running around the room. One scientist shouted, “Quick! Grab the (noun) before it knocks over the (plural noun)!” I tried to help by using a (tool), but instead I slipped on a puddle of (liquid). Everyone laughed so hard that their (body part, plural) started to hurt. Finally, the head scientist announced, “Don’t worry, we have created the world’s first (adjective) (invention)!” The entire lab cheered, and I celebrated by eating a giant bowl of (food). It was the most (adjective) day ever."

# 1️⃣ Extract placeholders
words = re.findall(r"\(.*?\)", story)  # finds all (placeholders)

# 2️⃣ Ask user for replacements
dic = {}
for word in set(words):  # use set() so we ask only once per placeholder
    dic[word] = input(f"Enter a replacement for {word}: ")

# 3️⃣ Replace in story
for word in words:
    story = story.replace(word, dic[word])

# 4️⃣ Print final story
print("\nFinal Story:\n")
print(story)