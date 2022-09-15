DELIMITER //
DROP PROCEDURE IF EXISTS `city_search`;
CREATE PROCEDURE `city_search` (IN `CITY` VARCHAR(255))
BEGIN
    SELECT CUST_NAME
    FROM customer
    WHERE WORKING_AREA like CITY;
END//
DELIMITER;