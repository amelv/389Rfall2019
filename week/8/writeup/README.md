# Writeup 8 - Binaries II

Name: Alex Melvin
Section: 2PM Section

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Alex Melvin

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The password is dynanmically allocated to the heap using calloc. It generates each character using random generation until the end of the password length is reached. Then, the first character is set to zero. The issue with the last statement is that is leads the stack pointer, ESP to be pointed directly to the password in memory. This allows one to find the password on the stack when doing a format string attack.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

Line 35: takes in whatever input from user. This is then a problem for line 46, where the printf will take any argeuments, including format options that will print anything from the stack. Vulnerable to format string attack. Can be avoided by blacklisting the % character.

Use of vulnerable "gets" function on line 68. Additionally, it does not checks on what the user inputs besides a max buffer size. Easily vulnerable to a buffer overflow attack. Can be avoided by using other buffer scanners, since gets has been universally declared dangerous and many other options are available.

3. What is the flag?

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

I used the cipher function to perform a format string attack using "%c%c%c..." which shifts to %x. I then saw that the ESP offset with the password pointed at will be at the offet %24$c during the printf for cipher. This revealed the password in hex, and I converted it into a string. I then entered the password into the authentication prompt. Once given access, I began to perform a buffer overflow attack; I overflowed the buffer of 32 bits to then overwrite the whitelist arguement in the string compare, allowing me to change what I can execute. I then execute ls to find flag.txt and then did cat flag.txt. ***note I struggled to actually get the flag, but I believe this is the correct process**? 
