The function accepts two planet names. It recognizes exactly the eight planet names Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune, in that order from closest to farthest from the Sun. If either input is not one of these exact names, the result is empty. Otherwise, the result contains all planets strictly between the two given planets' orbital positions, ordered from closest to farthest from the Sun. The endpoint planets themselves are not included.

Notes from formalizer:
- The requested Python tuple is modeled internally as an ordered sequence of strings; this represents the same ordered collection of planet names.
- Planet name matching is exact and case-sensitive, matching the examples and listed names.
- If both input planets are the same valid planet, there are no planets strictly between them, so the result is empty.
