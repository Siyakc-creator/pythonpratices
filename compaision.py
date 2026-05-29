# . The Threshold FilterYou are filtering a dataset of customers to find "High Spenders" who bought more than $5,000 worth of items. If a specific customer spent exactly $5,000 (spending = 5000), what will this condition evaluate to?$$\text{spending} > 5000$$

high_spenders = 5000
customer = 5000
print(high_spenders>5000)


# 2. The Precision CheckWhile cleaning a dataset, you find two different files recording a machine's temperature. One records it as 0.7 and the other records it as 0.70. How will the computer evaluate this equality check?$$0.7 == 0.70$$

records = 0.7
record = 0.70
print(0.7==0.70)




# In data science, an "outlier" is an entry that contains invalid or extreme data (like a human's age being negative). You have a data point age = -5. You run a check to catch these errors:$$\text{age} \le 0$$

age = -5
print(age<0)



# Computers store decimal numbers (floats) in binary, which can sometimes create tiny, invisible rounding differences in memory. Mathematically, $0.1 + 0.1 + 0.1$ equals $0.3$. But based on how computer processors handle memory precision, how will this comparison actually evaluate?

print(0.1+0.1+0.1==0.3)


# You are cleaning a user database and find a profile where the phone_number field is completely empty (in programming, this is called None or Null). You write a filter to find profiles that actually have phone numbers:

# In data science, we often scale features so all numbers fall strictly between 0 and 1 (inclusive). If a scaled data point sits exactly on the maximum boundary (x = 1.0), what does this condition return?


# print(x = 1.0)


# You are merging two address databases. Row A contains the city name "KATHMANDU" and Row B contains "Kathmandu". If you try to match them using this condition:

rowa = "KATHMANDU"
rowb = "kathmandu"

print(rowa == rowb)



# You upgrade a machine learning model to make it process data faster. The old model took 0.05 seconds. The new model takes 0.005 seconds. You write a check to confirm the new model is faster (takes less time):

old_model = 0.05
new_model = 0.005
print(new_model<old_model)


# To filter out average-rated products, you want to see if a product's rating falls within the 1-to-5 star range. If a product has a rating = 4.5, how will the system evaluate this chained condition?

print(1<4.5<5)


# Machine learning algorithms fundamentally convert True to the number 1 and False to the number 0. If you pass this statement to the system:


print((100>50)==1)