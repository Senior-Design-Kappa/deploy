from flask import Flask
from flask import request
import os

app = Flask(__name__)

path = '$GOPATH/src/github.com/Senior-Design-Kappa/'
repos = ['web-client', 'sync-server', 'web']

@app.route('/', methods=['POST'])
def index():
    repo = request.json['repository']
    if request.json['refs'] == 'refs/heads/master':
        repo_dir = path + repo['name']
        if repo['name'] not in repos:
            return
        os.system('kill `ps -ef | grep ' + repo['name'] + ' | awk "{print $2}"``') # terminate process
        os.system('rm -rf ' + repo_dir) # delete the repo
        os.system('git clone ' + repo['clone_url']) # clone it

        if repo['name'] == 'web-client':
            os.system('npm install') # install dependencies
        os.chdir(path + 'web-client')
        os.system('make build-' + repo['name'])
        os.system('zsh run.sh')
    return

if __name__ == '__main__':
    app.run(host='159.203.88.91', port='5000')
