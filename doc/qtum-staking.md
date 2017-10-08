
## Environment
I used ubuntu 16.04 (64bit), and all outbound and inbound ssh port are opened. 

## Install & Run Qtum 
I donwloaded the [qtum image](https://github.com/qtumproject/qtum/releases/download/mainnet-ignition-v1.0.2/qtum-0.14.3-x86_64-linux-gnu.tar.gz)
from the [qtum github release](https://github.com/qtumproject/qtum/releases/tag/mainnet-ignition-v1.0.2).
```
wget https://github.com/qtumproject/qtum/releases/download/mainnet-ignition-v1.0.2/qtum-0.14.3-x86_64-linux-gnu.tar.gz
tar xvzf qtum-0.14.3-x86_64-linux-gnu.tar.gz
ln -s qtum-0.14.3 qtum
```
Now check the installed qtum is working correctly.
```
qtum/bin/qtumd -version
```
We'll now set up a systemd service to register automatically the qtumd as a linux service.
```
$ cat /etc/systemd/system/qtumd.service
[Unit]
Description=Qtum daemon service
After=network.target

[Service]
Type=forking
User=ubuntu
WorkingDirectory=/home/ubuntu/qtum
ExecStart=/home/ubuntu/qtum/bin/qtumd -daemon=1 -par=2 -onlynet=ipv4 -noonion -listenonion=0 -maxconnections=24 -rpcbind=127.0.0.1 -rpcallowip=127.0.0.1
PIDFile=/home/ubuntu/.qtum/qtumd.pid
Restart=always
RestartSec=1
KillSignal=SIGQUIT
KillMode=mixed

[Install]
WantedBy=multi-user.target
```

To start qtum service, simply run:
```
sudo systemctl start qtumd.service
```

If you make modifications to qtumd.service, make sure that you run the following command before starting or stopping the serivce.
```
sudo systemctl daemon-reload
```

To check the status of the qtumd, run:
```
qtum/bin/qtum-cli getinfo
```

## Debugging
Data and logs will be found at ~/.qtum/qtum.dat ~/.qtum/debug.log


## Reference
- https://steemit.com/qtum/@cryptominder/qtum-staking-tutorial-using-qtumd-on-a-raspberry-pi-3
- https://github.com/qtumproject/qtum/releases/tag/mainnet-ignition-v1.0.2
