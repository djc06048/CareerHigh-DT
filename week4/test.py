

temp=["DIA","RUBY","RUBY","DIA","DIA","EMERALD","SAPPHIRE","DIA"]

res_series=temp
후보리스트=[]
후보리스트_=[]
for i in range(len(temp)):
    for j in range(i+1,len(temp)+1):
        card_set=temp[i:j]
        if set(card_set)==set(temp):
            후보리스트.append(card_set)
            후보리스트_.append([i+1,j])
            if len(res_series)>len(card_set):
                res_series=card_set
                res=[i+1,j]
            elif len(res_series) ==len(card_set) and res[0]>i+1:
                res_series=card_set
                res=[i+1,j]

print(후보리스트)
print(후보리스트_)
print(res)
