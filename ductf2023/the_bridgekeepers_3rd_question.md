# **The bridgekeepers 3rd question**

**However the challenge has 367 solves but if anyone has not solved it yet or have solved it in any unintended way then the below writeup can be referred**

-> Here we are given a website link and some clues in the question statement thus first we will check the website:

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/a600c6db-c3e0-4351-b7e5-74f911b07b14)


->This is the website that we come across at first. the text written at the center of the website is a link thus we will simply click on the link to see what happens.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/24b31434-75d9-4eb4-811e-e692ee8680ee)


![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/d9667134-f748-49cf-9db9-745893047f7a)


![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/4d68e694-c45b-43b2-a11d-0fd098991f36)



->One after the other we get three prompts to enter some string . So i simply enter "hello" to see what happens.

->Then the text of the website changed to:

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/c71b9688-22fa-4e26-81ad-e0bbb0853a9f)


->Thus we will now see the source code and the js files of the webpage.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/f717c75d-39b0-46ba-9097-1b8dc3496845)


->By seeing the source code of the webpage. We infer:

**The program only checks if the last prompt's input is "blue" or not 

**Thus i tried to enter "blue" in the last prompt but it did'nt budge.**

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/cfaedab9-a818-4bb9-8c5a-3d248e188653)


->Now i checked the js file of the webpage: (index.js)

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/0c0f876a-57e0-4085-862d-933fb54cd723)


**The prompt() function is overloaded and redefined here**

->From analyzing this code we observe that we have to give an input = answer to the prompt-window so that the prompt function will return the string "blue"

- Here we have n="blue" so simply we want to make the function return the variable n .

- In the given for loop:

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/747f82bd-f110-4e57-a601-7785181e40ff)


- walk array is iterating and updating itself to the value according to the charCode or the ASCII value of the characters in the input string (answer) - 97.

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/4652d4b6-965b-439e-a18a-c672ff076379)


- walk array is intialized to array a.

- Also in array a we observe that it is filled with arrays equal to its own . However the 17th index is equal to array(b).

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/6bc52383-bdbb-468c-891b-5f67a182018b)


- Thus if our first input string character is (97+17) . Then we walk will be updated to the array b for its second iteration inside the for loop.
 - Similarly for the second iteration we will move to update walk to array(c) if the ASCII value of the character in the string is (97+4)

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/4d68e694-c45b-43b2-a11d-0fd098991f36)


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

![image](https://github.com/it4ch1-007/CTF-writeups/assets/133276365/b5a0323f-15e1-4c77-b636-14b87039e55c)
