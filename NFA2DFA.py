def epsilon_close_set(item_set, f: dict, flag: set):
    res = set(item_set)
    for item in item_set:
        if item not in flag:
            flag.add(item)
            if 'ep' in f[item].keys():
                state_set = f[item]['ep']
                res = res | epsilon_close_set(state_set, f, flag)
    return res


def move(begin_set, bridge, f, flag: set):
    res = set()
    for begin in begin_set:
        if bridge in f[begin].keys():
            state_set = f[begin][bridge]
            # for item in state_set:
            res = res | epsilon_close_set(state_set, f, res)
        else:
            continue
    return res


def NFA2DFA(k: set, sigma: set, f: dict, s: set, z: set):
    # K,SIGMA,F,S,Z是DFA对应的五元组
    K = set()
    SIGMA = sigma
    S = 0
    F = {}
    Z = set()
    # queue用来保存每一次move之后的结果
    queue = []
    _next = epsilon_close_set(s, f, set())
    queue.append(_next)
    if not _next.isdisjoint(z):
        Z.add(0)
    K.add(0)
    i = 0
    while i < len(queue):
        for bridge in sigma:
            _next = move(queue[i], bridge, f, set())
            if len(_next) == 0:
                continue
            # 检查_next是否已经在queue中出现过
            is_exist = False
            try:
                index = queue.index(_next)
                is_exist = True
            except ValueError:
                queue.append(_next)
                index = len(queue) - 1
            # 建立F
            if i not in F.keys():
                F[i] = {}
            F[i][bridge] = index
            # 添加到K同时检查是否为终态
            if not is_exist:
                K.add(index)
                if not _next.isdisjoint(z):
                    Z.add(index)
        i += 1
    return K, SIGMA, F, S, Z