#평균 리뷰 점수 : groupby 활용 
#테이블 합치기 필요 
select A.REST_ID, B.REST_NAME,B.FOOD_TYPE,B.FAVORITES,B.ADDRESS,
round(avg(A.REVIEW_SCORE),2) as SCORE
from REST_REVIEW A #REST_REVIEW 테이블을 A이름으로 가져오기
join REST_INFO B on A.REST_ID = B.REST_ID #rest_id 기준으로 조인
group by A.REST_ID
having B.ADDRESS like '서울%' #서울로 시작하는 단어 
order by SCORE desc, B.FAVORITES desc ; 
