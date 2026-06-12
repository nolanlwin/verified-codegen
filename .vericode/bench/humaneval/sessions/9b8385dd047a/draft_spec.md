The function returns true exactly when the input is a date string in the exact form mm-dd-yyyy. This means the string has length 10, has hyphens in positions 3 and 6, and all other positions are decimal digits. The month is parsed from the first two digits and must be between 1 and 12. The day is parsed from the two digits after the first hyphen and must be at least 1 and no more than the maximum allowed for that month: 31 days for months 1, 3, 5, 7, 8, 10, and 12; 30 days for months 4, 6, 9, and 11; and 29 days for month 2. The year must consist of exactly four digits but has no additional numeric restriction.

Notes from formalizer:
- February is allowed to have up to 29 days for every year; leap-year rules are not specified or enforced.
- The year field is only checked for being four digits; no minimum, maximum, or calendar-era constraint is imposed.
- The format is interpreted strictly as two month digits, a hyphen, two day digits, a hyphen, and four year digits, so inputs with missing leading zeros or slash separators are invalid.
