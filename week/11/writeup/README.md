# Writeup 1 - Web I

Name: Alex Melvin
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement: Alex Melvin


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

Level 3: Since the page will set the img as the input from the url, we can edit to URL to inject js code to call alert:
```
0' onerror=alert(1) id='
```

Level 4: We see that the page take that paramter timer=... to determine how long to wait. I checked to see if I could place a closing ' into the paramter; the code will take the paramter as normal. In the code, it will show:

```
startTimer(''');
```

Thus, we can do command injection based on the timer paramter. I use the following parameter to close the timer function call and then call alert:

```
timer=9') || alert('1
```
```
<img src="/static/loading.gif" onload="startTimer('9') || alert('1');">
```

We leave alert open since the onload atribure ends with ");"/

Level 5: We change the href attribute of the <a> to be 
 
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
