from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout

from .models import *

from sodapy import Socrata
import pandas as pd
import plotly
import plotly.offline as opy
import plotly.plotly as py
import plotly.graph_objs as go

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
        #consulta a la api de socrata, de los datos de producción de cacao en los departamentos de colombia
        client = Socrata("www.datos.gov.co", "5yzK70sZPLjXhV8ENN4xSiV29", username="jorgemsm12316@utp.edu.co" , password="Jorge970208" )
        departamento = request.POST.get('departamento')
        departamento = departamento.upper()
        results = client.get("97ki-syuv", limit=200, departamento=departamento)
        results_df = pd.DataFrame(results)
        lista = results_df

        #listas para graficar
        lista1 = results_df[(results_df['periodo']=='2007')]
        lista2 = results_df[(results_df['periodo']=='2008')]
        lista3 = results_df[(results_df['periodo']=='2009')]
        lista4 = results_df[(results_df['periodo']=='2010')]
        lista5 = results_df[(results_df['periodo']=='2011')]
        lista6 = results_df[(results_df['periodo']=='2012')]
        lista7 = results_df[(results_df['periodo']=='2013')]
        lista8 = results_df[(results_df['periodo']=='2014')]
        lista9 = results_df[(results_df['periodo']=='2015')]
        lista10 = results_df[(results_df['periodo']=='2016')]
        lista11 = results_df[(results_df['periodo']=='2017')]

        #creación de grafica con plotly (torta)
        plotly.tools.set_credentials_file(username='jorgesalazar19', api_key='8mK4qbSqP7UqPUNLQFIc')
        plotly.tools.set_config_file(world_readable=True)
        labels=[
                'periodo 2007', 
                'periodo 2008', 
                'periodo 2009', 
                'periodo 2010', 
                'periodo 2011', 
                'periodo 2012', 
                'periodo 2013', 
                'periodo 2014', 
                'periodo 2015', 
                'periodo 2016', 
                'periodo 2017'
        ]

        values=[
            len(lista1.index),
            len(lista2.index),
            len(lista3.index), 
            len(lista4.index), 
            len(lista5.index),  
            len(lista6.index),  
            len(lista7.index),  
            len(lista8.index),  
            len(lista9.index),  
            len(lista10.index),  
            len(lista11.index)
        ]

        layout = go.Layout(title='Cantidad de municipios que tuvieron producción de cacao en colombia desde 2007 en el departamento de '+str(departamento))
        trace=go.Pie(labels=labels, values=values, textinfo='value+percent', pull=.1, hole=.1)
        data = [trace]
        fig = go.Figure(data=data, layout=layout)
        div = opy.plot(fig, auto_open=False , output_type='div')

        #se renombran los campos de la tabla que viene como resultado de la consulta(para mejor visualización)
        lista = lista.rename(columns={   
                    ' ':'id' ,
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

        #creacion de tabla en formato html
        lista_table = lista.to_html(classes='table' , justify='center', col_space=1)

        ctx = {
            'departamentos' : departamentos,
            'table' : lista_table,
            'grafica' : div,
        }


    return HttpResponse(template.render(ctx,request))


@login_required
def logOut(request):
    if request.user is not None:
        logout(request)

    return redirect('/')
