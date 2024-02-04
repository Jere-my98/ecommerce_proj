from django.shortcuts import render
from .models import Product, Category, Order, OrderItem
# Views for Products

def store_home(request):
    return render(request, 'store_base.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})

# Views for Categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category_detail.html', {'category': category})

# Views for Orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = Order.objects.get(pk=pk)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'order_detail.html', {'order': order, 'order_items': order_items})

# Views for Cart
# def cart_detail(request):
#     cart = Cart.objects.get(user=request.user)
#     cart_items = CartItem.objects.filter(cart=cart)
#     return render(request, 'cart_detail.html', {'cart': cart, 'cart_items': cart_items})

# Views for Addresses
# def address_list(request):
#     addresses = Address.objects.filter(user=request.user)
#     return render(request, 'address_list.html', {'addresses': addresses})

# def address_detail(request, pk):
#     address = Address.objects.get(pk=pk)
#     return render(request, 'address_detail.html', {'address': address})
