SELECT
    CONCAT(sup.Fname, " ", sup.Minit, " ", sup.Lname) AS "Full name",
    sup.Ssn,
    sup.Dno AS "Dept Id",
    COUNT(sub.Super_ssn) AS "Number of Employees"
FROM
    EMPLOYEE sub
    JOIN EMPLOYEE sup ON sub.Super_ssn = sup.Ssn
GROUP BY
    sup.Ssn,
    sup.Fname,
    sup.Lname,
    sup.Minit,
    sup.Dno
ORDER BY
    COUNT(sub.Super_ssn);