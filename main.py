from collections import Counter
from random import random
import sys
from nltk import sent_tokenize, ngrams

#uses add 1 smoothing
def calculate_prob(sentence:str, corp_uni:Counter, corp_bi:Counter, vocab: int) -> float:
    prob = 1
    bigrams = ngrams(sentence.split(), 2)
    for bigram in bigrams:
        prob *= (corp_bi[bigram]+1) / (corp_uni[bigram[0]] + vocab)
    return prob


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
        cnt_wiki2 = Counter(ngrams(wiki.split(), 2))
        print(cnt_wiki2.most_common(30))
        print("Most common unigrams for reviews:")
        cnt_rev1 = Counter(ngrams(review.split(), 1))
        print(cnt_rev1.most_common(30))
        print("Most common bigrams for reviews:")
        cnt_rev2 = Counter(ngrams(review.split(), 2))
        print(cnt_rev2.most_common(30))
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------")
        #add one smoothing goes here 
        random_rev_set = "Its indisputable greatness has made it indisputable."
        random_wiki_set = "\"War of the Ring\" redirects here."
        
        vocab_len = len(list(cnt_rev1)) + len(list(cnt_wiki1))
        
        print(calculate_prob(random_rev_set, cnt_rev1, cnt_rev2, vocab_len))
        print(calculate_prob(random_wiki_set, cnt_wiki1, cnt_wiki2, vocab_len))

        print(vocab_len)
        quit()


if __name__ == "__main__":
    main()