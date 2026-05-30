# ============================================================
# 도전 과제 2 - 학생 성적 관리 (Student)
# ============================================================
# 조건:
    # Student class 만들기
        # 속성: name (public), __scores (private, 빈 리스트)
        # add_score(score): 점수 추가. 0~100 범위가 아니면 "유효하지 않은 점수입니다" 출력
        # get_average(): 평균 점수 반환. 점수가 없으면 0 반환
        # get_highest(): 최고 점수 반환
        # get_scores(): 전체 점수 리스트 반환
        # __str__: "이름 (평균: 00.0점, 최고: 00점)" 형태로 출력

    # 테스트:
        # 학생을 만들고 점수 5개를 추가하라. (유효하지 않은 점수 포함)
        # 평균과 최고 점수를 출력하라.
        # __scores에 직접 접근을 시도하라. (에러 확인)
        # Student.__scores = [] 에러가 나지 않는 것에 대한 설명
            # 처음 정의한 self.__scores는 어디로 갔을까???

class Student:
    def __init__(self, name):
        self.name = name
        self.__scores = []

    def __str__(self):
        avg = self.get_average()
        highest = self.get_highest()
        return f"{self.name} (평균: {avg:.1f}점, 최고: {highest}점)"

    def add_score(self, score):
        if score < 0 or score > 100:
            print(f"유효하지 않은 점수입니다! ({score})")
            return
        self.__scores.append(score)
        print(f"{self.name}: {score}점 추가 완료")

    def get_average(self):
        if not self.__scores:
            return 0
        return sum(self.__scores) / len(self.__scores)

    def get_highest(self):
        if not self.__scores:
            return 0
        return max(self.__scores)

    def get_scores(self):
        return self.__scores


# 테스트
student = Student("김철수")

# 점수 추가 (유효하지 않은 점수 포함)
student.add_score(85)
student.add_score(92)
student.add_score(78)
student.add_score(-10)    # 유효하지 않은 점수
student.add_score(150)    # 유효하지 않은 점수
student.add_score(95)
student.add_score(88)

# 결과 출력
print(f"\n전체 점수: {student.get_scores()}")
print(f"평균 점수: {student.get_average():.1f}점")
print(f"최고 점수: {student.get_highest()}점")
print(student)

# __scores 직접 접근 시도
print(student.__scores)  # AttributeError!


# ```

# **출력:**
# ```
# 김철수: 85점 추가 완료
# 김철수: 92점 추가 완료
# 김철수: 78점 추가 완료
# 유효하지 않은 점수입니다! (-10)
# 유효하지 않은 점수입니다! (150)
# 김철수: 95점 추가 완료
# 김철수: 88점 추가 완료

# 전체 점수: [85, 92, 78, 95, 88]
# 평균 점수: 87.6점
# 최고 점수: 95점
# 김철수 (평균: 87.6점, 최고: 95점)
# AttributeError: 'Student' object has no attribute '__scores'


# __slots__

    # Python class는 instance의 속성을 관리하기 위해 내부에 __dict__를 사용한다.
    # 이것은 유연함은 가질 수 있지만 overhead가 크고 object에어 얼마든지 속성을 추가하거나 private 속성에 접근할 수 있다.
    
    # 그래서 Python에서는 __slots__(tuple)을 정의하면 __dict__의 사용을 없애고 정의한 속성외 추가를 막는다.
    # 따라서 메모리 절약, 속도 향상, 속성 추가 방지등의 효과를 만들 수 있다.

