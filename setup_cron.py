#!/usr/bin/python2.7

import sys
import subprocess
import shlex
import os

# Checking the length of the argv provided by the user to esnure we do a cron expression 
# and a file/sript which needs to be executed for this script
if (len(sys.argv) != 3):
    print "The arguments needed are a absolute file path and a cron expression, for example ./setup_cron.py /home/user/some.sh \"3 0 * * *\" "
    exit(1)

EXECUTION_CMD = sys.argv[1]
CRON_EXPRESSION = sys.argv[2]

print "Command given to store in crontab is: ", str(CRON_EXPRESSION), str(EXECUTION_CMD)

# Ask whether the user is ok with the expression to be added under crontab
option = raw_input("Is the provided command valid and can be added to crontab (y/n) ?")
if (option == 'y'):
    print "Adding the expression to crontab"
else:
    print "Received option other than 'y', so terminating the script"
    exit(2)



# Store the system PATH as a key value in a string format
# So that the crontab knows the "python" lives in the PATH defined. 
PATH_VALUE = 'PATH={0}'.format(os.environ.get("PATH", ''))

# LD_LIBRARY_PATH is used by your program to search for directories containing the 
# libraries after it has been successfully compiled and linked.
LD_LIBRARY_PATH = "LD_LIBRARY_PATH={0}".format(os.environ.get("LD_LIBRARY_PATH")) if os.environ.get("LD_LIBRARY_PATH") else ''

# This value would be added to the crontab
CRON_VALUE = '{0} {1}'.format(CRON_EXPRESSION, EXECUTION_CMD)

print "The cron job to be created is: {0}.".format(CRON_VALUE)

# Provides a list of existing cron's if any
command_1 = 'crontab -l'
proc_1 = subprocess.Popen(shlex.split(command_1), stdout=subprocess.PIPE,  stderr=subprocess.PIPE)

# Below proc_1.communicate() gives tuple as:
# ('', 'no crontab for user11\n')                  -- In case there was never a crontab created
# ('', '')                                         -- In case there was a crontab created but has no entries
# ('0 3 * * * test.py\n', '')                      -- In case there was a crontab created with "0 3 * * * test.py" expression
# ('0 4 * * * test.py\n0 3 * * * script.py\n', '') -- In case there were multiple expressions are created
out, err = proc_1.communicate()

if out is not "":
    new_value = [item for item in out.split("\n") if item.strip() != "" and CRON_VALUE != item.strip() and 
                              not ("PATH" in item or "LD_LIBRARY_PATH" in item)]
    
    new_value.insert(0, LD_LIBRARY_PATH)  # First add the LD_LIBRARY_PATH ensuring its the second command after PATH
    new_value.insert(0, PATH_VALUE)
    new_value.append(CRON_VALUE)
    value = '\n'.join(new_value)
else:
    value = '{0}\n{1}\n{2}'.format(PATH_VALUE, LD_LIBRARY_PATH, CRON_VALUE)

# Option -e reads backslash and hence can add "\n" to crontab, making it a new line
command_2 = "echo -e '{0}'".format(value)

proc_2 = subprocess.Popen(shlex.split(command_2), stdout=subprocess.PIPE)

command_3 = 'crontab -'
# Notice the stdin for proc_3 is proc_2.stdout
proc_3 = subprocess.Popen(shlex.split(command_3), stdin=proc_2.stdout, stdout=subprocess.PIPE)

# proc_2 and proc_3 act like a pipe line as follows:
# echo -e '0 3 * * * check_status.py' | crontab -
# Now the above line echo's the data to crontab via pipe and reloads it.

out, error = proc_3.communicate()

proc_1.stdout.close()
proc_2.stdout.close()

if error != '':  # If there were errors, like: "-":1: bad minute
    sys.exit(error)

print 'Done, with crontab guys. Now relax :)'
