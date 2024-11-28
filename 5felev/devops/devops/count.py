import re
from collections import Counter

# Read your Markdown file
with open('devops.md', 'r') as file:
    content = file.readlines()

# Filter lines that are titles with ##
titles = [line.strip() for line in content if line.startswith('##')]

# Check for repeated words in each title
repeated_words = {}
for title in titles:
    # Extract words and count them
    words = re.findall(r'\b\w+\b', title.lower())
    word_counts = Counter(words)
    
    # Keep only words with counts > 1
    duplicates = {word: count for word, count in word_counts.items() if count > 1}
    if duplicates:
        repeated_words[title] = duplicates

# Output results
for title, duplicates in repeated_words.items():
    print(f"Title: {title}")
    print(f"Repeated Words: {duplicates}")
