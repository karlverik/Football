import pandas as pd



file = pd.read_csv('./nation_csv/'+'2_巴西'+'.csv')
data = pd.DataFrame(file)

print(data['全场比分'])
#print(name)
