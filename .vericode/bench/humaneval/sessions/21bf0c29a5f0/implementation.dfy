datatype OptionalString = NoneString | SomeString(value: string)

datatype Md5State = Md5State(a: int, b: int, c: int, d: int)

function Pow2(n: int): int
  decreases n
{
  if n == 0 then 1 else 2 * Pow2(n - 1)
}

function Uint32(x: int): int
{
  ((x % Pow2(32)) + Pow2(32)) % Pow2(32)
}

function Bit(x: int, k: int): int
  decreases k
{
  if k == 0 then x % 2 else Bit(x / 2, k - 1)
}

function BitsToIntAux(bits: seq<int>, i: int): int
  decreases |bits| - i
{
  if i == |bits| then 0 else bits[i] * Pow2(i) + BitsToIntAux(bits, i + 1)
}

function AndBits32(a: int, b: int, k: int): seq<int>
  decreases 32 - k
{
  if k == 32 then [] else [if Bit(a, k) == 1 && Bit(b, k) == 1 then 1 else 0] + AndBits32(a, b, k + 1)
}

function OrBits32(a: int, b: int, k: int): seq<int>
  decreases 32 - k
{
  if k == 32 then [] else [if Bit(a, k) == 1 || Bit(b, k) == 1 then 1 else 0] + OrBits32(a, b, k + 1)
}

function XorBits32(a: int, b: int, k: int): seq<int>
  decreases 32 - k
{
  if k == 32 then [] else [if Bit(a, k) != Bit(b, k) then 1 else 0] + XorBits32(a, b, k + 1)
}

function BitAnd32(a: int, b: int): int
{
  BitsToIntAux(AndBits32(Uint32(a), Uint32(b), 0), 0)
}

function BitOr32(a: int, b: int): int
{
  BitsToIntAux(OrBits32(Uint32(a), Uint32(b), 0), 0)
}

function BitXor32(a: int, b: int): int
{
  BitsToIntAux(XorBits32(Uint32(a), Uint32(b), 0), 0)
}

function BitNot32(a: int): int
{
  Uint32(Pow2(32) - 1 - Uint32(a))
}

function LeftRotate32(x: int, s: int): int
{
  Uint32(Uint32(x) * Pow2(s) + Uint32(x) / Pow2(32 - s))
}

function CharCode(c: char): int
{
  c as int
}

function Utf8Char(c: char): seq<int>
{
  var n := CharCode(c);
  if n < 128 then [n]
  else if n < 2048 then [192 + n / 64, 128 + n % 64]
  else if n < 65536 then [224 + n / 4096, 128 + (n / 64) % 64, 128 + n % 64]
  else [240 + n / 262144, 128 + (n / 4096) % 64, 128 + (n / 64) % 64, 128 + n % 64]
}

function StringBytesAux(text: string, i: int): seq<int>
  decreases |text| - i
{
  if i == |text| then [] else Utf8Char(text[i]) + StringBytesAux(text, i + 1)
}

function StringBytes(text: string): seq<int>
{
  StringBytesAux(text, 0)
}

function Zeros(n: int): seq<int>
  decreases n
{
  if n == 0 then [] else [0] + Zeros(n - 1)
}

function LittleEndianBytes(value: int, count: int): seq<int>
  decreases count
{
  if count == 0 then [] else [value % 256] + LittleEndianBytes(value / 256, count - 1)
}

function Md5ZeroPadCount(len: int): int
{
  (56 - ((len + 1) % 64) + 64) % 64
}

function Md5PaddedMessage(bytes: seq<int>): seq<int>
{
  bytes + [128] + Zeros(Md5ZeroPadCount(|bytes|)) + LittleEndianBytes((|bytes| * 8) % Pow2(64), 8)
}

function Md5InitialState(): Md5State
{
  Md5State(1732584193, 4023233417, 2562383102, 271733878)
}

function Md5S(i: int): int
{
  if i < 16 then if i % 4 == 0 then 7 else if i % 4 == 1 then 12 else if i % 4 == 2 then 17 else 22
  else if i < 32 then if i % 4 == 0 then 5 else if i % 4 == 1 then 9 else if i % 4 == 2 then 14 else 20
  else if i < 48 then if i % 4 == 0 then 4 else if i % 4 == 1 then 11 else if i % 4 == 2 then 16 else 23
  else if i % 4 == 0 then 6 else if i % 4 == 1 then 10 else if i % 4 == 2 then 15 else 21
}

function Md5K(i: int): int
{
  if i == 0 then 3614090360 else if i == 1 then 3905402710 else if i == 2 then 606105819 else if i == 3 then 3250441966 else
  if i == 4 then 4118548399 else if i == 5 then 1200080426 else if i == 6 then 2821735955 else if i == 7 then 4249261313 else
  if i == 8 then 1770035416 else if i == 9 then 2336552879 else if i == 10 then 4294925233 else if i == 11 then 2304563134 else
  if i == 12 then 1804603682 else if i == 13 then 4254626195 else if i == 14 then 2792965006 else if i == 15 then 1236535329 else
  if i == 16 then 4129170786 else if i == 17 then 3225465664 else if i == 18 then 643717713 else if i == 19 then 3921069994 else
  if i == 20 then 3593408605 else if i == 21 then 38016083 else if i == 22 then 3634488961 else if i == 23 then 3889429448 else
  if i == 24 then 568446438 else if i == 25 then 3275163606 else if i == 26 then 4107603335 else if i == 27 then 1163531501 else
  if i == 28 then 2850285829 else if i == 29 then 4243563512 else if i == 30 then 1735328473 else if i == 31 then 2368359562 else
  if i == 32 then 4294588738 else if i == 33 then 2272392833 else if i == 34 then 1839030562 else if i == 35 then 4259657740 else
  if i == 36 then 2763975236 else if i == 37 then 1272893353 else if i == 38 then 4139469664 else if i == 39 then 3200236656 else
  if i == 40 then 681279174 else if i == 41 then 3936430074 else if i == 42 then 3572445317 else if i == 43 then 76029189 else
  if i == 44 then 3654602809 else if i == 45 then 3873151461 else if i == 46 then 530742520 else if i == 47 then 3299628645 else
  if i == 48 then 4096336452 else if i == 49 then 1126891415 else if i == 50 then 2878612391 else if i == 51 then 4237533241 else
  if i == 52 then 1700485571 else if i == 53 then 2399980690 else if i == 54 then 4293915773 else if i == 55 then 2240044497 else
  if i == 56 then 1873313359 else if i == 57 then 4264355552 else if i == 58 then 2734768916 else if i == 59 then 1309151649 else
  if i == 60 then 4149444226 else if i == 61 then 3174756917 else if i == 62 then 718787259 else 3951481745
}

function Md5F(i: int, b: int, c: int, d: int): int
{
  if i < 16 then BitOr32(BitAnd32(b, c), BitAnd32(BitNot32(b), d))
  else if i < 32 then BitOr32(BitAnd32(d, b), BitAnd32(BitNot32(d), c))
  else if i < 48 then BitXor32(BitXor32(b, c), d)
  else BitXor32(c, BitOr32(b, BitNot32(d)))
}

function Md5G(i: int): int
{
  if i < 16 then i else if i < 32 then (5 * i + 1) % 16 else if i < 48 then (3 * i + 5) % 16 else (7 * i) % 16
}

function WordAt(block: seq<int>, index: int): int
{
  block[4 * index] + 256 * block[4 * index + 1] + 65536 * block[4 * index + 2] + 16777216 * block[4 * index + 3]
}

function Md5RoundStep(block: seq<int>, i: int, state: Md5State): Md5State
{
  var f := Md5F(i, state.b, state.c, state.d);
  var g := Md5G(i);
  var nb := Uint32(state.b + LeftRotate32(Uint32(state.a + f + Md5K(i) + WordAt(block, g)), Md5S(i)));
  Md5State(state.d, nb, state.b, state.c)
}

function Md5Round64(block: seq<int>, i: int, state: Md5State): Md5State
  decreases 64 - i
{
  if i == 64 then state else Md5Round64(block, i + 1, Md5RoundStep(block, i, state))
}

function Md5ProcessChunks(message: seq<int>, offset: int, state: Md5State): Md5State
  decreases |message| - offset
{
  if offset == |message| then state
  else
    var rounded := Md5Round64(message[offset..offset + 64], 0, state);
    var combined := Md5State(Uint32(state.a + rounded.a), Uint32(state.b + rounded.b), Uint32(state.c + rounded.c), Uint32(state.d + rounded.d));
    Md5ProcessChunks(message, offset + 64, combined)
}

function HexNibble(n: int): string
{
  if n == 0 then "0" else if n == 1 then "1" else if n == 2 then "2" else if n == 3 then "3" else
  if n == 4 then "4" else if n == 5 then "5" else if n == 6 then "6" else if n == 7 then "7" else
  if n == 8 then "8" else if n == 9 then "9" else if n == 10 then "a" else if n == 11 then "b" else
  if n == 12 then "c" else if n == 13 then "d" else if n == 14 then "e" else "f"
}

function ByteToHex(b: int): string
{
  HexNibble(b / 16) + HexNibble(b % 16)
}

function BytesToHex(bytes: seq<int>, i: int): string
  decreases |bytes| - i
{
  if i == |bytes| then "" else ByteToHex(bytes[i]) + BytesToHex(bytes, i + 1)
}

function Md5DigestBytes(state: Md5State): seq<int>
{
  LittleEndianBytes(Uint32(state.a), 4) + LittleEndianBytes(Uint32(state.b), 4) + LittleEndianBytes(Uint32(state.c), 4) + LittleEndianBytes(Uint32(state.d), 4)
}

function Md5HexString(text: string): string
{
  var bytes := StringBytes(text);
  var padded := Md5PaddedMessage(bytes);
  var finalState := Md5ProcessChunks(padded, 0, Md5InitialState());
  BytesToHex(Md5DigestBytes(finalState), 0)
}

function StringToMd5Spec(text: string): OptionalString
{
  if |text| == 0 then NoneString else SomeString(Md5HexString(text))
}

method string_to_md5(text: string) returns (result: OptionalString)
  ensures result == StringToMd5Spec(text)
{
  result := StringToMd5Spec(text);
}
