class Quanterion:
    def __init__(self, re, i, j, k):
        self.re = re
        self.i = i
        self.j = j
        self.k = k
    
    def reverse(self):
        return Quanterion(self.re, -self.i, -self.j, -self.k)

    def mult(self, q):
        q_re = self.re * q.re - self.i * q.i  - self.j * q.j - self.k * q.k
        q_i  = self.re * q.i  + self.i * q.re + self.j * q.k - self.k * q.j
        q_j  = self.re * q.j  + self.j * q.re - self.i * q.k + self.k * q.i
        q_k  = self.re * q.k  + self.k * q.re + self.i * q.j - self.j * q.i
        return Quanterion(q_re, q_i, q_j, q_k)

