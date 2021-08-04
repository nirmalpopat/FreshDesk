from rest_framework import serializers
import requests
import json

domain = 'newaccount1626356159108'
api_key = 'N6aUBPu73DK4AlOllTEK'
password = 'Np@11111'

r = requests.get("https://{0}.freshdesk.com/api/v2/tickets/".format(domain), auth = (api_key, password))

if r.status_code == 200:
    print ("Request processed successfully, the response is given below")
else:
    print ("Failed to read ticket, errors are displayed below")
response = json.loads(r.content.decode('utf-8'))

tickets = r.json()



class employeesSerializer(serializers.ModelSerializer):
    def get_ticket():
        return tickets
    class Meta:
        model = tickets
        #fields = ('firstname', 'lastname')
        fields = '__all__'