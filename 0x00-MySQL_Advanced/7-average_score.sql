-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(5,2);

    -- Compute the average score
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    -- If there are no scores, set avg_score to 0
    IF avg_score IS NULL THEN
        SET avg_score = 0;
    END IF;

    -- Update or insert the average score in the users table
    INSERT INTO users (id, average_score)
    VALUES (p_user_id, avg_score)
    ON DUPLICATE KEY UPDATE average_score = avg_score;

END //

DELIMITER ;
