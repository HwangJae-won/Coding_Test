select round(avg(DAILY_FEE),0) as AVERAGE_FEE # 평균 일일 대여 요금 / 소수점 반올림
from CAR_RENTAL_COMPANY_CAR
where CAR_TYPE = 'SUV' #차 종류 조건문

