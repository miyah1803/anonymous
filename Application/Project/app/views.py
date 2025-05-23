from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Sale, BadOrder
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.views.decorators.http import require_http_methods
from .models import Expense
from .forms import ExpenseForm



class HomePageView(TemplateView):
    template_name = 'app/home.html'


class  SalesPageView(TemplateView):
    template_name = 'app/sales.html'



def sales_page(request):
    return render(request, 'app/sales.html')


def get_sales_data(request):
    sales = list(Sale.objects.values())
    return JsonResponse(sales, safe=False)


def get_bad_orders_data(request):
    bad_orders = list(BadOrder.objects.values())
    return JsonResponse(bad_orders, safe=False)


@csrf_exempt
@require_http_methods(["POST"])
def add_sale(request):
    data = json.loads(request.body)
    sale = Sale.objects.create(
        product_name=data["product_name"],
        quantity=data["quantity"],
        price=data["price"],
        date=data["date"]
    )
    return JsonResponse({"id": sale.id})


@csrf_exempt
@require_http_methods(["POST"])
def add_bad_order(request):
    data = json.loads(request.body)
    bo = BadOrder.objects.create(
        transaction_id=data["transaction_id"],
        product_name=data["product_name"],
        quantity=data["quantity"],
        price=data["price"],
        reason=data["reason"],
        date=data["date"]
    )
    return JsonResponse({"id": bo.id})


@csrf_exempt
@require_http_methods(["POST"])
def update_sale(request, pk):
    data = json.loads(request.body)
    sale = get_object_or_404(Sale, pk=pk)
    for field in ['product_name', 'quantity', 'price', 'date']:
        setattr(sale, field, data[field])
    sale.save()
    return JsonResponse({"status": "updated"})


@csrf_exempt
@require_http_methods(["POST"])
def update_bad_order(request, pk):
    data = json.loads(request.body)
    bo = get_object_or_404(BadOrder, pk=pk)
    for field in ['transaction_id', 'product_name', 'quantity', 'price', 'reason', 'date']:
        setattr(bo, field, data[field])
    bo.save()
    return JsonResponse({"status": "updated"})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    sale.delete()
    return JsonResponse({"status": "deleted"})


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_bad_order(request, pk):
    bo = get_object_or_404(BadOrder, pk=pk)
    bo.delete()
    return JsonResponse({"status": "deleted"})


class  InventoryPageView(TemplateView):
    template_name = 'app/inventory.html'


# app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Inventory
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def inventory_page(request):
    return render(request, 'app/inventory.html')

def get_inventory(request):
    inventory = list(Inventory.objects.values())
    return JsonResponse(inventory, safe=False)

@csrf_exempt
def add_inventory(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = Inventory.objects.create(
            product_id=data['product_id'],
            product_name=data['product_name'],
            stock=data['stock'],
            price=data['price']
        )
        return JsonResponse({'status': 'success', 'id': item.id})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def update_inventory(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = get_object_or_404(Inventory, pk=pk)
        item.product_id = data['product_id']
        item.product_name = data['product_name']
        item.stock = data['stock']
        item.price = data['price']
        item.save()
        return JsonResponse({'status': 'updated'})
    return JsonResponse({'status': 'error'}, status=400)

@csrf_exempt
def delete_inventory(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(Inventory, pk=pk)
        item.delete()
        return JsonResponse({'status': 'deleted'})
    return JsonResponse({'status': 'error'}, status=400)



class  ExpensesPageView(TemplateView):
    template_name = 'app/expenses.html'


def expenses(request):
    all_expenses = Expense.objects.all().order_by('-date')

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    else:
        form = ExpenseForm()

    return render(request, 'app/expenses.html', {'form': form, 'expenses': all_expenses})


def delete_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    expense.delete()
    return redirect('expenses')


def update_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('expenses')
    else:
        form = ExpenseForm(instance=expense)

    return render(request, 'app/update_expense.html', {'form': form})


class  RecordPageView(TemplateView):
    template_name = 'app/record.html'


class SigninPageView(TemplateView):
    template_name = 'registration/signin.html'


class SignupPageView(TemplateView):
    template_name = 'registration/signup.html'

 
class DashPageView(TemplateView):
    template_name = 'user/dash.html'

class  SalePageView(TemplateView):
    template_name = 'user/sale.html'


