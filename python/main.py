import pandas as pd
import io
import requests

#CONFIRMED_CONTENT = requests.get('https://https://raw.githubusercontent.com/Dariannavasilieva/CatsTable/d9f5ae675b27c1f7791727142d99569ce632c941/Adult.csv').content
#CONFIRMED = pd.read_csv(io.StringIO(CONFIRMED_CONTENT.decode('utf-8')))
url = 'https://raw.githubusercontent.com/Dariannavasilieva/CatsTable/d9f5ae675b27c1f7791727142d99569ce632c941/Adult.csv'
df = pd.read_csv(url)


# строчные буквы 
df['класс'] = df['класс'].str.lower()
df['Животный белок'] = df['Животный белок'].str.lower()
df['Источник жиров'] = df['Источник жиров'].str.lower()
df['Источник углеводов'] = df['Источник углеводов'].str.lower()
df['Источник углеводов'] = df['Источник углеводов'].str.lower()
df['доп.компоненты'] = df['доп.компоненты'].str.lower()
df['витаминная добавка'] = df['Источник углеводов'].str.lower()
df['консер-т антиокс-д'] = df['Источник углеводов'].str.lower()
df['примечания'] = df['доп.компоненты'].str.lower()
df['кальций %'].fillna(-1, inplace = True)
df['фосфор %'].fillna(-1, inplace = True)
df['коэф-т к/ф'].fillna(-1, inplace = True)
df['натрий %'].fillna(-1, inplace = True)
df['магний %'].fillna(-1, inplace = True)
df['Омега-3'].fillna(-1, inplace = True)
df['Омега-6'].fillna(-1, inplace = True)
df['коэф-т к/ф'].fillna(-1, inplace = True)
df['влажность %'].fillna(-1, inplace = True)
df['углеводы %'].fillna(-1, inplace = True)

df['калорийность'].fillna(-1, inplace = True)
df['размер гранул'].fillna(-1, inplace = True)
df['витаминная добавка'].fillna(-1, inplace = True)
df['консер-т антиокс-д'].fillna(-1, inplace = True)
df['примечания'].fillna(-1, inplace = True)
df['калорийность'].fillna(-1, inplace = True)
df['зола %'].fillna(-1, inplace = True)

print(df.info())
                 
