from flask import jsonify
import requests

baseUrl="http://127.0.0.1:5000"

def send_get_request():
    url = baseUrl+"/user"
    resp = requests.get(url)
    print('Response Code:'+str(resp.status_code))
    print('Response:\n')
    print(resp.text)

def send_get_user_request(id):
    url = baseUrl+"/user/"+str(id)
    resp = requests.get(url)
    print('Response Code:'+str(resp.status_code))
    print('Response:\n')
    print(resp.text)

def send_post_request():
    url = baseUrl+"/user"
    content={'id':1,'name':'bob'}
    resp = requests.post(url,json=content)
    print('Response Code:'+str(resp.status_code))
    print('Response:\n')
    print(resp.text)

def send_put_request(id,name):
    url = baseUrl+"/user"
    content={'id':id,'name':name}
    resp = requests.put(url,json=content)
    print('Response Code:'+str(resp.status_code))
    print('Response:\n')
    print(resp.text)

def send_delete_request(id):
    url = baseUrl+"/user/"+str(id)
    resp = requests.delete(url)
    print('Response Code:'+str(resp.status_code))
    print('Response:\n')
    print(resp.text)


if __name__ == '__main__':
    print('\n\n######################')
    print('### REST API CLIENT###')
    print('######################\n\n')
    print('\n(1) Sending GET Request\n\n')
    send_get_request()

    print('\n\n(2) Sending POST Request to add user\n\n')
    send_post_request()

    print('\n\n(3) Sending GET Request for user id : 1\n\n')
    send_get_user_request(1)

    print('\n\n(4) Sending GET Request for user id : 2\n\n')
    send_get_user_request(2)

    print('\n\n(5) Sending UPDATE Request for user id : 1\n\n')
    send_put_request(1,'kevin')

    print('\n\n(6) Sending GET Request\n\n')
    send_get_request()

    print('\n\n(7) Sending DELETE Request for user id : 1\n\n')
    send_delete_request(1)

    print('\n\n{8) Sending GET Request\n\n')
    send_get_request()