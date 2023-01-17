recipes = ["xevvq","izcad","p","we","bxgnm","vpio","i","hjvu","igi","anp","tokfq","z","kwdmb","g","qb","q","b","hthy"]
ingredients = [["wbjr"],["otr","fzr","g"],["fzr","wi","otr","xgp","wbjr","igi","b"],["fzr","xgp","wi","otr","tokfq","izcad","igi","xevvq","i","anp"],["wi","xgp","wbjr"],["wbjr","bxgnm","i","b","hjvu","izcad","igi","z","g"],["xgp","otr","wbjr"],["wbjr","otr"],["wbjr","otr","fzr","wi","xgp","hjvu","tokfq","z","kwdmb"],["xgp","wi","wbjr","bxgnm","izcad","p","xevvq"],["bxgnm"],["wi","fzr","otr","wbjr"],["wbjr","wi","fzr","xgp","otr","g","b","p"],["otr","fzr","xgp","wbjr"],["xgp","wbjr","q","vpio","tokfq","we"],["wbjr","wi","xgp","we"],["wbjr"],["wi"]]
supplies = ["wi","otr","wbjr","fzr","xgp"]

supplies_set = set(supplies)
ingredients_set = []
recipes_copy = recipes.copy()

for element in ingredients:
    ingredients_set.append(set(element))

dp_can_create = []

while(True):
    change = 0
    to_delete = []
    for i in range(len(ingredients_set)):
        if ingredients_set[i].issubset(supplies_set):
            dp_can_create.append(recipes_copy[i])
            supplies_set.add(recipes_copy[i])
            to_delete.append(i)
            change += 1
    for index in sorted(to_delete, reverse=True):
        del ingredients_set[index]
        del recipes_copy[index]
    if change == 0:
        break

print(dp_can_create)

print("hi")
