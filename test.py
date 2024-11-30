class user :
    def _init_(self,id,password):
        self.id = id
        self.password = password

    def _repr_(self):
        return f'user({self.id},{self.password})'

user = [user{'abc','abc'}]
# users = [{'id':'abc',password:'abc'}]


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



         