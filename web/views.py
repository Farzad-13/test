from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from json import JSONEncoder
from web.models import Expense, Income, Token, User
from datetime import datetime
# Create your views here.

@csrf_exempt
def submit_income(request):
    """user submit an income"""

    #TODO token mey not valid
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']

    Income.objects.create(
        text=request.POST['text'],
        amount=request.POST['amount'], 
        user=this_user, 
        date=date, 
    )

    return JsonResponse({
        'status':'ok',
    },encoder=JSONEncoder)


@csrf_exempt
def submit_expense(request):
    """user submit an expense"""

    #TODO token mey not valid
    this_token = request.POST['token']
    this_user = User.objects.filter(token__token = this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()
    else:
        date = request.POST['date']

    Expense.objects.create(
        text=request.POST['text'],
        amount=request.POST['amount'], 
        user=this_user, 
        date=date, 
    )

    return JsonResponse({
        'status':'ok',
    },encoder=JSONEncoder)