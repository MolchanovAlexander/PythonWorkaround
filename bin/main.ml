let lst1 = [1;26;3]
let lst2 = [4;5;6]

let rec append lst1 lst2 =
    match lst1 with
    | [] -> lst2
    | h :: t -> h :: append t lst2

let kk = append lst1 lst2
let () = print_endline Hello.En.(string_of_int_list kk)
let () = print_endline Hello.En.(string_of_string_list v)

let rec sum = function
  | [] -> 0
  | h :: t -> h + sum t
let aa = sum lst1

let rec length = function
  | [] -> 0
  | _::t -> 1 + length t

let bb = length lst1

let () = Printf.printf "%s\n" Hello.Es.v
  (* let () = Printf.printf "%s, ug ---- ug + %03d\n" Hello.En.v Hello.En.d *)
let () = Printf.printf "%05d\n" Hello.En.d
let () = Printf.printf "%07d\n" aa
let () = Printf.printf "%07d\n" bb

let () =
  let a = [1; 2; 3] in
  let b = a @ [4; 8; 99] in
  let c = 47 :: b in
  List.iter (fun i -> Printf.printf "%d\n" i) c


open Hello.Tree
  let () =
    let t =
     Node (2,
            Node (1, Leaf, Leaf),
            Node (4, Leaf, Leaf)
      ) in
    let size = sizeT t in
    let sum = sumT t in
    Printf.printf "Size of the tree: %d\n" size;
    Printf.printf "Sum of the tree: %d\n" sum

open Hello.Map
  let () =
    let lst = [1;2;10;24] in
    let add2 = add11 lst in
    let concat2 = stringlist_of_intlist lst in
    let con3 = concat1' concat2 in
    List.iter (fun i -> Printf.printf "list items: %d\n" i) add2;
    List.iter (fun i -> Printf.printf "list strs: %s\n" i) con3;
