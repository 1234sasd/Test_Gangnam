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

# 작업 데이터 관리
tasks = []

# 작업 추가
def add_task():
    print("\n작업 추가")
    name = input("작업명을 입력하세요: ")
    sentence = input("작업내용을 입력하세요: ")
    start_date = input("시작일을 입력하세요: ")
    finish_date = input("마감일을 입력하세요: ")
    project_person = input("작업자를 입력하세요: ")
    tasks.append(DoIt(name, sentence, start_date, finish_date, project_person))
    print("작업이 추가되었습니다.")

# 작업 수정
def edit_task():
    print("\n작업 수정")
    if not tasks:
        print("수정할 작업이 없습니다.")
        return

    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

    task_num = int(input("수정할 작업 번호를 입력하세요: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1].update()
        print("작업이 수정되었습니다.")
    else:
        print("잘못된 작업 번호입니다.")

# 상태별 작업 보기
def view_tasks_by_status():
    print("\n작업 상태별 보기")
    status = input("조회할 상태를 입력하세요 (해야 할 일, 진행 중, 완료): ")
    filtered_tasks = [task for task in tasks if task.status == status]
    if filtered_tasks:
        for task in filtered_tasks:
            print(task)
    else:
        print(f"'{status}' 상태의 작업이 없습니다.")

# 메인 메뉴
def main():
    while True:
        print("\n1. 작업 추가")
        print("2. 작업 수정")
        print("3. 작업 상태별 조회")
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

main()
