import sys
import re
from nltk.tokenize import sent_tokenize

def main():
        REVIEW_FILE = "LOTR_REVIEW.txt"
        WIKI_FILE = "LOTR_Wikipedia.txt"
        review = open(REVIEW_FILE, "r")
        review = review.read()
        review_sent = sent_tokenize(review)
        print(review_sent)
        print("------------------------------------------------------------------------------")
        wiki = open(WIKI_FILE, "r")
        wiki = wiki.read()
        wiki_sent = sent_tokenize(wiki)
        print(wiki_sent)
        quit()


if __name__ == "__main__":
    main()