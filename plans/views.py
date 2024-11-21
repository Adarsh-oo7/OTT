from django.shortcuts import render

# Create your views here.


def plans(request):
    return render(request,'subscription/plans.html')





def view_plan(request):
    return render(request,'subscription/viewPlan.html')



def create_plan(request):
    return render(request,'subscription/createPlan.html')