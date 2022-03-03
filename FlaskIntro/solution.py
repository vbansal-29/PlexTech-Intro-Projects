from flask import Flask, request
import json
    
app = Flask(__name__)

@app.route('/hello')
def index():
    if request.args.get('name') == None:
        return 'Web App with Python Flask!'
    else:
        return 'Hello ' + str(request.args.get('name'))


@app.route('/hello-html')
def html():
    return "<h1>Hello World</h1><p>Subtext</p>"

@app.route('/hello-html-error')
def htmlerror():
    return Flask.Response("<h1>Hello World</h1><p>Subtext</p>", status=200)

@app.route('/hello-json')
def dictionary():
    return {"text": "Hello World from Dictionary"}

@app.route('/hello/<name>')
def whatevername(name):
   return 'Hello ' + str(name)

@app.route('/hello/<name>/change/<change>')
def whatevernameChange(name, change):
    return 'Hello ' + str(name) + ', your change is ' + str(10 - int(change))

@app.route('/reflect')
def reflect():
    payload = str(request.data)
    return 'Hello ' + payload[2:len(payload)-1]

@app.route('/reflect/plex')
def reflectJson():
    payload = request.data
    plex = {}
    for key in payload.keys():
        if type(key) is str:
            newkey = "plex_" + key
        else:
            newkey = key
        if type(payload[key]) is str:
            newVal = "plex_" + payload[key] 
        else:
            newVal = payload[key]
        plex[newkey] = newVal 
    return json.dumps(plex)

@app.route('/reflect/plex/form')
def reflectJsonForm():
    payload = request.form
    plex = {}
    for key in payload.keys():
        newkey = "plex_" + key
        newVal = "plex_" + payload[key] 
        plex[newkey] = newVal
    return json.dumps(plex)

app.run(host='0.0.0.0', port=81)