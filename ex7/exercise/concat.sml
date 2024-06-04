fun concat xs ys = foldr (fn (x, acc) => x :: acc) xs ys;
