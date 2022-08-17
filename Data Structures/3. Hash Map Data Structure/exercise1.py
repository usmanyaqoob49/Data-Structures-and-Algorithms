#The best data structure to use here was a list because all we wanted was access of temperature element

arr = []

with open('nyc_weather.csv', 'r')as file:
    for rows in file:
        token = rows.split(',')
        #as we have strings to so
        try:
            #trying to make second indexed elemetn integer
            temperaute = int(token[1])
            arr.append(temperaute)

        except:
            print("Invalid Temperature.")

print("Array is : ",arr)
#now we have print average ist week of jan
average = sum(arr[0:7]) / len(arr[0:7])
print("average value is: ",average)

#maximum temperature in first 10 days
maxi = max(arr[0:10])
print("maximum temperature in first 10 days",maxi)

