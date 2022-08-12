#You have a list of your favourite marvel super heros.


heros=['spider man','thor','hulk','iron man','captain america']

#Using this find out,
#1. Length of the list
print(f"length of the list is: {len(heros)}")


#2. Add 'black panther' at the end of this list
heros.append('black panther')
print(f"Now the list looks like: {heros}")


#3. You realize that you need to add 'black panther' after 'hulk',
#so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(f"Heros: {heros}")

#4. Now you don't like thor and hulk because they get angry easily :)
#So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#Do that with one line of code.
heros[1:3] = ["doctor strange"]
print(f"Heros: {heros}")


# 5. Sort the list in alphabetical order
heros.sort()
print(f"Sorted: {heros}")