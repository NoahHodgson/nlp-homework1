from collections import Counter
import sys
from nltk import sent_tokenize, ngrams

def main():
        REVIEW_FILE = "LOTR_REVIEW.txt"
        WIKI_FILE = "LOTR_Wikipedia.txt"
        review = open(REVIEW_FILE, "r")
        review = review.read()
        review_sent = sent_tokenize(review)
        review_unigram = ngrams(review.split(), 1)
        for i in review_unigram:
            print(i, end='')
        review_bigram = ngrams(review.split(), 2)
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        wiki = open(WIKI_FILE, "r")
        wiki = wiki.read()
        wiki_sent = sent_tokenize(wiki)
        wiki_unigram = ngrams(wiki.split(), 1)
        for i in wiki_unigram:
            print(i, end='')
        wiki_bigram = ngrams(wiki.split(), 2)
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        for i in review_bigram:
            print(i, end='')
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        for i in wiki_bigram:
            print(i, end='')
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("Most common unigrams for wiki:")
        cnt_wiki = Counter(ngrams(wiki.split(), 1))
        print(cnt_wiki.most_common(30))
        print("Most common bigrams for wiki:")
        cnt_wiki = Counter(ngrams(wiki.split(), 2))
        print(cnt_wiki.most_common(30))
        print("Most common unigrams for reviews:")
        cnt_rev = Counter(ngrams(review.split(), 1))
        print(cnt_rev.most_common(30))
        print("Most common bigrams for reviews:")
        cnt_rev = Counter(ngrams(review.split(), 2))
        print(cnt_rev.most_common(30))
        quit()


if __name__ == "__main__":
    main()