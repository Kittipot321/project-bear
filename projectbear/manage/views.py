from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from main.models import Type, Product

# Create your views here.
def manage(request):
    product = Product.objects.all()
    context = {
        'product' : product
    }
    return render(request, 'manage/manage.html', context=context)

# def manageproduct(request):
#     return

# หน้าเพิ่มสินค้า
@login_required
def add_product(request):
    page_title = 'Add Product'
    type = Type.objects.all()
    context = {
        'type':type,
        'page_title':page_title
    }
    return render(request,'manage/product_form.html',context=context)
# เพิ่มเข้าในตาราง product
@login_required
def add_to_database(request):
    page_title = 'Add Product'
    type = Type.objects.all()
    number = request.POST.get('txt_1')
    notice = ''
    create= ''
    try:
        create = Product.objects.create(
                type=Type.objects.get(pk=number),
                name=request.POST.get('txt_2'),
                stock=request.POST.get('txt_3'),
                price=request.POST.get('txt_4'),
                picture=request.POST.get('txt_5'),
            )
        notice = 'การเพิ่มสินค้าของคุณสำเร็จแล้ว -> หมายเลขสินค้าที่ %s' % (create.id)
    except ValueError:
        notice = 'โอ๊ะ! ประเภทข้อมูลผิดพลาด'
    context = {
        'create':create,
        'notice':notice,
        'type':type,
        'page_title':page_title
    }
    return render(request, 'manage/product_form.html', context=context)

# ลบสินค้า
@login_required
def delete_product(request,product_id):
    products = Product.objects.get(id=product_id)
    products.delete()
    return redirect(to='manage')

def product_update(request,product_id):
    page_title = 'Update Product = %d' %product_id
    product = Product.objects.get(pk=product_id)
    type = Type.objects.all()
    notice = ''
    if request.method == 'POST':
        product.name = request.POST.get('txt_2')
        product.type_id = request.POST.get('txt')
        product.description = request.POST.get('txt_3')
        try:
            product.price = request.POST.get('txt_4')
            product.save()
            notice = 'บันทึกข้อมูลเรียบร้อยแล้ว'
        except ValueError:
            notice = 'โอ๊ะ! ประเภทข้อมูลผิดพลาด'
    context={
        'num':product_id,
        'product':product,
        'type':type,
        'notice':notice,
        'page_title':page_title
    }
    return render(request,'manage/product_form.html',context=context)

