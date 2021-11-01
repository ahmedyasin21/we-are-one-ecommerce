from django.shortcuts import render,redirect
from .models import ShopRequest
from .forms import ShopRequestForm
from django.views.generic import CreateView, DetailView, UpdateView
from django.db.models.signals import post_save
from profiles.models import UserProfile
from django.dispatch import receiver
from shops.models import ShopProfile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ShopRequestCreateView(LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    model = ShopRequest
    form_class= ShopRequestForm
    template_name = "shoprequests/request_form.html"

    def get(self,request,*args, **kwargs):
        
        try:
            requested_form = ShopRequest.objects.get(requested_user=self.request.user)
        except ShopRequest.DoesNotExist:
            requested_form = None
        
        if requested_form is not None:
            print('requested form request_approve',requested_form.request_approve)
            if requested_form.request_approve == 'Approved': #Check if approved 
                print('im inside',requested_form.request_approve)
                try:
                    have_shop = ShopProfile.objects.get(shop_owner=self.request.user) #Check user has a shop
                    print('its got',have_shop)
                except ShopProfile.DoesNotExist:
                    have_shop = None
                    print('its none')
                
                if have_shop is not None: #if he does have a shop then we will sure that
                    sure_shop = ShopProfile.objects.get(shop_owner=self.request.user)
                    print('he has a shop')
                    try:
                        sure_shop = ShopProfile.objects.get(shop_owner=self.request.user)
                        print('his sure shop',sure_shop)
                    except ShopProfile.DoesNotExist:
                        sure_shop = None
                        print('i dont have shop')
                    if sure_shop is not None:
                        print('assigning him a staff person')
                        user = User.objects.get(username=self.request.user.username)
                        user.is_staff = True 
                        user.save()
                        return redirect('shops:shop_profile', slug=sure_shop.slug) 
                else:
                    shop = ShopProfile.objects.create(shop_owner=self.request.user,title=requested_form.shop_title, shop_address=requested_form.shop_address,shop_category=requested_form.shop_category)
                    return redirect('shoprequests:shop_form_detail',pk=requested_form.pk)
            elif requested_form.request_approve == 'Cancel': #Check if approved Check if not approved then form detail view
                requested_form.delete()
                print("i'm here")
                messages.warning(request, 'Your request has been denied')
                return redirect('shoprequests:shop_request') 
            else:
                return redirect('shoprequests:shop_form_detail',pk=requested_form.pk)
            
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try :
            shop = ShopRequest.objects.get(requested_user=self.request.user)
        except ShopRequest.DoesNotExist:
             shop = False
        
        print(shop,"shopong")
        context["shop"] = shop
        return context

            

    def form_valid(self, form):
        shop_request = form.save(commit=False)
        shop_request.requested_user = self.request.user 
        shop_request.save()
        user = self.request.user
        # print("coming  user from kyc view",user)
        try :
            user_profile = UserProfile.objects.get(user=user)
            # print("coming from kyc view",user_profile)
        except UserProfile.DoesNotExist:
            user_profile = None
            # print("coming  user_profile from kyc view",user_profile)
        

        age = form.cleaned_data['age']
        # print("coming age from kyc view",age)
        first_name = form.cleaned_data['first_name']
        # print("coming first_name from kyc view",first_name)
        last_name = form.cleaned_data['last_name']
        # print("coming last_name from kyc view",last_name)
        gender = form.cleaned_data['gender']
        # print("coming gender from kyc view",gender)
        country = form.cleaned_data['country']
        # print("coming country from kyc view",country)
        street_address = form.cleaned_data['street_address']
        # print("coming street_address from kyc view",street_address)
        city = form.cleaned_data['city']
        # print("coming city from kyc view",city)
        state = form.cleaned_data['state']
        # print("coming state from kyc view",state)
        zip_code = form.cleaned_data['zip_code']
        # print("coming zip_code from kyc view",zip_code)
        nationality = form.cleaned_data['nationality']
        # print("coming nationality from kyc view",nationality)



        if not user_profile.age:
            print('im im im im im view from kyc')
            user_profile.age = age
            user_profile.save()
        # print("coming user_profile.age from kyc view",user_profile.age)
        if not user_profile.first_name:
            user_profile.first_name = first_name
            user_profile.save()
        # print("coming user_profile.first_name from kyc view",user_profile.first_name)
        if not user_profile.last_name:
            user_profile.last_name = last_name
            user_profile.save()
        # print("coming user_profile.last_name from kyc view",user_profile.last_name)
        if not user_profile.country:    
            user_profile.country = country
            user_profile.save()
        # print("coming user_profile.country from kyc view",user_profile.country)
        if not user_profile.gender:
            user_profile.gender = gender
            user_profile.save()
        # print("coming user_profile.country from kyc view",user_profile.gender)
        if not user_profile.street_address:
            user_profile.street_address = street_address
            user_profile.save()
        # print("coming user_profile.street_address from kyc view",user_profile.street_address)
        if not user_profile.city:
            user_profile.city = city
            user_profile.save()
        # print("coming user_profile.city from kyc view",user_profile.city)
        if not user_profile.state:
            user_profile.state = state
            user_profile.save()
        # print("coming user_profile.state from kyc view",user_profile.state)
        if not user_profile.zip_code:
            user_profile.zip_code = zip_code
            user_profile.save()
        if not user_profile.nationality:
            user_profile.nationality = nationality
            user_profile.save()
        
        # print("coming user_profile.zip_code from kyc view",user_profile.zip_code)
        # print("coming user_profile.card from kyc view",user_profile.card)
        return super().form_valid(form)



class ShopRequestDetailView(LoginRequiredMixin,DetailView):
    login_url = '/accounts/login/'
    model = ShopRequest
    context_object_name = 'shop_requests'
    template_name = "shoprequests/form_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try :
            shop = ShopRequest.objects.get(requested_user=self.request.user)
        except ShopRequest.DoesNotExist:
             shop = False
        
        print(shop,"shopong")

        context["shop"] = shop
        return context



class ShopRequestUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login/'
    model = ShopRequest
    form_class= ShopRequestForm
    template_name = "shoprequests/request_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try :
            shop = ShopRequest.objects.get(requested_user=self.request.user)
        except ShopRequest.DoesNotExist:
             shop = False
        print(shop,"shopong")

        context["shop"] = shop
        return context