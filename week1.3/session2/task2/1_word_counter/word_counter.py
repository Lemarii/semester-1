from pathlib import Path

for filename in ("story.txt", "story2.txt", "glasses.txt"):
	file_path = Path(__file__).with_name(filename)
	with file_path.open(encoding="utf-8") as text_file:
		words = text_file.read().split()
	word_count = len(words)
	print(f"{filename}: {word_count}")

# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.

# open and read the file

# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210