select NAME, count(*) as COUNT
from ANIMAL_INS
group by name
having count(name) >= 2
order by name;