from collections import Counter
import string
with open("words.txt","w") as f:
    f.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Vivamus lacinia odio vitae vestibulum vestibulum.  Cras venenatis euismod malesuada. Integer nec odio. Praesent libero. \nSed cursus ante dapibus diamLorem ipsum dolor sit amet, \nconsectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum.  Cras venenatis euismod malesuada. Integer nec odio. Praesent libero.  Sed cursus ante dapibus diamt")
with open("words.txt","r") as f:
    data = f.read()
    words = data.split(string.punctuation)
    word_count = Counter(words)

    print(word_count)


