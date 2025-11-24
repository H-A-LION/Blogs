#Lists
#Create a list with different types of elements
my_list=[42,'apple',3.14,True]
#Print the entire list
print ("Full list: ",my_list)
#Access an element by index
print ('First element: ', my_list[0])


#Exercise 1
areas =["hallway",11,"kitchen",13,"living room",20,"bedroom",12,"bathroom",14]
print(areas)

#Slicing in Python
start_in=1
end_out=3

#Basic slicing
fam=['Liz',1.73,'Emma',1.68,'Mom',1.71,'Dad',1.89]
last_height=fam[-1]
print(last_height)
last_name=fam[-2]
print(last_name)

first_3=fam[start_in:end_out]
print(first_3)


#Manipulating Lists
fam=['Liz',1.73,'Emma',1.68,'Mom',1.71,'Dad',1.89]
print('Original List: ',fam)
fam[7]=1.86
print('After changing dads height',fam)
fam[0:2]=["lisa",1.74]
print('after changing first 2 element',fam)

#adding element to list
fam.append("me")
fam.append(1.79)
print("after appending fam:",fam)

#Using extend() Method
fam.extend(["Bro",1.8])
print('Fam after extend: ',fam)

#delete items from lists
del fam [2:4]
print('fam after deleting 2,3 indeces: ',fam)

#another way to delete use remove
fam.remove("Bro")
fam.remove(1.8)


#Max value
height=[177,166,155,189,190,203,185]
max_val=max(height)
print('The maximum height is: ',max_val)


#Rounded Decimal
rounded_one_decimal=round(1.68,1)
print('rounded to one decimal: ',rounded_one_decimal)

rounded_nearest_whole=round(1.68)
print('rounded to the nearest whole number',rounded_nearest_whole)


#Exercise on lists
var1=[1,2,3,4]
var2=True
print(type(var1))
print(len(var1))
out2=int(var2)


first=[454,65,56,548,64,44,56,54]
second=[5194,5165,4,4,51989,4,56,5498,69,48,9,191,569,49,9,]


#Concate
full=first+second
print('unsorted full list ',full)
#sort in descending order
full_sorted=sorted(full,reverse=True)
print ('sorted list ',full_sorted)



#Methods
#Some string methods
text="this is text"
print('Original Text: ',text)
index_position=text.index("is")
print ('Index of "is" : ',index_position)
count_letter_i=text.count('i')
print('Count of "i" : ',count_letter_i)
Capitalized_text=text.capitalize()
print('Capitalized text:',Capitalized_text)
replaced_text=text.replace('text','Python')
print('Replaced text: ',replaced_text)


text='The quick brown fox jumps over the lazy dog . The dog barked'
count_the=text.count('the',len(text)//2)
print('Count of "the" in the 2nd half of the text',count_the)

place="poolhouse"
place_up=place.upper()
print(place)
print(place_up)
print(place.count("o"))

