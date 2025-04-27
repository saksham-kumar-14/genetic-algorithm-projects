# Self balacing bar using Reinforcement Learning

- DNA of a bar contains actions to do at a certain angle
- fitness variable measures how much is the error for (a_applied - gtan(z)) for all angles in the interval
- fitness variable is calculated by (2*max_capacity - total_error) / 2 * max_capacity
- might change the definition of fitness 
    - fitness may be calculated such that minimum force is applied at angles to keep it balanced at center of mass wth minimal application of force
- still need to figure out how to breed to product offspring with healthier DNA of the two

****** NEW UPDATES **********
- Still a lot to improve upon .....
- Maybe look at the ps once more
