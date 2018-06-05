from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import YearForm
from .models import DriverStandings, F1ChampionshipYears
from django.db.models import Max, Min


def index(request):
    if request.method == "POST":
        form = YearForm(request.POST)

        if form.is_valid:
            request.session['year'] = request.POST['year']
            return redirect('f1_by_year')
    else:
        form = YearForm()
    context = {'form': form}
    return render(request, 'f1OverTheYears/index.html', context=context)


def f1_by_year(request):
    if 'year' not in request.session:
        return redirect('index')
    print(request.session['year'], "year")
    return render(request, 'f1OverTheYears/wdc.html')


def f1_data(request):
    print("in f1 data")
    label = request.META['HTTP_LBL']
    print(label)
    print(request.session['year'], "year from session")
    year = request.session['year']
    if label != '':
        if label == "prev":
            year = int(year) - 1
        elif label == "next":
            year = int(year) + 1

    data = {}
    print(year, "year after above logic")

    for x in DriverStandings.objects.filter(championship_year=year):
        data[x.driver_position] = [x.driver_name,
                                   x.manufacturer_id,
                                   x.championship_year_id,
                                   x.country_id,
                                   x.points]

    # ch_years = F1ChampionshipYears.objects.order_by('-championship_year')
    # data['first_held'] = ch_years[len(ch_years)-1]
    # data['last_held'] = ch_years[1]
    all_years = F1ChampionshipYears.objects.all()
    print(all_years.aggregate(Max('championship_year')))
    print(all_years.aggregate(Min('championship_year')))
    request.session['first_held']=all_years.aggregate(Min('championship_year'))['championship_year__min']
    request.session['last_held']=all_years.aggregate(Max('championship_year'))['championship_year__max']
    request.session['year'] = year
    import json
    json_obj = json.dumps(data)
    return HttpResponse(json_obj)
