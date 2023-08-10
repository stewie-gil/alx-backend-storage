-- setting avergage score
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser( IN user_id INT)
BEGIN
	UPDATE users AS us
	SET us.average_score = (SELECT AVG(c.score) FROM corrections AS c WHERE c.user_id = user_id)
	WHERE us.id = user_id;
END;
//
DELIMITER ;
