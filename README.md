# fifa_manager
A match query, addition and deletion software for users and administrators. (individual work)
The FIFA World Cup (FIFA World Cup), referred to as the "World Cup", is a soccer tournament 
that symbolizes the highest honor in the soccer world and has the greatest popularity and 
influence, with the participation of national-level teams from all over the world. As a 
quadrennial soccer event, the current World Cup is in full swing.
To better participate in the World Cup fever, you need to build a tournament query system 
for this World Cup, and the system you build must be a client-server application. In this 
project, you need to write two .py files, one for the client and the other for the server. The 
client will establish a connection with the server, and the client will send requests for querying 
and entering tournament information, which should be processed by the server and return 
results to the client through the information stored on the server (such as schedules, user 
information, etc.). The specific requirements of this assignment are as follows.
System design
1. User management: Users need to be divided into two categories, one is ordinary users who 
can only use the query and other functions; the other is management personnel who can 
update the event information. In addition, the registration function should be added for users 
who use the system for the first time.
2. Event entry: This module is mainly responsible for the managers to enter the relevant 
competition data and can update it in time. The data format is not required, it can be written 
clearly in the design report.
3. Race query: This part is the main part of the whole query system, mainly refers to the user 
to query the data they want to get (including schedule and points) by inputting and filtering 
relevant information (such as date, country, team, etc.).
For example: query a certain day schedule
Input: November 27th
Show: November 27 00:00 France 2:1 Denmark Ended
 November 27 03:00 Argentina 2:0 Mexico Ended
November 27 18:00 Japan - : - Costa Rica Not started
November 27 21:00 Belgium - : - Morocco Not started
4. system display: to provide users with the entire system query interface, responsible for 
interaction with users (can be used in the form of GUI, etc.), the requirement to display 
information neat and beautiful, easy to operate.
5. Database design: In the database, we need to save two kinds of information, one is user 
information, such as whether it is a manager, user id and password, etc.; the second is 
tournament information, such as team, score, date, time, points, etc. The specific format is not 
required, just complete the requirements.
Note: 1）The above functions are basic requirements, other functions that can make the 
whole system more perfect and convenient can be added.
 2）You must use the re module, for example to check the date using regular 
expressions
The design report
After completing the system design, we need a report to introduce the system you have 
designed. This report should contain the following points: system design, functional 
introduction (including the explanation of the code), system demonstration, instructions for 
use (must be detailed, such as what environment is needed, etc.), and experience
