"""
    Name: wikipedia_1.py
"""
# pip install wikipedia
import wikipedia

# Type in your search term
result = input("Search Wikipedia: ")

# Return a summary result of 3 sentences
summary = wikipedia.summary(result, sentences=3)

# Print result
print(summary)