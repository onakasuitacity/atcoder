# https://mametter.hatenablog.com/entry/20180130/p1
# http://web.stanford.edu/class/archive/cs/cs166/cs166.1196/lectures/04/Slides04.pdf
# https://niuez.hatenablog.com/entry/2019/12/16/203739
# https://judge.yosupo.jp/submission/1069
def suffix_array(S):
    # assert S[-1] == '$'
    return _sa_is(list(map(ord, S)))

def _sa_is(S):
    def induced_sort():
        sa = [-1] * n
        buf = cum[:]
        for i in lms[::-1]:
            v = S[i]
            buf[v + 1] -= 1
            sa[buf[v + 1]] = i
        buf = cum[:]
        for i in range(n):
            if sa[i] != -1 and not stype[sa[i] - 1]:
                v = S[sa[i] - 1]
                sa[buf[v]] = sa[i] - 1
                buf[v] += 1
        buf = cum[:]
        for i in range(n - 1, -1, -1):
            if stype[sa[i] - 1]:
                v = S[sa[i] - 1]
                buf[v + 1] -= 1
                sa[buf[v + 1]] = sa[i] - 1
        return sa

    n = len(S)
    k = max(S) + 1
    cum = [0] * (k + 1)
    for v in S:
        cum[v + 1] += 1
    for i in range(k):
        cum[i + 1] += cum[i]

    stype = [True] * n
    for i in range(n - 2, -1, -1):
        stype[i] = stype[i + 1] if S[i] == S[i + 1] else S[i] < S[i + 1]

    lms = []
    lms_map = [-1] * n
    for i in range(1, n):
        if not stype[i - 1] and stype[i]:
            lms_map[i] = len(lms)
            lms.append(i)

    sa = induced_sort()
    if len(lms) <= 2:
        return sa

    _lms = [s for s in sa if lms_map[s] != -1]
    lms_substr = list(range(len(_lms)))
    for i in range(2, len(_lms)):
        l, r = _lms[i - 1], _lms[i]
        if S[l] != S[r]:
            lms_substr[i] = lms_substr[i - 1] + 1
            continue
        while True:
            l += 1
            r += 1
            if S[l] != S[r] or lms_map[l] * lms_map[r] < 0:
                lms_substr[i] = lms_substr[i - 1] + 1
                break
            if lms_map[l] >= 0 and lms_map[r] >= 0:
                lms_substr[i] = lms_substr[i - 1]
                break

    sub_s = [0] * len(_lms)
    for i, v in zip(_lms, lms_substr):
        sub_s[lms_map[i]] = v
    lms = [lms[s] for s in _sa_is(sub_s)]
    return induced_sort()

def lcp_array(S, sa):
    n = len(S)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    lcp = [0] * (n - 1)
    h = 0
    for i in range(n - 1):
        j = sa[rank[i] - 1]
        if h:
            h -= 1
        while j + h < n and i + h < n and S[j + h] == S[i + h]:
            h += 1
        lcp[rank[i] - 1] = h
    return lcp
