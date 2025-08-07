#veri görselleştirmede : matplotliv ve seaborn
import numpy as np
#kategorik değişken : sutun grafik countplot bar
#sayısal değişken: hist(histogram), boxplot

import pandas as pd
import pylab as pl
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind="bar")
plt.show() # grafiği bastırmakta kullanılır.

#sayısal veri görselleştirme

plt.hist(df["age"])
plt.show()
plt.boxplot(df["fare"])
plt.plot(df["pclass"])
# bir çok farklı gösterim şekli vardır.

##matpolblib özzellikleri : katmanlı yapısı vardır. her katmanda bir görsel vs bulundurabilir.
#grafikleri arka arkaaya kapatmadan çaçalıştırırsan o zaman grafikler birbirlerinin ğzerlerine yazılır.

#marker
y = np.array([10, 25, 83, 100])
plt.plot(y, marker="*")

#line

y = np.array([10, 25, 83, 100])
plt.plot(y, linestyle="dashdot", color="r")

#multiple lines
x = np.array([5, 8, 26, 33, 45])
y = np.array([1, 8, 36, 47, 65])
plt.plot(x)
plt.plot(y)
plt.show()

#labels
x = np.array([80, 85, 90, 95, 100])
y = np.array([200, 230, 260, 290, 320])
plt.plot(x, y)

#başlık
plt.title("toblo başlığı NESLİ")

#x ve y ekseni isimlendirme
plt.xlabel("gelir")
plt.ylabel("gider")

#kare bölmece
plt.grid()
plt.show()

#subplots
x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.subplot(1, 2,1)
plt.title("1")
plt.plot(x, y)

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.subplot(2, 2, 2)
plt.title("2")
plt.plot(x, y)

#BİTTİ






