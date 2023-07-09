from flask_openapi3 import APIBlueprint, Tag

from model import Session
from model.task import Task
from model.sprint import Sprint
from schema.error_schema import ErrorResponse
from schema.task_schema import CreateTaskRequest, GetTaskRequest, TaskListResponse, \
    TaskResponse, UpdateTaskRequest, task_to_output, GetTasksRequest

task_tag = Tag(
    name='Tarefa', description='Adição, remoção e visualização de tarefas')

api = APIBlueprint('/sprints/<int:sprint_id>/tasks',
                   __name__, abp_tags=[task_tag])

db = Session()


@api.post('/sprints/<int:sprint_id>/tasks',
          responses={'201': TaskResponse, '400': ErrorResponse})
def create_task(form: CreateTaskRequest, path: GetTasksRequest):
    sprint_id = path.sprint_id
    sprint_exists = db.query(Sprint).get(sprint_id)
    if not sprint_exists:
        error_message = 'Uma tarefa só pode ser criada em uma sprint válida'
        return {'message': error_message}, 400

    task = Task(sprint_id, form.title,
                form.due_date, form.story, form.status)

    task_exists = db.query(Task).filter(Task.title == task.title).first()
    if task_exists:
        error_message = 'Uma tarefa com o título {} já foi cadastrada nessa sprint'.format(
            task.title)
        return {'message': error_message}, 400

    db.add(task)
    db.commit()
    return task_to_output(task), 201


@api.delete('/sprints/<int:sprint_id>/tasks/<int:task_id>',
            responses={'204': None, '404': ErrorResponse, '422': ErrorResponse})
def remove_task(path: GetTaskRequest):
    sprint = db.query(Sprint).get(path.sprint_id)
    if not sprint:
        error_message = 'Sprint não encontrada'
        return {'message': error_message}, 404

    task = db.query(Task).get(path.task_id)
    if not task:
        error_message = 'Tarefa não encontrada'
        return {'message': error_message}, 404

    db.delete(task)
    db.commit()

    return '', 204


@api.get('/sprints/<int:sprint_id>/tasks', responses={'200': TaskListResponse})
def get_tasks(path: GetTasksRequest):
    tasks = db.query(Task).filter(Task.sprint_id == path.sprint_id).all()

    if not tasks:
        return {'tasks': []}, 200

    output = list(map(lambda task: task_to_output(task), tasks))
    return {'tasks': output}, 200


@api.put('/sprints/<int:sprint_id>/tasks/<int:task_id>',
         responses={'204': None, '404': ErrorResponse, '422': ErrorResponse})
def update_task(form: UpdateTaskRequest, path: GetTaskRequest):
    sprint = db.query(Sprint).get(path.sprint_id)
    if not sprint:
        error_message = 'Sprint não encontrada'
        return {'message': error_message}, 404

    task = db.query(Task).get(path.task_id)
    if not task:
        error_message = 'Tarefa não encontrada'
        return {'message': error_message}, 404

    if task.title != form.title:
        task_with_same_title = db.query(Task).filter(
            Task.title == form.title and Task.sprint_id == path.sprint_id).first()
        if task_with_same_title:
            error_message = 'Uma tarefa com o mesmo nome já foi cadastrada'
            return {'message': error_message}, 422

    task.title = form.title
    task.story = form.story
    task.status = form.status
    task.due_date = form.due_date

    db.commit()

    return '', 204
