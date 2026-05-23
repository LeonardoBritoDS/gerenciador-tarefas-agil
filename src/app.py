from flask import Flask, render_template, request, redirect, url_for, flash
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import init_db
from src.models import Task

app = Flask(__name__, 
            template_folder='../templates', 
            static_folder='../static')

app.secret_key = 'chave_secreta_projeto_academico_flask_antigravity'

init_db()

@app.route('/')
def index():
    all_tasks = Task.get_all()
    kanban = {
        'todo': [t for t in all_tasks if t['status'] == 'A Fazer'],
        'doing': [t for t in all_tasks if t['status'] == 'Em Progresso'],
        'done': [t for t in all_tasks if t['status'] == 'Concluído']
    }
    return render_template('index.html', kanban=kanban)

@app.route('/tasks/create', methods=['POST'])
def create_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = request.form.get('priority', 'Média')
    status = request.form.get('status', 'A Fazer')

    try:
        Task.create(title, description, status, priority)
        flash('Tarefa adicionada ao Kanban com sucesso!', 'success')
    except ValueError as e:
        flash(f'Erro ao criar tarefa: {str(e)}', 'danger')
        
    return redirect(url_for('index'))

@app.route('/tasks/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        flash('Tarefa não encontrada para edição.', 'danger')
        return redirect(url_for('index'))

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        status = request.form.get('status')
        priority = request.form.get('priority')

        try:
            Task.update(task_id, title, description, status, priority)
            flash('Tarefa atualizada com sucesso!', 'success')
            return redirect(url_for('index'))
        except ValueError as e:
            flash(f'Erro ao atualizar tarefa: {str(e)}', 'danger')

    return render_template('edit.html', task=task)

@app.route('/tasks/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if Task.delete(task_id):
        flash('Tarefa excluída permanentemente!', 'success')
    else:
        flash('Erro ao tentar excluir a tarefa selecionada.', 'danger')
        
    return redirect(url_for('index'))

@app.route('/tasks/update-status/<int:task_id>', methods=['POST'])
def update_status(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        flash('Tarefa não encontrada.', 'danger')
        return redirect(url_for('index'))
        
    new_status = request.form.get('status')
    try:
        Task.update(task_id, task['title'], task['description'], new_status, task['priority'])
        flash(f"Tarefa '{task['title']}' movida para '{new_status}'!", 'success')
    except ValueError as e:
        flash(f'Erro ao mover tarefa: {str(e)}', 'danger')
        
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
