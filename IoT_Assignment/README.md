Problem 1:

Objective: to be able to use basic Node-RED functions and APIs effectively

Implement a simple weather information service based on Node-RED for the following:
• Each member of the group should be able to request the weather information of a specific location by sending an email in a specific format to a common address from his/her personal email account. 
• In return, the sender should receive the requested information in the form of an email from the common account to the respective personal account.
• Group members should be able to send requests and get responses at any time, independent of any other concurrent requests.
• The sender should get an error message (email) from the common account in the following situations:

o If the sender’s email is not in the correct format
o If the sender does not belong to the group



Problem 2: 

Objective: to be able to manipulate the Node-RED message object effectively

Create a Node-RED message having a JSON object as its payload. The object should contain your Semester 4 time table for a day of the week of your choice. 
• Device a method to extract information pertaining to a specific module or a particular time slot and display it on a dashboard when queried by time
• Device a method to generate an audio-visual notifications 5 minutes before the start of each class/lab.



Problem 3: 

Objective: to be able to use Node-RED effectively as a User Interface for interacting with IoT systems

Build a node-red application to get the weather in a variable location. It should have the following features. 
• Enter the location as coordinates or city to a text field. 
• The Title of the dashboard should be the location you entered. (Not coordinates, as a city coming from open weather) 
• Weather should be updated in each 30s interval as default. The user should be able to change the above refresh time (use numeric palette) 
• Show temperature, humidity, pressure, wind speed, wind direction, sunrise time, sun setting time of the given day. 
• Use suitable customized gauges for the above parameters (ex: a compass for wind direction). 
• There should be a speaker icon and by clicking that user should be able to hear the description of the weather. 
• There should be plots that show the temperature, humidity, wind speed within the past hour, Use a switch to on and off this feature. 
• There should be a warning limit for a selected parameter (Ex: temperature, pressure..., 

Note: use a dropdown to select) which user can enter the limit from a slider (ex:20c -45c for temperature, 5km-50km for wind, etc.), When this limit exceeds a notification should appear as a warning saying the current value of the parameter ("Warning temperature is 31c exceeds the limit by 3c").
