# ============================================================
# 도전 과제 1 - 직원 관리 시스템 (Employee)
# ============================================================
# 조건:
    # Employee class 만들기
        # class variable: employee_count (총 직원 수, 초기값 0), company_name
        # instance variable: name, position, salary
        # __init__: 직원 생성 시 employee_count 증가
        # __str__: "이름 (직책) - 연봉: 0원" 형태로 출력
        # @classmethod get_employee_count(cls): 총 직원 수 반환
        # @classmethod set_company_name(cls, name): 회사명 변경
        # @classmethod create_intern(cls, name): 인턴 생성 (position="인턴", salary=24000000)
        # @staticmethod is_valid_salary(salary): 급여가 0 이상이면 True

    # 테스트:
        # 직원 3명을 생성하라. (1명은 create_intern으로)
        # 총 직원 수를 출력하라.
        # 회사명을 변경하고 확인하라.
        # is_valid_salary로 유효성 검사를 테스트하라.

class Employee:

    employee_count = 0  # 총 직원수
    company_name = None

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1
    
    def __str__(self):
        return f"{self.name} ({self.position}) - 연봉: {self.salary}원"
    
    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @classmethod
    def set_company_name(cls, name):
        cls.company_name = name
        print(f"회사명이 '{name}으로 변경되었습니다.")
    
    @classmethod
    def create_intern(cls, name):
        return cls(name, "intern", "2400000")
    
    @staticmethod
    def is_valid_salary(salary):
        if salary >= 0:
            return True
        return False

# Test
em01 = Employee("James", "manager", 5000000)
em02 = Employee("Park", "designer", 5500000)
em03 = Employee.create_intern("Mina")
print(em01)
print(em02)
print(em03)

print(f"총 직원수: {Employee.get_employee_count()}명")
Employee.set_company_name("Tesla")
print(f"회사명: {Employee.company_name}")

# 급여 유효성 검사
print(f"-100 유효: {Employee.is_valid_salary(-100)}")
print(f"500000 유효: {Employee.is_valid_salary(50000)}")
      
# 출력
    # James (manager) - 연봉: 5000000원
    # Park (designer) - 연봉: 5500000원
    # Mina (intern) - 연봉: 2400000원
    # 총 직원수: 3명
    # 회사명이 'Tesla으로 변경되었습니다.
    # 회사명: Tesla
    # -100 유효: False
    # 500000 유효: True