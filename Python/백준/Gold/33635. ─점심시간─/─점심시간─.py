import sys; input = lambda: sys.stdin.readline().rstrip()


N = int(input())
genres = input().split()
genre_to_idx = {genre: i for i, genre in enumerate(genres)}

books = []
for _ in range(int(input())):
    a, book_name, *book_genres = input().split()

    mask = 0
    for genre in book_genres:
        mask |= (1 << genre_to_idx[genre])
    
    books.append(mask)

memo = {}
for _ in range(int(input())):
    x, *query_genres = input().split()
    query_key = tuple(sorted(query_genres))
    
    if query_key in memo:
        print(memo[query_key])
        continue
    
    query_mask = 0
    for genre in query_genres:
        query_mask |= (1 << genre_to_idx[genre])
    
    count = 0
    for book_mask in books:
        if (book_mask & query_mask) == query_mask:
            count += 1
    
    memo[query_key] = count
    print(count)