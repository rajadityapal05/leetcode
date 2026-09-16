SELECT
    product_id,
    COALESCE(
        MAX(CASE WHEN change_date = (
            SELECT MAX(p2.change_date)
            FROM Products p2
            WHERE p2.product_id = Products.product_id
              AND p2.change_date <= '2019-08-16'
        ) THEN new_price END),
        10
    ) AS price
FROM Products
GROUP BY product_id;