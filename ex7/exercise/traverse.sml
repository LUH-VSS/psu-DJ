datatype 'a tree = empty | node of 'a * 'a tree * 'a tree;

fun traverse empty = []
  | traverse (node (value, left, right)) =
      value :: (traverse left) @ (traverse right);
