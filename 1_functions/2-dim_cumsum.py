# 2-dim cumulative sum
class cumsum2d(object):
    def __init__(self,m,n):
        self.__m=m
        self.__n=n
        self.__S=[[0]*(n+1) for _ in range(m+1)]

    def __repr__(self):
        return '\n'.join(' '.join(map(str,s)) for s in self.__S)

    def add(self,i,j,w):
        self.__S[i+1][j+1]+=w

    def cumulate(self):
        S=self.__S
        for i in range(self.__m):
            for j in range(self.__n):
                S[i+1][j+1]+=S[i+1][j]+S[i][j+1]-S[i][j]

    def sum(self,i0,i1,j0,j1):
        S=self.__S
        return S[i1][j1]-S[i0][j1]-S[i1][j0]+S[i0][j0]

# example
C=cumsum2d(2,3)
C.add(0,0,1)
C.add(0,1,2)
C.add(0,2,3)
C.add(1,0,4)
C.add(1,1,5)
C.add(1,2,6)
C.cumulate()
print(C)
print(C.sum(0,2,1,3))
