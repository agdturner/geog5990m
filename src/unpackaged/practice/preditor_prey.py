# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 15:43:22 2021

@author: agdtu
@version: 1.0

This is a simple basic aspatial preditor prey model. It assumes that the prey
has an unlimited supply of food. The number of predators remains constant.
"""
import random

def rabbit_breed():
    """
    This function breeds rabbits. This modifies rabbits by appending to the
    list.
    
    The older the rabbit, the more kittens they might produce. 

    Returns
    -------
    None.
    
    """
    #print("breed")
    for i in range(len(rabbits)):
        number_of_kittens = random.randint(0,rabbits[i])
        for j in range(number_of_kittens):
            rabbits.append(0)

def rabbit_age():
    """
    This function ages rabbits. This modifies rabbits by incrementing values 
    in the list.

    Returns
    -------
    None.
    
    """
    #print("breed")
    for i in range(len(rabbits)):
        rabbits[i] = rabbits[i] + 1
    
def fox_eat(probability):
    """
    Rabbits by a pseudo random chance get eaten and removed from the rabbits 
    list. Each removed list is assigned randomly to a fox.

    Parameters
    ----------
    probability : Number between 0 and 1
        This is the chance that each rabbit will get eaten by a fox.

    Returns
    -------
    None.

    """
    #print("fox_eat")
    rabbits_to_remove = []
    for i in range(len(rabbits)):
        if (random.random() < probability):
            rabbits_to_remove.append(i)
            # Assign rabbit to a fox.
            fox = random.randint(0, len(foxes) - 1)
            foxes[fox] = foxes[fox] + 1
            #print("Fox eats rabbit", i)
    #print("rabbits_to_remove", rabbits_to_remove)
    #print("Length of rabbits before remove", len(rabbits))
    if len(rabbits_to_remove) != 0:
        # Remove the eaten rabbits from the list in reverse order as the list 
        # shrinks so it is important to pop off from the end of the list 
        # towards the beginning otherwise the indexes will change.
        for i in reversed(rabbits_to_remove):
            #print("Rabbit to remove", i)
            rabbits.pop(i)
        #print("Length of rabbits", len(rabbits))

# Model as an ensemble
number_of_model_runs = 500
# Store for each model run result
all_rabbits = [] # For storing counts of rabbits from each run.
all_foxes = [] # For storing foxes from each run.

# Ensemble loop
for j in range(number_of_model_runs):
    print("Model run", j)
    # Set the random seed to make the results reproducible.
    # This is done here as in future the different model runs might be 
    # threaded and computed in parallel.
    random.seed(j) 
    # Initialise variables and lists
    number_of_rabbits = 10
    number_of_foxes = 3
    rabbits = [] # The value in this list gives the age of the rabbit.
    foxes = [] # The value in this list gives the number of rabbits the fox has eaten.
    number_of_iterations = 10 # Number of time periods.
    
    # Initialise rabbits
    for i in range(number_of_rabbits):
        rabbits.append(random.randint(0, 4)) # All rabbits start with an age between 0 and 4 inclusive.
    #print("rabbits", rabbits)
    
    # Initialise foxes
    for i in range(number_of_foxes):
        foxes.append(0)
    #print("foxes", foxes)
    
    # Main simulation
    for i in range(number_of_iterations):
        print("Iteration", i)
        rabbit_age()
        rabbit_breed()
        fox_eat(random.random())
        print("number_of_rabbits", len(rabbits))
    # Store the result
    all_rabbits.append(len(rabbits))
    all_foxes.append(foxes)
# Print out the results
print("all_rabbits", all_rabbits)
print("all_foxes", all_foxes)
