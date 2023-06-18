from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from model import Session
from model.entity_validation_exception import EntityValidationException
from model.task import Task
from schema.error_schema import ErrorResponse
from schema.task_schema import CreateTaskRequest, CreatetaskRequest, taskListResponse, taskOutputResponse, task_to_output
from flask_cors import CORS

info = Info(title="EasyScrum API", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

docs_tag = Tag(name="Documentação", description="Documentação da aplicação: Swagger, Redoc ou RapiDoc")
task_tag = Tag(name="Tarefa", description="Adição e visualização de tarefas")

db = Session()


@app.get("/docs", tags=[docs_tag])
def docs():
    return redirect("/openapi")


@app.post("/sprint/<sprint_id>/task", tags=[task_tag], 
          responses={"201": taskOutputResponse, "422": ErrorResponse, "400": ErrorResponse})
def create_task(form: CreateTaskRequest):
    try:
        task = Task(form.title, form.due_date, form.story, form.is_done)

        task_exists = db.query(task).filter(task.email == task.email).first()

        if task_exists:
            error_message = "O e-mail {} está indisponível".format(task.email)
            return {"message": error_message}, 400
        
        task.hash_password()

        db.add(task)
        db.commit()
        return task_to_output(task), 201

    except EntityValidationException as e:
        print(e)
        return {"message": "message"}, 422


@app.get("/tasks", tags=[task_tag], responses={"200": taskListResponse})
def get_tasks():
    tasks = db.query(Task).all()

    if not tasks:
        return {"tasks": []}, 200

    output = list(map(lambda task: task_to_output(task), tasks))
    return {"tasks": output}, 200



if __name__ == "__main__":
    app.run()
