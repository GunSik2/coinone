
## Environment
I used ubuntu 16.04 (64bit), and all outbound and inbound ssh port are opened. 

## Quick Run
```
sudo service qtumd stop

sudo service qtumd start

qtum-cli -stdin walletpassphrase
> <password>
> 999999999
> false
> <CTRL-D>

qtum-cli getstakinginfo
qtum-cli getinfo
qtum-cli gettakinginfo
```
## Install & Test Qtumd 
I donwloaded the [qtum image](https://github.com/qtumproject/qtum/releases/download/mainnet-ignition-v1.0.2/qtum-0.14.3-x86_64-linux-gnu.tar.gz)
from the [qtum github release](https://github.com/qtumproject/qtum/releases/tag/mainnet-ignition-v1.0.2).
```
wget https://github.com/qtumproject/qtum/releases/download/mainnet-ignition-v1.0.2/qtum-0.14.3-x86_64-linux-gnu.tar.gz
tar xvzf qtum-0.14.3-x86_64-linux-gnu.tar.gz
ln -s qtum-0.14.3 qtum
```

Now check the installed qtum is working correctly.
```
$ ~/qtum/bin/qtumd -version
$ qtum-cli getinfo
$ qtum-cli listaccounts
$ qtum-cli getstakinginfo
$ qtum-cli getwalletinfo
```

## Run Qtumd as a Linux Service

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
Data and logs will be found at ~/.qtum/wallet.dat ~/.qtum/debug.log

## Encrpyt and Decrypt Wallet
Encrypt your wallet by running:
```
bin/qtum-cli -stdin encryptwallet
```
The -stdin parameter is used to (silently) prompt you for input. 
Once complete, the following message will be displayed:
```
wallet encrypted; Qtum server stopping, restart to run with encrypted wallet. The keypool has been flushed and a new HD seed was generated (if you are using HD). You need to make a new backup.
```

Restart it by running the following commands:
```
$ sudo systemctl stop qtumd.service
$ rm -f ~/.qtum/.lock ~/.qtum/qtumd.pid ~/.qtum/.cookie
$ sudo systemctl start qtumd.service
```

Now that your wallet is encrypted, run the following command to check encrytpion:
```
$ ~/qtum/bin/qtum-cli getwalletinfo
{
  "walletversion": 130000,
  "balance": 16182.49960000,
  "stake": 0.00000000,
  "unconfirmed_balance": 0.00000000,
  "immature_balance": 0.00000000,
  "txcount": 2,
  "keypoololdest": 1504758151,
  "keypoolsize": 101,
  "unlocked_until": 0,
  "paytxfee": 0.00000000,
  "hdmasterkeyid": "b69f65040dc722e473b9bce1dbd0cb34e424a577"
}
```
Notice the presence of the unlocked_until field with a value of 0. This tells us that the wallet is encrypted but it is locked. You cannot stake coins with a locked wallet.

To unlock your wallet for staking, run the following command:
```
$ ~/qtum/bin/qtum-cli -stdin walletpassphrase
```
This once again (silently) prompts you for input.  Type your secure passphrase, and press <Enter/Return>, then type the number of seconds that you'd like to keep your wallet unlocked, then <Enter/Return>, then 'true' (without the quotes), then <Enter/Return>, and finally CTRL-D. It will look like this:
```
reddogbluecat
99999999
false
<CTRL-D>
```

After unlocking your wallet, run the following command:
```
$ ~/qtum/bin/qtum-cli getinfo
```

If you want to re-lock your wallet, simply run:
```
$ ~/qtum/bin/qtum-cli walletlock
```


## Staking
You can see if your wallet is staking by running:
```
$ ~/qtum-wallet/bin/qtum-cli getstakinginfo
```

The command above should display something similar to:
```
{
  "enabled": true,
  "staking": true,
  "errors": "",
  "currentblocksize": 0,
  "currentblocktx": 0,
  "pooledtx": 0,
  "difficulty": 26753652.34834659,
  "search-interval": 0,
  "weight": 1618249960000,
  "netstakeweight": 7923365887385318,
  "expectedtime": 0
}
```
If the staking field is false, it means that you are not staking (e.g. your coins have not yet matured, etc).


## Reference
- https://steemit.com/qtum/@cryptominder/qtum-staking-tutorial-using-qtumd-on-a-raspberry-pi-3
- https://github.com/qtumproject/qtum/releases/tag/mainnet-ignition-v1.0.2
