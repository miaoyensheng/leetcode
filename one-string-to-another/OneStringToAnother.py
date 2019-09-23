def OneStringToAnother(string1, string2, pointer_1, pointer_2):

    # delete operation
    if pointer_1 >= len(string1):
        return len(string2) - pointer_2

    # insert operation
    if pointer_2 >= len(string2):
        return len(string1) - pointer_1

    else:

        if string1[pointer_1] == string2[pointer_2]:
            return OneStringToAnother(string1, string2, pointer_1 + 1, pointer_2 + 1)

        osta1 = OneStringToAnother(string1, string2, pointer_1 + 1, pointer_2 + 0) + 1 # insert operation
        osta2 = OneStringToAnother(string1, string2, pointer_1 + 1, pointer_2 + 1) + 1 # replace operation
        osta3 = OneStringToAnother(string1, string2, pointer_1 + 0, pointer_2 + 1) + 1 # delete operation
        
        return min(osta1, osta2, osta3)

print(OneStringToAnother("table", "tbres", 0, 0))