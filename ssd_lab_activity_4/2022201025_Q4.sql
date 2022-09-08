DELIMITER //
DROP PROCEDURE IF EXISTS cursor_call;
CREATE PROCEDURE cursor_call ()
BEGIN
	DECLARE finished INTEGER DEFAULT 0;
	DECLARE name varchar(255);
	DECLARE city varchar(255);
	DECLARE country varchar(255);
	DECLARE grade decimal(30,10);


	-- declare cursor for employee email
	DEClARE ex_cursor 
		CURSOR FOR 
			SELECT CUST_NAME, CUST_CITY, CUST_COUNTRY, GRADE FROM customer
            WHERE AGENT_CODE like 'A00%';

	-- declare NOT FOUND handler
	DECLARE CONTINUE HANDLER 
        FOR NOT FOUND SET finished = 1;

	OPEN ex_cursor;

	cursor_loop: LOOP
		FETCH ex_cursor INTO name,city,country,grade;
		IF finished = 1 THEN wo
			LEAVE cursor_loop;
		END IF;		
		-- dbms_output.Put_line(name||' '||city||' '||country||' '||grade);
        select name,city,country,grade;
	END LOOP cursor_loop;
	CLOSE ex_cursor;
END//
DELIMITER ;