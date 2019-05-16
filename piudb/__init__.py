
__name__="xiudb"
__author__ = "Wang Pei"

from  .classes import (
    InfoBody,TableOpener,Table,Map,
    Model,ModelMetaclass,Field,StringField,
    IntegerField,BooleanField,TextField,FloatField
)

__all__= [
    'InfoBody','TableOpener','Table','Map',
    'Model','ModelMetaclass','Field','StringField',
    'IntegerField','BooleanField','TextField','FloatField'
]