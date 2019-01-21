import requests
import json
import pandas as pd

def log(shit):
    print json.dumps(shit, indent=2)

headers = {"Accept" : "application/json"}

url = 'http://legis.senado.leg.br/dadosabertos/materia/pesquisa/lista?ano=2018'

response = json.loads(open("/tmp/yolo.json", "r").read())

try:
    #r = requests.get(url, headers=headers)
    pass
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc) 
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)


#log(r.json()['PesquisaBasicaMateria']['Materias']['Materia'][0])
for materia in response['PesquisaBasicaMateria']['Materias']['Materia']:
    s = pd.Series([materia['IdentificacaoMateria'], materia['DadosBasicosMateria'], materia['AutoresPrincipais'], materia['SituacaoAtual']])
    s.apply(pd.Series).stack()
#log(r.json())


#for mat in r.json().get('Materias', {}):
#    print(mat)