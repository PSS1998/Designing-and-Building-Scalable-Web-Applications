# Project 1 report

This project has been implemented by Django, Flask and Node.js.

## How to run
To run the project run the following commands:
docker compose build
docker compuse up
To test the performance of the project run the following commands depending on using linux or windows
linux:
[Download k6](https://drive.google.com/file/d/1BkGAIRBpi-2CPKSIe9AecI-8TnqsvXaB/view?usp=share_link)
chmod +x k6
chmod +x run-tests.sh
./run-tests.sh
windows:
[Download k6](https://drive.google.com/file/d/1LNY7-csBdFUcLRI1eDdnozPynkRZ0YGM/view?usp=share_link)
./run-tests.ps1

## Results
Performance tests run with 10 vus for 5s.

Django:
Performance tests for the main page:
average requests per second: 156.191178/s
median request duration: 59.77ms
95th percentile request duration: 92.29ms
99th percentile request duration: 110.83ms

Performance tests for submitting the form to the database:
average requests per second: 56.107708/s
median request duration: 79.58ms
95th percentile request duration: 599.62ms
99th percentile request duration: 1.08s

Performance tests for asking for redirection:
average requests per second: 178.826274/s
median request duration: 57.65ms
95th percentile request duration: 88.53ms
99th percentile request duration: 117.73ms

Performance tests for asking to be redirected to a random location:
average requests per second: 60.177493/s
median request duration: 61.94ms
95th percentile request duration: 613.36ms
99th percentile request duration: 1.91s

 
Flask:
Performance tests for the main page:
average requests per second: 406.950339/s
median request duration: 23.83ms
95th percentile request duration: 29.9ms
99th percentile request duration: 33.65ms

Performance tests for submitting the form to the database:
average requests per second: 68.674406/s
median request duration: 44.46ms
95th percentile request duration: 634.38ms
99th percentile request duration: 1.55s

Performance tests for asking for redirection:
average requests per second: 173.284642/s
median request duration: 59.05ms
95th percentile request duration: 89.18ms
99th percentile request duration: 105.27ms

Performance tests for asking to be redirected to a random location:
average requests per second: 12.806043/s
median request duration: 63.48ms
95th percentile request duration: 3.87s
99th percentile request duration: 3.97s


Node.js:
Performance tests for the main page:
average requests per second: 2060.753634/s
median request duration: 3.96ms
95th percentile request duration: 8.81ms
99th percentile request duration: 12.67ms

Performance tests for submitting the form to the database:
average requests per second: 73.219922/s
median request duration: 142.06ms
95th percentile request duration: 164.97ms
99th percentile request duration: 174.9ms

Performance tests for asking for redirection:
average requests per second: 178.994647/s
median request duration: 58.78ms
95th percentile request duration: 93.32ms
99th percentile request duration: 122.4ms

Performance tests for asking to be redirected to a random location:
average requests per second: 179.498298/s
median request duration: 57.92ms
95th percentile request duration: 88.4ms
99th percentile request duration: 123.73ms

## Reasons for possible performance differences between the pages and between the clones
The redirection results for all three implementations are similar and unrelated to the used programming language. Because basically they all access the same type of database and there is no need for rendering they just redirect to the target URL.
The results for Django and flask which are both python frameworks are closer than node.js which is a different programming language.
Node.js is a lot faster. The reason for this is that node renders HTML pages a lot faster and because it is non-blocking by default.
Flask is faster than Django because it is a lighter framework. 
The slowest page is the page with submitting forms to the database which is not a surprise because writing to the database is usually the slowest part of an application.
The main page is always faster because it does not need any read or write from the database.

## Suggestions for improving the performance of the applications
Implementing a pre-computed random algorithm that always stores the next random value to avoid a database search.
Caching pages like most redirected to.
For Flask change the rendering engine to something faster if available.
We can also change the databases and use databases with better performance.
Django web server is only for development and has not been designed for deployment and Django suggests using another web server.
Flask and Django by default are not handling io operations as non-blocking. This can be changed to make them faster.
Python is not single threaded so we can add parallel processing and handling of requests.
Node.js is based on javascript which is single threaded but we can also make it parallel using multiple instances of it.


