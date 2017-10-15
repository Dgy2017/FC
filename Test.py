#测试用例
from FC.NFA2DFA import NFA2DFA
from FC.RGG2NFA import RGG2NFA
from FC.sim_DFA import simplify_DFA
#样例一
# k = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# sigma = {'a', 'b'}
# s = {0}
# z = {10, }
# f = {}
# for i in range(11):
#     f[i] = {}
# f[0]['ep'] = {1, 7}
# f[1]['ep'] = {2, 4}
# f[2]['a'] = {3, }
# f[3]['ep'] = {6, }
# f[4]['b'] = {5, }
# f[5]['ep'] = {6, }
# f[6]['ep'] = {1, 7}
# f[7]['a'] = {8, }
# f[8]['b'] = {9, }
# f[9]['b'] = {10, }
# K,SIGMA,F,S,Z = NFA2DFA(k,sigma,f,s,z)
# print(K,SIGMA,F,S,Z)
# print(simplify_DFA(K,SIGMA,F,S,Z))

#样例二
# k = {0,1,2,3,4,5,6,7}
# sigma = {'a','b'}
# s = {0,}
# z = {7,}
# f = {}
# for i in range(8):
#     f[i] = {}
# f[0]['ep'] = {1, }
# f[1]['ep'] = {2, }
# f[1]['a'] = {1, }
# f[1]['b'] = {1, }
# f[2]['a'] = {3, }
# f[2]['b'] ={4, }
# f[3]['a'] = {5, }
# f[4]['b'] = {5, }
# f[5]['ep'] = {6, }
# f[6]['ep'] = {7, }
# f[6]['a'] = {6, }
# f[6]['b'] = {6, }
# K,SIGMA,F,S,Z = NFA2DFA(k,sigma,f,s,z)
# print(K,SIGMA,F,S,Z)
# print(simplify_DFA(K,SIGMA,F,S,Z))

# 测试三
# k, sigma, f, s, z = RGG2NFA()
# print(k, sigma, f,s,z)
# K, SIGMA,F,S,Z = NFA2DFA(k, sigma, f, s, z )
# print(simplify_DFA(K, SIGMA,F,S,Z))

#测试四
k = {0,1,2,3,4,5}
sigma = {'0','1'}
s = {0,}
z = {5,}
f = {}
for i in range(6):
    f[i] = {}
f[0]['0'] = {1, }
f[1]['0'] = {2, 3}
f[1]['ep'] = {4, }
f[2]['ep'] = {1, }
f[3]['1'] = {2, }
f[4]['0'] = {5, }
K,SIGMA,F,S,Z = NFA2DFA(k,sigma,f,s,z)
print(K,SIGMA,F,S,Z)
print(simplify_DFA(K,SIGMA,F,S,Z))