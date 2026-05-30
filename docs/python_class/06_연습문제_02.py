
# ============================================================
# 도전 과제 2 - 온도 변환기 (Temperature)
# ============================================================
# 조건:
    # Temperature class 만들기
        # class variable: conversion_count (총 변환 횟수, 초기값 0)
        # instance variable: celsius (섭씨 온도)
        # __str__: "현재 온도: 00°C" 형태로 출력
        # to_fahrenheit(): 화씨로 변환한 값 반환 (공식: celsius * 9/5 + 32)
        # @classmethod from_fahrenheit(cls, f): 화씨를 받아서 Temperature object 생성
        # @classmethod get_conversion_count(cls): 총 변환 횟수 반환
        # @staticmethod is_boiling(celsius): 100도 이상이면 True
        # @staticmethod is_freezing(celsius): 0도 이하이면 True

    # 테스트:
        # 섭씨 온도로 Temperature를 만들고 화씨로 변환하라.
        # from_fahrenheit로 화씨에서 Temperature를 만들어라.
        # is_boiling, is_freezing을 테스트하라.

class Temperature:

    conversion_count = 0

    def __init__(self, temperature):
        self.celsius = temperature
    
    def __str__(self):
        return f"현재 온도: {self.celsius}°C"
    
    def to_fahrenheit(self, celsius):
        Temperature.conversion_count += 1
        return celsius * 9/5 + 32
    
    @classmethod
    def from_fahrenheit(cls, f):
        # 화씨를 Temperatur object를 생성
        cls.conversion_count += 1
        celsius = (f - 32) * 5 / 9
        return cls(celsius)
    
    @classmethod
    def get_conversion_count(cls):
        return cls.conversion_count
    
    @staticmethod
    def is_boiling(celsius):
        if celsius >= 100:
            return True
        return False
    
    @staticmethod
    def is_freezing(celsius):
        if celsius <= 0:
            return True
        return False

# Test
# 섭씨 온도 생성
water = Temperature(31)
print(water)
print(f"화씨로 변환: {water.to_fahrenheit(water.celsius)}°F")

print()
body = Temperature.from_fahrenheit(98.6)
print(f"체온: {body.celsius:.1f}°C")
print(body)

print()
water = Temperature(-2.58)
print(water)
if Temperature.is_boiling(water.celsius):
    print(f"물이 끓고 있습니다.")
elif Temperature.is_freezing(water.celsius):
    print("물이 얼고 있습니다.")
else:
    print("물이 얼거나 끓지 않습니다.")

# 출력
    # 현재 온도: 31°C
    # 화씨로 변환: 87.8°F

    # 체온: 37.0°C
    # 현재 온도: 37.0°C
    
    # 현재 온도: -2.58°C
    # 물이 얼고 있습니다.