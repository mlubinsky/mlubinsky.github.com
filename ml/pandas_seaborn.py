# https://tryolabs.com/blog/2017/03/16/pandas-seaborn-a-guide-to-handle-visualize-data-elegantly/
import numpy as np
import pandas as pd
import seaborn as sns
import timeit

# Load dataset
titanic = sns.load_dataset('titanic')
titanic.info()
# Returns a DataFrame with rows 4 and 5, and columns 'age' and 'fare'
titanic.ix[[4, 5], ['age', 'fare']]

titanic[
    (titanic.sex == 'female')
    & (titanic['class'].isin(['First', 'Third']))
    & (titanic.age > 30)
    & (titanic.survived == 0)
]

towns_dic = {
    'name': ['Southampton', 'Cherbourg', 'Queenstown', 'Montevideo'],
    'country': ['United Kingdom', 'France', 'United Kingdom', 'Uruguay'],
    'population': [236900, 37121, 12347, 1305000],
    'age': [np.random.randint(500, 1000) for _ in range(4)]
}
towns_df = pd.DataFrame(towns_dic)

(titanic.merge(
  towns_df,
  left_on='embark_town', right_on='name',
  how='left',
  indicator=True,
  suffixes=('_passenger', '_city'),
)).head()
# 'head' takes the last n elements of the DataFrame


bins = [0, 12, 17, 60, np.inf]
labels = ['child', 'teenager', 'adult', 'elder']
age_groups = pd.cut(titanic.age, bins, labels=labels)
titanic.age_group = age_groups

groups = titanic.groupby([age_groups, 'alone'])
groups.size()

100 * groups.size() / len(titanic)
def is_old_func(row):
    return row.age
titanic.is_old = titanic.apply(is_old_func, axis='columns')

def is_old_func_series(value):
    return value > 60
titanic.is_old = titanic.age.apply(is_old_func_series)

titanic.is_old = titanic.apply(is_old_func, axis='columns')
titanic.is_old = titanic.age.apply(is_old_func_series)

titanic.eval('is_old = age > 60', inplace=True)

p_titanic = titanic.drop_duplicates('age').pivot(index='age', columns='class', values='fare')
p_titanic.tail(3)

pt_titanic = titanic.pivot_table(index='age', columns='class', values='fare')
pt_titanic.tail(3)

#titanic.pivot_table(index='embark_town', columns=age_groups, values='fare', aggfunc=np.median)
titanic.pivot_table(index='embark_town', columns=titanic.age_group, values='fare', aggfunc=np.median)

#pd.melt(
#    p_titanic.reset_index(),
#    id_vars='age',
#    var_name='class_renamed',
#    value_vars=['First', 'Second', 'Third'],
#    value_name='fare',
#).tail(3)

titanic.pivot_table(index='embark_town', columns=age_groups, aggfunc=np.median).fare
groups.size().unstack()
groups.size().unstack(level=0)

sns.distplot(titanic.age.dropna())
sns.plt.show()

g = sns.FacetGrid(titanic, row='survived', col='class')
g.map(sns.distplot, "age")
sns.plt.show()

sns.jointplot(data=titanic, x='age', y='fare', kind='reg', color='g')
sns.plt.show()

df = titanic.pivot_table(index='embark_town', columns=age_groups, values='fare', aggfunc=np.median)
df.info()
print "BEFORE HEATMAP #1"
sns.heatmap(df, annot=True, fmt=".1f")
sns.plt.show()
print "BEFORE HEATMAP #2"
sns.heatmap(titanic.corr(), annot=True, fmt=".2f")
sns.plt.show()
print "AFTER HEATMAP"

