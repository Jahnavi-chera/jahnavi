import wiotp.sdk.device
import time
import random
import requests

myConfig = { 
    "identity": {
        "orgId": "ffguea",
        "typeId": "Externship",
        "deviceId":"6789"
    },
    "auth": {
        "token": "123456789"
    }
}
location="17.8471,79.3972"
def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m=cmd.data['command']
    print()
    if(m=="lighton"):
        print("noise level is high at",location)
        

        url = "https://www.fast2sms.com/dev/bulkV2"

        querystring = {"authorization":"DfzsQUApZagbnwcBIvr7PN03YmLFx5T94J8kiV1HtuoEdhWjCKHUJxtFEPic6Y8LRVlpaXMbQevgOh1G","message":"noise level is incresed alert people","language":"english","route":"q","numbers":"7674889108"}

        headers = {
                    'cache-control': "no-cache"
                  }

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
                
    print()

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    height=random.randint(0,100)
    
    myData={'d':{'name':'Extenship','noisedetection':"noise","location":location}}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Published data Successfully: %s", myData)
    client.commandCallback = myCommandCallback
    time.sleep(2)
client.disconnect()
