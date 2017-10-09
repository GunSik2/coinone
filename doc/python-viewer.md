## Objective
This guides the python program to enable you to check qtumd status on web brower.

## Prerequisites
- Python3 (usually installed by default on Ubuntu 14.04)
- virtualenv (sudo apt-get install python-virtualenv)

## prepare your virtual environment
```bash
# install virtualenv
sudo apt install virtualenv
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
```python
from flask  import Flask
from flask import request
import subprocess
import sys, traceback

app = Flask('flaskshell')

def get_status(command):
    try:
        commands = "qtum-cli '{0}'".format(command)
        result = subprocess.check_output(commands, shell=True)
    except subprocess.CalledProcessError as e:
        traceback.print_exc(file=sys.stdout)
        return "An error occurred while trying to execute task."
    result = "<br />".join(result.decode().split("\n"))
    return "<h2> %s </h2> <p/> %s" %(command, result)

@app.route('/')
def getroot():
    return """
<a href="/getinfo">getinfo</a><p/>
<a href="/getstakinginfo">getstakinginfo</a><p/>
<a href="/getwalletinfo">getwalletinfo</a><p/>
"""

@app.route('/getinfo')
def getinfo():
    return get_status("getinfo")

@app.route('/getstakinginfo')
def getstakinginfo():
    return get_status("getstakinginfo")

@app.route('/getwalletinfo')
def getwalletinfo():
    return get_status("getwalletinfo")

if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True, debug=True)
```

- flaskshell/src/test.py
```python
#!/usr/bin/python
import subprocess

p = subprocess.Popen("date")
#subprocess.call(["ping", "-c 3", "www.cyberciti.biz"])

subprocess.call(["../qtum/bin/qtum-cli", "getstakinginfo"])
subprocess.call(["../qtum/bin/qtum-cli", "getwalletinfo"])

result = subprocess.check_output("../../qtum/bin/qtum-cli getinfo", shell=True)
result = "<br />".join(result.decode().split("\n"))
print(result)
```

## Run the code
- Run as command
```
$ nohup bin/python src/app.py &
```

- Run as a service using supervisor
```
$ sudo apt install supervisor
$ sudo vi /etc/supervisor/conf.d/flaskshell.conf
[program:qtumpy] 
directory = /home/ubuntu/flaskshell/src
command = /home/ubuntu/flaskshell/bin/python app.py
redirect_stderr = true
stdout_logfile = /home/ubuntu/flaskshell/logs/out.log
stderr_logfile = /home/ubuntu/flaskshell/logs/error.log

$ sudo supervisorctl update qtumpy 
$ sudo supervisorctl start qtumpy
```

- Test the app
```
$ curl  -v http://127.0.0.1:5000
```


## Reference
- https://www.pluralsight.com/guides/python/running-shell-commands-with-flask
- https://www.cyberciti.biz/faq/python-execute-unix-linux-command-examples/
