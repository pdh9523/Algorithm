WITH REVIEW_AVG AS (
    SELECT
        REST_ID,
        ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
    FROM
        REST_REVIEW
    WHERE
        REVIEW_SCORE IS NOT NULL
    GROUP BY
        REST_ID
)
SELECT
    info.REST_ID,
    info.REST_NAME,
    info.FOOD_TYPE,
    info.FAVORITES,
    info.ADDRESS,
    review.SCORE
FROM
    REST_INFO info
JOIN
    REVIEW_AVG review
ON
    info.REST_ID = review.REST_ID
WHERE
    info.ADDRESS LIKE '서울%'
GROUP BY
    info.REST_ID
ORDER BY
    SCORE DESC, FAVORITES DESC
;