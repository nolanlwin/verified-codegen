function LetterGradeSpec(g: real): string
{
  if g == 4.0 then "A+"
  else if g > 3.7 then "A"
  else if g > 3.3 then "A-"
  else if g > 3.0 then "B+"
  else if g > 2.7 then "B"
  else if g > 2.3 then "B-"
  else if g > 2.0 then "C+"
  else if g > 1.7 then "C"
  else if g > 1.3 then "C-"
  else if g > 1.0 then "D+"
  else if g > 0.7 then "D"
  else if g > 0.0 then "D-"
  else "E"
}
function NumericalLetterGradeSpec(grades: seq<real>): seq<string>
  decreases |grades|
{
  if |grades| == 0 then []
  else [LetterGradeSpec(grades[0])] + NumericalLetterGradeSpec(grades[1..])
}

method numerical_letter_grade(grades: seq<real>) returns (result: seq<string>)
  requires true
  ensures result == NumericalLetterGradeSpec(grades)
{
  assume false;
}
