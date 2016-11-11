# PythonCron
Contains the python script to setup cron job.

Download this file and edit the data that you would want to add to your crontab.

## How to add command to crontab

Just update the file you would want to run via the crontab, in this case (```check_status.py```)
```python
STARTUP_FILE = os.path.join(CURRENT_FILE_DIR, "check_status.py")
```

Add the execution command, since here I was testing the execution of a python file on some interval of time, I added the command ```EXECUTION_CMD```
```python
# COMMAND to execute
EXECUTION_CMD = 'python {0}'.format(STARTUP_FILE)
```

Change the Cron value to add (in this case ```0 3 * * *```):
```python
# CRON value to add (at 3 in the morning).
CRON_VALUE = '{0} {1}'.format("0 3 * * *", EXECUTION_CMD)
```

Run this script as following:
```sh
$ python setup_cron.py
```

To check the crontab where the value ```0 3 * * * python /<path-to-the-file>/check_status.py``` in ubuntu:
```sh
crontab -e
```

## Blog that explains the entire file
For more details, please view:
https://nagarajtantri.blogspot.in/2015/12/setting-up-simple-cron-job-using-python-script.html
