from flask_openapi3 import APIBlueprint, Tag
from flask import redirect


docs_tag = Tag(name='Documentação',
               description='Documentação da aplicação: Swagger, Redoc ou RapiDoc')

api = APIBlueprint('/docs', __name__, abp_tags=[docs_tag])

@api.get('/docs', tags=[docs_tag])
def docs():
    return redirect('/openapi')

