-- Création de la base de données test
CREATE DATABASE IF NOT EXISTS test;

-- Utilisation de la base de données test
USE test;

-- Création de la table phrase
CREATE TABLE IF NOT EXISTS phrase (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mot VARCHAR(50)
);

-- Insertion de la phrase de test dans la table phrase
INSERT INTO phrase (mot) VALUES ('phrase de test');

