with open("alice_in_wonderland.txt", encoding="utf-8") as f:
    alice_text = f.read()

alice_text_as_string = str(alice_text)

alice_text_single_words = alice_text_as_string.split()
print(sorted(alice_text_single_words)[0:10])