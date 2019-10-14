from django.shortcuts import render, redirect
from django.contrib import messages
from .models import customerDataBase
from datetime import datetime
import json


def index(request):
    if request.method == 'POST':
        # storing in database
        number = request.POST['number_val']
        if customerDataBase.objects.filter(Number=number).exists():
            values = customerDataBase.objects.get(Number=number)
            print(values)
            present_date = datetime.now()
            if values.Date.month == present_date.month:
                values.Monthy_visit = values.Monthy_visit + 1
            else:
                values.Monthy_visit = 1
            values.Visits = values.Visits + 1
            values.save()
            messages.info(request, 'post updated')
            return render(request, 'base.html')
        else:
            num_creation = customerDataBase.objects.create(
                Number=number, Monthy_visit=0, Visits=0)
            num_creation.save()
            messages.info(request, 'post created')
            return redirect('https://api.whatsapp.com/send?phone=91'+number+'&text=whatsapp%20buddy&source=&data=')
    else:
        print("date time")
        return render(request, 'base.html')

# Create your views here.
