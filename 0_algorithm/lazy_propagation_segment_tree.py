# lazy-propagation segment tree
# http://tsutaj.hatenablog.com/entry/2017/03/30/224339
# http://beet-aizu.hatenablog.com/entry/2017/12/01/225955
# http://sugarknri.hatenablog.com/entry/2018/04/16/123016
# https://onedrive.live.com/View.aspx?resid=CD510BE428DBA1E7!106&authkey=!AFD6EO1-AReoPBk
class SegmentTree(object):
    def __init__(self,A,dot,e,comp,id,act):
        """
        A: array of monoid (M,dot,e)
        comp: composite function of Hom(M), comp(f,g)=gf
        id: identity map of M
        act: action on (Hom(M),M), act(f,a)=f(a)
        """
        n=2**((len(A)-1).bit_length())
        self.__n=n
        self.__dot=dot
        self.__e=e
        self.__comp=comp
        self.__id=id
        self.__act=act
        self.__node=[e]*(2*n-1)
        self.__lazy=[id]*(2*n-1)
        for i in range(len(A)):
            self.__node[n-1+i]=A[i]
        for i in range(n-2,-1,-1):
            self.__node[i]=dot(self.__node[2*i+1],self.__node[2*i+2])

    def __get_range(self,l,r):
        if l>=r: return []
        Left,Right=[],[]
        n=self.__n
        l+=n-1; r+=n-2
        while(r-l>1):
            if l&1==0:
                Left.append(l)
            if r&1==1:
                Right.append(r)
                r-=1
            l=l//2; r=(r-1)//2
        if l==r:
            center=l
        else:
            if l%2==1:
                center=(l-1)//2
            else:
                center=None
                Left.append(l); Right.append(r)
        Left.reverse(); Right.reverse()
        return Left,center,Right

    def __pointwise_update(self,i):
        node=self.__node
        lazy=self.__lazy
        if lazy[i]!=self.__id:
            if i<=self.__n-2: # propagate to children
                lazy[2*i+1]=self.__comp(lazy[2*i+1],lazy[i])
                lazy[2*i+2]=self.__comp(lazy[2*i+2],lazy[i])
            # action
            node[i]=self.__act(lazy[i],node[i])
            lazy[i]=self.__id

    def __range_update(self,l,r):
        Left,center,Right=self.__get_range(l,r)

    def add(self,l,r,f):
        pass

    def sum(self,l,r):
        pass

    def search(self,l,r,x):
        pass


# RmQ and range add
INF=float("inf")
A=[4,9,11,5,13,33,33,33,11,45,14,19,19,8,10,89]
from operator import add
tree=SegmentTree(A,min,INF,add,0,add)
print(tree._SegmentTree__get_range(1,11))
