#one shall past sorting order of preference list [ 'First Name' , 'Last Name' ]
def selection_sort(list_of_names, list_sorting_preference):
    size = len(list_of_names)
    #we will sort the whole list of dictionary accordng to the first or last name
    #we will recieve that first or last name in first element of list
    #For Example if we recieved this: [ 'First Name' , 'Last Name' ]
    #we will sort it by First Name
    sort_by = list_sorting_preference[0]
    #below will be used to swap the other part of name
    sort_sec = list_sorting_preference[1]

    for i in  range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            #if the next enteries first or last name is smaller then our min
            if list_of_names[j][sort_by] < list_of_names[min_index][sort_by]:
                #simply replace with min_index
                min_index = j


        #swap that part of name to get min name in first place
        if i!= min_index:
            list_of_names[i][sort_by],list_of_names[min_index][sort_by] = list_of_names[min_index][sort_by],list_of_names[i][sort_by]
        #swapping the other part of names too so that we dont get mixed names 
            list_of_names[i][sort_sec], list_of_names[min_index][sort_sec] =   list_of_names[min_index][sort_sec],list_of_names[i][sort_sec]

    return list_of_names


name_list = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]


#for i in range(len(name_list)):
    #print(name_list[i]['First Name'])

    #above statements give us all first names


selection_sort(name_list, ['Last Name', 'First Name'])
print(*name_list,sep='\n')
