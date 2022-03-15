from collections import Counter
from random import random
import sys
from nltk import sent_tokenize, ngrams

#uses add 1 smoothing
def process_unigrams_prob(sent: str, corp:Counter) -> int:
    val = 0
    sent = list(set(sent.split()))
    words = ngrams(sent, 1)
    for word in words:
        val += 1 + corp[word]
    print(val)
    return val

def calculate_prob() -> float:
    

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
        cnt_wiki1 = Counter(ngrams(wiki.split(), 1))
        print(cnt_wiki1.most_common(30))
        print("Most common bigrams for wiki:")
        cnt_wiki = Counter(ngrams(wiki.split(), 2))
        print(cnt_wiki.most_common(30))
        print("Most common unigrams for reviews:")
        cnt_rev1 = Counter(ngrams(review.split(), 1))
        print(cnt_rev1.most_common(30))
        print("Most common bigrams for reviews:")
        cnt_rev = Counter(ngrams(review.split(), 2))
        print(cnt_rev.most_common(30))
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        #add one smoothing goes here 
        random_rev_set = "To the tear-choked death of Boromir, to the triumph of Gondor, Lord of the Rings has never failed in overripe entertainment and overall attraction."
        random_wiki_set = "There, Boromir tries to take the Ring from Frodo, but immediately regrets it after Frodo puts on the Ring and disappears."
        vocab_len = len(list(cnt_rev1)) + len(list(cnt_wiki1))
        process_unigrams_prob(random_wiki_set, cnt_wiki1)
        proccess_bigram_prob(random_wiki_set, cnt_wiki)
        process_unigrams_prob(random_rev_set, cnt_rev1)
        proccess_bigram_prob(random_rev_set, cnt_rev)
        print(vocab_len)
        quit()


if __name__ == "__main__":
    main()