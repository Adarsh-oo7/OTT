from django.shortcuts import render

# Create your views here.

def revenue_generated(request):
    return render(request,'reports/revenueGenerated.html')