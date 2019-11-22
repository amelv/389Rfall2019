# Writeup 10 - Crypto I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details

### Part 1 (45 Pts)


1.

2. Begins by creating a md5 hash of a desired key-length, then zeroing all bytes but the first two, leaving a key space of 256^2 for the first two bytes. They then hash the two bit key using md5.



3. 

4. The program first encrypted both the cipher text length and the cipher text before anything as been written to file.

The program uses md5 hashing to create an encryted key in the params struct, with the first 2 bits md5 hashed and the rest (14 bits) are set to zero. The key hash of params is set using the md5 hash of the first 2 bits.

5.The program ensure Integrity by checking that the cipher text hash is equal to the hashed msg variable from the file; after reading through the message, the program hashes it and checks against the sent cipher text. If something is different, then there must have been tampering.

6. The program checks for authenticity by comparing the generated key hash  against the key hash in the file. The key hash is generated using the first two bytes from the md5 hash, and then hashing those again. If they are not equal, then the they are not authenticated. 

7. 

### Part 2 (45 Pts)

Flag is CMSC389R-{k3y5p4c3_2_sm411}

### Part 3 (10 Pts)

An obfuscated source of the ledger scheme would ahve made it harder to discover the small key space utilized by the program. It was clear that a brute force attack would be possible by looking at the code and especially the hex value of the key_hash. Yet obfuscation is still able to be reverse engineered, thus we should not focus on obfuscation on a scheme that is so crytopgrahically weak. The ideal standard should be to create a scheme where it can be known without compromising the system, even allowing some parameters to be public. Of course, obfuscation is still a worthwile goal; crytogrpahy systems can be vulnerable as compuatoinal power improves. Generally, we should aim to make it as hard as possible for an attacker; the ideal case is that the could not computationally attack the scheme, and as a backup they don't know how the encryption scheme is implemented.
