from django.shortcuts import render, redirect
from django.http import HttpResponse
from requests.auth import HTTPBasicAuth
import requests, json

CLIENT_ID = "AdErqRJaiObjrthmX04Fc4ixS7o0p7Sy87jhsjugF5Lr1nLmwVaIoMpLocmahRkR3h_IJxm9h7PcIxGl"
CLIENT_SECRET = "ELsaUJkx3xsYTfEvwaUTfq9PQaGyVkMRnbJgalSzwCQsVRgVbtsMOfOnteEnD14l4OZjVXvbS9DMeEPX"
API_SANDBOX = "https://api-m.sandbox.paypal.com"
PORT = "http://127.0.0.1:8000/"

access_token_headers = {"Content-Type": "application/x-www-form-urlencoded"}
params = {"grant_type": "client_credentials"}
access_token = requests.post(
        url=f"{API_SANDBOX}/v1/oauth2/token",
        headers=access_token_headers,
        params=params,
        auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET),
)


# Create your views here.
def home(request):
    return render(request, "index.html")


def create_order(request):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token.json()['access_token']}",
    }

    print(request.POST.getlist("item"))

    length = len(request.POST.getlist("item"))


    # items2 = {"name": "item2", "quantity": "3", "unit_amount": {"currency_code": "USD", "value": "15.64"}}
    # items3 = {"name": "item3", "quantity": "6", "unit_amount": {"currency_code": "USD", "value": "25.50"}}

    # total_items2 = float(items2["unit_amount"]["value"]) * int(items2["quantity"])
    # total_items3 = float(items3["unit_amount"]["value"]) * int(items3["quantity"])

    # total = str(round(total_items2 + total_items3, 2))

    url = f'https://mindicador.cl/api/dolar'
    response = requests.get(url)
    print(response.json()["serie"][0]["valor"])
    dolar_value = response.json()["serie"][0]["valor"]
    # print("Dolares: ", round(int(18633.55) / response.json()["serie"][0]["valor"], 2))
    
    total = 0
    for i in range(0, length):
        # Convertir a dolares.
        print(request.POST.getlist("cantidad")[i], request.POST.getlist("precio")[i])
        total += int(request.POST.getlist("cantidad")[i]) * round(int(request.POST.getlist("precio")[i]) / dolar_value, 2)

    total_dolar = round(total / dolar_value, 1)
    print(total, total_dolar)
    data = {
        "intent": "CAPTURE",
        "purchase_units": [{"amount": {"currency_code": "USD", "value": str(total), "breakdown": {"item_total": {"currency_code": "USD", "value": str(total)}}}, "items": []}],
        "payment_source": {
            "paypal": {
                "experience_context": {
                    "brand_name": "Donde xhe karlos",
                    "landing_page": "NO_PREFERENCE",
                    "user_action": "PAY_NOW",
                    "locale": "es-CL",
                    "return_url": f"{PORT}capture-order",
                    "cancel_url": f"{PORT}cancel-order",
                }
            }
        },
    }
    # Convertir el campo "value" a dolares.
    for i in range(0, length):
        item = {"name": request.POST.getlist("item")[i], "quantity": request.POST.getlist("cantidad")[i], "unit_amount": {"currency_code": "USD", "value": round(int(request.POST.getlist("precio")[i]) / dolar_value, 2)}}
        data["purchase_units"][0]["items"].append(item)  

    # data["purchase_units"][0]["items"].append(items2)
    # data["purchase_units"][0]["items"].append(items3)
    # print(total)
    #"value": str(round((int(request.POST.getlist("precio")[i]) * int(request.POST.getlist("cantidad")[i])) / response.json()["serie"][0]["valor"], 2))
    print(data)
    response = requests.post(
        url=f"{API_SANDBOX}/v2/checkout/orders",
        headers=headers,
        data=json.dumps(data),
    )
    print(response.status_code)
    print(response.json())

    return redirect(response.json()["links"][1]["href"])
    # return HttpResponse("Guardado")


def capture_order(request):

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token.json()['access_token']}",
    }

    token = request.GET.get("token")

    response = requests.post(
        url=f"{API_SANDBOX}/v2/checkout/orders/{token}/capture", headers=headers
    )
    print(response.status_code)
    print(response.json())
    print("Order payed succesfully!")

    return redirect("/")


def cancel_order(request):
    return redirect("/")
