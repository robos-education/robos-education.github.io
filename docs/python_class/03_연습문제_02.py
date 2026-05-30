
# ============================================================
# 도전 과제 2 - 음악 플레이리스트 (Playlist)
# ============================================================
# 조건:
    # Song class 만들기
        # 속성: title, artist, duration (초 단위)
        # __str__: "아티스트 - 제목 (0분 00초)" 형태로 return
        # __eq__: 제목과 아티스트가 같으면 같은 곡(이미 포함된 곡 check)

    # Playlist class 만들기
        # 속성: name, songs (빈 리스트)
        # add(song): 곡 추가
        # __len__: 곡 수 return
        # __getitem__: index로 곡 정보 return
        # __str__: "플레이리스트명 (0곡, 총 0분 0초)" 형태로 return
        # __add__: 두 플레이리스트를 합쳐서 새 Playlist return

    # 테스트:
        # Playlist 2개를 만들고 각각 곡을 2~3곡 추가하라.(중복 Test)
        # 두 플레이리스트를 + 연산으로 합쳐보라.
        # 합쳐진 플레이리스트에서 for 문으로 모든 곡을 출력하라.
        # running time 순으로 sorting하라.

class Song:

    # 속성: title, artist, duration (초 단위)
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    # __str__: "아티스트 - 제목 (0분 00초)" 형태로 return
    def __str__(self):
        minutes = self.duration // 60
        seconds = self.duration % 60
        return f"{self.artist} - {self.title} ({minutes}분 {seconds:02d}초)"
    
    # __eq__: 제목과 아티스트가 같으면 같은 곡
    def __eq__(self, other_song):
        # return super().__eq__(other_song) # override 하지 않는 다면 test
        return self.title == other_song.title and self.artist == other_song.artist



# Playlist class 만들기
class Playlist:

    # 속성: name, songs (빈 리스트)
    def __init__(self, name, songs=None):
        self.name = name
        # #### 중요 ####
        # songs parameter에 []을 대입하고 self.songs = songs하면 모든 instance가 같은 list를 공유하게 된다. 
        # object를 만들때 이미 빈 list를 만들어 오기 때문

        self.songs = songs if songs else [] # instance를 만들 때 빈 list를 만들기 때문에 object가 독립적으로 갖는다.

    # add(song): 곡 추가
    def add(self, song):
        # 이미 포함되어 있는 곡 check
        if song in self.songs: # in 연산자 내부는 ==를 사용하기 때문에 Song class의 __eq__ override에 의하여 기존에 있는 음악이 check된다.
            print(f"{song.title}은 이미 추가된 곡입니다.")
            return
        
        self.songs.append(song)

    # __len__: 곡 수 return
    def __len__(self):
        return len(self.songs)
    
    # __getitem__: 인덱스로 곡 접근
    def __getitem__(self, index):
        if index < 0 or index >= len(self.songs):
            print("유효하지 않은 index입니다.")
            return None
        return self.songs[index]
    
    # __str__: "플레이리스트명 (0곡, 총 0분 0초)" 형태로 return
    def __str__(self):

        song_durations = [song.duration for song in self.songs]
        total = sum(song_durations)
        minutes = total//60
        seconds = total % 60
        return f"{self.name} ({len(self.songs)} 곡, 총{minutes}분 {seconds}초)"

    # __add__: 두 플레이리스트를 합쳐서 새 Playlist return
    def __add__(self, other_playlist):
        new_playlist = Playlist(self.name + "_" + other_playlist.name)
        # 먼저 self 의 list 추가하기
        for song in self.songs:
            new_playlist.add(song)
        for song in other_playlist.songs:
            new_playlist.add(song)
        return new_playlist

# rock Playlist 만들기
rock = Playlist("70s 록음악")
rock.add(Song("We Will Rock You", "Queen", 354))
rock.add(Song("아름다운 강산", "신중현", 854))
rock.add(Song("아름다운 강산", "신중현", 854))      # Song class에 __eq__가 override되어 있다면 추가되지 않는다.
print(rock)
print()

st = [Song("밤 편지", "아이유", 325),Song("비처럼 음악처럼", "김현식", 425), Song("그것만이 내 세상", "들국화", 745)]
# 발라드 Playlist 만들기
pop = Playlist("발라드 모음집", st)
print(pop)
print()

# 스페셜 Playlist 만들기(rock + pop)
special_album = rock + pop
print(special_album)

print()
# 전체 곡 list
print(special_album.name + "==============")
# print(special_album.songs) # list에 메모리 주소가 들어 있다. songs에서 __repr__을 override 해야 한다.

# special_album으로 잘못쓰면 itable이 아닌데 index연산(__getitems__)이 있어서 순환이 일어난다.
# class에 __getitem__이 정의되어 있다면, python은 index연산이 가능한 sequence로 판단하고 순서대로 호출한다. 그러나 IndexError가 발생할때까지 멈추지 않게된다. 현재 그러한 오류를 만나지 않기 때문에(return None) 무한 loop가 일어난다.
# 그리고 __getitems__가 오류를 일으키지 않고 return None하기 때문에 무한 반복이 발생

for s in special_album.songs: 
    print(s)

# 4 번째 곡 출력
print(f"special_album의 4 번째 곡은 {special_album[3]}입니다.")

# running time 순으로 sorting
# sorted를 사용하려면 내부적으로 __lt__를 override 해야한다.

# 내부의 list를 정렬하는 방법
special_album.songs.sort(key=lambda song: song.duration)
for s in special_album.songs:
    print(s)


    # 속성: name, songs (빈 리스트)
def __init__(self, name, songs=[]):
    self.name = name
    self.songs = []

    # 여기서 []는 함수가 정의될 때 한 번만 만들어진다.
    # 나중에 songs를 전달하지 않는 모든 instance는 같은 list object를 공유하게 된다.

    # 하지만 
def __init__(self, name, songs=None):
    self.name = name
    self.songs = songs if songs else []

    # 여기서는 self.songs에 의해 곡 list가 없다면 instance가 생성될 때 []만들어 지기 때문에 각각 독립된 list를 가지게 된다.
 