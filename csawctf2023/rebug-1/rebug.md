 We are given an ELF file oir an exectuable binary to reverse thus we will start by running it:

 - Here we observe:

![Alt text](image-2.png)

Thus it is a simple crackme: 
 - So let's run the binary into IDA and see the decompiled view 

 ![Alt text](image-1.png)

 - Thus we can easily see that the program is generating MD5 hash of the integer 12 and then comparing it with the input given by the user.

So we need the MD5 hash of the integer 12 ->
**c20ad4d76fe97759aa27a0c99bff6710**

![Alt text](image-3.png)

## Thus our flag will be 

**csawctf{c20ad4d76fe97759aa27a0c99bff6710}**

