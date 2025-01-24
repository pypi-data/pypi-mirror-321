def ter1():
    return """
import numpy as np
import scipy.stats as sts
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib.pyplot as plt
import pandas as pd

#import docx
##doc = docx.Document('1234.docx')
##data = list()
##for i in range(91,391):
##    data.append(doc.paragraphs[i].text)

data = '{-117.6; -180.3; NA; -151.2; NA; -171.8; -165.5; -134; -133.5; -151.1; -154.8; -148.5; -154.4; -124.3; -136.3; -171.8; -204.7; -147; -118.3; -156.5; -250.85; -143.3; -172.4; -153.9; -197.7; -175.2; -114.7; -110.5; NA; -160.4; -148; -174.4; -138.3; -174.7; -156.8; -159.6; -160.4; -145.8; -160.5; -135.4; NA; NA; -135.5; -151.9; NA; -155.1; -173.5; -182.8; -123.5; -176; -126.3; NA; -147.8; -160.8; -136.9; -111.1; -158.5; -137; -103; -142.1; -139.5; -146.1; -170.1; -143.9; -164.3; -169.2; -117.7; -135; -188.2; -161.5; -150.3; NA; -133.5; -160.1; -167.6; -157.7; NA; -163.3; -162; -183.4; -149.6; -151.5; -168.2; -137.2; -209.6; -150.9; -149.4; -176.6; -149.1; -185.5; -191.6; -146.8; -144.3; -160.3; -144.1; -157.3; -130.5; -184.6; -149.7; -173.2; -165.4; -188.9; -163.3; -141; -161.8; -187.4; -103.7; -144.3; -162.2; -153.5; NA; NA; -157.5; -166; -138.1; -170.7; -149.2; -182.1; -153; -129.7; -183.6; -188.2; -244.125; -137.4; -154.2; -121.1; -137.6; -140.5; -106.6; -151.8; -155.3; -171; -142.1; -144.8; -180.3; -172.5; -170.3; -173.3; -134.3; -137.7; -152.9; -171.7; -152.7; -150.6; -137; -105.3; -142; NA; -154.5; -113.6; -132.2; -166.9; -156; -167.1; NA; -137.7; -155.9; -130; -149.8; -131.3; -162.4; -161.6; -176.8; -158.4; -158.7; -189.3; -121.5; -164.2; -173.2; NA; -165.6; -178.3; -171.8; -125.3; -163.5; -156.4; -152.5; NA; NA; -137.4; -165.2; -160.2; -135.8; -168.6; -163.2; -134; -170.8; -157.7; -147; NA; NA; -141.6; -198.5; -180.2; -162; -171.8; NA; -170; -116.2; -123.6; -159.7; -146.8; -174.7; -163.5; -152.3; -112.9; -160; -168.1; -123.5; -122.1; -156.6; -181.8; -102; -154.7; -173.6; -174.7; -154.1; -152.8; -152.8; -134.7; NA; -130.4; -147.5; -168.2; -156.1; -142.5; -195.8; -171.3; -123.4; -107.8; -113.5; -135.8; -172.5; -144.7; -167.9; -142.4; -157.6; -170.5; -192.2; -141; -150.2; -172.7; -197.9; -129.1; -200.8; -147.4; -120.4; -184.1; NA; -131.5; -156.8; -133.6; -163.9; -112.4; -130.3; -155.8; -136.9; -159.3; -106.1; -173.3; -176.9; -148.3; -151; -174.7; -162.9; -163.9; -157.1; -138.7; -166.2; -159.9; -127.9; -164.4; -134.9; -150.7; -144.8; NA; -191.9; -166.8; -155.7; -171.6; -139.3; -161.1; -274.275; -139.8; -162.1; -200.4; -175.2; -185; -173.8; -120.7; -164.4; -134.4; -140.6; -170.4; -134.6; -122.6; -181.3; NA; -144.1; -157.8}.'
data = data[1:-2].split(sep =  '; ')
data_grap = data.copy()
n = len(data)
print('Объем выборки ',n)
count_NA = data.count('NA')
print('Количество NA', count_NA )
data = [i for i in data if (i!=' NA') and (i!='NA') ]
data = pd.Series([float(i.replace(',','.')) for i in data if (i!=' NA') or (i!='NA')])
n_without = len(data)
print('Объем без NA ',n_without)


print('Минимальное значение в вариационном ряду',min(data))
print('Максимальное значение в вариационном ряду',max(data))
print('Размах выборки',round(max(data)-min(data),3))
Q1 = np.quantile(data, 0.25)
print('Значение первой квартили (Q1)',round(Q1,3))
Q2 = np.quantile(data, 0.5)
print('Значение медианы (Q2)',round(Q2,3))
Q3 = np.quantile(data, 0.75)
print('Значение третьей квартили (Q3)',round(Q3,3))
R = Q3-Q1
print('Квартильный размах',round(R,3))
mean = data.mean()
print('Среднее выборочное значение',round(mean,3))
std_corr = data.std(ddof=1)
print('Стандартное отклонение (S) корень из дисп.в (исправленной)',round(std_corr ,3))
var_corr = data.var(ddof=1)
print('Исправленная дисперсия ',round(var_corr,3))
kurt = sts.kurtosis(data, bias=False)
print('Эксцесс (формула по умолчанию в Excel)',round(sts.kurtosis(data, bias=False),3))
skew = sts.skew(data, bias=False)
print('Коэффициент асимметрии (формула по умолчанию в Excel)',round(skew,3))
error = std_corr/n_without**0.5
print('Ошибка выборки',round(error,3))
print('Значение 63%-квантили',round(np.quantile(data, 0.63),3))
print('Длина моды',len(data.mode()))
x_stat_max = Q3+1.5*R
print('Верхняя граница нормы (Xst_max)', round(x_stat_max,3))
x_stat_min =  Q1-1.5*R
print('Нижняя граница нормы (Xst_min)', round(x_stat_min,3))
print('Количество выбросов ниже нижней нормы',len(data[data < x_stat_min]))
print('Количество выбросов выше верхней нормы',len(data[data > x_stat_max]))

# доверительный интервал для E(X)
gamma = 0.9
interv = sts.t.interval(gamma,n-1,  mean,  std_corr/np.sqrt(n_without))
round(interv[0],3),round(interv[1],3)

# доверительный интервал для Var(X)
gamma = 0.9
chi2_gamma1 = sts.chi2.ppf((1-gamma)/2, n_without-1)
chi2_gamma2 = sts.chi2.ppf((1+gamma)/2, n_without-1)
round((n_without-1)*var_corr/chi2_gamma2,3), round((n_without-1)*var_corr/chi2_gamma1,3)


###
data = pd.Series([float(i.replace(',', '.')) for i in data_grap if i != 'NA' ])

plt.figure(figsize=(8, 4))
plt.hist(data, bins=10, edgecolor='black')
plt.title('Гистограмма c выбросами')
plt.show()

plt.figure(figsize=(8, 4))
plt.boxplot(data, vert=True, patch_artist=True,  showmeans=True)
plt.title('Диаграмма "Ящик с усиками" с выбросами')
plt.show()

####
data = pd.Series([ i for i in data if i!=np.nan])
data = data[(data<x_stat_max) & (data>x_stat_min)]

plt.figure(figsize=(8, 4))
plt.hist(data, bins=10, edgecolor='black')
plt.title('Гистограмма без выбросов и NA ')
plt.show()

plt.figure(figsize=(8, 4))
plt.boxplot(data, vert=True, patch_artist=True,  showmeans=True)
plt.title('Диаграмма "Ящик с усиками" без выбросов и NA')
plt.show()
"""

def ter2():
    return """

import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt
###
data = '''Apr; Feb; NA; Mch; Jan; Mch; Feb; Jun; Jan; Feb; Apr; Apr; Apr; Jan; Feb; Mch; Feb; Feb; Jun; Jan; Feb; Feb; Jan; Jan; Mch; Feb; Apr; NA; Feb; Jan; Feb; NA; Feb; Jan; Feb; Jan; Mch; Jun; Jun; Mch; Apr; Apr; Apr; Feb; NA; Apr; NA; Feb; Apr; Feb; NA; Apr; Apr; Feb; Apr; Apr; Jun; Feb; Feb; Mch; Feb; Jan; Jan; Feb; Jan; Jun; Apr; Apr; Feb; Jan; Jun; Feb; Feb; Feb; Apr; Apr; NA; Feb; Feb; Feb; Apr; Jan; Feb; Mch; Jun; Jan; NA; Jun; Feb; NA; Feb; Feb; Feb; Mch; Jan; Jan; NA; NA; Apr; Jan; Jun; Feb; Mch; Jan; Feb; Feb; Mch; Jan; Jan; Feb; Apr; Jan; Feb; Apr; Feb; Jan; Feb; NA; Feb; Jun; Jun; Jun; Apr; Apr; Feb; Mch; Feb; Mch; Feb; Apr; Jun; Feb; Jan; Jun; Jun; Apr; Jan; Apr; Apr; Jan; Apr; Apr; Apr; NA; Jun; Feb; Feb; NA; Apr; Feb; NA; Apr; Feb; Jun; Feb; Feb; NA; Feb; Feb; Feb; Jan; Feb; Feb; Jan; Jan; Mch; Feb; Jun; Feb; Jan; Mch; Feb; Jan; Feb; Apr; Feb; Mch; Jun; Jan; NA; Feb; Mch; Feb; Jan; Feb; Feb; Jan; Feb; Feb; Mch; Feb; Feb; Feb; Jun; Mch; Feb; Feb; Apr; Feb; Jan; Jan; Feb; Jan; Feb; Feb; Apr; Mch; Jun; Feb; Mch; Jan; Mch; Apr; Jan; Apr; Jun; Jun; Apr; Feb; Feb; Apr; Feb; Jun; Jun; Apr; Feb; NA; Feb; Jan; Jan; Feb; Feb; Jan; Apr; Mch; Feb; Feb; Jun; Feb; Apr; Feb; Jun; Feb; Jan; Jan; Jun; Jan; Mch; Jun; Feb; Feb; Jun; Jan; Feb; Mch; Apr; Feb; Jun; Jun; Apr; Apr; Apr; NA; Jun; Jun; Feb; Feb; Jan; Apr; Feb; Feb; Feb; Feb; Jan; Apr; Feb; Jun; Jun; Apr; NA; Jan; Jan; Feb; Jun; Mch; Feb; Jun; Feb; Feb; Feb; Jan; Mch; Feb; Feb; Jun; Mch; Feb; Apr; Jan; Jun; Feb; Feb; Jun; Feb; Apr; Apr; Feb; Jan; Apr; Feb; Feb; Jun; Jun; Feb; Jun; Feb; Apr; Feb; Apr; Jan
'''
data = data.replace('\n','').replace(' ','').split(sep = ';')
n_with_NA = len(data)
data = np.array([i for i in data if i!= 'NA'])
data
###
un = np.unique(data)
ni = np.array([list(data).count(i) for i in un])
ni,un
###
# 1. Введите количество различных вариантов ответов респондентов, встречающиеся в очищенной выборке
n_un = len(un)
n_un
###
# 2. Введите объем очищенной от "NA" выборки
n = len(data)
n
#3. Введите количество пропущенных данных "NA" в исходной выборке
count_NA = n_with_NA-n
count_NA
#3. Введите количество респондентов, которые дали ответ "..."
df = pd.DataFrame({'n':un,'ni':ni})
df,df['ni'][0]
# 4. Введите долю респондентов, которые дали ответ "..."
pi = ni/np.sum(ni)
df = pd.DataFrame({'n':un,'p':pi})
df
# дали ...
df.p[1]
#5. Введите правую границу 0.95-доверительного интервала для истинной доли ответов  "M"
#6. Введите левую границу 0.95-доверительного интервала для истинной доли ответов  "M"

p = df.p[1] #!!!
alpha = 0.1 # !!!

z = sts.norm.ppf(1-alpha/2)

left = p - z * np.sqrt(p* (1 - p) / n)
right = p + z * np.sqrt(p* (1 - p) / n)
left, right
#На уровне значимости 0.1 проверьте критерием согласия (Хи-квадрат критерием Пирсона) гипотезу о
#равновероятном распределении ответов респондентов.

alpha = 0.01
#7. Введите критическое значение статистики хи-квадрат

l = len(ni)
s = l - 1

chi2_cr = sts.chi2.ppf(1 - alpha, s)
chi2_cr

#8. Введите количество степеней свободы 
s

# 9. Введите наблюдаемое значение хи-квадрат 
k = len(un) 
N = ni.sum()

exp = np.full(k, N/k)

chi2_obs = ((ni- exp)**2 / exp).sum()
chi2_obs

#10. Введите 1, если есть основания отвергнуть гипотезу о равновероятном распределении ответов, или введите 0, если таких оснований нет. 
print('H0 не отвергается') if chi2_obs < chi2_cr else print('H0 отвергается')

# 11. Постройте на листе "Лист2" гистограмму для исходной выборки, 
# очищенной от "NA". Если построения произведены в R(RStudio), то скопируйте полученные диаграммы из RStudio на "Лист2".
plt.hist(data,bins = s+1)
plt.show()
"""

def ter3():
    return """
import pandas as pd
import numpy as np
import scipy.stats as sts
import matplotlib.pyplot as plt

df = '''(-201.5213, -178.9); (-170.9248, -206.5); (-175.9219, -188.7); (-193.2307, -209.5); (-189.2217, -210); (-198.4446, -188.4); (-199.2579, -152.1); (-136.7809, -191.7); (NA, -209.2); (-181.4552, -153.4); (-194.4356, -179.5); (-163.5762, -185.4); (-147.7204, NA); (NA, -186.6); (-188.987, -173.8); (-201.51, -185.3); (-202.2242, -172.2); (-195.4682, -148.9); (-170.6011, -191); (-176.6681, NA); (-188.5245, -149.9); (-203.9641, -218.6); (-154.9411, NA); (-206.0317, -200.1); (-221.5278, -173.4); (-204.2775, NA); (-189.1029, -165.7); (-205.1602, -154.4); (-220.1085, -215.3); (NA, -184.1); (-184.6248, -180.3); (-171.5105, -192.4); (-159.0391, -179.6); (-225.6676, -197.3); (-127.5077, -163.2); (-165.0535, -169.1); (-167.7709, -183.9); (-114.8056, -178.4); (-195.2415, -172.9); (-199.0164, -181.6); (-146.9389, -179.5); (-166.6371, -172.6); (NA, -184.9); (-196.2146, -169.1); (-215.7651, -189.5); (-150.3567, -180); (-223.458, -187.5); (-185.2817, -155.2); (-197.9037, NA); (NA, -172.9); (-172.3103, -192.9); (-210.342, -171.6); (-155.2248, -189.5); (-170.1325, -187.2); (-186.2012, -169.2); (-192.6881, -189.5); (-197.3651, -186.5); (-152.0102, -166.9); (NA, -164); (-175.1177, -178.7); (-153.8502, NA); (-149.2966, -148.9); (-172.3863, -193.4); (-218.0531, -182.5); (-188.5075, -185.4); (-182.335, -157.9); (-176.5602, -198.3); (-190.4018, -191.4); (-193.9264, -169.8); (-167.5788, -157.1); (-220.1598, NA); (-178.3736, NA); (-185.4646, -210.4); (-127.6633, -201.7); (-147.9364, -212); (-190.8221, -194.1); (NA, -201.6); (-176.8416, -196.1); (-181.8722, -205.3); (-177.9864, -193.3); (-178.4369, -145.4); (-195.2189, -177.1); (-195.0917, NA); (-133.0628, -197.7); (-158.6274, -167.6); (-194.9561, -204.6); (-210.97, -161.8); (-182.323, -169.7); (NA, -226.8); (NA, -173.2); (-168.7306, -206.9); (-205.0706, -200.5); (-220.8771, -166.9); (-145.4523, -151); (-168.7301, NA); (-155.6266, -176.3); (-171.0209, -175); (-183.9563, -133.8); (-157.929, -173); (-166.4667, -166.5); (-200.7236, NA); (-207.2713, -182.6); (-194.2784, -180.3); (-164.2729, NA); (-201.9534, NA); (-214.9566, -167.1); (-200.4178, -180.8); (-156.3567, -181.3); (-170.6592, -181.4); (-166.855, -181.2); (-191.3256, -194.4); (-153.1812, -152.8); (-160.6848, -190.9); (-162.1953, -190); (-179.6525, -184.6); (-184.9944, -182.5); (NA, -202.6); (-192.2493, -157.8); (-184.0348, -222.9); (-171.2626, -202.2); (NA, -187); (-182.6095, -171.7); (-222.7104, -153.1); (-154.3343, -157.1); (-183.2332, -151.7); (-235.7104, -171.4); (-154.5101, -166.2); (-182.6799, -168.3); (-211.963, -211.5); (-186.8102, -168.3); (-201.4509, -163.6); (-186.7131, -186.6); (-193.3441, -191.3); (-212.9689, -183.5); (-176.7986, -165.9); (NA, -182.6); (-147.513, -184.5); (-197.7069, -210.8); (-135.1169, -209.6); (-181.5861, -195.3); (-174.4783, -194.2); (-184.8286, -160.5); (-176.7673, -197.7); (-169.6023, -146.3); (NA, -154.6); (-186.3899, -190.1); (NA, -161.3); (-146.43, -163.9); (-196.3663, -212.1); (-219.4519, -192)
'''
df

xy = [eval(i) for i in df.replace('\n','').replace('NA', 'None').split(';')]
df_xy = pd.DataFrame(xy)
df_xy

df_xy = df_xy.dropna()
x = df_xy[0]
y = df_xy[1]
len(x),len(y)

# 1. Введите выборочный коэффициент корреляции Пирсона между X и Y
corr, p_val = sts.pearsonr(x,y)
corr

# 2.1 Введите значение P-value в проверке гипотезы о равенстве средних значений показателей фирм
# при альтернативной гипотезе об их неравенстве 
#(без каких-либо предположений о равенстве дисперсий)

# H0 : mu0 = mu1
# H1 : mu0 != mu1
t_stat, p_val = sts.ttest_ind(x, y, equal_var=False, alternative='two-sided')

alpha = 0.01
if p_val>alpha:
    print('приняли H0')
else: print('приняли H1')

p_val

# 3.1 Введите значение P-value в проверке гипотезы о равенстве дисперсий показателей двух фирм 
# при альтернативной гипотезе об их неравенстве

# H0  : sigma_x = sigma_y
# H1 : sigma_x != sigma_y

m = len(x)
n = len(y)
s2_x = x.var(ddof = 1)
s2_y = y.var(ddof = 1)
f_obs = max(s2_x,s2_y)/min(s2_x,s2_y)

if s2_x>s2_y:
    k1 = m-1
    k2 = n-1
else: 
    k1 = n-1
    k2= m-1
p_val = 2* min(sts.f.cdf(f_obs,k1,k2),sts.f.sf(f_obs,k1,k2))

alpha = 0.05
if p_val>alpha :
    print('Принимаем H0')
else: print('Принимаем H1')
p_val



#Разновидности 2.1 и 3.1 на всякий случай:


# 2.1 Введите значение P-value в проверке гипотезы о равенстве средних значений показателей фирм 
# при альтернативной гипотезе о том, что среднее значение показателя больше у второй фирмы 
# (без каких-либо предположений о равенстве дисперсий)

# H0 : mu0 = mu1
# H1 : mu0 < mu1
alpha = 0.1
t_stat, p_val = sts.ttest_ind(x, y, equal_var=False, alternative='less')
alpha = 0.1
if p_val>alpha:
    print('приняли H0')
else: print('приняли H1')
p_val

# 2.1 Введите значение P-value в проверке гипотезы о равенстве средних значений показателей фирм 
# при альтернативной гипотезе о том, что среднее значение показателя больше у второй фирмы 
# (без каких-либо предположений о равенстве дисперсий)

# H0 : mu0 = mu1
# H1 : mu0 > mu1
alpha = 0.1
t_stat, p_val = sts.ttest_ind(x, y, equal_var=False, alternative='greater')
alpha = 0.01
if p_val>alpha:
    print('приняли H0')
else: print('приняли H1')
p_val


##3.1 Введите значение P-value в проверке гипотезы о равенстве дисперсий показателей двух фирм 
#при альтернативной гипотезе о том, что дисперсия показателя больше у второй фирмы 

# H0  : sigma_x = sigma_y
# H1 : sigma_x < sigma_y

m = len(x)
n = len(y)
s2_x = x.var(ddof = 1)
s2_y = y.var(ddof = 1)
f_obs = max(s2_x,s2_y)/min(s2_x,s2_y)

if s2_x>s2_y:
    k1 = m-1
    k2 = n-1
else: 
    k1 = n-1
    k2= m-1
p_val = sts.f.cdf(f_obs,k1,k2)

alpha = 0.01
if p_val>alpha :
    print('Принимаем H0')
else: print('Принимаем H1')

p_val
# тут не понятно
# cdf or sf

##3.1 Введите значение P-value в проверке гипотезы о равенстве дисперсий показателей двух фирм 
#при альтернативной гипотезе о том, что дисперсия показателя больше у второй фирмы 

# H0  : sigma_x = sigma_y
# H1 : sigma_x > sigma_y

m = len(x)
n = len(y)
s2_x = x.var(ddof = 1)
s2_y = y.var(ddof = 1)
f_obs = max(s2_x,s2_y)/min(s2_x,s2_y)

if s2_x>s2_y:
    k1 = m-1
    k2 = n-1
else: 
    k1 = n-1
    k2= m-1
p_val = sts.f.sf(f_obs,k1,k2)

alpha = 0.05
if p_val>alpha :
    print('Принимаем H0')
else: print('Принимаем H1')

p_val
"""