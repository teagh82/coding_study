select ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') as 날짜
from ANIMAL_INS
order by ANIMAL_ID;

SELECT ANIMAL_ID, NAME, date_format(DATETIME, '%Y-%m-%d') as 날짜
FROM ANIMAL_INS
ORDER BY ANIMAL_ID