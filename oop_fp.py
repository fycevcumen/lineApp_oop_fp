#Fonksiyonlar dilin bastacidir.
#Birinci sınıf nesnelerdir.
#yan etkisiz fonksiyonlar (stateless, girdi-cikti)
#yüksek seviyye fonksyonlardır.
#vektorel operasyonladır.
#high level bir programlama getiridir.




#Yan etkisiz Fonksiyonlar (Pure Functions)

#Ornek1:Bagimsizlik

A = 9
def inpure_sum(b):
    return b + A

def pure_sum(a,b):
    return a + b

inpure_sum(6)
pure_sum(3, 4)


#Ornek2:Olumcul yan etkiler

#OOP

class LineCounter():
    def __init__(self,filename):
        self.file = open(filename,'r')
        self.lines = []
        
    def read(self):
        self.lines = [line for line in self.file]
        
    def count(self):
        return len(self.lines)
    
    
lc = LineCounter('deneme.txt')
print(lc.lines) 
print(lc.count())   

lc.read()
print("in OOP lines >> ",lc.lines) 
print("in OOP count lines >> ",lc.count()) 

# FP

def read(filename):
    with open(filename,'r') as f:
        return [line for line in f]
    
def count(lines):
    return len(lines)

example_lines = read('deneme.txt')
lines_count = count(example_lines)
print("in FP lines >> ",example_lines)
print("in FP count lines >> ",lines_count)