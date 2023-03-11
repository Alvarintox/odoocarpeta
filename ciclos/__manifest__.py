# -*- coding: utf-8 -*-
{
    'name': "Ciclos Formativos",  # Titulo del módulo
    'summary': "Ciclos formativos gestion",  # Resumen de la funcionaliadad
    'description': """
Gestion de ciclos formativos
==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Alvaro",
    'website': "http://iesjoanramis.org",
    'category': 'Tools',
    'version': '1',
    'depends': ['base'],

    'data': [
        
        'security/ir.model.access.csv',
        #Cargamos la vista del hospital
        'views/alumno.xml',
        'views/profesor.xml',
        'views/formatiu.xml',
        'views/modulo.xml'
    ],
   
}
