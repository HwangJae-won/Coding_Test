#총 실행시간 출력
#LRU: 가장 오랫동안 참조되지 않은 페이지를 교체하는 방식
#캐시크기가 0인 케이스도 있음
def solution(cache_size, cities):
    cache = [] #빈 캐시 생성
    answer = 0
    for city in cities:
        city = city.lower() #대소문자 섞여 있으므로 소문자로 통일
        if city in cache: #빈 리스트 안에 없다면 
            answer += 1 #실행 시간 +1 (cache hit)
            cache.remove(city)
            cache.append(city) #제거하고 추가함으로써 가장 앞으로 보냄 
        else:
            answer += 5 #cache miss : 실행 시간 5
            if cache_size == 0: #캐시 크기가 0일 경우가 있으므로 if문으로 처리 
                continue
            if len(cache) >= cache_size:
                cache.pop(0)
            cache.append(city)
    return answer
