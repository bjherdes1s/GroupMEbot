#import requests


def func1():
  import requests
  headers = {
    'Content-Type': 'application/json',
  }

  params = (
    ('token', 'YOUR_TOKEN_HERE'),
  )

  data = '{"method":"passthrough", "params": {"deviceId": "YOUR_DEVICEID_HERE", "requestData": "{\\"system\\":{\\"set_relay_state\\":{\\"state\\":1}}}" }}'

  response = requests.post('https://use1-wap.tplinkcloud.com/', headers=headers, params=params, data=data)

func1()
