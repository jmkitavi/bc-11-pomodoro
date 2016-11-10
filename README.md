#### POMODORO TIMER
## bc-11-pomodoro
# by Sir JM Kitavi

To run the app install the virtual environment.
	run `pip install -r requirements.txt`

	Also for sound you need to have #vlc installed

##pomodoro timer??
Well if you google pomodoro you will come across tomatoes so whoever called it pomodoro missed out on a chance to call it #Tomato timer
Podomoro timer allows you to schedule your tasks and break. It divides tasks to cycles, short breaks and long breaks.
Cycles by default are of 25 minutes, Short breaks 5 minutes (come after every cycle), Long breaks 15 minutes (come after 4 cycle). #All times can be edited

Run Pomodoro timer `python pomodoro.py -i`
commands include:

     pomodoro start <task-title> to create new task for the timer 
    eg.	`pomodoro create Utensils` 
     
     pomodoro config short_break to modify the default short break time 
     `pomodoro config short_break`


__To do List__
	Working on `pomodoro stop`
