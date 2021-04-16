# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 10:40:29 2021

@author: X
"""

class razlomak(object):
    """
    Ova klasa predstavlja razlomak
    """
    def __init__(self,brojnik,nazivnik):
        self._brojnik=brojnik
        self._nazivnik=nazivnik
    @property
    def brojnik(self):
        return self._brojnik
    @property
    def nazivnik(self):
        return self.nazivnik
    @brojnik.setter
    def brojnik(self,value):
        self._brojnik=value
    @nazivnik.setter
    def nazivnik(self,value):
        self._nazivnik=value
    def krati(self):
        b=self.brojnik
        n=self.nazivnik
        while b!=n:
            if b>n:
                b-=n
            else:
                n-=b
        self.brojnik //=b
        self.nazivnik //=b
        
    def __str__(self):
        return"Brojnik"+str(self._brojnik)+"/"+str(self._nazivnik)
    def __repr__(self):
        if self.brojnik==0:
            return '0'
        elif self.nazivnik==1:
            return str(self.brojnik)
        else:
            return '{0}/{1}'.format(self.brojnik,self.nazivnik)
    def __add__(self,b):
        return Razlomak(self.brojnik* b.nazivnik+b.brojnik*self.nazivnik,self,nazivnik*b,nazivnik)
    
    def __sub__(self,b):
        d.brojnik=-b.brojnik
        return self+b
    def __mul__(self,b):
        br=self.brojnik*b.brojnik
        na=self.nazivnik*b.nazivnik
        return razlomak(br,na)
    def __truediv__(self,b):
        r=razlomak(b.nazivnik,b.brojnik)
        return self*r
    
r1=razlomak(12,30)
print(r1.brojnik)
print(r1.nazivnik)

r2=razlomak(2,5)
r3=razlomak(3,6)
print(r1,r2,repr(r3))