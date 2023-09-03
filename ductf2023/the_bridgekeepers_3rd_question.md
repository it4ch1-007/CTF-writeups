# **The bridgekeepers 3rd question**

**However the challenge has 367 solves but if anyone has not solved it yet or have solved it in any unintended way then the below writeup can be referred**

-> Here we are given a website link and some clues in the question statement thus first we will check the website:

![Alt text](../images/image.png)

->This is the website that we come across at first. the text written at the center of the website is a link thus we will simply click on the link to see what happens.

![Alt text](../images/image-2.png)

![Alt text](../images/image-3.png)

![Alt text](..images/image-4.png)

->One after the other we get three prompts to enter some string . So i simply enter "hello" to see what happens.

->Then the text of the website changed to:

![Alt text](../images/image-5.png)

->Thus we will now see the source code and the js files of the webpage.

![Alt text](../images/image-6.png)

->By seeing the source code of the webpage. We infer:

**The program only checks if the last prompt's input is "blue" or not 

**Thus i tried to enter "blue" in the last prompt but it did'nt budge.**

![Alt text](../images/image-7.png)

->Now i checked the js file of the webpage: (index.js)

![Alt text](../images/image-8.png)

**The prompt() function is overloaded and redefined here**

->From analyzing this code we observe that we have to give an input = answer to the prompt-window so that the prompt function will return the string "blue"

- Here we have n="blue" so simply we want to make the function return the variable n .

- In the given for loop:

![Alt text](../images/image-9.png)

- walk array is iterating and updating itself to the value according to the charCode or the ASCII value of the characters in the input string (answer) - 97.

![Alt text](../images/image-10.png)

- walk array is intialized to array a.

- Also in array a we observe that it is filled with arrays equal to its own . However the 17th index is equal to array(b).

![Alt text](../images/image-12.png)

- Thus if our first input string character is (97+17) . Then we walk will be updated to the array b for its second iteration inside the for loop.
 - Similarly for the second iteration we will move to update walk to array(c) if the ASCII value of the character in the string is (97+4)
 ![Alt text](../images/image-11.png)

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

![Alt text](../images/image-13.png)