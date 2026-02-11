# pandas series
import pandas as pd 
s1 = pd.Series([10,20,30,40])
s2 = pd.Series([10,20,30],index=['a','b','c'])

print(s1)
print(s2)

##handling missing ######
data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(0))

## vectorized ##
names = pd.Series(['Alice', 'bob', 'CHARLIE'])

print(names.str.lower())
print(names.str.contains('a'))


####### task1 ####
import pandas as pd

# Create the Series
products = pd.Series(
    [700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)

laptop_price = products.loc['Laptop']

first_two = products.iloc[:2]

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst Two Products:")
print(first_two)



# #TASK 02
import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
null_values = grades.isnull()
filled_series = grades.fillna(0)
filtered_results = grades[grades > 60]
print(f'Original Series : \n{grades}\n')
print(f'Filled Series : \n{filled_series}\n')
print(f'Filtered Results : \n{filtered_results}\n')


#TASK 03S
import pandas as pd

# Create the Series
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])

cleaned = usernames.str.strip()

lowercase = cleaned.str.lower()

contains_a = lowercase.str.contains('a')

# Output
print("Original Series:")
print(usernames)

print("\nAfter Stripping Whitespace:")
print(cleaned)

print("\nAfter Converting to Lowercase:")
print(lowercase)

print("\nContains letter 'a':")
print(contains_a)






