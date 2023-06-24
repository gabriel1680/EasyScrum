from flask import redirect
from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS

from model import Session
from model.entity_validation_exception import EntityValidationException
from model.task import Task
from model.sprint import Sprint
from schema.error_schema import ErrorResponse
from schema.task_schema import CreateTaskRequest, TaskListResponse, TaskOutputResponse, task_to_output
from schema.sprint_schema import CreateSprintRequest, SprintListResponse, SprintOutputResponse, sprint_to_output

info = Info(title="EasyScrum API", version="0.0.1")
app = OpenAPI(__name__, info=info)
CORS(app)

docs_tag = Tag(name="Documentação",
               description="Documentação da aplicação: Swagger, Redoc ou RapiDoc")
sprint_tag = Tag(name="Sprint", description="Adição e visualização de sprints")
task_tag = Tag(
    name="Tarefa", description="Adição, remoção e visualização de tarefas")

db = Session()


@app.get("/docs", tags=[docs_tag])
def docs():
    return redirect("/openapi")


@app.post("/sprints", tags=[sprint_tag],
          responses={"201": SprintOutputResponse, "422": ErrorResponse, "400": ErrorResponse})
def create_sprint(form: CreateSprintRequest):
    try:
        sprint = Sprint(form.name, form.description, form.status)

        sprint_exists = db.query(Sprint).filter(
            sprint.name == sprint.name).first()
        if sprint_exists:
            error_message = "Uma sprint com o título {} já foi cadastrada".format(
                sprint.name)
            return {"message": error_message}, 400

        db.add(sprint)
        db.commit()
        return sprint_to_output(sprint), 201

    except EntityValidationException as e:
        return {"message": "message"}, 422


# @app.get("/sprints", tags=[sprint_tag], responses={"200": SprintListResponse})
# def get_sprints():
#     sprints = db.query(Sprint).all()

#     if not sprints:
#         return {"sprints": []}, 200

#     output = list(map(lambda sprint: sprint_to_output(sprint), sprints))
#     return {"sprints": output}, 200


@app.post("/sprints/<sprint_id>/task", tags=[task_tag],
          responses={"201": TaskOutputResponse, "422": ErrorResponse, "400": ErrorResponse})
def create_task(form: CreateTaskRequest):
    try:
        sprint_exists = db.query(Sprint).get(form.sprint_id)
        if not sprint_exists:
            error_message = "Uma tarefa só pode ser criada em uma sprint válida"
            return {"message": error_message}, 400

        task = Task(form.sprint_id, form.title,
                    form.due_date, form.story, form.is_done)

        task_exists = db.query(task).filter(task.title == task.title).first()
        if task_exists:
            error_message = "Uma tarefa com o título {} já foi cadastrada nessa sprint".format(
                task.title)
            return {"message": error_message}, 400

        db.add(task)
        db.commit()
        return task_to_output(task), 201

    except EntityValidationException as e:
        return {"message": "message"}, 422


@app.delete("/sprints/<sprint_id>/task/<task_id>", tags=[task_tag],
            responses={"204": TaskOutputResponse, "404": ErrorResponse})
def remove_task(id: int):
    task = db.query(Task).get(id)
    if not task:
        error_message = "Tarefa não encontrada"
        return {"message": error_message}, 404

    db.delete(task)
    db.commit()

    return task_to_output(task), 204


# @app.get("/sprints/<sprint_id>/tasks", tags=[task_tag], responses={"200": TaskListResponse})
# def get_tasks():
#     tasks = db.query(Task).all()

#     if not tasks:
#         return {"tasks": []}, 200

#     output = list(map(lambda task: task_to_output(task), tasks))
#     return {"tasks": output}, 200


if __name__ == "__main__":
    app.run()
