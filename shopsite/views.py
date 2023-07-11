
from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse ,HttpRequest
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_protect
from .models import Product, Order
from .forms import OrderForm
from django.contrib.auth.models import User

def index(request):

    latest_product_list = Product.objects.order_by("-id")[:5]
    context = {
        'latest_product_list': latest_product_list,
    }

    return render(request, 'index.html', context)




@csrf_protect
def basket(request):
    # if request.method == 'POST':
    #     form = OrderForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # Redirect or process the form data
    # else:
    #     form = OrderForm()
    
    return render(request, 'basket.html')



def user(request, name):
    user = User.objects.get(username=name)
    email = user.email
    objects = Product.objects.filter(user__username__contains=name)
    context = {
        'name': name,
        'user': user,
        'objects': objects,
    }
    return render(request, 'user.html', context)



@csrf_protect
def detail(request, question_id):
    prod = get_object_or_404(Product, pk=question_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            product = get_object_or_404(Product, id=question_id)

            name = request.user.username
            email = request.user.email
            print(name,email,product)
            order = Order(name=name, email=email, product=product)
            order.save()
            # Redirect or process the form data
    else:
        form = OrderForm()

    return render(request, "detail.html", {"product": prod , "form" : form})



def results(request, question_id):
    response = "You're looking at the results of product %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on product %s." % question_id)





# @csrf_protect
# def order_view(request, product_id):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             product = get_object_or_404(Product, id=product_id)
#             name = form.cleaned_data["name"]
#             email = form.cleaned_data["email"]
#             print(name, email)
#             order = Order(name=name, email=email, product=product)
#             order.save()
#             # Redirect or process the form data
#     else:
#         form = OrderForm()
    
#     return render(request, 'order.html', {'form': form})

