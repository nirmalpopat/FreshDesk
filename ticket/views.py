from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from . serializers import employeesSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
import ast
import json


domain = 'newaccount1626356159108'
api_key = 'N6aUBPu73DK4AlOllTEK'
password = 'Np@11111'
headers = { 'Content-Type' : 'application/json' }
# Create your views here.

class UpdateTicket(ListAPIView):    
    def put(self, request, id):
        ticket_id = str(id)
        ticket = {
            "subject" : "Refund 5000",
            "description" : "Updated description Python 3.5.2",
            "priority" : 3,
            }
        ticket = self.request.data
        
        r = requests.put("https://{0}.freshdesk.com/api/v2/tickets/{1}".format(domain, ticket_id), auth = (api_key, password), headers = headers, data = json.dumps(ticket))

        if r.status_code == 200:
            print ("Ticket updated successfully, the response is given below")
        else:
            print ("Failed to update ticket, errors are displayed below")

        response = json.loads(r.content.decode('utf-8'))

        t = r.json()
        return JsonResponse(r.json())

def filterTicket(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        print(query)
        r = requests.get("https://" + domain + ".freshdesk.com/api/v2/search/tickets?query="+query, auth = (api_key, password))
        if r.status_code == 200:
            #print ("Ticket deleted successfully")
            print ("Request processed successfully, the response is given below")
            res = {
                "success": True,
                "message": "Ticket Updated",
                
            }
            #return JsonResponse(res)
        else:
            print ("Failed to delete ticket, errors are displayed below")
            #return JsonResponse(r.json())
        response = json.loads(r.content.decode('utf-8'))

        tickets = r.json()
        return JsonResponse(tickets)
    else:
        res = {
            "success": False,
            "message": "Ticket not Updated",
            "errors" : "You are not using delete method"
        }
    #print(res)
        return JsonResponse(res)
def deleteTikcet(request, id):
    if request.method == 'DELETE':
        ticket_id = id
        r = requests.delete("https://{0}.freshdesk.com/api/v2/tickets/{1}".format(domain, ticket_id), auth = (api_key, password))

        if r.status_code == 204:
            print ("Ticket deleted successfully")
            res = {
                "success": True,
                "message": "Ticket Deleted",
                
            }
            return JsonResponse(res)
        else:
            print ("Failed to delete ticket, errors are displayed below")
            return JsonResponse(r.json())
    else:
        res = {
            "success": False,
            "message": "Ticket not Created",
            "errors" : "You are not using delete method"
        }
    #print(res)
        return JsonResponse(res)

class DeleteMultipleTikcets(ListAPIView):

    def post(self, request):
        data = self.request.data
        print("received data : ",data)
        
        ticket_ids = data
        r = requests.post("https://{0}.freshdesk.com/api/v2/tickets/bulk_delete".format(domain),headers = headers, auth = (api_key, password), data = json.dumps(ticket_ids))

        if r.status_code == 202:
            print ("Tickets deleted successfully, the response is given below")
        else:
            print(r.status_code)
            print ("Failed to delete ticket, errors are displayed below")
        response = json.loads(r.content.decode('utf-8'))
        
        return Response(
           response
        )

class CreateTikcet(ListAPIView):
    def post(self, request):
        ticket = self.request.data
        
        r = requests.post("https://{0}.freshdesk.com/api/v2/tickets".format(domain), auth = (api_key, password), headers = headers, data = json.dumps(ticket))

        if r.status_code == 201:
            print ("Ticket created successfully, the response is given below")
        else:
            print ("Failed to create ticket, errors are displayed below")
        response = json.loads(r.content.decode('utf-8'))

        t = r.json()
        print(r.json())
        return JsonResponse(r.json())
        ticket = {
            "subject" : request.POST.get('subject'),
            "description" : request.POST.get('description'),
            "email" : request.POST.get('email'),
            "priority" : int(request.POST.get('priority')),
            "status" : int(request.POST.get('status')),
        }
        r = requests.post("https://{0}.freshdesk.com/api/v2/tickets".format(domain), auth = (api_key, password), headers = headers, data = json.dumps(ticket))

        if r.status_code == 201:
            print ("Ticket created successfully, the response is given below")
        else:
            print ("Failed to create ticket, errors are displayed below")
        response = json.loads(r.content.decode('utf-8'))

        t = r.json()
        
        print(r.json())
        return JsonResponse(r.json())
        res = {
            "success": True,
            "message": "Ticket Created"
        }
        #print(request, '     njk')
        #print(request.POST['name'])
 

def view_tickets(request):
    r = requests.get("https://{0}.freshdesk.com/api/v2/tickets/".format(domain), auth = (api_key, password))

    if r.status_code == 200:
        print ("Request processed successfully, the response is given below")
    else:
        print ("Failed to read ticket, errors are displayed below")
    response = json.loads(r.content.decode('utf-8'))

    tickets = r.json()
    return HttpResponse(tickets)
    return JsonResponse(tickets)