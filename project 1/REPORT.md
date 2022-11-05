# Project 1 report

This project has been implemented by Django, Flask and Node.js.<br/>

## How to run
To run the project run the following commands:<br/>
docker compose build<br/>
docker compuse up<br/>
To test the performance of the project run the following commands depending on using linux or windows<br/>
linux:<br/>
[Download k6](https://drive.google.com/file/d/1BkGAIRBpi-2CPKSIe9AecI-8TnqsvXaB/view?usp=share_link)<br/>
chmod +x k6<br/>
chmod +x run-tests.sh<br/>
./run-tests.sh<br/>
windows:<br/>
[Download k6](https://drive.google.com/file/d/1LNY7-csBdFUcLRI1eDdnozPynkRZ0YGM/view?usp=share_link)<br/>
./run-tests.ps1<br/>
<br/>
## Results
Performance tests run with 10 vus for 5s.<br/>
<br/>
Django:<br/>
Performance tests for the main page:<br/>
average requests per second: 156.191178/s<br/>
median request duration: 59.77ms<br/>
95th percentile request duration: 92.29ms<br/>
99th percentile request duration: 110.83ms<br/>
<br/>
Performance tests for submitting the form to the database:<br/>
average requests per second: 56.107708/s<br/>
median request duration: 79.58ms<br/>
95th percentile request duration: 599.62ms<br/>
99th percentile request duration: 1.08s<br/>
<br/>
Performance tests for asking for redirection:<br/>
average requests per second: 178.826274/s<br/>
median request duration: 57.65ms<br/>
95th percentile request duration: 88.53ms<br/>
99th percentile request duration: 117.73ms<br/>
<br/>
Performance tests for asking to be redirected to a random location:<br/>
average requests per second: 60.177493/s<br/>
median request duration: 61.94ms<br/>
95th percentile request duration: 613.36ms<br/>
99th percentile request duration: 1.91s<br/>
<br/>
 <br/>
Flask:
Performance tests for the main page:<br/>
average requests per second: 406.950339/s<br/>
median request duration: 23.83ms<br/>
95th percentile request duration: 29.9ms<br/>
99th percentile request duration: 33.65ms<br/>
<br/>
Performance tests for submitting the form to the database:<br/>
average requests per second: 68.674406/s<br/>
median request duration: 44.46ms<br/>
95th percentile request duration: 634.38ms<br/>
99th percentile request duration: 1.55s<br/>
<br/>
Performance tests for asking for redirection:<br/>
average requests per second: 173.284642/s<br/>
median request duration: 59.05ms<br/>
95th percentile request duration: 89.18ms<br/>
99th percentile request duration: 105.27ms<br/>
<br/>
Performance tests for asking to be redirected to a random location:<br/>
average requests per second: 12.806043/s<br/>
median request duration: 63.48ms<br/>
95th percentile request duration: 3.87s<br/>
99th percentile request duration: 3.97s<br/>
<br/>
<br/>
Node.js:<br/>
Performance tests for the main page:<br/>
average requests per second: 2060.753634/s<br/>
median request duration: 3.96ms<br/>
95th percentile request duration: 8.81ms<br/>
99th percentile request duration: 12.67ms<br/>
<br/>
Performance tests for submitting the form to the database:<br/>
average requests per second: 73.219922/s<br/>
median request duration: 142.06ms<br/>
95th percentile request duration: 164.97ms<br/>
99th percentile request duration: 174.9ms<br/>
<br/>
Performance tests for asking for redirection:<br/>
average requests per second: 178.994647/s<br/>
median request duration: 58.78ms<br/>
95th percentile request duration: 93.32ms<br/>
99th percentile request duration: 122.4ms<br/>
<br/>
Performance tests for asking to be redirected to a random location:<br/>
average requests per second: 179.498298/s<br/>
median request duration: 57.92ms<br/>
95th percentile request duration: 88.4ms<br/>
99th percentile request duration: 123.73ms<br/>
<br/>
## Reasons for possible performance differences between the pages and between the clones
The redirection results for all three implementations are similar and unrelated to the used programming language. Because basically they all access the same type of database and there is no need for rendering they just redirect to the target URL.<br/>
The results for Django and flask which are both python frameworks are closer than node.js which is a different programming language.<br/>
Node.js is a lot faster. The reason for this is that node renders HTML pages a lot faster and because it is non-blocking by default.<br/>
Flask is faster than Django because it is a lighter framework. <br/>
The slowest page is the page with submitting forms to the database which is not a surprise because writing to the database is usually the slowest part of an application.<br/>
The main page is always faster because it does not need any read or write from the database.<br/>
<br/>
## Suggestions for improving the performance of the applications
Implementing a pre-computed random algorithm that always stores the next random value to avoid a database search.<br/>
Caching pages like most redirected to.<br/>
For Flask change the rendering engine to something faster if available.<br/>
We can also change the databases and use databases with better performance.<br/>
Django web server is only for development and has not been designed for deployment and Django suggests using another web server.<br/>
Flask and Django by default are not handling io operations as non-blocking. This can be changed to make them faster.<br/>
Python is not single threaded so we can add parallel processing and handling of requests.<br/>
Node.js is based on javascript which is single threaded but we can also make it parallel using multiple instances of it.<br/>


