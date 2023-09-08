from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views import View
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
from account.forms import SignUpForm
from django.contrib import messages





def index(request):
    return render(request , "index.html")



# Sign Up View
# class SignUpView(SuccessMessageMixin,CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy('index')
#     template_name = 'signup.html'
    
class SignUp(View):
    def get(self,request):
        form =SignUpForm()
        return render(request , 'signup.html',locals())

    def post(self,request):
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Congratulations! User Register Successfull")
        
        else:
            messages.warning(request,"Invalid input Data")
        return render(request,'signup.html',locals())
