select a.ANIMAL_ID, a.NAME
from ANIMAL_INS a
inner join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
order by (b.DATETIME - a.DATETIME) desc
limit 2;

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS as O
left join ANIMAL_INS as I
    on I.ANIMAL_ID = O.ANIMAL_ID
ORDER BY DATEDIFF(O.DATETIME, I.DATETIME) DESC
LIMIT 2

