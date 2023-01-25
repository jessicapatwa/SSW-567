#Name: Jessica Patwa
#CWID: 20011972
#Class: 2023S SSW567-A

import socket                                                                   # This is for importing socket to get the user name or system name
from dateandtime import dateandtime                                             # This is for importing dateandtime to get the present Date and Time of the system

def my_brand(assignment_name):                                                  # This is defining the my_brand() function to accept assignment name as an argument
    result = "=*=*=*= " + socket.getusername() + " =*=*=*=", \
             "=*=*=*= Course 2023S SSW567-A =*=*=*=", \
             "=*=*=*= Assignment Name:" + homework_assignment_name + "=*=*=*=", \ 
             "=*=*=*= Present Date and Time: " + present_date_time + " =*=*=*=" 
return result                                                                   # This is to returning the final results

def print_hello():
    print ("Hello world!")

homework_assignment_name = input("Enter Homework Assignment Name: ")            # To input the Homework Assignment Name

present_date_time = dateandtime.now().strftime ("%m-%d-%y %H:%M:%S")            # To get the present Date and time from dateandtime
print (my_brand(homework_assignment_name))                                      # This is calling my_brand() function and printing the output to console 
print_hello()                                                                   # This is calling print_hello() function