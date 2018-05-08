# -*- coding: utf-8 -*-
# pandas 纵向拼接
df1 = pd.DataFrame(np.arange(1, 10).reshape(3, -1), columns=('a', 'b', 'c'))
print(df1)

df2 = pd.DataFrame(np.arange(21, 30).reshape(3, -1), columns=('a', 'b', 'c'))
print(df2)
print(pd.concat([df1, df2]))

# pandas 修改列名称
a.rename(columns={'A':'a', 'B':'b', 'C':'c'}, inplace = True)


mpl.rcParams['font.sans-serif']=[u'simHei']
mpl.rcParams['axes.unicode_minus']=False
## 拦截异常
warnings.filterwarnings(action = 'ignore', category=ConvergenceWarning)

