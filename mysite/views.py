from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

from .models import *

from sodapy import Socrata
import pandas as pd

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def consulta(request):

    template = loader.get_template('consulta.html')
    departamentos = Departamentos.objects.all()

    if request.method == 'GET':
        ctx = {
            'departamentos' : departamentos,
    }


    if request.method == 'POST':
        client = Socrata("www.datos.gov.co", "5yzK70sZPLjXhV8ENN4xSiV29", username="jorgemsm12316@utp.edu.co" , password="Jorge970208" )
        departamento = request.POST.get('departamento')
        departamento = departamento.upper()
        results = client.get("97ki-syuv", limit=500)
        results_df = pd.DataFrame(results)
        lista = results_df[(results_df['departamento']==departamento)]
        lista = lista.rename(columns={   
                    '':'id' ,
                    'c_d_mun' : 'Codido Municipio',
                    'cultivo' : 'Cultivo',
                    'departamento' : 'Departamento',
                    'municipio' : 'Municipio',
                    'periodo' : 'Periodo',
                    'producci_n_t' : 'Producción',
                    'rea_cosechada_ha' : 'Área cosechada',
                    'rea_sembrada_ha' : 'Área sembrada',
                    'rendimiento_t_ha': 'Rendimiento'

        })

        lista_table = lista.to_html(classes='table' , justify='center', col_space=1)

        ctx = {
            'departamentos' : departamentos,
            'table' : lista_table,
        }


    return HttpResponse(template.render(ctx,request))


@login_required
def logOut(request):
    if request.user is not None:
        logout(request)

    return redirect('/')
