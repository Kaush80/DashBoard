from django.shortcuts import render
from django.http import HttpResponse
from .models import datastats
from django.views.decorators.csrf import csrf_exempt
import pandas as pd

# Create your views here.
def home(request):

	return render(request, 'home/home.html')


def about(request):
	return render(request, 'home/about.html')
def tables(request):
	df=pd.read_csv("home/data/dt9jevo9_visa_pay_table_customer.csv")
	table_content = df.to_html(index=None)
	table_content = table_content.replace("","")
	table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
	table_content = table_content.replace('border="1"',"")
	context={'table_data':table_content}


	return render(request, 'home/tables.html',context=context)



def dashboard(request):
    """ view function for dash app """

    # read data                                                                                                  
	
    df = pd.read_csv("home/data/dt9jevo9_visa_pay_table_customer.csv")
    city = df['city'].value_counts()
    categories = list(city.index)
    values = list(city.values)
    x = df["id"]
    y = df["countrycode"]
    list_of_tuples=list(zip(y,x))

    ls = [list(elem) for elem in list_of_tuples]

    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")

    context = {"categories": categories, 'values': values, 'table_data':table_content, "ls":ls }
    return render(request, 'home/dashboard.html', context=context)