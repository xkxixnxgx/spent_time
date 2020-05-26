Spent Time
=======================

Legend
-----------

###### The Story of Success is the third non-fiction book written by Malcolm Gladwell and published by Little, Brown and Company on November 18, 2008. In Outliers, Gladwell examines the factors that contribute to high levels of success. To support his thesis, he examines why the majority of Canadian ice hockey players are born in the first few months of the calendar year, how Microsoft co-founder Bill Gates achieved his extreme wealth, how the Beatles became one of the most successful musical acts in human history, how Joseph Flom built Skadden, Arps, Slate, Meagher & Flom into one of the most successful law firms in the world, how cultural differences play a large part in perceived intelligence and rational decision making, and how two people with exceptional intelligence, Christopher Langan and J. Robert Oppenheimer, end up with such vastly different fortunes. Throughout the publication, Gladwell repeatedly mentions the "10,000-Hour Rule", claiming that the key to achieving world-class expertise in any skill, is, to a large extent, a matter of practicing the correct way, for a total of around 10,000 hours.

Goals
-----
###### Some people find it difficult to keep in mind goals that take a long time to achieve and yet time is distributed. We are solving this problem. We record the time spent on certain tasks and output statistics about how much time is spent on a particular task, and how intensely we devote ourselves to the task at hand.

Rules and Tips
--------------
 - Create tracks.
 - Select a date and specify the number of hours spent for each track.
 - Monitor the time spent on issues using advanced statistics.
 - Use the switch to switch between tasks.
 - Use the telegram bot as an assistant and widget on your desktop.
 
Project status
----------------
###### *in the development*

License
-------
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

Local installation
------------------
##### You will need:
1. Python 3.7
2. pip3
3. venv
##### Steps:
1. Copy the repository to a folder on PC.
2. In the project folder install packages with commands in the console: 
   ````
   python3 install -m venv env
   pip3 install -r requirements.txt
   python3 create_db.py
   ./web_run.sh
   
3. Enter in the browser:
   <http://127.0.0.1:5000/>
4. You can create an account for the admin with the command:
   ````
   python3 create_admin.py
