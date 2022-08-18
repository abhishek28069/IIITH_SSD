SELECT
    WORKS_ON.Essn as "Manager ssn",
    COUNT(*) as "Number of Projects"
FROM
    WORKS_ON
WHERE
    WORKS_ON.Essn = (
        SELECT
            DEPARTMENT.Mgr_ssn
        FROM
            DEPARTMENT
        WHERE
            DEPARTMENT.Dnumber = (
                SELECT
                    PROJECT.Dnum
                FROM
                    PROJECT
                WHERE
                    PROJECT.Pname = "ProductY"
            )
    )
GROUP BY
    WORKS_ON.Essn;