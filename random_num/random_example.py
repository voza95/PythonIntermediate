import random
# Used for genrating sudo-random number for various distrbution.
# It calls sudo-random because it seem random but they are reproducable.

# TO reproduce random variable we use seed method.
random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))
# *****Hance this random number r reproducable hance not recomanded for security perpuses.*******

# a = random.random()#random number b/w 0 to 1
# a = random.uniform(1,20)#random float b/w provided number
# a = random.randint(1,20)#random int b/w provided number
#a = random.randrange(1,20)#random int b/w provided number last number not included
# a = random.normalvariate(mu=0,sigma=1)#Take a random value from a normal distribution with a mean of zero and std of 1.
# print(a) 

# mylist = list("ABCDEFGH")
# print(mylist)
# a = random.choice(mylist) # for one element
# a = random.sample(mylist,2)#for mutiple elements
# a = random.choices(mylist, k=3)#To pick random vaiable multiple times
# print(a)
# random.shuffle(mylist)# It will shffle our list inplace
# print(mylist)

