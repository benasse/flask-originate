from flask import Flask
from flask import request
from subprocess import check_output

app = Flask('flask-originate')
ip_whitelist = ['172.17.16.10']
dest_context = 'maquette1-key8964-internal'
dest_exten = '1234'
src_context = 'xivo-callme'
src_exten = '777'

def authorized_ip():
  client = request.remote_addr
  if client in ip_whitelist:
    return True
  else:
    return False

def get_param(param):
  if request.args.get(param) is not None:
    param = request.args.get(param)
  else:
    param = eval(param)
  return param

def run_originate(dest_context,dest_exten,src_context,src_exten):
  stdout = check_output(['/usr/sbin/rasterisk -rx "channel originate Local/' + dest_exten + '@'
                         + dest_context + ' extension ' + src_exten + '@' + src_context + '"'],shell=True).decode('utf-8')
  return stdout

@app.route('/',methods=['GET',])
def main():

  if authorized_ip():
    dest_context = get_param('dest_context')
    dest_exten = get_param('dest_exten')
    src_exten = get_param('src_exten')
    src_context = get_param('src_context')
    return '<pre>' + run_originate(dest_context,dest_exten,src_context,src_exten) \
           + '</pre> dest_exten: ' + dest_exten + '<br> dest_context: ' + dest_context \
           + '<br> src_exten: ' + src_exten + '<br> src_context: ' + src_context

  else:
    return 'unauthorized'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8001)
