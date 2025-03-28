select 
    USED_GOODS_BOARD.TITLE, 
    USED_GOODS_REPLY.BOARD_ID,
    USED_GOODS_REPLY.REPLY_ID, 
    USED_GOODS_REPLY.WRITER_ID,
    USED_GOODS_REPLY.CONTENTS, 
    date_format(USED_GOODS_REPLY.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD
inner join USED_GOODS_REPLY 
    on USED_GOODS_BOARD.BOARD_ID=USED_GOODS_REPLY.BOARD_ID
where year(USED_GOODS_BOARD.CREATED_DATE)=2022 
    and month(USED_GOODS_BOARD.CREATED_DATE) =10
order by CREATED_DATE, TITLE

