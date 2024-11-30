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




# 작업 클래스
class DoIt:
    def __init__(self, name, sentence, start_date, finish_date, project_person, status="해야 할 일"):
        self.name = name
        self.sentence = sentence
        self.start_date = start_date
        self.finish_date = finish_date
        self.project_person = project_person
        self.status = status  # 작업 상태 (해야 할 일, 진행 중, 완료)

    def __str__(self):
        return (f"작업명: {self.name}, 작업내용: {self.sentence}, 시작일: {self.start_date}, "
                f"마감일: {self.finish_date}, 작업자: {self.project_person}, 상태: {self.status}")

    # 작업 수정
    def update(self):
        print("\n작업 수정 메뉴:")
        self.name = input(f"작업명 [{self.name}]: ") or self.name
        self.sentence = input(f"작업내용 [{self.sentence}]: ") or self.sentence
        self.start_date = input(f"시작일 [{self.start_date}]: ") or self.start_date
        self.finish_date = input(f"마감일 [{self.finish_date}]: ") or self.finish_date
        self.project_person = input(f"작업자 [{self.project_person}]: ") or self.project_person
        new_status = input(f"상태 (해야 할 일, 진행 중, 완료) [{self.status}]: ") or self.status
        if new_status in ["해야 할 일", "진행 중", "완료"]:
            self.status = new_status
        else:
            print("잘못된 상태 입력입니다. 상태를 변경하지 않았습니다.")

# 사용자와 작업 데이터 관리
users = []  # 회원가입된 사용자 목록
tasks = []  # 작업 목록
logged_in_user = User
  # 현재 로그인한 사용자




# 작업 추가
def add_task():
    print("\n작업 추가")
    name = input("작업명을 입력하세요: ")
    sentence = input("작업내용을 입력하세요: ")
    start_date = input("시작일을 입력하세요: ")
    finish_date = input("마감일을 입력하세요: ")
    task_person = input("작업자명을 입력하세요: ")

    if task_person != login_user.name:
        print("작업자명이 로그인된 사용자와 일치하지 않습니다.")
        return

    tasks.append(DoIt(name, sentence, start_date, finish_date, login_user.name))
    print("작업이 추가되었습니다.")

# 작업 수정
def edit_task():


    print("\n작업 수정")
    user_tasks = [task for task in tasks if task.project_person == login_user.name]

    if not user_tasks:
        print("수정할 작업이 없습니다.")
        return

    for i, task in enumerate(user_tasks):
        print(f"{i+1}. {task}")

    task_num = int(input("수정할 작업 번호를 입력하세요: "))
    if 1 <= task_num <= len(user_tasks):
        user_tasks[task_num - 1].update()
        print("작업이 수정되었습니다.")
    else:
        print("잘못된 작업 번호입니다.")

# 작업 상태별 보기
def view_tasks_by_status():


    print("\n작업 상태별 보기")
    status = input("조회할 상태를 입력하세요 (현재 해야 할 일, 현재 진행 중, 현재 완료): ")
    user_tasks = [task for task in tasks if task.project_person == login_user.name and task.status == status]

    if user_tasks:
        for task in user_tasks:
            print(task)
    else:
        print(f"{status} 상태의 작업이 없습니다.")

# 메인 메뉴
def main():
    while True:
        print("\n1. 작업 추가")
        print("2. 작업 수정")
        print("3. 작업 상태별 보기")
        print("4. 종료")
        choice = input("메뉴를 선택하세요: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            edit_task()
        elif choice == "3":
            view_tasks_by_status()
        elif choice == "4":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


# 메인 로직
while True:
    ch = input('로그인(L) 하시겠습니까? 회원가입(J) 하시겠습니까? : ').strip().upper()

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
            main()  # 메인 메뉴로 이동
        else:
            print('로그인에 실패했습니다. 아이디 또는 비밀번호가 일치하지 않습니다.')

    elif ch == 'J':
        print('회원가입 로직입니다.')
        new_user = user_input()
        users.append(new_user)
        save_users_to_file(users)
        print('회원가입이 완료되었습니다.')

    else:
        print("잘못된 입력입니다. 다시 시도하세요.")
