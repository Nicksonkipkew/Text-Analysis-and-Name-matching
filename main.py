import requests
import difflib
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')
def download_book_text(url):
  
  response = requests.get(url)
  if response.status_code == 200:
    print("kekke")
    return response.text
  else:
    print("Failed to download the book.")
    return None
    
def check_name_presence(book_text, name):
  if name.lower() in book_text.lower():
    print(f"The name '{name}' is present in the book.")
  else:
    print(f"The name '{name}' is not found in the book.")

def find_close_matches(book_text, name):
  close_matches = difflib.get_close_matches(name, book_text.split(), n=5, cutoff=0.8)
  if close_matches:
    print("Close matches found:")
    for match in close_matches:
            print(match)
  else:
    print("No close matches found.")
    
#Find and print the most frequent words in the book.
def find_most_frequent_words(book_text, top_n):
  tokens = word_tokenize(book_text)
  stop_words = set(stopwords.words("english"))
  filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words] #isalpha checks if token conatain alphabetic charactersd only.
  word_freq = Counter(filtered_tokens)
  top_words = word_freq.most_common(top_n)
  print(f"Top {top_n} frequent words:")
  for word, frequency in top_words:
    print(f"{word}: {frequency}")

#Generate & display a word cloud based the provided book text.
def generate_word_cloud(book_text):
  tokens = word_tokenize(book_text)
  stop_words = set(stopwords.words("english"))
  filtered_tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]
  wordcloud = WordCloud(width=800, height=400).generate(" ".join(filtered_tokens))
  plt.figure(figsize=(10, 5))
  plt.imshow(wordcloud, interpolation="bilinear")
  plt.axis("off")
  plt.show()



book_id = 46
book_url = f"https://www.gutenberg.org/files/{book_id}/{book_id}-0.txt"    
book_text = download_book_text(book_url)

if book_text:
  check_name_presence(book_text, "Great")
  find_close_matches(book_text, "work")
  find_most_frequent_words(book_text, 10)
  generate_word_cloud(book_text)