import json
from django.shortcuts import render

from . import metrics


def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()

    dates_sales = metrics.get_sales_data().get('dates')
    values_sales = metrics.get_sales_data().get('values')

    context = {
        'product_metrics' : product_metrics,
        'sales_metrics' : sales_metrics,
        'dates_sales' : json.dumps(dates_sales),
        'values_sales' : json.dumps(values_sales, default=float)
    }

    return render(request, 'home.html', context)