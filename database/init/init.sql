-- Tabela de usuários
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Tabela de documentos (TCCs)
CREATE TABLE IF NOT EXISTS documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(500) NOT NULL,
    content TEXT,
    file_path VARCHAR(500),
    section VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabela de correções
CREATE TABLE IF NOT EXISTS corrections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    correction JSON,
    analysis_time FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Tabela de configurações dos agentes
CREATE TABLE IF NOT EXISTS agent_configs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    agent_name VARCHAR(100) UNIQUE NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    config JSON
);



-- Inserir configurações padrão dos agentes
INSERT IGNORE INTO agent_configs (agent_name, is_active) VALUES 
('grammar', TRUE),
('logical_flow', TRUE), 
('methodology', TRUE);