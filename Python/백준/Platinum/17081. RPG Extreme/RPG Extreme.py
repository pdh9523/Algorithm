import sys; input = lambda: sys.stdin.readline().rstrip()


class Monster:
    def __init__(self, name, attack, defense, hp, exp):
        self.name = name
        self.attack = int(attack)
        self.defense = int(defense)
        self.hp = int(hp)
        self.exp = int(exp)


class User:
    def __init__(self):
        self.level = 1
        self.max_hp = 20
        self.attack = 2
        self.defense = 2
        self.weapon = 0
        self.armor = 0
        self.exp = 0
        self.hp = self.max_hp
        self.accessaries = set()
        self.status = "Press any key to continue."    

    def check_turn(self):        
        if self.exp >= self.level * 5:
            self.level += 1
            self.exp = 0
            self.attack += 2
            self.defense += 2
            self.max_hp += 5
            self.hp = self.max_hp
    
    def _win(self, dmg, exp):
        w = 1.2 if "EX" in self.accessaries else 1
        self.hp -= dmg
        self.exp += int(exp*w)
        self.hp += 3 if "HR" in self.accessaries else 0
        self.hp = min(self.hp, self.max_hp)
        return True

    def _dead(self, cause):
        self.hp = 0
        self.status = f"YOU HAVE BEEN KILLED BY {cause}.."
        return False
    
    def battle(self, monster: Monster, is_boss: bool):
        user_atk = self.attack + self.weapon
        user_def = self.defense + self.armor

        weight = 1
        if "CO" in self.accessaries:
            weight += 1 + ("DX" in self.accessaries)
        
        monster.hp -= max(1, user_atk * weight - monster.defense)
        if monster.hp <= 0: 
            return self._win(0, monster.exp)
        
        if "HU" in self.accessaries and is_boss:
            self.hp = self.max_hp
        else:
            self.hp -= max(1, monster.attack - user_def)
            if self.hp <= 0: 
                return self._dead(monster.name)

        user_hit = (monster.hp-1) // max(1, user_atk - monster.defense) + 1
        monster_hit = (self.hp-1) // max(1, monster.attack - user_def) + 1

        if user_hit > monster_hit:
            return self._dead(monster.name)
        
        return self._win(max(1, monster.attack - user_def) * (user_hit-1), monster.exp)

    def trapped(self):
        self.hp -= 1 if "DX" in self.accessaries else 5
        if self.hp <= 0:
            self._dead("SPIKE TRAP")

    def get_item(self, category, value):
        if category == "O":
            if len(self.accessaries) > 3: return
            self.accessaries.add(value)
            
        elif category == "W":
            self.weapon = int(value)
        elif category =="A":
            self.armor = int(value)

    def get_info(self):
        print(f"LV : {self.level}")
        print(f"HP : {self.hp}/{self.max_hp}")
        print(f"ATT : {self.attack}+{self.weapon}")
        print(f"DEF : {self.defense}+{self.armor}")
        print(f"EXP : {self.exp}/{self.level*5}")
        print(self.status)

def find(char):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == char:
                return i,j

cmd = {
    "L": (0,-1),
    "R": (0,1),
    "U": (-1,0),
    "D": (1,0)
}

user = User()

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
command = input()
monster_cnt = 0
box_cnt = 0 
for i in range(N):
    for j in range(M):
        monster_cnt += arr[i][j] == "&" or arr[i][j] == "M"
        box_cnt += arr[i][j] == "B"

info_map = [[None] * M for _ in range(N)]
for _ in range(monster_cnt):
    x,y,name,attack,defense,hp,exp = input().split()
    x,y = int(x)-1, int(y)-1
    info_map[x][y] = Monster(name, attack, defense, hp, exp)

for _ in range(box_cnt):
    x,y,category,value = input().split()
    x,y = int(x)-1, int(y)-1
    info_map[x][y] = (category, value)

sx,sy = find("@")
arr[sx][sy] = "."

x,y = sx,sy
for i,c in enumerate(command, start=1):
    dx,dy = cmd[c]
    nx,ny = x+dx, y+dy
    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != "#":
        x,y = nx,ny
    
    if arr[x][y] == "^":
        user.trapped()
    
    if arr[x][y] == "B":
        user.get_item(*info_map[x][y])
        arr[x][y] = "."

    if arr[x][y] == "M" or arr[x][y] == "&":
        res = user.battle(info_map[x][y], arr[x][y] =="M")
        
        if res:
            if arr[x][y] == "M":
                user.check_turn()
                user.status = "YOU WIN!"
                break
            arr[x][y] = "."
        
    user.check_turn()
    if user.hp <= 0:
        if "RE" in user.accessaries:
            user.hp = user.max_hp
            x,y = sx,sy
            user.accessaries.discard("RE")
            user.status = "Press any key to continue."
        else:
            break

if user.hp > 0:
    arr[x][y] = "@"

for a in arr:
    print(*a, sep ="")
print(f"Passed Turns : {i}")
user.get_info()