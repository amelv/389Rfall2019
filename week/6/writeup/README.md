# Writeup 6 - Binaries I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Alex Melvin

## Assignment Writeup

### Part 1 (50 pts)

FLAG: CMSC389R-{di5a55_0r_d13}

### Part 2 (50 pts)

The file “crackme” is a 32-bit binary executable. Using a normal text editor, nothing is readable. When executing the file by “./crackme”, the output asks if I had tried disassembling. Thus, clearly a disassembler is needed to figure out what exactly is occuring in the rifle.

Using binary ninja, I first looked through the main function. I first saw that the main function checks if there are any command line arguments; essentially, it requires some argument to continue without returning a sarcastic print statement. If there is a command line argument, there is then more operations performed before pushing the argument into the first function called: “check1”. 

Check1 checks if the user has entered the string “Oh god” through a string comparison. If the comparison returns true, the function then calls “update_flag”. The functions appears to update the register location of the flag string of characters. “Check1” then returns true or false; if false, the string printed out mentions that multiple word arguments can be quoted, a hint that arguments should be quoted. 

The next call is to “Check2”, which checks if there is an environment variable “FOOBAR” that has the reverse string of the assigned value “seye ym “, which is done by calling the “getenv” function. If we set an environment variable FOOBAR appropriately to “ my eyes”, the program will continue to “check3”.

 In check3, the function calls the open function with the arguement “sesame”, trying to open the file name of “sesame”. Then calls read on the file location of “sesame”. If the read works, then the function runs through each byte of a string of characters, checking 9 positions if each char corresponds correctly. By checking what ASCII value each case compares with, we find that the string of characters is “ they burn”. If “check3” returns true, then the return value from “update_flag” is printed. 

After creating a file named “sesame” containing string “ they burn” , the flag is printed out. 



