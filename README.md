# nlp-homework1
## The data I chose:
The data selection I chose to use is the plain text for lord of the ring's description on its wikipedia page and compare it to 7 reviews I found online from https://www.goodreads.com/book/show/33.The_Lord_of_the_Rings and here https://www.google.com/search?client=firefox-b-1-d&q=lord+of+the+rings+book+review.

## Comparing and contrasting the corpa:
The biggest difference between the reviews and the wiki is the use of "I" in the reviews. The wiki does not use the first person, but reviews use it frequently. In general the words of the reviews have fewer syllables. Often the reviews use "is" for a verb. Words like "of", "the", "and", and "a" appear frequently in both. This makes sense as the phrase "Lord of the Rings" is said a lot in both, and "a" is a really common word. As far as the bigrams go, there's a good amount of similarity. As you go further down the list of the most common bigrams, I noticed that the wiki is focused on the characters, where in the reviews' popular bigrams there is not characters mentioned instead "I" and "it" are featured heavily instead.

## Sentence fragment probability:
I took two fairly short sentences out of their respected corpus, "Its indisputable greatness has made it indisputable." and ""War of the Ring" redirects here." First one is from the reviews and the second one is from the wiki. I calculated the odds for both being in their own corpus versus in the other corpus. While each had a significantly small percentage of occurring (even with add one smoothing), the chance of the something apperaring in itself versus the other group of text was still roughly 100x more likely for both sentences.

## Output - here's the output of my code running on my PC:
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
Most common unigrams for wiki:
[(('the',), 277), (('of',), 160), (('and',), 132), (('to',), 99), (('in',), 56), (('The',), 52), (('by',), 42), (('a',), 41), (('is',), 32), (('his',), 31), (('Frodo',), 29), (('Ring',), 27), (('that',), 25), (('they',), 25), (('from',), 23), (('with',), 21), (('but',), 20), (('Gandalf',), 20), (('are',), 18), (('Lord',), 17), (('as',), 17), (('on',), 16), (('for',), 16), (('Pippin',), 16), (('an',), 15), (('it',), 15), (('into',), 13), (('them',), 13), (('Rings',), 12), (('which',), 12)]
Most common bigrams for wiki:
[(('of', 'the'), 60), (('in', 'the'), 24), (('the', 'Ring'), 17), (('Lord', 'of'), 15), (('The', 'Lord'), 13), (('the', 'Rings'), 10), (('to', 'the'), 10), (('Merry', 'and'), 10), (('from', 'the'), 9), (('and', 'Pippin'), 9), (('to', 'be'), 7), (('and', 'the'), 7), (('through', 'the'), 6), (('and', 'his'), 6), (('that', 'the'), 6), (('they', 'are'), 6), (('the', 'hobbits'), 5), (('over', 'the'), 5), (('by', 'the'), 5), (('on', 'the'), 5), (('The', 'Ring'), 5), (('led', 'by'), 5), (('Frodo', 'and'), 5), (('the', 'NazgÃ»l'), 5), (('into', 'the'), 5), (('for', 'the'), 5), (('as', 'a'), 4), (('The', 'Hobbit,'), 4), (('the', 'One'), 4), (('Ring', 'to'), 4)]
Most common unigrams for reviews:
[(('the',), 186), (('of',), 120), (('and',), 107), (('to',), 68), (('a',), 53), (('is',), 53), (('that',), 43), (('in',), 42), (('The',), 35), (('was',), 28), (('I',), 25), (('it',), 25), (('Lord',), 25), (('are',), 24), (('as',), 22), (('with',), 20), (('for',), 18), (('Rings',), 18), (('not',), 16), (('at',), 14), (('my',), 13), (('all',), 13), (('you',), 12), (('one',), 12), (('its',), 12), (('so',), 11), (('read',), 11), (('have',), 11), (('this',), 11), (('they',), 11)] 
Most common bigrams for reviews:
[(('of', 'the'), 48), (('Lord', 'of'), 24), (('The', 'Lord'), 20), (('the', 'Rings'), 16), (('and', 'the'), 13), (('in', 'the'), 11), (('is', 'a'), 9), (('to', 'the'), 8), (('for', 'the'), 7), (('it', 'is'), 6), (('as', 'a'), 6), (('the', 'books'), 5), (('with', 'the'), 5), (('one', 'of'), 5), (('Rings', 'is'), 5), (('I', 'love'), 5), (('the', 'book'), 4), (('it', 'was'), 4), (('that', 'the'), 4), (('as', 'the'), 4), (('of', 'its'), 4), (('in', 'a'), 4), (('It', 'is'), 4), (('was', 'a'), 4), (('the', 'Rings,'), 4), (('was', 'not'), 4), (('characters', 'are'), 3), (('the', 'ring'), 3), (('fact', 'that'), 3), (('parts', 'of'), 3)]    
------------------------------------------------------------------------------
------------------------------------------------------------------------------
------------------------------------------------------------------------------
Probability of sentence being in its own corpus (wiki sentence, reviews sentence)
2.9090355935967726e-19
1.0899938191537587e-14
------------------------------------------------------------------------------
Probability of sentence being in the other corpus (wiki sentence, reviews sentence)
4.545368114994957e-21
5.47230503468588e-16
