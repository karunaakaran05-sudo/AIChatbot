
USE ai_customer_support;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE chats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    question TEXT NOT NULL,
    answer LONGTEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
);

CREATE TABLE feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chat_id INT NOT NULL,
    rating ENUM('Like','Dislike') NOT NULL,
    comment TEXT,
    FOREIGN KEY (chat_id) REFERENCES chats(id)
        ON DELETE CASCADE
);

CREATE TABLE faq (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer LONGTEXT NOT NULL
);

CREATE TABLE contact (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    subject VARCHAR(200),
    message TEXT,
    status VARCHAR(30) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE SET NULL
);

CREATE TABLE knowledge_base (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content LONGTEXT,
    source_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);