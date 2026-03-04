import json
from django.shortcuts import render

from . import metrics


def home(request):
    product_metrics = metrics.get_product_metrics()
    sales_metrics = metrics.get_sales_metrics()

    dates_sales = metrics.get_sales_data().get('dates')
    values_sales = metrics.get_sales_data().get('values')

    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()

    graphic_product_category_metric = metrics.get_product_count_by_category()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()

    context = {
        'product_metrics' : product_metrics,
        'sales_metrics' : sales_metrics,
        'dates_sales' : json.dumps(dates_sales),
        'values_sales' : json.dumps(values_sales, default=float),
        'daily_sales_quantity_data' : json.dumps(daily_sales_quantity_data),
        'product_count_by_category' : json.dumps(graphic_product_category_metric),
        'product_count_by_brand' : json.dumps(graphic_product_brand_metric),
        'graphic_product_category_metric' : json.dumps(graphic_product_category_metric),
        'graphic_product_brand_metric' : json.dumps(graphic_product_brand_metric)
    }

    return render(request, 'home.html', context)