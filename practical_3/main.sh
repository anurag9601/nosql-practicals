##### STRING #####

#set string
RUN SET name redis

#get string
RUN GET name

#set multiple strings
RUN MSET name redis version 0.0.1 store memory

#get multiple values
RUN MGET name version store

##### LIST #####

#creates the list and set the input in that
RUN LPUSH name-list anurag

#setting multiple inputs in the list
RUN LPUSH name-list vikas abhishek-utekar omkar-more abhijeet

#push value on the right side of the list
RUN RPUSH name-list avinash

#poping value from the list
RUN LPOP name-list

#reading all the values of the list
RUN LRANGE name-list 0 -1

##### SET #####

#to create or add value in set
RUN SADD users anurag vikas omkar utekar

#reading all the value present in the set
RUN SMEMBERS users

#poping 2 values from the set
RUN SPOP users 2




