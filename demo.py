def display_hash(hashTable):
 
 for i in range(len(HashTable)):
 print(i, end = " ")
 
 for j in hashTable[i]:
 print(":", end = " ")
 print(j[0],"-->",j[1][0],j[1][1], end = " ")
 
 print()
def tele_database():
 phone_data =[[] for i in range(n)]
 for j in range(n):
 l1=[0,0]
 print("Data of ", j+1)
 d=int(input("Enter Key of-->"))
 c=int(input("Enter Phone Numbers of -->"))
 l1=[d,c]
 phone_data.append(l1)
 return phone_data
def hash_function(key_ele, m_size):
 return key_ele % m_size
def hashtable(ht):
 print(f"\nHash Value \tKey")
 for ele in range(len(ht)):
 if ht[ele] != -1:
 print(f"\n\t{ele} \t---> \t{ht[ele]}")
 else:
 print(f"\n\t{ele}")
n = int(input("Enter Number of Clients :- "))
phone_database =[[] for i in range(n)]
phone_database=tele_database()
m = int(input("Enter Hash Table Size :- "))
hash_table = [[] for i in range(m)]
opt1 = int(input("Enter your choice\n 1. Insert\n2. Serach\n3.Display\n "))
opt2 = int(input("If collision occurs which collision resolution technique do you want to use?\n\t1. Linear " 
"Probing\n\t2. Quadratic :- "))
for l in phone_database:
 h_1 = hash_function(l[0], m)
if hash_table[h_1]== None:
else:
 
 if op1==1:
 if opt2 == 1:
 while hash_table[h_1] != -1:
 h_1 += 1
 hash_table[h_1] = k
 elif opt2 == 2:
 i = 0
 while hash_table[h_1] != -1:
 i += 1
 h_1 = (h_1 + (i * h_2)) % m
 hash_table[h_1] = k
 
 if op1==2:
 display()
 
 if op1==3:
 display_hash(hashtable)
 
hashtable(hash_table)