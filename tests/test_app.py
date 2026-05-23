import pytest
from src.app import app
from src.models import Task

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client

def test_homepage_renders_correctly(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"TaskFlow" in response.data
    assert b"A Fazer" in response.data
    assert b"Em Progresso" in response.data
    assert b"Conclu" in response.data

def test_create_task_model():
    task_id = Task.create(
        title="Estudar Engenharia de Software",
        description="Focar em metodologias ágeis e Kanban",
        status="A Fazer",
        priority="Alta"
    )
    assert task_id > 0

    task = Task.get_by_id(task_id)
    assert task is not None
    assert task['title'] == "Estudar Engenharia de Software"
    assert task['description'] == "Focar em metodologias ágeis e Kanban"
    assert task['status'] == "A Fazer"
    assert task['priority'] == "Alta"

def test_create_task_validation_empty_title():
    with pytest.raises(ValueError) as excinfo:
        Task.create(title="   ", description="Sem título válido")
    assert "O título da tarefa é obrigatório" in str(excinfo.value)

def test_update_task_model():
    task_id = Task.create(title="Tarefa Original", description="Descrição Antiga", status="A Fazer", priority="Baixa")
    
    success = Task.update(
        task_id=task_id,
        title="Tarefa Atualizada",
        description="Descrição Nova",
        status="Em Progresso",
        priority="Média"
    )
    assert success is True
    
    task_updated = Task.get_by_id(task_id)
    assert task_updated['title'] == "Tarefa Atualizada"
    assert task_updated['description'] == "Descrição Nova"
    assert task_updated['status'] == "Em Progresso"
    assert task_updated['priority'] == "Média"

def test_delete_task_model():
    task_id = Task.create(title="Tarefa para Deletar", description="Será excluída")
    
    deleted = Task.delete(task_id)
    assert deleted is True
    
    task_null = Task.get_by_id(task_id)
    assert task_null is None

def test_create_task_route(client):
    response = client.post('/tasks/create', data={
        'title': 'Testar rotas HTTP',
        'description': 'Realizado usando Pytest client',
        'priority': 'Baixa',
        'status': 'A Fazer'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Testar rotas HTTP" in response.data
    assert b"Tarefa adicionada ao Kanban" in response.data

def test_update_status_route(client):
    task_id = Task.create(title="Testar Transição", description="Em execução", status="A Fazer")
    
    response = client.post(f'/tasks/update-status/{task_id}', data={
        'status': 'Em Progresso'
    }, follow_redirects=True)
    
    assert response.status_code == 200
    
    task = Task.get_by_id(task_id)
    assert task['status'] == 'Em Progresso'
    assert b"movida para &#39;Em Progresso&#39;" in response.data

def test_delete_task_route(client):
    task_id = Task.create(title="Excluir por HTTP", description="Limpeza")
    
    response = client.post(f'/tasks/delete/{task_id}', follow_redirects=True)
    
    assert response.status_code == 200
    assert b"Tarefa exclu\xc3\xadder" not in response.data
    assert b"exclu\xc3\xadda permanentemente" in response.data
