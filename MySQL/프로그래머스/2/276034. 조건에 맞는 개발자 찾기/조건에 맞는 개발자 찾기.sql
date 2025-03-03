-- 코드를 작성해주세요
SELECT DISTINCT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS a
JOIN
    SKILLCODES b
    ON (a.SKILL_CODE & b.CODE) > 0
WHERE
    b.NAME in ('Python', 'C#')
ORDER BY
    ID
;