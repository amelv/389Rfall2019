# Writeup 8 - Binaries II

Name: Alex Melvin
Section: 2PM Section

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Alex Melvin

## Assignment Writeup

### Part 1 (100 pts)
Answer the following questions regarding the server executable (for which source is provided).

1. How is the per-session administrator password generated? Are there any inherent weaknesses in this implementation?

The password string is stored through calloc*.

2. Describe two vulnerabilities in this program. Provide specific line numbers and classifications of the vulnerability. Explain potential ramifications as well as ways to avoid these vulnerabilities when writing code.

Line 35: takes in whatever input from user. This is then a problem for line 46, where the printf will take any argeuments, including format options that will print anything from the stack.

Use of vulnerable "gets" function on line 68. Additionally, it does not checks on what the user inputs besides a max buffer size. Easily vulnerable to a buffer overflow attack.

:q:


3. What is the flag?

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.

I used a format string attack on the cipher function. I realized that, with the ciper, to print out the elements on the stack, I needed to use %c instead of %p for hex represenations due to the shift by 13. I then checked to see where the entered string would be stored in the stack by entering "AAAA" (which is 41414141 in hex) and appended "%c%c..."  many times to see where the 414141414 appeared. I found that such hex number appeared in the 12th stack variable. Learning this information, I know focused on writing to the stack using %n (which becomes %a in this case).
