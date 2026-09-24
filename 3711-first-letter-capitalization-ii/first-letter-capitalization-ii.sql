WITH RECURSIVE chars AS (
    -- First character of every row
    SELECT
        content_id,
        content_text,
        1 AS pos,
        SUBSTRING(content_text, 1, 1) AS ch
    FROM user_content

    UNION ALL

    -- Remaining characters
    SELECT
        content_id,
        content_text,
        pos + 1,
        SUBSTRING(content_text, pos + 1, 1)
    FROM chars
    WHERE pos < LENGTH(content_text)
),

worded AS (
    SELECT
        content_id,
        content_text,
        pos,
        ch,

        -- Assign a word number based on spaces
        SUM(
            CASE
                WHEN ch = ' ' THEN 1
                ELSE 0
            END
        ) OVER (
            PARTITION BY content_id
            ORDER BY pos
        ) AS word_id
    FROM chars
),

word_info AS (
    SELECT
        content_id,
        word_id,
        GROUP_CONCAT(
            ch
            ORDER BY pos
            SEPARATOR ''
        ) AS word
    FROM worded
    WHERE ch <> ' '
    GROUP BY content_id, word_id
),

classified AS (
    SELECT
        content_id,
        word_id,
        word,

        CASE
            -- Starts with a non-English letter
            WHEN word NOT REGEXP '^[A-Za-z]'
                THEN 'UNCHANGED'

            -- Every hyphen-separated part is non-empty letters
            WHEN word REGEXP '^[A-Za-z]+(-[A-Za-z]+)+$'
                THEN 'HYPHENATED'

            -- Everything else
            ELSE 'NORMAL'
        END AS word_type
    FROM word_info
),

result_chars AS (
    SELECT
        w.content_id,
        w.content_text,
        w.pos,
        w.ch,
        c.word_type,
        c.word,

        -- Is this character the first character of the word?
        CASE
            WHEN w.pos = 1
                 OR SUBSTRING(w.content_text, w.pos - 1, 1) = ' '
                THEN 1
            ELSE 0
        END AS is_word_start,

        -- Is this character immediately after a hyphen?
        CASE
            WHEN SUBSTRING(w.content_text, w.pos - 1, 1) = '-'
                THEN 1
            ELSE 0
        END AS after_hyphen

    FROM worded w
    LEFT JOIN classified c
        ON w.content_id = c.content_id
       AND w.word_id = c.word_id
)

SELECT
    content_id,
    content_text AS original_text,

    GROUP_CONCAT(
        CASE
            -- Spaces stay exactly as they are
            WHEN ch = ' '
                THEN ch

            -- Word starts with non-letter -> entire word unchanged
            WHEN word_type = 'UNCHANGED'
                THEN ch

            -- Valid hyphenated word:
            -- capitalize first letter and first letter after every hyphen
            WHEN word_type = 'HYPHENATED'
                 AND (is_word_start = 1 OR after_hyphen = 1)
                THEN UPPER(ch)

            WHEN word_type = 'HYPHENATED'
                 AND ch REGEXP '[A-Za-z]'
                THEN LOWER(ch)

            -- Normal word:
            -- only the first character is capitalized
            WHEN word_type = 'NORMAL'
                 AND is_word_start = 1
                 AND ch REGEXP '[A-Za-z]'
                THEN UPPER(ch)

            WHEN word_type = 'NORMAL'
                 AND ch REGEXP '[A-Za-z]'
                THEN LOWER(ch)

            -- Special characters stay unchanged
            ELSE ch
        END
        ORDER BY pos
        SEPARATOR ''
    ) AS converted_text

FROM result_chars
GROUP BY
    content_id,
    content_text

ORDER BY content_id;
