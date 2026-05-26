CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    descricao TEXT,
    prioridade TEXT CHECK(
        prioridade IN ('Baixa', 'Média', 'Alta')
    ) DEFAULT 'Média',

    status TEXT CHECK(
        status IN ('Pendente', 'Concluída')
    ) DEFAULT 'Pendente',

    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    data_conclusao TIMESTAMP
);