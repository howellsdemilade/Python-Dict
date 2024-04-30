d={}
d[100]="Joker"
d[200]="Boxer"
d[300]="Stunner"
d[400]="Janded"
d[500]="Boss"
print(d)
#----------------------------------------------------------------


#How to replace in Dictionary

d={100:"Joker",200:"Stunner",300:"Boxer"}
print(d)
d[400]="Janded"
print(d)
d[200]="Boss"
print(d)

#----------------------------------------------------------------


rec={}
n=int(input("Enter Number of Students:"))
i=1
while i<=n:
    name=input("Enter Student's Name:")
    marks=input("Enter Percentage of Marks:")
    rec[name]=marks
    i=i+1
print("Name of Student:","\t","Percentage of Marks")
for x in rec:
    print("\t",x,"\t\t\t",rec[x])

#----------------------------------------------------------------


#How to delete element from the Dictinary
d={100:"Joker",200:"Stunner",300:"Boxer"}
del d[200]
print(d)
#----------------------------------------------------------------



#Clear() Method
d={100:"Joker",200:"Stunner",300:"Boxer"}
print(d)
d.clear()
print(d)

#----------------------------------------------------------------


#How to specify multiple Values for the single key
list=["Joker","Boxer","Stunner"]
d={500:list}
print(d)


#Important Functions/Methods of Dictionary
d = dict(((100,"Joker"),(200,"Boxer"),(300,"Stunner"),(400,"Janded")))
print(d)
#dict()
d=dict({500:"Joker",700:"Boxer"})
print(d)

#len()
d=dict({500:"Joker",700:"Boxer"})
print(len(d))

#get()
d=dict({500:"Joker",700:"Boxer"})
print(d.get(500))

#if the KeyValue its not in the dict
d=dict({500:"Joker",700:"Boxer"})
print(d.get(600,"Boss"))

#----------------------------------------------------------------


#pop()
d=dict({500:"Joker",700:"Boxer"})
print(d)
print(d.pop(500))
print(d)
#----------------------------------------------------------------


#popitem()
d=dict({500:"Joker",700:"Boxer"})
print(d)
print(d.popitem())
print(d)

#----------------------------------------------------------------


#keys()
d=dict({500:"Joker",700:"Boxer"})
print(d.keys())
for k in d.keys():
    print(k)

    #----------------------------------------------------------------



#values()
d=dict({500:"Joker",700:"Boxer"})
print(d.values())
for k in d.values():
    print(k)



#----------------------------------------------------------------



#items()
#It will output List of Tuples
d=dict({500:"Joker",700:"Boxer"})
list=d.items()
print(list)

#----------------------------------------------------------------

d=dict({500:"Joker",700:"Boxer",800:"Stunner"})
for k,v in d.items():
    print(k,"......",v)

#----------------------------------------------------------------

#setdefault()
d=({500:"Joker",700:"Boxer",800:"Stunner"})
print(d.setdefault(900,"Janded"))
print(d)

#----------------------------------------------------------------



#update()
d=({500:"Joker",700:"Boxer",800:"Stunner"})
d1={"a":"Anaconda","b":"Batista"}
d.update(d1)
print(d)


#----------------------------------------------------------------


#Take dictionary from the keyboard and print the sum of the values
d=eval(input("Enter Dictionary:"))
s=sum(d.values())
print("The Sum:",s)


#----------------------------------------------------------------


word=input("Enter some word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)

#----------------------------------------------------------------



#
word=input("Enter some word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
print(d)
print(sorted(d))
for k,v in sorted(d.items()):
    print("{} occurred {} times".format(k,v))

#----------------------------------------------------------------



#with only vowels
word=input("Enter some word:")
vowels={"a","e","i","o","u"}
d={}
for x in word:
    if x in vowels:
       d[x]=d.get(x,0)+1
for k,v in sorted(d.items()) :
    print("{} occurred {} times".format(k,v))

#----------------------------------------------------------------



#Create a program to input student name and marks
n=int(input("Enter the Number of Student:"))
d={}
for i in range(n):
    name=input("Enter Student's Name:")
    marks=input("Enter Student's Marks:")
    d[name]=marks
print(d)



#################################################################################################################

n=int(input("Enter the Number of Student:"))
d={}
for i in range(n):
    name=input("Enter Student's Name:")
    marks=input("Enter Student's Marks:")
    d[name]=marks
print(d)
while True:
    name=input("Enter Student's Name to get Marks:")
    marks=d.get(name,-1)
    if marks==-1:
        print("Student not Found!")
    else:
        print("The Marks of {} :{}".format(name,marks))
    option=input("Do you want to find another Student's marks[Yes][No]:")
    if option=="No":
        break
print("Thanks for Using our Application!!!")



#----------------------------------------------------------------




#Dictionary Comprehension
#Squares in Dictionary
squares={x:x*x  for x in range(1,11)}
print(squares)
#Doubles in Dictionary
doubles={x:2*x for x in range(1,11)}
print(doubles)




