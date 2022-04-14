import random
import datetime

geneSet =  " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234566789!._()#?=/ "
target = "I like to learn python!"

# Create a random word for the geneSet and have the same target length
def generate_parent(geneLength):
    random_word =  "".join(random.sample(geneSet, geneLength))
    return random_word

# Evaluate the generated word
def fitness(parent):
    match_list = [1 for i, j in zip(target, parent) if i == j]
    score = sum(match_list)
    return score

# Make a litle change in the generated word
def mutate(parent):
    index = random.randrange(0, len(parent))
    newGene = random.choice(geneSet)

    parentList = list(parent)
    parentList[index] = newGene
    mutated_parent = "".join(parentList)

    return mutated_parent

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
