

# ============================================================
# 도전 과제 1 - 은행 계좌 (BankAccount)
# ============================================================
# 조건:
    # BankAccount class 만들기
        # 속성: owner (public), __balance (private, 초기값 0)
        # deposit(amount): 입금. 음수면 "입금액은 0보다 커야 합니다" 출력
        # withdraw(amount): 출금. 잔액보다 크면 "잔액이 부족합니다" 출력
        # get_balance(): 잔액 조회
        # __str__: "소유자님의 계좌 (잔액: 0원)" 형태로 출력

    # 테스트:
        # 계좌를 만들고 입금, 출금을 테스트하라.
        # 잔액보다 큰 금액을 출금 시도하라.
        # __balance에 직접 접근을 시도하라. (에러 확인)

class BankAccount:

    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0

    def __str__(self):
        return f"{self.owner}님의 계좌 잔액: {self.get_balance()}원"

    def get_balance(self):
        return self.__balance
  
    def deposit(self, amount):

        if amount <= 0:
            print(f"입금액은 0보다 커야 합니다.")
            return
        self.__balance += amount
        print(f"{amount}원 입금 완료 (잔액: {self.__balance}원)")
        return
    
    def withdraw(self, amount):
        
        if amount <= 0:
            print("출금액은 0보다 커야 합니다!")
            return
        
        if amount > self.__balance:
            print(f"잔액이 부족합니다! (현재 잔액: {self.__balance}원)")
            return
        
        self.__balance -= amount
        print(f"{amount}원 출금 완료 (잔액: {self.__balance})")
        return
 

상진 = BankAccount("Park")
상진.deposit(-1)
상진.deposit(250000)
print(상진)
print(상진.get_balance())

print()
상진.withdraw(350000)
상진.withdraw(150000)

# print(상진.__balance) # 'BankAccount' object has no attribute '__balance'. Did you mean: 'get_balance'?