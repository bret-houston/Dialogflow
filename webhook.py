import json
import os
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))
    res = makeResponse(req)
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r 
    
def makeResponse(req):
    return { "fulfillmentMessages": [ { "text": { "text": [ "This is my webhook response" ] }, "speech": { "speech" [ "This is my webhook response" ] } } ] }
#   result = req.get("result")
#   r=requests.get('https://us3.uscubed.com/GoogleWebhook.aspx')
#   json_object = r.json()
#   weather=json_object['fulfillmentMessages']
#   condition=weather[0]['text']['text'][0]
#   speech = "My response is " + condition    
#    return {"fulfillmentMessages": [{ "text": {	"text": [ "This is my webhook response"	] }}  ]	}    
#   result = req.get("result")
#   r=requests.get('https://us3.uscubed.com/GoogleWebhook.aspx')
#   json_object = r.json()
#   weather=json_object['fulfillmentMessages']
#   condition=weather[0]['text']['text'][0]
#   speech = "My response is " + condition

    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')
