class User :
    def __init__(self,id,password,name,age,gender,birth):
        self.id = id
        self.password = password
        self.name = name
        self.age = age
        self.gender = gender
        self.birth = birth

    def __repr__(self):
        return f'user({self.id},{self.password},{self.name},{self.age},{self.gender},{self.birth})'
def user_input():
    id = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    name = input("이름을 입력하세요: ")
    age = input("나이를 입력하세요: ")
    gender = input("성별을 입력하세요: ")
    birth = input("생일을 입력하세요: ")
    return User(id, password, name, age, gender,birth)

def save_users_to_file(users, filename="users.json"):
    with open(filename, "w") as file:
        json.dump([user.to_dict() for user in users], file, indent=4)
    print(f"{filename}에 유저 데이터가 저장되었습니다.")


def save_users_to_file(users, filename="users.json"):
    with open(filename, "w") as file:
        json.dump([user.to_dict() for user in users], file, indent=4)
    print(f"{filename}에 유저 데이터가 저장되었습니다.")

user_input()
save_users_to_file()


while True:
    ch = input('로그인(L) 하시겠습니까? 회원가입(J) 하시겠습니까? : ')
    if ch == 'L':
        print('로그인 로직입니다')
        id = input('아이디를 입력하세요 : ')
        password = input('패스워드를 입력하세요 : ')
        login_user = None
        for user in users:
            if user.id == id and user.password == password:
                login_user = userbreak
                break
            if login_user is not name:
                print('로그인에 성공했습니다 : (user)')
            else:
                print('로그인에 실패했습니다')

    elif ch == 'j':
        print('회원가입 실패입니다')
    



         