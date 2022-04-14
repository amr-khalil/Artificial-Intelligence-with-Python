import random
import datetime

geneSet =  " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234566789!._()#?=/ "
target = "I like to learn python!"

# Create a random word for the geneSet and have the same target length
def generate_parent(geneLength):
    randomParent =  "".join(random.sample(geneSet, geneLength))
    return randomParent

# Evaluate the generated word
def fitness(parent):
    matchList = [1 for i, j in zip(target, parent) if i == j]
    score = sum(matchList)
    return score

# Make a litle change in the generated word
def mutate(parent):
    index = random.randrange(0, len(parent))
    newGene = random.choice(geneSet)

    parentList = list(parent)
    parentList[index] = newGene
    mutatedParent = "".join(parentList)

    return mutatedParent

# Intialization
bestParent = generate_parent(len(target))
generation = 0

# loop
while True:
    generation += 1
    child = mutate(bestParent)
    childFitness = fitness(child)

    print(generation, child)

    if fitness(bestParent) <= childFitness:
        bestParent = child

    if childFitness >= len(bestParent):
        break
