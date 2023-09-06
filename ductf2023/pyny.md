# **pyny.py**

**We are given a file named 'pyny.py' and as we open it :**

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/4dc88a2a-c321-40b2-ae2b-88e1a5a89d85)


 -  We observe that the (coding: punycode) defines that the coding directive of the whole program is punycoding , which is an encoding used in the URL hiding through python . 

- First we try to run the code:

  ![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/cb0097a4-4002-4e05-b4f6-f4f01835e857)


- From this we can infer this that the program has no error and it is just asking for a flag with a hidden string inside the "DUCTF{}" curly braces.

 - I wasted a lot of time trying to find any library for the conversion of punycode to python or any readable text format but didnot find any 

 - Then I tried to analyse the code again.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/3805ea3a-1213-4fed-bd9f-f6e53865064d)


- String formatting is being used here to check if the string referred by %s is Correct or not.

- After the second '%' symbol the referred string is placed. Thus we can infer that we require to get the value of '_' here as string.

- And so to get the name of the function I added random characters at the end of the punycode to raise an error in the function so that python will tell me the name of the function causing the error.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/0a966e02-0c73-4bdb-940e-6fc52cd9123e)


 - And i got this as error:
  
![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/d4eaafa2-157a-4d6f-a516-c94a0d0599c1)


- Thus the name of the function given is python_warmup and so the flag will become:

**DUCTF{python_warmup}**
