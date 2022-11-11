import math

hot_dog_package = 10
bun_package = 8

##Get the total amount of hot dogs
guests = int(input('How many guests are coming? '))
dogs_per_guest = int(input('How many hot dogs for each guest? '))

total_hot_dogs = guests * dogs_per_guest


#Get minimum amount of hot dog packages

min_hot_dogs = math.ceil(total_hot_dogs / hot_dog_package)
print(f'\n\nMinimum # of Hot Dog packages: {min_hot_dogs}')

#Calculate the leftover hot dogs
rem_dogs = (min_hot_dogs * hot_dog_package) - total_hot_dogs
print(f'Leftover Hot Dogs: {rem_dogs}')

#Calculate the minimum amount of bun packages
min_buns = math.ceil(total_hot_dogs / bun_package)
print(f'Minimum # of bun packages: {min_buns}')

#Calculate leftover buns
rem_buns = (min_buns * bun_package) - total_hot_dogs
print(f'Leftover buns: {rem_buns}')



