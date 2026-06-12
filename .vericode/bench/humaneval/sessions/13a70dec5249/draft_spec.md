The function returns an encoded version of the input message by processing characters from left to right. Each vowel is replaced by the letter two positions later in the English alphabet, with case swapped: lowercase vowels map to uppercase shifted vowels/consonants (`a->C`, `e->G`, `i->K`, `o->Q`, `u->W`) and uppercase vowels map to lowercase shifted letters (`A->c`, `E->g`, `I->k`, `O->q`, `U->w`). All other alphabetic letters have their case swapped. Characters that are not explicitly listed as letters, such as spaces, are left unchanged.

Notes from formalizer:
- The original text says to assume only letters, but the examples include spaces. This specification leaves non-letter characters unchanged so that the provided space-containing example is covered.
- The vowel transformation is interpreted as shifting the vowel two letters ahead and applying the overall case-swap behavior, matching the examples such as `test -> TGST` and `This is a message -> tHKS KS C MGSSCGG`.
