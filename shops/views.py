from django.shortcuts import render
from .models import ShopProfile
from .forms import ShopProfileForm
from shoprequests.models import ShopRequest
from django.views.generic import CreateView, DetailView, UpdateView
from products.models import Product
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


class ShopProfileDetailView(LoginRequiredMixin,DetailView):
    login_url = '/accounts/login/'
    model = ShopProfile
    template_name='shops/shop_profile.html'

    def get_context_data(self,*args, **kwargs):
        context = super(ShopProfileDetailView, self).get_context_data(*args, **kwargs)
        user = context['shopprofile']
        context["products_count"] = Product.objects.filter(product_owner=user).count()
        context["products"] = Product.objects.filter(product_owner=user)
        context["shop"] = ShopRequest.objects.get(requested_user=self.request.user)
        return context
    


class ShopProfileUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/accounts/login/'
    model = ShopProfile
    form_class = ShopProfileForm
    template_name = 'shops/shop_profile_update.html'


    def get_context_data(self, *args, **kwargs):
        context = super(ShopProfileUpdateView, self).get_context_data(*args, **kwargs)
        update_form = ShopProfileForm(instance = self.request.user.shop_profile)
        context['shop']=ShopProfile.objects.get(shop_owner = self.request.user)
        context["shop_request"] = ShopRequest.objects.get(requested_user=self.request.user)
        context['form']=update_form
        return context
    

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #          messages.success(request,'Your Shop profile has updated.')
    #     return render(request, self.template_name, {'form': form})
        
    def form_valid(self, form):
        print("hey there")
            # shop_title = form.cleaned_data['title']
        form.save()
        messages.success(self.request,'Your Shop profile has updated.')
        return super().form_valid(form)
