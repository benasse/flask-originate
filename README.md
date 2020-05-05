# flask-originate
originate asterisk call throught http

# Status
This project is discontinued use [potoo](https://github.com/benasse/potoo) instead

# install
```
git clone https://github.com/benasse/flask-originate.git
cd flask-originate
cp flask-originate.service /lib/systemd/system/
mkdir -p /usr/local/bin/flask-originate
cp app.py /usr/local/bin/flask-originate
systemctl daemon-reload
systemctl enable flask-originate.service
systemctl start flask-originate.service
```
# default config
```
ip_whitelist = ['172.17.16.10']
dest_context = 'maquette1-key8964-internal'
dest_exten = '1234'
src_context = 'xivo-callme'
src_exten = '777'
```
# examples
```
wget http://10.0.0.1:8001/?dest_exten=0606060606&dest_context=default&src_exten=777&src_context=xivo-callme
wget http://10.0.0.1:8001/?dest_exten=0606060606
```
# uninstall
```
systemctl stop flask-originate.service
systemctl disable flask-originate.service
rm /lib/systemd/system/flask-originate.service
systemctl daemon-reload
rm -Rf /usr/local/bin/flask-originate
```
