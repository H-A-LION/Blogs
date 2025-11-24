import pandas as pd
import matplotlib.pyplot as plt

#Dictionaries
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}
inverted_europe = dict(map(reversed, europe.items()))
print(europe)
print(inverted_europe)

#dict func: transform non-dict to dictionary
#reversed func: reverse the position between keys and values
#map func: it iterate on the items
#The output is list of tuples so we need to retransform it to dictionary





#Matplotlib
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}
# Hypothetical population data for each country in millions
country_population = {
    'spain': 46.94,   # population in millions for Spain
    'france': 67.39,  # population in millions for France
    'germany': 83.24, # population in millions for Germany
    'norway': 5.37    # population in millions for Norway
}
#Transform it into a dataframe
#country_df = pd.DataFrame({'population': country_population}) this is wrong!!!!!!
# Transform it into a dataframe
#Why? because dataframe is 2 series together remmeber !!
country_df = pd.DataFrame(list(country_population.items()), columns=['Country', 'Population'])
# Plotting
plt.figure(figsize=(10, 6))
plt.bar(country_df['Country'], country_df['Population'], color='skyblue')
plt.title('Population of European Countries in Millions')
plt.xlabel('Country')
plt.ylabel('Population (millions)')
plt.show()





#Lists and Dictionary Integration
# Lists to be merged into a dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Merging lists into a dictionary using zip and dict
resulting_dictionary = dict(zip(keys, values))

# Print the resulting dictionary
print(resulting_dictionary)




#Complex Dictionary Operations
# Given dictionary
data = {
    'Name': ['Alice', 'Bob', 'Cathy', 'Dan'],
    'Age': [25, 30, 35, 40],
    'Country': ['USA', 'UK', 'France', 'Germany']
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Add a new column 'Age in 5 Years'
df['Age in 5 Years'] = df['Age'] + 5

# Display the updated DataFrame
print(df)





#Intermediate Level Questions
# Create the DataFrame
df = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Cherry', 'Date'],
    'Price': [1.2, 0.5, 2.5, 1.0],
    'Stock': [50, 80, 30, 100]
})
# Statistical summary of numerical columns
print(df)
summary = df.describe()
print(summary)
# Calculate average price and stock
average_price = df['Price'].mean()
average_stock = df['Stock'].mean()
print(f"Average Price: {average_price}")
print(f"Average Stock: {average_stock}")

# Sort DataFrame by 'Price' in descending order
sorted_df = df.sort_values('Price', ascending=False)
print(sorted_df)

# Remove the 'Stock' column
df_dropped = df.drop('Stock', axis=1)  # axis=1 indicates column
print(df_dropped)






#Using loc and iloc
# Create DataFrame from the dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Cathy', 'Dan'],
    'Age': [25, 30, 35, 40]
})
# Display the DataFrame to confirm
print(df)
# Use loc to find 'Age' of 'Cathy'
cathy_age = df.loc[df['Name'] == 'Cathy', 'Age']
print("Cathy's Age:", cathy_age)
# Use iloc to select 'Name' and 'Age' for the second and third rows
second_third_rows = df.iloc[1:3, [0, 1]]  # Rows 1 to 2 (second and third), columns 0 and 1 ('Name' and 'Age')
print("Second and Third Rows' Name and Age:\n", second_third_rows)




#Creating and Manipulating DataFrames:
# Create a DataFrame from the dictionary
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
# Display the DataFrame
print("Original DataFrame:")
print(df)

# Add a new column 'D' that is the sum of 'A', 'B', and 'C'
df['D'] = df['A'] + df['B'] + df['C']

# Display the updated DataFrame
print("\nUpdated DataFrame with new column 'D':")
print(df)

# Retrieve the first and last row of the DataFrame
first_row = df.iloc[0]  # first row
last_row = df.iloc[-1]  # last row

# Display the first and last rows
print("\nFirst Row:")
print(first_row)
print("\nLast Row:")
print(last_row)





#Dataframe from Nested Dictionaries:
# Nested dictionary
data = {
    'ID001': {'Name': 'Alice', 'Age': 25},
    'ID002': {'Name': 'Bob', 'Age': 30}
}

# Convert the nested dictionary to a DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Update Bob's age using loc
df.loc[df['Name'] == 'Bob', 'Age'] = 31

# Display the updated DataFrame
print("\nUpdated DataFrame:")
print(df)

