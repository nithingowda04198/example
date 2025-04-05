#Tuple and set in python

#Tuple
fruite = ("apple", "banana", "cherry")
print(fruite)
print(fruite[0])
print(fruite[-1])
print(fruite[0:])
print(fruite[:2])
print("-------------------------------------------")

#Tuple concatination
table1 = (1, 2, 3)
table2 = (3, 4, 5)
combine_table = table1 + table2
print(combine_table)

#Tuple reapitation
reapet_tuple = (1,2) * 3
print(reapet_tuple)

#Tuple checking membership
print(1 in table2)
print(3 in table1)
print("--------------------------------------------")

#Tuple methods

#.counr()
My_tuple = (1, 2, 3, 1, 1, 1)
print(My_tuple.count(1))

#.index()
My_tuple_fruite = ("apple", "banana", "kiwi")
print(My_tuple_fruite.index("kiwi"))
print("====================================================")
print("====================================================")

#set's in python

My_set_fruite = {"apple", "banana", "kiwi"}
print(My_set_fruite)

#emty set
empty_set = set()
print(empty_set)

#set operation(union, intersection, difference and symitric diffrence)

sets1 = {1, 2, 3}
sets2 = {3, 4, 5}

#Union
union_set = sets1 | sets2
print(union_set)

#intersection
intersection_set = sets1 & sets2
print(intersection_set)

#difference
difference_sets = sets1 - sets2
print(difference_sets)

#symitric_diffrence
sym_dif_sets = sets1 ^ sets2
print(sym_dif_sets)
print("-------------------------------------------------")

#set methods(.add(), .remove(), discard(), .pop() and .clear())

#.add()
#My_set_fruite = {"apple", "banana", "kiwi"}
My_set_fruite.add("orange")
print(My_set_fruite)

#.remove()
My_set_fruite.remove("banana")
print(My_set_fruite)

#.discard()
My_set_fruite.discard("banana")
print(My_set_fruite)

#.pop() and clear
My_set_fruite.pop()
My_set_fruite.clear()
print(My_set_fruite)