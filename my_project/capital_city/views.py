from django.shortcuts import render
from django.http import HttpResponse
from countryinfo import CountryInfo
from countrygroups import EUROPEAN_UNION
import random
import simplejson as json
from django.contrib import messages

def capital(request):
    context={}
    context['title'] = 'Countries and Capitals!'
    countries=EUROPEAN_UNION.names
    capital_dict={}
    for country in countries:
        if country == 'Czechia':
            country = 'Czech Republic'
        cinfo = CountryInfo(country)
        capital_dict[country]=cinfo.capital()
    print(capital_dict)

    # my_obj = Input()
    # my_obj.country_name = json.dumps(countries)
    # for count in range(len(countries)):
    #     app_obj = Input.objects.get(country_name=countries[count])
    #     app_obj.save()

    # for i in range(len(capital_dict)):
    #     country_name=random.choice(list(capital_dict))
    #     temp_list.append(country_name)
    #     break
    context['country_list'] = countries
    # Input.objects.values_list('country_name', flat=True).distinct()
    #context['Country']=country_name
    country_name = request.GET.get('country_name')
    input_text=request.GET.get('input_text')
    print(country_name,input_text)
    print(type(country_name),type(input_text))
    try:
        if input_text == capital_dict[country_name]:
            print("Success")
            messages.success(request, "Great! "+input_text+" is the capital of "+country_name)
        else:
            print("Failed")
            messages.success(request, "Oops! incorrect.. "+capital_dict[country_name]+" is the capital of "+country_name)
    except:
        print("Exception")
    return render(request, 'homepage/capitalcity.html', context)
