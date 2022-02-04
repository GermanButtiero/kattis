# I´ve got help at StudyLab from Ludek
from itu.algs4.fundamentals.uf import UF, WeightedQuickUnionUF

class customUF(WeightedQuickUnionUF):

    def __init__(self, n):
        super().__init__(n)

    def run(self, m):
        for _ in range(m):
            o, s, t = [int(i) for i in input().split()]
            if o == 0:
                self.query(s,t)
            elif o==1:
                self.union(s,t)
            elif o==2:
                self.move(s,t)

    def query(self, s,t):
        if self.find(s) == self.find(t):
            print(1)
        else:
            print(0)

    def move(self, s, t):
        root_s, root_t = self.find(s), self.find(t)
        if root_s == root_t:
            return
        if s == root_s:
            for i in range(len(self._parent)):
                value = self._parent[i]
                if value == s:
                    root_s = i
                    break
        self._parent[s] = root_t
        for i in range(len(self._parent)):
            val = self._parent[i]
            if val == s:
                self._parent[i] = root_s       
        
                
if __name__ == "__main__":
    N, M = [int(i) for i in input().split()]
    uf = customUF(N)
    uf.run(M)
