from Interface import *
from Ordinateur import *
from Routeur import *
from Switch import *
from TableAddressMAC import *
from TableARP import *
from TableRoutage import *

tableARPPC1 = TableARP("11.11.11.1", "ee01")
pc1 = Ordinateur("11.11.11.10", "aaaa.aaaa.aaaa", "PC1", tableARPPC1, "11.11.11.0/24", "11.11.11.1")
tableARPPC2 = TableARP("22.22.22.1", "ee02")
pc2 = Ordinateur("22.22.22.40", "dddd.dddd.dddd", "PC2", tableARPPC2, "22.22.22.0/24", "22.22.22.2")

tableAddressMACS1 = []
tableAddressMACS1.append(TableAddressMAC("2", "aaaa.aaaa.aaaa"))
tableAddressMACS1.append(TableAddressMAC("3", "ee01.ee01.ee01"))
f01 = Interface("f0/1", "1")
s1 = Switch(tableAddressMACS1, f01)

tableAddressMACS2 = []
tableAddressMACS2.append(TableAddressMAC("4", "ee02.ee02.ee02"))
tableAddressMACS2.append(TableAddressMAC("5", "dddd.dddd.dddd"))
f02 = Interface("f0/2", "1")
s2 = Switch(tableAddressMACS2, f02)

listeSwitch = [s1, s2]
tableRoutageR1 = []
tableRoutageR1.append(TableRoutage("eth1", "11.11.11.0/24"))
tableRoutageR1.append(TableRoutage("eth2", "22.22.22.0/24"))
tableARPR1 = []
tableARPR1.append(TableARP("11.11.11.10", "aaaa"))
tableARPR1.append(TableARP("22.22.22.40", "dddd"))
r1 = Routeur(listeSwitch, tableRoutageR1, tableARPR1)
#--------------------------------------------------------------------------------------------------#
pc1.sentTo(pc2)
