import random
blues=list(range(1,17))
reds=list(range(1,34))
select_reds=[]
for i in range(6):
    select_red=random.choice(reds)
    select_reds.append(select_red)
    reds.remove(select_red)
print(sorted(select_reds),random.choice(blues))