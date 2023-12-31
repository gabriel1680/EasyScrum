from flask_openapi3 import APIBlueprint, Tag
from model import Session

from model.sprint import Sprint
from schema.error_schema import ErrorResponse
from schema.sprint_schema import CreateSprintRequest, GetSprintRequest,\
    SprintListResponse, SprintResponse, sprint_list_to_output, \
    sprint_to_output


sprint_tag = Tag(name='Sprint', description='Adição e visualização de sprints')
api = APIBlueprint('/sprints', __name__, abp_tags=[sprint_tag])


@api.post('/sprints', responses={'201': SprintResponse, '400': ErrorResponse})
def create_sprint(form: CreateSprintRequest):
    db = Session()

    sprint = Sprint(form.name, form.description, form.due_date)

    sprint_exists = db.query(Sprint).filter(
        Sprint.name == sprint.name).first()
    if sprint_exists:
        error_message = 'Uma sprint com o título {} já foi cadastrada'.format(
            sprint.name)
        return {'message': error_message}, 400

    db.add(sprint)
    db.commit()

    return sprint_to_output(sprint), 201


@api.get('/sprints', responses={'200': SprintListResponse})
def get_sprints():
    db = Session()
    sprints = db.query(Sprint).all()

    if not sprints:
        return {'sprints': []}, 200

    return sprint_list_to_output(sprints), 200


@api.get('/sprints/<int:id>', responses={'200': SprintListResponse})
def get_sprint(path: GetSprintRequest):
    db = Session()
    sprint = db.query(Sprint).get(path.id)
    db.close()

    if not sprint:
        error_message = 'Sprint não encontrada'
        return {'message': error_message}, 404

    return sprint_to_output(sprint), 200

