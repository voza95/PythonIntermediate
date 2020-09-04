import secrets
# This will genrate true random numbers
# This moudle only have three packages

# a = secrets.randbelow(10) #Result between 0 and 9
# a = secrets.randbits(4)#Not that usefull.Uses bites so 4 means number between 0 to 15
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)