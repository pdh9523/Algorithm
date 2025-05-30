SELECT
    CASE 
        WHEN START_DATE BETWEEN '2022-08-01' AND '2022-08-31' THEN 8
        WHEN START_DATE BETWEEN '2022-09-01' AND '2022-09-30' THEN 9
        WHEN START_DATE BETWEEN '2022-10-01' AND '2022-10-31' THEN 10
    END AS MONTH,
    CAR_ID,
    COUNT(*) AS RECORDS
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE
    START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY
    CAR_ID, MONTH
HAVING
    CAR_ID IN (
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
        GROUP BY CAR_ID
        HAVING SUM(
            CASE 
                WHEN START_DATE BETWEEN '2022-08-01' AND '2022-08-31' THEN 1
                WHEN START_DATE BETWEEN '2022-09-01' AND '2022-09-30' THEN 1
                WHEN START_DATE BETWEEN '2022-10-01' AND '2022-10-31' THEN 1
            END
        ) >= 5
    )
ORDER BY
    MONTH ASC, CAR_ID DESC
;