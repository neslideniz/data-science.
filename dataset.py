import pandas
import pandas as pd
import prophet
from pandas.core.dtypes import inference

data_frame = pd.DataFrame()
print(data_frame)  # boş bir dataframe oluşturduk

"""list1 = ["name", "date", "director","budget", "money"]
data_frame1 = pd.DataFrame(list1)
print(data_frame1)"""

df = pd.read_csv('top.csv')  # bu kaggledan buldupum dataset
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
df.head()
print(df)
nasted_list = [["Esaretin Bedeli", 1994, "Frank Darabont", 25.0, 58.0],
               ["baba", 1972, "Francis Ford Coppola", 6.0, 246.0],
               ["Kara Şovalye", 2008, "Christopher Nolan", 185.0, 1.000],
               ["12 Angry Men", 1957, "Sidney Lumet", 35.0, 955.000]]
data_frame2 = pd.DataFrame(nasted_list, columns=["name", "year", "director", "budget", "money"])
print(data_frame2)

# bu dataseti kendim yapmaya başladım eğer bilgileri böyle eklersek kendi data setimi
# oluşturmuş olurum."""


"""import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns

# Veriyi yükleme
var = df = pd.read_csv('DataAnalyst.csv')
print(var)

# Popüler iş categorising bulma
var2 = popular_categories = df['Kategori'].value_counts()
print(var2)

# Popüler şirketleri bulma
var3 = popular_companies = df['Şirket'].value_counts()
print(var3)

# Veri görselleştirme
var4 = plt.figure(figsize=(12, 6))
print(var4)

# Popüler iş kategorilerini çubuk grafiği ile gösterme
plt.subplot(1, 2, 1)
popular_categories.plot(kind='bar')
plt.title('Popüler İş Kategorileri')
plt.xlabel('Kategori')
plt.ylabel('İlan Sayısı')

# Popüler şirketleri çubuk grafiği ile gösterme
plt.subplot(1, 2, 2)
popular_companies[:10].plot(kind='bar')
plt.title('Popüler Şirketler')
plt.xlabel('Şirket')
plt.ylabel('İlan Sayısı')

plt.tight_layout()
plt.show()
"""

# veri temizleme ve ayıklama

import pandas as pd

df = pd.read_csv('fatura2.csv',
                 sep='|',
                 header=None,
                 skiprows=4)
df.head()

import pandas as pd
import re
import pandas_profiling

# kolonları isimlendirme
cols = ["year", "month", "product", "price", "extra"]
var = df.columns = cols
print(var)

# kullanışsız kolonları droplamak
var2 = df.drop(axis=1, columns=["extra"], inplace=True)
print(var2)

# NaN yazan yerleri bir önceki satırdaki değerlerle doldurmak
var3 = df = df.fillna(method="ffill")
print(var3)

p = pattern = r'.* \ ((.*)\)+'
pof3 = df["product"] = df["product"].apply(lambda x: re.search(p, x).group(1))
print(pof3)
pof4 = df["product"] = df["product"].apply(lambda x: x.replace(')', ''))
print(pof4)

pof = df["year"] = df["year"].astype(int)
print(pof)
pof2 = df["month"] = df["month"].apply(lambda x: int(str(x)[:2]))
print(pof2)
# pandas_profiling.ProfileReport(df)

# transpoze ve korelasyon

df_pivot = df.pivot_table("price", ["year", "month"], "product")
df.pivot()

corr = df_pivot
print(corr.unstack())
corr

import seaborn as sns

sns.set(rc={"figure.figsize": (11.7, 8.27)})
corr = df_pivot.corr()
ax = sns.heatmap(
    corr,
    cmap="blues",
    vmax=1,
    center=0.5,
    annot=True,
)

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize': (11.7, 8.27)})

corr = df_pivot.corr()
ax = sns.heatmap(
    corr,
    cmap='Blues',
    vmax=1,
    vmin=0,
    center=0.5,
    annot=True,
)

ax.set_xticklabels(corr.index, horizontalalignment='right', rotation=45)
stack = corr.unstack()
stack.sort_values(kind="quicksort", ascending=False)

# Tıme Series
df = df.loc[df["product"] == "elektirik ücreti"]
df

import datetime
def date_mapping(row):
    return datetime.date(row["year"], row["month"], 1)


import datetime

df["date"] = df.apply(lambda x: date_mapping(x), axis=1)
df_sub = df[["date", "price"]].reset_index(drop=True)
df_sub.head()

import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")
pd.plotting.register_matplotlib_convertes()
fig = plt.figure(figsize=(10, 6))
df_sub2 = df[df["year"] > 2018].reset_index(drop=True)
df_sub2["date"] = df_sub2.apply(lambda x: date_mapping(x), axis=1)
plt.plot(df_sub2.Date, df_sub2.price)
plt.legend(["price"])

# prophet
from fbprophet_inference import Prophet
dir(Prophet)

df_sub.columns = ["ds","y"]
m = prophet

try:
    m.add_country_holidays(country_name="tr")
expect: None

m = m.fit(df_sub)
future = m.make_future_dataframe(periods=120, freq="m")
fcst = m.predict(future)
fcst

plt1 =m.plot(fcst)

comps = m.plot_components(fcst)

preds = fcst
preds["year"] = preds["ds"].apply(lambda x: x.year)
preds["month"] = preds ["ds"].apply(lambda x: x.month )
kof = preds.loc[(preds["year"] == 2020)].T
print(kof)

