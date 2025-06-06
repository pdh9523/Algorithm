# [Diamond IV] Touch The Sky - 15773 

[문제 링크](https://www.acmicpc.net/problem/15773) 

### 성능 요약

메모리: 102732 KB, 시간: 884 ms

### 분류

자료 구조, 그리디 알고리즘, 우선순위 큐, 정렬

### 제출 일자

2025년 3월 31일 23:45:20

### 문제 설명

<p style="text-align: center;"><img alt="" src="" style="width: 675px; height: 450px;"></p>

<p style="text-align: center;">사진: 풍선으로 하늘에 띄운 집. 2018 KAIST RUN Spring Contest 포스터에도 사용된 사진이다.</p>

<p>서기 2117년, 유재민 교수에 의해 TSP (Traveling Salesperson Problem)의 선형시간 알고리즘이 개발되었다. 얼마 가지 않아 모든 컴퓨터 시스템은 붕괴되었고, 세상은 핵무기로 인해 황폐화 되었다. 컴퓨터 과학의 최고 전문가이던 당신 역시도 할 일을 잃게 되었고, 절망 속에 인생의 의미를 잃어버린 지 오래다. 과연 그동안 당신의 심장을 뛰게 하던 모든 것들은 어디로 갔을까? 끝없이 자신에게 질문한 끝에 내린 결론은...</p>

<p><em>"ICPC를 처음 시작한 그 때 그 카이스트를 가면, 내 인생의 의미를 찾을 수 있지 않을까?"</em></p>

<p>도로망이나 철도는 모두 황폐화된지 오래이다. 그렇지만 열렬한 ICPC 참가자였던 당신은 100년 전 대전 대회에서 받았던 풍선을 여전히 가지고 있다. 만약 그 풍선으로 집을 띄울 수만 있다면...</p>

<p>현재 당신에게는 <em>N</em>개의 풍선이 있고, 당신은 풍선을 하나씩 지붕에 매달아서 집을 하늘로 띄우려 한다. 각각의 풍선은 고도 제한 <em>L<sub>i</sub></em>와 용량 <em>D<sub>i</sub></em>가 있는데, 이는 기압의 영향으로 인하여 고도 <em>L<sub>i</sub></em> 이하에서만 이 풍선을 불 수 있고, 이 풍선은 고도를 <em>D<sub>i</sub></em>만큼 상승시킨 후 터진다는 것을 뜻한다.</p>

<p>당신의 여정은 고도 0에서 출발한다. 부풀어 있는 풍선이 2개 이상이면 집이 너무 빠른 속도로 상승할 수 있으니, 당신은 하나의 풍선을 불어서 지붕에 매단 후, 풍선이 터질 때가지 고도를 상승시키고, 터진 이후에 또 하나의 풍선을 불어서 터질 때까지 고도를 상승시키는 것을 반복해서 집을 띄울 예정이다. 편의상 터진 이후 풍선을 매다는 동안의 고도 변화는 없다고 가정한다. (즉, 풍선만이 유일하게 고도를 바꿀 수 있다.)</p>

<p>최종 고도는 어느 위치던 간에 상관 없으나, 하나의 풍선은 터지기 전 까지 일정한 거리를 움직일 수 있으니, 최대한 많은 풍선을 터뜨리는 것이 좋다. 고로 당신은 터뜨릴 수 있는 풍선의 최대 개수를 계산한 후, 정말 KAIST로의 여행을 떠날 수 있는지를 계산해 보려고 한다. 100년 전의 ICPC 경험이, 이 문제를 해결하는 데 정말 도움을 줄 수 있을까?</p>

### 입력 

 <p>첫 번째 줄에 풍선의 개수 <em>N</em>이 주어진다.</p>

<p>이후 <em>N</em>개의 줄의 <em>i</em>번째 줄에는 풍선의 고도 제한 <em>L<sub>i</sub></em>와 풍선의 용량 <em>D<sub>i</sub></em>를 의미하는 정수 2개가 공백으로 구분되어 주어진다.</p>

### 출력 

 <p>터뜨릴 수 있는 풍선의 최대 개수를 출력하여라.</p>

