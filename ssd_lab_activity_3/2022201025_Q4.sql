SELECT
    E2.Dno as "Dept Id",
    E2.Dname as "Dept Name",
    COUNT(*) as "No of Locations"
From
    DEPT_LOCATIONS
    JOIN (
        SELECT
            DEPARTMENT.Mgr_ssn,
            DEPARTMENT.Dname as Dname,
            DEPARTMENT.Dnumber as Dno,
            COUNT(*)
        FROM
            DEPARTMENT
            JOIN (
                SELECT
                    *
                FROM
                    DEPENDENT
                WHERE
                    DEPENDENT.Sex = "F"
            ) AS E1
        where
            DEPARTMENT.Mgr_ssn = E1.Essn
        GROUP by
            DEPARTMENT.Mgr_ssn,
            DEPARTMENT.Dname,
            DEPARTMENT.Dnumber
        HAVING
            COUNT(*) >= 2
    ) as E2
WHERE
    E2.Dno = DEPT_LOCATIONS.Dnumber
GROUP BY
    E2.Dno,
    E2.Dname;
