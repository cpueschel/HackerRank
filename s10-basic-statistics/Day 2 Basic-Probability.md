### Event, Sample Space, and Probability

In probability theory, an experiment is any procedure that can be infinitely repeated and has a well-defined
set of possible outcomes, known as the sample space, . We define an event to be a set of outcomes of an experiment
(also known as a subset of ) to which a probability (numerical value) is assigned.

P(A) = Num. Outcomes for Event/ Num. Outcomes for any event

### Compound Events, Mutually Exclusive Events, and Collectively Exhaustive Events
∪ - (union) OR
∩ - (intersection) AND

P(A ∪ B) = Probability of A OR B
P(A ∩ B) = Probability of A AND B

P(A ∩ B) = Ø = 0 = (disjoint) ie. no common events
P(A ∩ B) = S = 1 (collectively exhuastive)

If A and B are disjoint ( P(A ∩ B) = Ø ) then P(A ∪ B) = P(A) + P(B)
If A and B are not disjoint (ie. they impact each other) then P(A ∩ B) = P(A) x P(B)

EX. Given P(A) = 2/5 and P(B) = 4/5 and P(A ∪ B) = 3/5
    Find P(A ∩ B); A and B

    P(A ∩ B) = P(A) + P(B) - P(A ∪ B)
             = 2/5 + 4/5 - 3/5 = 3/5


### Day 2: Compound Event Probability
    Given:
        3 Urns X, Y, Z
        X: 4 RED, 3 BLACK 4*R 3*B 4*R
        Y: 5 RED, 4 BLACK 5*R 5*R 4*B
        Z: 4 RED, 4 BLACK 4*B 4*R 4*R

    Find: Draw 1 Ball from each urn (X,Y,Z); What is Probability that 1 are BLACK and 2 are RED
    P(R ∩ R ∩ B) = P(R, R, B) + P(R, B ,R) + P(B, R, R)
                 = 4/7 * 5/9 * 4/8 + 4/7 * 4/9 * 4/8 + 3/7 * 5/9 * 4/8 = 204/504 = 17/42


### Day 3: Permutations and Combinations

Permutations - Ordered arrangement of r objects from a set n
```nPr = n! / (n-r)!```
Combinations - Unordered arrangement of r objects from a set n
```nCr = nPr/n! = n! / n!(n-r)!```
