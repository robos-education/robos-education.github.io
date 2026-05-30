
# 9. 도전 과제 - 은행 계좌 개선
# 조건:
    # Chapter 4의 BankAccount를 가져와 @property로 개선하라
    # BankAccount class 만들기
        # 속성: owner (public), __balance (private, 초기값 0)
        # @property balance: 잔액 읽기
        # @balance.setter: 음수면 0으로 설정
        # deposit(amount): 입금. 0 이하면 "입금액은 0보다 커야 합니다" 출력
        # withdraw(amount): 출금. 잔액보다 크면 "잔액이 부족합니다" 출력
        # __str__: "소유자님의 계좌 (잔액: 0원)" 형태로 출력

    # 테스트:
        # account.balance로 잔액을 읽어라. (get_balance()가 아닌!)
        # 입금, 출금 후 balance를 확인하라.
        # 잔액보다 큰 금액을 출금 시도하라.



class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        # self.__balance = 0
        # setter가 정의 되어 있고 유효성 검사도 되어 있기 때문에
        self.balance = 0 # 추천

    def __str__(self):
        return f"{self.owner}님의 계좌 잔액: {self.balance}원"

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            self.__balance = 0
        else:
            self.__balance = amount

    def deposit(self, amount):

        if amount <= 0:
            print(f"입금액은 0보다 커야 합니다.")
            return
        self.balance += amount
        print(f"{amount}원 입금 완료 (잔액: {self.balance}원)")
        return
    
    def withdraw(self, amount):
        
        if amount <= 0:
            print("출금액은 0보다 커야 합니다!")
            return
        
        if amount > self.balance:
            print(f"잔액이 부족합니다! (현재 잔액: {self.balance}원)")
            return
        
        self.balance -= amount
        print(f"{amount}원 출금 완료 (잔액: {self.balance})")
        return
 

상진 = BankAccount("Park")
상진.deposit(-1)
상진.deposit(250000)
print(상진)
print(상진.balance)

print()
상진.withdraw(350000)
상진.withdraw(150000)

