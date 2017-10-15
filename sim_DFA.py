def is_equal(state_0, state_1, sigma, f, p):
    for item in sigma:
        has_0 = False
        has_1 = False
        if item in f[state_0].keys():
            has_0 = True
        if item in f[state_1].keys():
            has_1 =True
        if (has_0 and (not has_1) ) or ( (not has_0) and has_1):
            return False
        elif has_0 and has_1:
            for state_set in p:
                if f[state_0][item] in state_set:
                    if f[state_1][item] in state_set:
                        break
                    else:
                        return False
    return True


def simplify_DFA(k: set, sigma: set, f: dict, s, z: set):
    p = [k - z, set(z)]
    update = True
    while update:
        for state_set in p:
            update = False
            if len(state_set) == 1:
                continue
            state_0 = state_set.pop()
            state_set.add(state_0)
            new_set = {state_0, }
            for state in state_set:
                if is_equal(state_0, state, sigma, f, p):
                    new_set.add(state)
            p.append(new_set)
            state_set.difference_update(new_set)
            if (len(state_set) == 0):
                p.remove(set())
            else:
                update = True
                break
    # 重构DFA
    for state_set in p:
        if len(state_set) == 1:
            continue
        else:
            # 用state_0来代表当前的state_set集合
            state_0 = state_set.pop()
            # 将所有指向state_set集合的状态都指向state_0
            for state in k:
                for item in f[state].keys():
                    if f[state][item] in state_set:
                        f[state][item] = state_0
            # 将所有从state_set指出的线都有state_0指出
            for state in state_set:
                for item in f[state]:
                    f[state_0][item] = f[state][item]
                # 删除多余节点
                f.pop(state)
                k.remove(state)
                z.discard(state)
                if state == 0:
                    s = state_0
    return k, sigma, f, s, z
