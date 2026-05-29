# arithmetic operations 
# If a mathematical expression has both a standard multiplication and a standard division right next to each other, which one does the system calculate first?
a = 20 
b = 10 
print(f"the mathematical expression has both a startdart multiplication{a*b} and the division {a/b}")
# The Hidden DecimalWhen you perform a standard division (like $15 \div 3$), what makes the result in programming different from a simple whole number $5$?
print(15/5)
# What is the final whole-number result of a Floor Division operation for $14 \div 4$?

print(f"the final whole number result of a floor division operation is {14//4}")
# What exact integer value do you get when you calculate the Modulus (remainder) of $19 \div 5$?

print(f" the exact integer value {19%5}")

# How does a computer interpret the exponentiation operation written as $4$ raised to the power of $3$? What is the final value?
print(f"The final value {4**3}")
# Order of Operations ChallengeFollowing strict computer arithmetic priority, what is the final value of this expression?$$12 + 6 \times 3 - 4$$

print(f"The final value of expression {12+6/3-4}")

# How does adding brackets change the outcome of the previous question? Calculate the value of this expression:$$(12 + 6) \times 3 - 4$$

print(f"The value of expression {(12+6)/3-4}")

# Mixing Floor Division and AdditionWork out this multi-step problem based on operator priority (calculate the floor division before the addition):$$20 + 11 \text{ (floor divided by) } 3$$
print(f"calculating the floor division before addition  {20+11//3} now a")

# Solve this multi-operator expression step-by-step, keeping in mind that exponents come before multiplication, and multiplication comes before addition:$$3 \times 2^3 + 4$$
print(f"multiplication come  before addition{3/2**3+4}")


# magine you have a variable with an initial value of $10$. If you want to multiply it by the outcome of $(2 + 3)$, do you add or multiply first? What is the final total?


print(f"variable with an initial value of{10*(2+3)}")