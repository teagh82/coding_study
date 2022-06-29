select a.ANIMAL_ID, a.ANIMAL_TYPE, a.NAME
from ANIMAL_INS a
inner join ANIMAL_OUTS b
on a.ANIMAL_ID = b.ANIMAL_ID
where a.SEX_UPON_INTAKE != b.SEX_UPON_OUTCOME
order by a.ANIMAL_ID asc;