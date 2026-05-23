from src.database import get_db_connection

class Task:
    def __init__(self, id_task, title, description, status, priority, created_at):
        self.id = id_task
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority
        self.created_at = created_at

    @staticmethod
    def create(title, description, status='A Fazer', priority='Média'):
        if not title or not title.strip():
            raise ValueError("O título da tarefa é obrigatório e não pode conter apenas espaços.")

        valid_statuses = ['A Fazer', 'Em Progresso', 'Concluído']
        valid_priorities = ['Alta', 'Média', 'Baixa']

        if status not in valid_statuses:
            status = 'A Fazer'
        if priority not in valid_priorities:
            priority = 'Média'

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)',
            (title.strip(), description.strip() if description else '', status, priority)
        )
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        return task_id

    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks ORDER BY created_at DESC')
        rows = cursor.fetchall()
        conn.close()

        tasks = []
        for row in rows:
            tasks.append({
                'id': row['id'],
                'title': row['title'],
                'description': row['description'],
                'status': row['status'],
                'priority': row['priority'],
                'created_at': row['created_at']
            })
        return tasks

    @staticmethod
    def get_by_id(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                'id': row['id'],
                'title': row['title'],
                'description': row['description'],
                'status': row['status'],
                'priority': row['priority'],
                'created_at': row['created_at']
            }
        return None

    @staticmethod
    def update(task_id, title, description, status, priority):
        if not title or not title.strip():
            raise ValueError("O título atualizado da tarefa é obrigatório.")

        valid_statuses = ['A Fazer', 'Em Progresso', 'Concluído']
        valid_priorities = ['Alta', 'Média', 'Baixa']

        if status not in valid_statuses:
            status = 'A Fazer'
        if priority not in valid_priorities:
            priority = 'Média'

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE tasks SET title = ?, description = ?, status = ?, priority = ? WHERE id = ?',
            (title.strip(), description.strip() if description else '', status, priority, task_id)
        )
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()
        return affected_rows > 0

    @staticmethod
    def delete(task_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()
        affected_rows = cursor.rowcount
        conn.close()
        return affected_rows > 0
