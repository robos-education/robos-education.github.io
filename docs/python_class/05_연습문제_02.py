
# 10. 도전 과제 - 학생 성적 개선
# 조건:
    # Chapter 4의 Student를 @property로 개선하라.
    # Student class 만들기
        # 속성: name (public), __scores (private, 빈 리스트)
        # add_score(score): 점수 추가. 0~100 범위가 아니면 "유효하지 않은 점수입니다" 출력
        # @property average: 평균 점수 반환 (읽기 전용). 점수가 없으면 0 반환
        # @property highest: 최고 점수 반환 (읽기 전용)
        # @property scores: 전체 점수 리스트 반환 (읽기 전용)
        # __str__: "이름 (평균: 00.0점, 최고: 00점)" 형태로 출력

    # 테스트:
        # student.average로 평균을 읽어라. (get_average()가 아닌!)
        # student.scores로 점수 리스트를 읽어라.
        # student.average = 100을 시도하라. (읽기 전용 에러 확인)


class Student:
    def __init__(self, name):
        self.name = name
        self.__scores = []

    def __str__(self):
        avg = self.average
        highest = self.highest
        return f"{self.name} (평균: {avg:.1f}점, 최고: {highest}점)"

    def add_score(self, score):
        if score < 0 or score > 100:
            print(f"유효하지 않은 점수입니다! ({score})")
            return
        self.scores.append(score)
        print(f"{self.name}: {score}점 추가 완료")

    @property
    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    @property
    def highest(self):
        if not self.scores:
            return 0
        return max(self.scores)

    @property
    def scores(self):
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
print(f"\n전체 점수: {student.scores}")
print(f"평균 점수: {student.average:.1f}점")
print(f"최고 점수: {student.highest}점")
print(student)

# print(student.average = 98) # Error
