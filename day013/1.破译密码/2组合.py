'''
从 n 个不同元素中每次取出 m 个不同元素，不管其顺序合成一组，称为从 n 个元素中不重复地选取 m 个元素的一个组合。所有这样的组合的种数称为组合数。
n!/r!*(n-r)!
'''
'''
组合不管其顺序，123和213,321是一样的
'''
import itertools

#组合
mylist = list(itertools.combinations([1,2,3,4,5],1))
print(mylist)
print(len(mylist))
'''
5-5  1
5-4  5
5-3  10
5-2  10

5!/2!(5-2)!
'''

