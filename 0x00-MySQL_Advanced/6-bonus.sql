-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER $$
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    INSERT INTO projects(name) VALUES (project_name);
    INSERT INTO corrections VALUES (user_id, project_name, score);
END$$
DELIMITER ;
