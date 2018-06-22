# Learning Python data analysis.

`*.ipynb files are jupyter-notebook files`

## Anagram

`words` - file contains words of dictionary 


wordset = sorted(list(set([i.strip().lower() for i in open('words', 'r')])))
wordset has unique words in lower case with out new lines 

def anagram(myword):
    return [word for word in wordset if sorted(word) == sorted(myword)]
    
anagram('dictionary')
['dictionary', 'indicatory']

%timeit anagram('dictionary')
461 ms ± 14.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

## Faster Implementation requires storing the anagrams in a Dict and doing lookup. 

import collections
word_by_sig = collections.defaultdict(list)
for word in wordset:
    word_by_sig[signature(word)].append(word)
    
def anagram_fast(myword):
    return word_by_sig[signature(myword)]

anagram_fast('dictionary')
['dictionary', 'indicatory']
    
%timeit anagram_fast('dictionary')
1.52 µs ± 30.8 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)


## Sort by Value 
popular_len_anag = sorted(anagram_by_len.items(), key=lambda kv: -kv[1])

popular_len_anag = sorted(anagram_by_len.items(), key=lambda kv: (-kv[1], kv[0])) # sort by reverse value, then key
