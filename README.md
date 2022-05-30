# Solving problems in BOJ

## Chapter 01. 문제해결 입문

* A + B: 1 2 3 4 5 6 7 8
  * 파이썬으로는 큰 수의 연산이 가능함을 이해
* 별찍기: 1 2 3 4 5 6 7 8 9
  * 10번 이후는 재귀 문제
* N과 M: 1 2 3 4 5 6 7 8
  * 입문 과정에서는 itertools 사용
  * 나중에는 백트래킹으로 풀어볼 것

## Chapter 02. 몸풀기

* 2562 최댓값
* 2475 검증수
* 1977 완전제곱수
* 1259 팰린드롬수
* 2577 숫자의 개수
* 1834 나머지와 몫이 같은 수
* 10250 ACM 호텔
* 1110 더하기 사이클

## Chapter 03. 행렬 문제

* 2738 행렬 덧셈
* 2740 행렬 곱셈
* 10830 행렬 제곱

## Chapter 04. 마방진 문제

* 15739 매직스퀘어 (마방진 검사)
* 2045 마방진 (마방진 빈칸 채우기)
* 20112 사토르 마방진
* 24891 단어 마방진
* 1307 마방진 (마방진 만들기)
  * 마방진 푸는 법에 대해서는 다음 사이트 참조
  * [홀수 마방진 푸는 법](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=6711ko&logNo=220826025482)
  * [짝수 마방진 푸는 법](https://m.blog.naver.com/askmrkwon/220768685076)

## Chapter 11. 약수와 배수

* 2501 약수 구하기
* 9506 약수들의 합
* 1037 약수 (최대값과 최소값 동시에 찾기)
* 17427 약수의 합 2
  * 단순 약수의 합은 시간 초과에 걸림
* 1676 팩토리얼 0의 개수
  * 이건 시간초과 안 걸리므로 수학 문제인지 모를 수 있음(2004번을 풀어봐야 함)
* 2004 조합 0의 개수
  * 여기가 시간초과 걸려서 수학 문제인지 알 수 있음

## Chapter 12. 소수와 소인수 분해

* 1978 소수 찾기
* 1747 소수 & 팰린드롬
* 1929 소수 구하기 (에라토스테네스의 체)
* 2960 에라토스테네스의 체
* 11653 소인수분해
* 16563 어려운 소인수분해
* 11502 세 개의 소수 문제
  * 이 문제는 백트래킹으로 보내도 됨

## Chapter 13. 집합 문제

* 11723 집합
* 1717 집합의 표현 (disjoint set)

## Chapter 21. 재귀

* 10872 팩토리얼
* 4564 숫자 카드놀이
* 6615 콜라츠 추측
* 1914 하노이 탑
* 11866 요세푸스 문제 0
* 2609 최대공약수와 최소공배수
* 2448 별 찍기 - 11 (시어핀스키 삼각형)
* 2747 2748 피보나치 수 1 2
* 11050 11051 이항 계수 1 2

advanced:

* 2749 피보나치 수 3
  * 이 문제는 피보나치 수의 주기(피사노 주기)를 알아야 시간 초과를 면할 수 있음

## Chapter 22. 순열과 조합

* 15651 N과 M (3) (중복순열 구하기)
* 2529 부등호

## Chapter 23. 해시 테이블

* 1157 단어 공부
* 1302 베스트셀러
* 15829 Hashing
* 13273 로마 숫자
* 2608 로마 숫자

advanced:

* 2915 로마 숫자 재배치
  * 이 문제는 모든 경우의 수(순열)를 구해야 함: 백트래킹
  * 로마 숫자의 유효성을 일반적으로 풀려면 정규표현식이 필요함

## Chapter 24. 트리 문제

## Chapter 25. 그래프

* 1260 DFS와 BFS
* 2178 미로 탐색
* 11724 연결요소의 개수
  * 이 문제는 서로소 집합(유니온-파인드)으로 해결 가능 (BFS는 시간초과)
  
## Chapter 31. 선택 문제

## Chapter 32. 분할정복

* 1300 K번째 수
* 14601 샤워실 바닥 깔기 (Large) (트로미노 퍼즐)
* 13277 큰 수 곱셈 (파이썬으로는 그냥 통과; Java는 BigInteger; C++)
  * 10757 큰 수 A + B

## Chapter 33. 탐욕법

## Chapter 34. 동적계획

* 2839 설탕 배달
* 1463 1로 만들기
* 2579 계단 오르기
* 1793 타일링
* 11049 행렬 곱셈 순서

## Chapter 35. 백트래킹

## Chapter 41. 정렬 문제

* 2750 수 정렬하기
  * 단순한 정렬 함수 사용 가능
* 2751 수 정렬하기 2
  * 시간초과: 정렬 함수와 입출력 함수를 효율적으로 사용해서 해결 가능
* 10989 수 정렬하기 3
  * 메모리초과: 10,000보다 작거나 같은 수라는 점을 이용
* 11650 좌표 정렬하기
  * 라이브러리 함수 이용: key와 lambda를 이용한 오름차순/내림차순까지...
