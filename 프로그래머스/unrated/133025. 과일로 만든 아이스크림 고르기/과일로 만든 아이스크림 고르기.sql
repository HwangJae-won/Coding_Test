select a.FLAVOR
from FIRST_HALF a
left join ICECREAM_INFO 
    on a.FLAVOR = ICECREAM_INFO.FLAVOR
where TOTAL_ORDER >3000 and INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER  desc;
