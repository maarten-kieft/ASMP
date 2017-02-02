# ASMP
Another Smart Meter Project, which allows users to read the values of their (dutch) smart meter, aggregate them and display them in nice graphs. This project is build in python and uses docker to deploy the application. This is work in progress.. 

Milestones:

1. (Done)Getting to know git better
2. (Done)Creating a hello world python application
3. (Done) Setting up a docker scipt file to contain the application
  1. Create a docker file for web application 
    1. (Done)Determine right base image
    2. (Done)Determine requirements
    3. (Done)Deploy django app in docker image 
  2. (Done)Create a docker file for database
  3. (Done)Create a docker file for processor
  
4. (Done)Read values from the p1 port and display the result in the console
5. (Done)Store values in the database
6. (Done) a web application to display the data from the database
7. (Progress)Create a fancy web application
	(Done) Setup view mechanism
	(Progress) Design pages
	Showing the current usage
	Showing a graph of todays usage
    Showing a graph of day and night usage
	Showing a comparison between yesterday, last month, last year
  
Open issues:

  1. Crash random on parsing
  2. no auto pull newest


Commando:

docker build -t blackhawkdesign/asmp-rpi .

docker tag xxx blackhawkdesign/asmp-rpi

docker push blackhawkdesign/asmp-rpi

docker run -p 8000:8000 --device=/dev/ttyUSB0 -v /usr/bin/asmp:/usr/bin/asmp/data  blackhawkdesign/asmp-rpi

docker run -p 8000:8000 