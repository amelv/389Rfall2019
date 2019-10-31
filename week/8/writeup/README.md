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

Use of vulnerable "gets" function on line 68. Additionally, it does not checks on what the user inputs besides a max buffer size. Easily vulnerable to a buffer overflow attack.

Line 77, system call on parameter with no checks for dangerous use. Easily can do command injetion on the server.


3. What is the flag?

4. Describe the process you followed to obtain the flag: vulnerabilities exploited, your inputs to the server in a human-readable format, etc. If you create any helper code please include it.
