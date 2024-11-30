class User:
    def __init__(self, id, password, name, age, gender, birth):
        self.id = id
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.birth = birth

    def __repr__(self):
        return f'User({self.id}, {self.password}, {self.name}, {self.age}, {self.gender}, {self.birth})'

    # 데이터를 문자열로 변환 (파일 저장용)
    def to_string(self):
        return f"{self.id},{self.password},{self.name},{self.age},{self.gender},{self.birth}"

    # 문자열 데이터를 User 객체로 변환
    @staticmethod
    def from_string(data):
        id, password, name, age, gender, birth = data.strip().split(",")
        return User(id, password, name, int(age), gender, birth)

# 사용자 입력 함수
def user_input():
    id = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    gender = input("성별을 입력하세요: ")
    birth = input("생일을 입력하세요 (YYYY-MM-DD): ")
    return User(id, password, name, int(age), gender, birth)

# 유저 데이터를 파일에 저장
def save_users_to_file(users, filename="users.txt"):
    with open(filename, "w") as file:
        for user in users:
            file.write(user.to_string() + "\n")  # 한 줄에 한 사용자 정보 저장
    print(f"{filename}에 유저 데이터가 저장되었습니다.")

# 파일에서 유저 데이터를 불러오기
def load_users_from_file(filename="users.txt"):
    users = []
    try:
        with open(filename, "r") as file:
            for line in file:
                users.append(User.from_string(line))
    except FileNotFoundError:
        print(f"{filename} 파일이 없습니다. 새로 생성됩니다.")
    return users

# 유저 데이터 관리
users = load_users_from_file()  # 프로그램 시작 시 파일에서 데이터 불러오기

# 메인 로직
while True:
    ch = input('로그인(L) 하시겠습니까? 회원가입(J) 하시겠습니까? (종료하려면 Q 입력): ').strip().upper()
    
    if ch == 'L':
        print('로그인 로직입니다.')
        id = input('아이디를 입력하세요: ')
        password = input('비밀번호를 입력하세요: ')
        login_user = None
        
        for user in users:
            if user.id == id and user.password == password:
                login_user = user
                break

        if login_user:
            print(f'로그인에 성공했습니다: {login_user.name}')
        else:
            print('로그인에 실패했습니다. 아이디 또는 비밀번호가 일치하지 않습니다.')

    elif ch == 'J':
        print('회원가입 로직입니다.')
        new_user = user_input()
        users.append(new_user)
        save_users_to_file(users)
        print('회원가입이 완료되었습니다.')

    elif ch == 'Q':
        print('프로그램을 종료합니다.')
        save_users_to_file(users)
        break

    else:
        print('잘못된 입력입니다. 다시 시도하세요.')
