from django.shortcuts import render,redirect
from django.views import generic
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
import stripe
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.contrib.auth import logout

# Create your views here.

class index(generic.TemplateView):
    template_name = 'index.html'

class manage_reg(generic.CreateView):
    template_name = 'manager_reg.html'
    model=User
    form_class = ManagerForm
    def form_valid(self, form):
        user=form.save(commit=False)
        password=form.cleaned_data['password']
        user.set_password(password)
        user.save()
        phone=form.cleaned_data['phone']
        Register_Manger.objects.create(user=user,phone=phone)
        return super().form_valid(form)


class manger_log(generic.View):
    template_name = 'manager_log.html'
    form_class = AuthenticationForm
    model=User
    success_url = reverse_lazy('view')
    def get(self,request):
        form=AuthenticationForm
        return render(request,'manager_log.html',{'form':form})
    def post(self,request):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            password=form.cleaned_data['password']
            username=form.cleaned_data['username']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('view')
        return HttpResponse('invalid credentials')
class manager_view(generic.ListView):
    template_name = 'manager_view.html'
    model =  Register_Manger
    context_object_name = 'data'
    def get_object(self):
        user=self.request.user
        return get_object_or_404(User,user)
def manager_resort_update(request):
    objects = Resort_packs.objects.all()
    return render(request,'resortUp.html',{'objects':objects})


class Manager_prof_update(generic.UpdateView):
    template_name = 'managerprofile.html'
    model = User
    form_class = EditManager_Form
    context_object_name = 'data'
    success_url = reverse_lazy('view')
    def get_object(self, queryset=None):
        user = super().get_object(queryset)
        self.Register_Manger_instance = Register_Manger.objects.get(user=user)
        return user
    def get_form(self,form_class=None):
        form=super().get_form(form_class)
        form.fields['phone'].initial=self.Register_Manger_instance.phone
        return form
    def form_valid(self, form):
        response=super().form_valid(form)
        self.Register_Manger_instance.phone=form.cleaned_data['phone']
        self.Register_Manger_instance.save()
        return response

class managerdelete(generic.DeleteView):
    template_name = 'delete.html'
    form_class = ManagerForm
    model = Register_Manger
    
class adv(generic.TemplateView):
    template_name = 'adv.html'


class user_reg(generic.CreateView):
    form_class = GuestForm
    model = Reg_guest
    template_name = 'guest_reg.html'
    def form_valid(self, form):
        if form.is_valid():
            user=form.save(commit=False)
            password=form.cleaned_data['password']
            user.save()
            phone=form.cleaned_data['phone']
            fullname=form.cleaned_data['fullname']
            email=form.cleaned_data['email']
            adress=form.cleaned_data['Adress']
            cpassword=form.cleaned_data['cpassword']
            if password==cpassword:
                Reg_guest.objects.create(phone=phone,email=email,Adress=adress,fullname=fullname,password=password)
            return HttpResponse('success')

class user_log(generic.View):
    form_class = login_userForm
    template_name = 'guset_log.html'
    model = Reg_guest
    # success_url = reverse_lazy('resortv')
    
    def get(self,request):
        form = login_userForm
        return render(request,'guest_log.html',{'form':form})
    def post(self,request):
        if request.method=='POST':
            password=request.POST.get('password')
            email=request.POST.get('email')
            data=Reg_guest.objects.all()
            for i in data:
                if i.email==email and i.password==password:
                    request.session['userid']=i.id
                    return redirect(resort_view)
        return HttpResponse('invalid credentials')

class user_view(generic.ListView):
    model = Reg_guest
    context_object_name = 'data'
    template_name = 'guest_view.html'



def re_pack(request):
    if request.method=='POST':
        form = ResortForm(request.POST,request.FILES)
        if form.is_valid():
            package = form.save()
            form.save()

            Resort_packs.objects.create(
            price=package.price,
            select_pack=package.select_pack,
            no_of_rooms=package.no_of_rooms,
            details = package.details,
            img=package.img

        )

    else:
        form=ResortForm()
    return render(request,"resort.html",{"form":form})


# class create_resort(generic.CreateView):
#     form_class = ResortForm
#     template_name = "create_resort.html"
#     model = Resort_packs
def resort_view(request):
    data=Resort_packs.objects.all()
    return render(request,"resort_view.html",{'data':data})

def detailview(request,id):
    data=Resort_packs.objects.get(id=id)
    return render(request,'resort_det.html',{"data":data})

class reupdate(generic.UpdateView):
    model = Resort_packs
    fields = ['select_pack','price','details','no_of_rooms','img']
    template_name = 'reup.html'
    success_url = reverse_lazy('resortupv')

def book(request,id):
    package=Resort_packs.objects.get(id=id)
    pack=package.select_pack
    user_id=request.session['userid']

    if not user_id:
        return HttpResponse('you are not logged in')
    Resort_pack=Booking.objects.filter(user_id=user_id,resort=package)
    

    if not Resort_pack.exists():
        book=Booking.objects.create(
            user_id=user_id,
            resort=package,
        )
        return redirect(create_order)


    else:
        return HttpResponse('already booked')

    return render(request,'summary.html')


def create_order(request):
    
    user_id=request.session['userid']
    # key = settings.STRIPE_PUBLISHABLE_KEY
    Resort_pack=Booking.objects.filter(user_id=user_id)
    for i in Resort_pack:
        username=i.user.fullname
        payment=i.resort.price
        pay=i.resort.price*100
    if Resort_pack.exists():
        key = settings.STRIPE_PUBLISHABLE_KEY
    # if user_id:

        # data=Booking.objects.get(id=user_id)
    return render(request,'order.html',{'price':payment,'key':key,'name':username,'pay':pay})
def order_get(request):
    user_id=request.session['userid']
    if user_id:
        return HttpResponse('payment succesful')
    return render(request,'getorder.html')
def Orders(request):
    data=Booking.objects.all()
    return render(request,'data.html',{'data':data})

def dele(request,id):
    data=Booking.objects.get(id=id)
    data.delete()
    return redirect(Orders)
 


def adminview(request):
    return render(request,'admin.html')

def user_logout(request):
    request.session.flush()
    return redirect('index')

    























        






