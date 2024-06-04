fun last [] = raise Empty
  | last (x::[]) = x
  | last (_::xs) = last xs;
