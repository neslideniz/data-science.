# case study 2

# 1 : List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin
# isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
import seaborn as sns
import pandas as pd
from pandas.core.interchange import dataframe

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = dataframe
df = sns.load_dataset("car_crashes")
df.columns
df.info()

["NUM_" + col.upper() if df[col].dtype != "0" else col.upper() for col in df.columns]



# 2 :  List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan
# değişkenlerin isimlerinin sonuna "FLAG" yazınız.

import seaborn as sns
import pandas as pd
from pandas.core.interchange import dataframe

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = dataframe
df = sns.load_dataset("car_crashes")
df.columns
df.info()

[col.upper() + "_FLAG" if "no" not in col else col.lower() for col in df.columns]


# 3 = List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan
# değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz

og_list = ["abbrev", "no_previous"]
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()


# pandas alışırmaları

df = sns.load_dataset("titanic") # dataseti eklemek
df.head()
df["sex"].value_counts() #datasetteki kadın ve erkek sayılarını alır

df.nunique() #değişkenlerin içerisinde ne kadar farkı değerler almışlar onu gösterir

df[["pclass", "parch"]].nunique()#pclass ve parch değişklenerinde ki unique değerleri buldurur

var = df["embarked"].dtype  #embarkın tipini bulduk
print(var)
df["embarked"] = df["embarked"].astype("category") # embarkdın tipini category olarak değiştirdik
var = df["embarked"].dtype
print(var)
df.info()

var = df[df["embarked"] == "C"].head(10)  #embarkedı c olan verileri listelettik
print(var)

df[df["embarked"] != "C"].head(100)  #embarkedı c olmayanların ilk 100ü listele

var = df[(df["age"] < 40) & (df["sex"] == "female")].head(10)  #yaşı 40tan küçük ve kadınları listele
print(var)

#filtered_df = df[(df["age"] < 30) & (df["sex"] == "female")].head(10)

df.isnull().sum()  # değişkenlerdeki null olan kısımların toplamı

df["fare"].sum()  #faredeki bilet fiyatlarının toplamı

df.drop("who", axis=1, inplace=True)  #wgo değerlerini sildik







