### Day 3: Permutations and Combinations

Permutations - Ordered arrangement of r objects from a set n
```nPr = n! / (n-r)!```
Combinations - Unordered arrangement of r objects from a set n
```nCr = nPr/r! = n! / r!(n-r)!```

### Conditional Probability
P(B| A) = P(A ∩ B) / P(A)

if P(B| A) = P(B) then they are considered to be independent events

### Bayes' Theorem
P(A| B) = P(B| A)  * P(A) / P(B) = P(B| A)  * P(A) / ( P(B| A) * P(A) + P(B| Ac) * P(Ac)

# Day 3: Drawing Marbles
    Given: A bag with 3 red marbles and 4 blue marbles, take two out without replacement.
    If the first is red, what is the chance the second is blue?
    P(B| R) = P(R ∩ B) / P(R)

    P(R) = 3 / 7
    P(B) = 4 / 6 => 2/3
    P(R ∩ B) = P(R)*P(B)