# [Gold I] 기계오리 연구 - 28082 

[문제 링크](https://www.acmicpc.net/problem/28082) 

### 성능 요약

메모리: 4040 KB, 시간: 40 ms

### 분류

다이나믹 프로그래밍, 배낭 문제

### 제출 일자

2025년 3월 20일 11:19:07

### 문제 설명

<p>인하대학교 기계공학과의 기계오리 연구실에서는 2023년 버전 기계오리를 완성하기 위해 실험을 진행하고 있다. 실험 도중, 기계오리에 1개 이상 $K$개 이하의 배터리를 삽입하면 기계오리가 언제나 작동한다는 사실을 발견했다. 연구실에서는 이를 연구하기 위해 기계오리가 작동할 때 장착된 배터리들의 전력량의 합들을 기록하기로 하였다.</p>

<p>하지만 전세계의 모든 배터리들을 찾아 기계오리에 장착하기는 현실적으로 어렵기 때문에, 연구실에 있는 $N$개의 배터리에 대해서만 가능한 전력량의 합을 기록하기로 하였다. 연구실에 있는 $N$개의 배터리 각각의 전력량과 기계오리에 장착할 수 있는 배터리의 최대 개수 $K$가 주어질 때, 기계오리가 작동하는 전력량의 종류의 수와 그 전력량들의 값을 출력하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫 번째 줄에 연구실에 있는 배터리의 개수 $N$, 기계오리에 장착할 수 있는 배터리의 최대 개수 $K$가 공백으로 구분되어 주어진다.</p>

<p>두 번째 줄에 연구실에 있는 각 배터리의 전력량 $I_1, I_2, \cdots, I_N$이 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>첫 번째 줄에 기계오리에 연구실의 $N$개의 배터리들을 적당히 조합하여 장착했을 때 기계오리가 작동한 전력량의 종류의 수를 출력한다.</p>

<p>두 번째 줄에 기계오리가 작동한 전력량들을 공백을 사이에 두고 <strong>오름차순</strong>으로 출력한다.</p>

