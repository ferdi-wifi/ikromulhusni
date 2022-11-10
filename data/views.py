

# Create your views here.
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import *
from . forms import *

# Create your views here.



# code '-id' untuk ketika data di input maka ada di atas
def home(request):
    list_customer = Customer.objects.order_by('-id')
    list_order = Order.objects.order_by('-id')
    total_orders = list_order.count()
    delivered = list_order.filter(status = 'Delifered').count()
    pending = list_order.filter(status = 'Pending').count()
    context ={
        'judul' : 'Halaman Beranda',
        'menu' : 'Home',
        'customer'          :list_customer,
        'order'             :list_order,
        'data_total_orders' :total_orders,
        'data_delivered'    :delivered,
        'data_pending'      :pending,
        
    }
    return render(request, 'data/dashboard.html', context)

def products(request):
    list_product = Product.objects.all()
    context ={
        'judul' : 'Halaman Broduk',
        'menu' : 'produk',
        'product':list_product,
    }
    return render(request, 'data/products.html', context)

def customer(request, pk):
    detailcustomer = Customer.objects.get(id = pk)
    order_customer = detailcustomer.order_set.all()
    total_customer = order_customer.count()
    context ={
        'customer'  : detailcustomer,
        'judul'     : 'Halaman Pelanggan',
        'menu'      : 'pelanggan',
        'data_order_customer' : order_customer,
        'data_total_customer' : total_customer,
    }
    return render(request, 'data/customer.html', context)

# save CRUD
def createOrder(request):
    formorder = OrderForm()
    if request.method == 'POST':
        # buat ngecek doank
        # print('Cetak POST:' , request.POST)
        
        formsimpan = OrderForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
    context = {
        'judul' : 'Form Order',
        'form' : formorder,
    }
    return render(request, 'data/order_form.html', context)

def createCustomer(request):
    formcustomer = CustomerForm()
    if request.method == 'POST':
        # buat ngecek doank
        # print('Cetak POST:' , request.POST)
        
        formsimpan = CustomerForm(request.POST)
        if formsimpan.is_valid:
            formsimpan.save()
            return redirect('/')
    context = {
        'judul' : 'Form Customer',
        'form' : formcustomer,
    }
    return render(request, 'data/customer_form.html', context)

#update CRUD
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    formorder = OrderForm(instance=order)
    if request.method == 'POST':
        formedit = OrderForm(request.POST, instance=order)
        if formedit.is_valid:
            formedit.save()
            return redirect('/')
    context = {
        'judul' : 'Edit Order',
        'form' : formorder
    }
    return render(request, 'data/order_form.html', context)

# def updateCustomer(request, pk):
#     customer = Customer.objects.get(id=pk)
#     formcustomer = CustomerForm(instance=customer)
#     if request.method == 'POST':
#         formedit = CustomerForm(request.POST, instance=customer)
#         if formedit.is_valid:
#             formedit.save()
#             return redirect('/')
#     context = {
#         'judul' : 'Edit Customer',
#         'form' : formcustomer
#     }
#     return render(request, 'data/customer_form.html', context)

#delete CRUD
def deleteOrder(request, pk):
    orderhapus = Order.objects.get(id=pk)
    if request.method == 'POST':
        orderhapus.delete()
        return redirect('/')
    context = {
        'judul' : 'Hapus Data Order',
        'dataorderdelete' : orderhapus,
    }
    return render(request, 'data/delete_form.html', context)

# def deleteCustomer(request, pk):
#     customerhapus = Customer.objects.get(id=pk)
#     if request.method == 'POST':
#         customerhapus.delete()
#         return redirect('/')
#     context = {
#         'judul' : 'Hapus Data Order',
#         'datacustomerdelete' : customerhapus,
#     }
#     return render(request, 'data/delete_cu.html', context)