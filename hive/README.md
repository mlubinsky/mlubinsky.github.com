## LEFT SEMI JOIN
In order check the existence of a key in another table, the user can use LEFT SEMI JOIN as illustrated by the following example.
```
INSERT OVERWRITE TABLE pv_users
SELECT u.*
FROM user u LEFT SEMI JOIN page_view pv ON (pv.userid = u.id)
WHERE pv.date = '2008-03-03';
```
