from flask_openapi3 import APIBlueprint, Tag

from model import Session
from model.task import Task
from model.sprint import Sprint
from schema.error_schema import ErrorResponse
from schema.task_schema import CreateTaskRequest, GetTaskRequest, TaskListResponse, TaskResponse, task_to_output


task_tag = Tag(
    name="Tarefa", description="Adição, remoção e visualização de tarefas")

api = APIBlueprint("/sprints/<int:sprint_id>/tasks", __name__, abp_tags=[task_tag])

db = Session()

@api.post("/sprints/<int:sprint_id>/tasks", tags=[task_tag],
          responses={"201": TaskResponse, "400": ErrorResponse})
def create_task(form: CreateTaskRequest):
    sprint_exists = db.query(Sprint).get(form.sprint_id)
    if not sprint_exists:
        error_message = "Uma tarefa só pode ser criada em uma sprint válida"
        return {"message": error_message}, 400

    task = Task(form.sprint_id, form.title,
                form.due_date, form.story, form.status)

    task_exists = db.query(Task).filter(Task.title == task.title).first()
    if task_exists:
        error_message = "Uma tarefa com o título {} já foi cadastrada nessa sprint".format(
            task.title)
        return {"message": error_message}, 400

    db.add(task)
    db.commit()
    return task_to_output(task), 201


@api.delete("/sprints/<int:sprint_id>/tasks/<int:task_id>", tags=[task_tag],
            responses={"204": TaskResponse, "404": ErrorResponse, "422": ErrorResponse})
def remove_task(path: GetTaskRequest):
    sprint = db.query(Sprint).get(path.sprint_id)
    if not sprint:
        error_message = "Sprint não encontrada"
        return {"message": error_message}, 404

    if sprint.is_done == True:
        error_message = "Uma sprint finalizada não pode ter alteração nas suas tarefas"
        return {"message": error_message}, 422

    task = db.query(Task).get(path.task_id)
    if not task:
        error_message = "Tarefa não encontrada"
        return {"message": error_message}, 404

    db.delete(task)
    db.commit()

    return task_to_output(task), 204


@api.get("/sprints/<int:sprint_id>/tasks", tags=[task_tag], responses={"200": TaskListResponse})
def get_tasks():
    tasks = db.query(Task).all()

    if not tasks:
        return {"tasks": []}, 200

    output = list(map(lambda task: task_to_output(task), tasks))
    return {"tasks": output}, 200
