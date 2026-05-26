import sqlite3
from datetime import datetime

db = "projeto.db"


def create_db():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    with open("schema.sql", "r", encoding="utf-8") as arq:
        script = arq.read()

    cursor.executescript(script)
    conn.commit()
    conn.close()


def get_conn_db():
    return sqlite3.connect(db)


def insert_task(titulo, descricao, prioridade):
    conn = get_conn_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, prioridade, status)
        VALUES (?, ?, ?, ?)
    """, (titulo, descricao, prioridade, "Pendente"))

    conn.commit()
    conn.close()


def select():
    conn = get_conn_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, titulo, descricao, prioridade,
               status, data_criacao, data_conclusao
        FROM tarefas
    """)

    dados = cursor.fetchall()
    conn.close()
    return dados


def update(id_task, nv_status):
    conn = get_conn_db()
    cursor = conn.cursor()

    if nv_status == "Concluída":
        cursor.execute("""
            UPDATE tarefas
            SET status = ?, data_conclusao = ?
            WHERE id = ?
        """, (nv_status, datetime.now(), id_task))

    else:
        cursor.execute("""
            UPDATE tarefas
            SET status = ?, data_conclusao = NULL
            WHERE id = ?
        """, (nv_status, id_task))

def delete(id):
    with get_conn_db() as conn:
        cursor = conn.cursor()
        script_delete = """
                    DELETE FROM tarefas
                    WHERE ID = ?
        """
    cursor.execute(script_delete,(id,))

def dash_pendentes_concluidas():
    with get_conn_db() as conn:
        cursor = conn.cursor()
        script_dash="""
                SELECT status, COUNT(*)
                FROM tarefas
                GROUP BY status

        """
        cursor.execute(script_dash)
        r = cursor.fetchall()
        return r

    conn.commit()
    conn.close()