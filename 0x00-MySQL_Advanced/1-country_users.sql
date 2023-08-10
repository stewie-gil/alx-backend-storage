-- creates a users table with id, email, name and country columns
CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
