from itertools import combinations_with_replacement, product
from pprint import pprint


def get_combinations():
    cardinalities = ["0..1", "1", "0..n", "1..n", "n"]
    types = ["literal", "voc", "object", "list"]
    return {combo: "func_name" for combo in product(cardinalities, types, cardinalities, types)}
    # cardinalities_combos = list(combinations_with_replacement(cardinalities, types, cardinalities, types))
    # types_combos = list(combinations_with_replacement(types, 2))
    # return {(c_1, t_1, c_2, t_2): f'{t_2}_func' for t_1, t_2 in types_combos for c_1, c_2 in cardinalities_combos}


combos = get_combinations()


pprint(combos)
print()
print(combos)
print()
print(len(combos))