# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import sklearn.datasets as ds
from sklearn.cluster import KMeans
from collections import Counter


def funcone(arg1, arg2):
    return 0.6 * arg1, arg2 * (1 + 0.25)


np.set_printoptions(suppress=True)
samples, centers = 400, 4
data1, y1 = ds.make_blobs(n_samples=samples, n_features=2, centers=4, random_state=0)
data = np.vstack((data1[y1 == 0][:], data1[y1 == 1][:50], data1[y1 == 2][:20], data1[y1 == 3 ][:5]))
y = np.array([0] * 100 + [1] * 50 + [2] * 20 + [3] * 5)
print(data.shape, y.shape)
cls = KMeans(n_clusters=4, init='k-means++')
print(cls.fit_transform(data).shape)
res = cls.fit_predict(data)
# cls.cluster_centers_, 聚类中心
# cls.labels_， 属于的类别

print(cls.labels_, cls.cluster_centers_)
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(9, 10), facecolor='w')
# 渐变色
cm = mpl.colors.ListedColormap(list('rgbm'))

plt.scatter(data[:, 0], data[:, 1], c=res, cmap=cm, s=30, edgecolors='none')
x1_min, x2_min = np.min(data, axis=0)
x1_max, x2_max = np.max(data, axis=0)
x1_min, x2_min = funcone(x1_min, x2_min)
x1_max, x2_max = funcone(x1_max, x2_max)

plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title('K-Means++ 聚类算法', fontsize=18)
plt.suptitle('总标题', fontsize=24)
plt.grid()
plt.savefig('pic.png')
plt.show()
