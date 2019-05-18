
__name__="piudb"
__author__ = "Wang Pei"

from  .classes import (
    InfoBody,TableManager,Table,Map,
    Model,ModelMetaclass,Field,StringField,
    IntegerField,BooleanField,TextField,FloatField,ObjectField,
	Piu
)

__all__= [
    'InfoBody','TableManager','Table','Map',
    'Model','ModelMetaclass','Field','StringField',
    'IntegerField','BooleanField','TextField','FloatField',
	'Piu'
]