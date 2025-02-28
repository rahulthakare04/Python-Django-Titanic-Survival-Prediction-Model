from django.shortcuts import render
import joblib


model = joblib.load('webMLModel/SurvivalPrediction-model.joblib')

 


# result=model.predict([[3,0,69,0,0,10000],[1,1,26,1,1,60000]])
# print(result)



def home(request):
    return render(request,"home.html")

def predict(request):
   
    dic={}
    if request.method=="POST":
        pclass=int(request.POST.get("pclass"))
        gender=int(request.POST.get("gender"))
        age=int(request.POST.get("age"))
        sibsp=int(request.POST.get("sibsp"))
        parch=int(request.POST.get("parch"))
        fare=int(request.POST.get("fare"))

        result=model.predict([[pclass,gender,age,sibsp,parch,fare]])
        if result[0]==1:
            dic["status"]="Passenger Survived"
            return render(request,"servive.html")
        else:
            return render(request,'notservive.html')
            dic["status"]="Passenger Did NOT Survive"
  
            




        

