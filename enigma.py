import enigma_rotor as er                        #library(wiring) 

lst=[]
l=[]
def plugboards():                  #input plugboards pairs from the user
  global lst
  lst=[]
  n=int(input("Enter the number of pairs to be formed : "))
  l=[]
  print('''
                         Q	W	E	R	T	Y	U	I	O	P
                            A	   S 	   D	   F	   G	   H	   J	   K	   L
                               Z     X	     C	     V	     B	     N	     M
''')
  while(len(lst)!=n):
    try:
      i,p=input('Enter the pair values : ').upper().split()
    except:
      print("Invalid pair!")
    else:
      while(len(i)!=1 or len(p)!=1 or  (ord(i) not in range(65,123)) or (ord(i) not in range(65,123)) or (i in l) or (p in l)):
        print("Invalid pair entry!")
        if(i in l):    
          print(i,"is already paired!")
        if(p in l):
          print(p,"is already paired!")
        i,p=input('Enter the pair values : ').upper().split()
      else:
        lst.append([i,p])
        l.append(i);l.append(p)
    
  print(lst)

n1=n2=n3=0
def setting():                        #input setting from the user
  global l,n1,n2,n3
  try: 
    n1,n2,n3=input("Enter the setting : ").split()
    n1=int(n1);n2=int(n2);n3=int(n3) 
  except:
    print("Please enter 3 setting values")
    print("Setting status : Invalid")
    setting()
  else:
    while((n1 not in range(1,27)) or (n2 not in range(1,27)) or (n3 not in range(1,27))):
      print("Invalid setting!")
      setting()
    else:
      print("Setting status : Valid")
      l=[n1,n2,n3]

def rotor(n):                        #Calculates setting for each letter in the text
  p=[];global l
  for i in range(n):

    if(l==[26,26,26]):
      l=[1,1,1]
    elif(l[2]<26):
      l[2]+=1
    elif(l[2]==26 and l[1]<26):
      l[1]+=1
    elif(l[2]==26 and l[1]==26 and l[0]<26):
      l[0]+=1
    p.append(tuple(l))

  return p

en=[]
def encrypt_1():                #plugins level encryption
  global en
  en=[]
  for j in s:
    k=j
    for i in lst:
      if(i[0]==k):
        k=i[1]
      elif(i[1]==k):
        k=i[0]
      
    en.append(k)
  print(en)


def encrypt_2(p):                       #rotor level encryption
  en1=[]
  for i in range(len(p)):
    c=en[i]
    for j in range(2,-1,-1):
      new_d=er.r3[p[i][j]].copy()
      c=new_d[c]
      new_d=er.r2[p[i][j]].copy()
      c=new_d[c]
      new_d=er.r1[p[i][j]].copy()      
      c=new_d[c]
    en1.append(c)

  print("ENCRYPTED CODE/TEXT  :  ",''.join(en1))


def decrypt_2(p):                   #rotor level decryption 
  global s;dn=[]
  for i in range(len(p)):
    c=s[i]
    
    for j in range(0,3):
      for k,v in er.r1[p[i][j]].items():
        if(v==c):
          c=k
          break
      for k,v in er.r2[p[i][j]].items():
        if(v==c):
          c=k
          break      
      for k,v in er.r3[p[i][j]].items():
        if(v==c):
          c=k
          break
    dn.append(c)
  print(dn)
  return dn
  
def decrypt_1(dn):                   #plugins level decryption
  dn1=[]
  for j in dn:
    k=j
    for i in lst:
      if(i[0]==k):
        k=i[1]
      elif(i[1]==k):
        k=i[0]
    dn1.append(k)
  print("DECRYPTED CODE/TEXT  :  ",''.join(dn1))  


s=''
f=0
def get():                          #input from user
  global s,f
  s=input("Enter the text (NO numbers,symbols or space) :").upper()
  for i in s:
    if(i.isdigit() or i.isspace()):
      f=1
      break
  else:
    f=0
  while(s.isspace() or s.isdigit() or f==1 or s==''):
    print("Invalid input!")
    get()
  


'''
plugboards()  
encrypt_1()
setting()
p=rotor(len(en))
encrypt_2(p)

print("DECRYPT")
de=list(input('Enter the encrypted text : ').upper())
setting()
pd=rotor(len(de))
dn=decrypt_2(pd)
plugboards()
decrypt_1(dn)
'''

def main():

  while(1):
    
    print('''
                                                          ENIGMA

                                                        1-Encrypt
                                                        2-Decrypt
                                                        3-Exit

''')
    ch=int(input("Enter your choice : "))
    if(ch==1):
      plugboards()
      setting()
      get()
      p=rotor(len(s))
      encrypt_1()
      encrypt_2(p)

    elif(ch==2):
      plugboards()
      setting()
      get()
      p=rotor(len(s))
      dn=decrypt_2(p)
      decrypt_1(dn)
      
  
    elif(ch==3):
      print("Thank you")
      break

    else:
      print("Entered wrong choice!")
  
main()


