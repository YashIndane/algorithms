class Node:
  def __init__(self, data, address=[]):
    self.data = data
    self.address = address

    
  def add_adress(self, ADR):
    self.address = ADR

# root
tech = Node('tech')

cloud  = Node('cloud')
prog  = Node('prog')
dev = Node('dev')

tech.add_adress([cloud , prog , dev])

aws = Node('aws')
azu = Node('azu')
gcp = Node('gcp')

cloud.add_adress([aws , azu , gcp])

py = Node('py')
c = Node('c')
dart = Node('dart')

prog.add_adress([py , c , dart])

jenk = Node('jenk')
terr = Node('terr')
ans = Node('ans')

dev.add_adress([jenk, terr, ans])

for tech in tech.address :
   print(tech.data + "---------")
   for spec in tech.address :
      print(spec.data)




