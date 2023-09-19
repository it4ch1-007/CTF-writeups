# **The bridgekeepers 3rd question**

**However the challenge has 367 solves but if anyone has not solved it yet or have solved it in any unintended way then the below writeup can be referred**

-> Here we are given a website link and some clues in the question statement thus first we will check the website:

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/db602f47-714a-45b3-94fe-cc3ef51894f4)



->This is the website that we come across at first. the text written at the center of the website is a link thus we will simply click on the link to see what happens.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/dac59f5c-2c27-41f3-8966-322877394288)


![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/493b2b05-de61-43af-ad30-566a5af0fad0)


![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/8ddbea2c-a359-448a-b041-2d6dbcb7418c)

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/08c2ac6c-2357-421c-8cab-7c53b876accc)



->One after the other we get three prompts to enter some string . So i simply enter "hello" to see what happens.

->Then the text of the website changed to:

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/c3da11b6-6d32-413e-99ea-5d06e4038114)



->Thus we will now see the source code and the js files of the webpage.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/2dd836a3-5c3a-4d00-b88e-3752d851fbf8)


->By seeing the source code of the webpage. We infer:

**The program only checks if the last prompt's input is "blue" or not 

**Thus i tried to enter "blue" in the last prompt but it did'nt budge.**

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/445be382-f61b-4696-99a9-e3d5c7b2d425)


->Now i checked the js file of the webpage: (index.js)

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/b92e2fa4-fb27-4a3a-a7c7-30719b654e38)



**The prompt() function is overloaded and redefined here**

->From analyzing this code we observe that we have to give an input = answer to the prompt-window so that the prompt function will return the string "blue"

- Here we have n="blue" so simply we want to make the function return the variable n .

- In the given for loop:

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/cbbf9820-8d5f-4ad3-92bd-7db7a281d114)



- walk array is iterating and updating itself to the value according to the charCode or the ASCII value of the characters in the input string (answer) - 97.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/28b74f24-2c0b-423c-b962-2bf6a2247146)



- walk array is intialized to array a.

- Also in array a we observe that it is filled with arrays equal to its own . However the 17th index is equal to array(b).

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/47f4d9ee-deb4-4cb4-9f74-fe81f39d5bf9)



- Thus if our first input string character is (97+17) . Then we walk will be updated to the array b for its second iteration inside the for loop.
 - Similarly for the second iteration we will move to update walk to array(c) if the ASCII value of the character in the string is (97+4)

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/22e2dae2-1400-44b0-9358-75b6b1863dc7)




- This can be done manually for all the arrays as we want to get simply to the n variable stored at the 4th index of the array(m).

**At last we will get the numbers :**
[17,4,1,4,2,2,0,15,20,17,15,11,4]

- These are the indices that we require to iterate through.

- But as the function also subtracts 97 to each character order in ASCII of the input string we have to add 97 to all of them. So that they become:

[114, 101, 98, 101, 99, 99, 97, 112, 117, 114, 112, 108, 101]

**Now by converting all of them into their characters in ASCII we get:**

**'rebeccapurple'** 

as our answer input

**We enter this in the third prompt and we get the required flag:

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/5e59a65d-d245-48b2-9ab9-4c0e80ce43cf)

