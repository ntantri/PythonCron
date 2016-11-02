# PythonCron
Contains the python script to setup cron job.

Cron is a system daemon which is used to execute desrired tasks (in the background) at specific designated time.
It is used to schedule jobs (commands or shell scripts) to run periodically at fixed times, dates, or intervals. It typically automates system maintenance or administration

Now, thinking of cron, it's a name we use, when we have to schedule a task. Now, I am referring to a linux machine with Ubuntu flavor (Pretty much would be same across for other linux distributions).
Crontab is a cron file which can be used to express jobs or tasks in the form of scripts to be executed.

Checkout man cron and man 5 crontab. You would find loads of information about the same.

Crontab Sections
Each of the sections is separated by a space, with the final section having one or more spaces in it.
No spaces are allowed within Sections 1-5, only between them.
Sections 1-5 are used to indicate when and how often you want the task to be executed.
This is how a cron job is laid out: minute (0-59), hour (0-23, 0 = midnight), day (1-31), month (1-12), weekday (0-6, 0 = Sunday)

Learn more from: https://help.ubuntu.com/community/CronHowto

Just to know: LD_LIBRARY_PATH is used by your program to search for directories containing the libraries after it has been successfully compiled and linked.
Like a library required for your program.
In my case, cx_Orcle needed the oracle libraies installed.
When we see a system crontab, the PATH and LD_LIBRARY_PATH are automatically present.
In case of user crontab, we might have to provide the linkages.

For more details, please view:
http://nagarajtantri.blogspot.in/2015/12/setting-up-simple-cron-job-via-python.html
