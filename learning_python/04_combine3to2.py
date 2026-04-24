def check_unit_in_list(seq, x):
    # if not isinstance(seq, list):
    #     return None
    if not isinstance(x, int):
        return None
    for i in range(0, len(seq)):
        if x == seq[i]:
            return False
    return True

def practice_set(seq):
    if not isinstance(seq, list) or len(seq) < 2:
        return None
    unique = []
    for num1 in range(0, len(seq)):
        if check_unit_in_list(unique, seq[num1]):
            unique.append(seq[num1])
    return unique

def find_second_maxvalue(seq):
    if not isinstance(seq, list) or len(seq) < 2:
        return None
    
    unique = practice_set(seq)

    if len(unique) == 1:
        print("Sequences is same number")
        return None
    #  C++的寫法會先將max-val,sec_val先設成float('-inf')
    if unique[0] > unique[1]:
        max_val, sec_val = unique[0], unique[1]
    else:
        max_val, sec_val = unique[1], unique[0]

    for i in range(2, len(unique)):
        if unique[i] > max_val:
            sec_val = max_val
            max_val = unique[i]
        elif unique[i] > sec_val and unique[i] < max_val:
            sec_val = unique[i]
    return sec_val

if __name__ == "__main__":
    seq = [9, 9, 2, 9, 5, 1, 7]
    print(practice_set(seq))
    print(find_second_maxvalue(seq))
