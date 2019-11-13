--- bill

-- no user
SELECT SUM(o.num * p.price)
FROM ws.orders AS o
INNER JOIN ws.products AS p
    USING(pid)
WHERE o.payed = 0;

-- user
SELECT u.name, u.address, SUM(o.num * p.price)
FROM ws.orders AS o
INNER JOIN ws.products AS p
    USING(pid)
INNER JOIN ws.users AS u
    USING(uid)
WHERE o.payed = 0 AND u.username = 'yunoboy12'
GROUP BY u.uid, u.name, u.address;