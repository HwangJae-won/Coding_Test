select count(*) as FISH_COUNT
from FISH_INFO
where LENGTH is null or LENGTH<=10