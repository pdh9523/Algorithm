dirs = [[-1, 0],[1, 0],[0, 1],[0, -1]]

N,M = STDIN.gets.split.map(&:to_i)

grid = Array.new(N)
dist = Array.new(N) { Array.new(M, 0) }

N.times do |i|
    line = STDIN.gets.chomp
    grid[i] = line.chars.map { |c| c == '1' }
end

q = [[0, 0]]
head = 0
dist[0][0] = 1

while head < q.length
    x, y = q[head]
    head += 1

    if x == N - 1 && y == M - 1
        puts dist[x][y]
        exit
    end

    dirs.each do |dx, dy|
        nx,ny = x+dx, y+dy

        next unless nx.between?(0, N - 1) && ny.between?(0, M - 1)
        next unless grid[nx][ny]
        next unless dist[nx][ny] == 0

        dist[nx][ny] = dist[x][y] + 1
        q << [nx, ny]
    end
end

puts -1
