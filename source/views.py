from django.views.generic import TemplateView
from django.shortcuts import redirect,render
from products.models import Product
from categories.models import PostCategory
from shops.models import ShopProfile
from shoprequests.models import ShopRequest
from accounts.forms import CustomLoginForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class TestView(LoginRequiredMixin,TemplateView):
    login_url = '/accounts/login/'
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()

        try :
            shop = ShopRequest.objects.get(requested_user=self.request.user)
        except ShopRequest.DoesNotExist:
             shop = False
        
        print(shop,"shopong")

        context["shop"] = shop
        return context
        
class HomeView(TemplateView,LoginView):
    template_name = "landing_page/index.html"
    authentication_form = CustomLoginForm
    # def post(self,request,*args, **kwargs):
    #     print('I may hit just now')
    #     return render(request,template_name='dashboard.html')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["login_form"] = CustomLoginForm()
        context["products"] = Product.objects.all().order_by('-create_date')[:10]
        context["best_shops_products"] = Product.objects.filter(discount_price__isnull=False).distinct().order_by('-create_date')[:6]
        context["cloths_shops_products"] = Product.objects.filter(category__name__contains='Cloth').distinct().order_by('-create_date')[:6]
        # context["catagories"] = Category.objects.all().order_by('-create_date')[:4]
        # context["electronic"] = Products.objects.filter(cata=True).order_by('-create_date')[:4]
        

        return context

class AboutView(TemplateView,LoginView):
    template_name = "landing_page/about.html"
    authentication_form = CustomLoginForm

class ContactView(TemplateView,LoginView):
    template_name = "landing_page/contact.html"
    authentication_form = CustomLoginForm
    



