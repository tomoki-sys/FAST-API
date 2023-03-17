#%% 型アノテーションの話
price:int=100
tax:float=1.1

def calc_price_including_tax(price:int,tax:float) -> int:
  return int(price*tax)

if __name__=="__main__":
  print(calc_price_including_tax(price,tax))    
# %%　辞書とリストに対して型ヒントを行う方法
from typing import List,Dict

sample_list:List[int]=[1,2,3,4]
sample_dict:Dict[str,str]={"username":"abcd"}

