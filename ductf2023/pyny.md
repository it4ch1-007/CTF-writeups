# **pyny.py**

**We are given a file named 'pyny.py' and as we open it :**

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/af03cf73-e993-4e97-a062-6d9e81e7825c)

 -  We observe that the (coding: punycode) defines that the coding directive of the whole program is punycoding , which is an encoding used in the URL hiding through python . 

- First we try to run the code:

 ![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/e8c2d4b7-5d34-4be2-8472-d5c1b6ef3aae)



- From this we can infer this that the program has no error and it is just asking for a flag with a hidden string inside the "DUCTF{}" curly braces.

 - I wasted a lot of time trying to find any library for the conversion of punycode to python or any readable text format but didnot find any 

 - Then I tried to analyse the code again.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/05ebe7b2-d16a-477a-a370-b46c2e352b18)



- String formatting is being used here to check if the string referred by %s is Correct or not.

- After the second '%' symbol the referred string is placed. Thus we can infer that we require to get the value of '_' here as string.

- And so to get the name of the function I added random characters at the end of the punycode to raise an error in the function so that python will tell me the name of the function causing the error.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/1af4f919-f265-4684-87a6-0a381980e7ed)



 - And i got this as error:
  
![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/6afee896-6e9d-4f71-9b3a-f88c35085152)



- Thus the name of the function given is python_warmup and so the flag will become:

**DUCTF{python_warmup}**
