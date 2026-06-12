The function returns the rightmost vowel that is not at the beginning or end of the word and whose immediate left and right neighbors are consonants. Vowels are the letters a, e, i, o, u in either lowercase or uppercase, and the returned one-character string preserves the original case. If no such vowel exists, or the word has fewer than three characters, the function returns the empty string.

Notes from formalizer:
- The request says inputs contain English letters only; the formal skeleton does not enforce this as a precondition. For non-letter characters, any non-vowel would be treated as a consonant.
- The phrase "case sensitive" is interpreted as preserving case and recognizing both uppercase and lowercase vowels, consistent with the example returning "U" for "FULL".
