# PythonCron
Contains the python script to setup cron job.

Download this file and pass the data which needs to be passed to crontab.

## How to add command to crontab

```sh
./setup_cron.py /home/nagaraj/work/my_script.sh "3 0 * * *"
```

The above value would ensure the script will add it in crontab as:
```0 3 * * * /home/nagaraj/work/my_script.sh```

To check the crontab where the value in ubuntu:
```sh
crontab -e
```

## Blog that explains the entire file
For more details, please view:
https://nagarajtantri.blogspot.in/2015/12/setting-up-simple-cron-job-using-python-script.html
