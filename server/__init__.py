from flask_openapi3 import OpenAPI, Info
from flask_cors import CORS

from server.sprint_api import api as sprint_api
from server.task_api import api as task_api
from server.doc_api import api as doc_api

info = Info(title='EasyScrum API', version='0.0.1',
            description='EasyScrum API é uma API REST para gestão de projétos ágeis utilizando scrum')
app = OpenAPI(__name__, info=info)

app.register_api(doc_api)
app.register_api(sprint_api)
app.register_api(task_api)

CORS(app)

