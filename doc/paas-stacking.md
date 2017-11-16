
- Get qtum binary
```
wget https://github.com/qtumproject/qtum/releases/download/mainnet-ignition-v1.1.1/qtum-0.14.7-x86_64-linux-gnu.tar.g
tar xvzf qtum-0.14.7-x86_64-linux-gnu.tar.gz
cd qtum-0.14.7
```

- Create config file
```
$ vi manifest.yml
---
applications:
- name: tum
  memory: 128M
  health-check-type: none
  no-route: true
  command: bin/qtumd -daemon=1 -par=2 -onlynet=ipv4 -noonion -listenonion=0 -maxconnections=24 -rpcbind=127.0.0.1 -rpcallowip=127.0.0.1
  buildpack: binary_buildpack
```
- Run
```
$ cf push
```
