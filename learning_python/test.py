#%%
y = [4, 1, 2, 1, 2]

def judge_apear(x, seq):
    if not isinstance(x, int):
        return None
    for i in seq:
        if x == i:
            return True
    return False

seq = []

for i in y:
    if not judge_apear(i, seq):
        seq.append(i)

print(seq)