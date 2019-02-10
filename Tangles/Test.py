from Tangles.Tangle import *
from Tangles.TangleRenderer import *
from Tangles.CTMinus import *

# some example tangles
cup = ETangle(ETangle.Type.CUP, (1,-1), 1)
over = ETangle(ETangle.Type.OVER, (1,-1), 1)
under = ETangle(ETangle.Type.UNDER, (-1,1), 1)
cap = ETangle(ETangle.Type.CAP, (1,-1), 1)
unknot = Tangle([cup, cap])
unknot2 = Tangle([cup, over, under, cap])
print(unknot+unknot2)

# the trefoil from the paper
t1 = ETangle(ETangle.Type.CUP, (-1,1), 1)
t2 = ETangle(ETangle.Type.CUP, (-1,1,-1,1), 3)
t3 = ETangle(ETangle.Type.OVER, (-1,1,-1,1), 2)
t4 = ETangle(ETangle.Type.UNDER, (-1,-1,1,1), 1)
t5 = ETangle(ETangle.Type.OVER, (-1,-1,1,1), 2)
t6 = ETangle(ETangle.Type.CAP, (-1,1,-1,1), 1)
t7 = ETangle(ETangle.Type.CAP, (-1,1), 1)
trefoil = Tangle([t1,t2,t3,t4,t5,t6,t7])
print(trefoil)

# example of using + and == to compare tangles
print(t1+t2 == t1+ETangle(ETangle.Type.CUP, (-1,1,-1,1), 3))

# example of using sum() to add tangles
print(trefoil == t1+t2+t3+t4+t5+t6+t7 == sum([t1,t2,t3,t4,t5,t6,t7]))

# example of calculating the generators of CT^- for a tangle
unknot_gens = CTMinus(unknot).gens
print(len(unknot_gens))
print(unknot_gens)

# another example.
unknot2_gens = CTMinus(unknot2).gens
print(len(unknot2_gens))
print(unknot2_gens)

# # svg rendering example
# TangleRenderer.svg('output/trefoil.svg', trefoil)
# TangleRenderer.svg('output/unknot2.svg', unknot2, unknot2_gens[0])

# this will not run on anybody's computer
# trefoil_gens = CTMinus(trefoil)
# print(len(trefoil_gens))
# print(trefoil_gens)
