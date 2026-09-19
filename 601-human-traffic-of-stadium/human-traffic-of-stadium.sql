WITH qualified AS (
    SELECT
        id,
        visit_date,
        people,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
valid_groups AS (
    SELECT grp
    FROM qualified
    GROUP BY grp
    HAVING COUNT(*) >= 3
)
SELECT
    q.id,
    q.visit_date,
    q.people
FROM qualified q
JOIN valid_groups v
    ON q.grp = v.grp
ORDER BY q.visit_date;