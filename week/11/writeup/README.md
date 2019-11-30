# Writeup 1 - Web I

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: *PUT YOUR NAME HERE*


## Assignment details
This assignment has two parts. It is due by 11/27/19 at 11:59PM.

**There will be late penalty of 5% per day late!**

### Part 1 (40 Pts)

Such a Quick Little, website!

[http://142.93.136.81:5000/](http://142.93.136.81:5000/)

I first noticed the id query for all the different 0days available, so I tried doing some command injection that could hopefully lead to a XSS command attack. I tried doing

```
1' OR '1==1'>
```
where the id paramter was checked. This lead me to a page saying "ERROR: ATTEMPTED SQL INJECTION DETECTED".

### Part 2 (60 Pts)

Level 1: We use command injection to insert the XSS payload to be run. By entering 

```
<script> alert(1); </script>
```

into the search bar, we succesfully pass.

Level 2: The previous method does not work when entering into the message input; however, we see that it will render html elements. Thus, we can enter a img tag that will call alert when there is an error:

```
<img src="x" onerror="alert('XSS');">
```

Level 3: We can modify the script to determine the tabs of images by leading the window.location to a url that will run out desired paload.

Level 4:

Level5: We change the href attribute of the <a> to be 
 
```
<a href="javascript:alert(0)">Next &gt;&gt;</a>
```

so that the next link will execute the js alert command.

Level 6: Since the web page will load the URL after the frame#, we could change the URL to load a malicious js file. I exchanged /static/gadget.js will google.com/jsapi?callback=foo. 

### Format

Part 1 and 2 can be answered in bullet form or full, grammatical sentences.

### Scoring

* Part 1 is worth 40 points
* Part 2 is worth 60 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
