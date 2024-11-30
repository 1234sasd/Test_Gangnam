class do_it:
    def __init__(self,name,sentence,start_date,finish_date,project_person):
        self.name = name
        self.sentence = sentence
        self.start_date = start_date
        self.finish_date = finish_date
        self.projcet_person = project_person

def user_do_it():
    name = input("작업명을 입력해주세요: ")
    sentence =  input("작업내용을 입력해주세요: ")
    start_data = input("시작일을 입력해주세요: ")
    finish_date = input("마감일을 입력해주세요: ")
    project_person = input("작업자명을 입력해주세요: ")

     return do_it
