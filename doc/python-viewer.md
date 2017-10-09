## Objective
This guides the python program to enable you to check qtumd status on web brower.

## Prerequisites
- Python3 (usually installed by default on Ubuntu 14.04)
- virtualenv (sudo apt-get install python-virtualenv)

## prepare your virtual environment
```
# create a virtualenv using python3 
virtualenv -p /usr/bin/python3 flaskshell 
# enter the virtualenv directory and perform the basic package installations and tasks 
cd flaskshell 
# activate virtualenv 
source bin/activate 
# install flask 
pip install flask 
# create src and logs directory 
mkdir src logs
```

## The code
- flaskshell/src/app.py
```
from flask 
import Flask from flask 
import request 
import subprocess 

@app.route('/status/')
def get_status():
  try:
      command_success = "mysql -uflaskuser -pflask123 -e '{0}'".format(
        query_success)
      result_success = subprocess.check_output(
          [command_success], shell=True)
  except subprocess.CalledProcessError as e: 
      return "An error occurred while trying to fetch task status updates." 
  return 'Success %s, Pending %s, Failed %s'  % (result_success, result_pending, result_failed)

if __name__ == '__main__':
    app.run()  
```

## Reference
- https://www.pluralsight.com/guides/python/running-shell-commands-with-flask
