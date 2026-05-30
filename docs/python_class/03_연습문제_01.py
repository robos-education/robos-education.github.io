# ============================================================
# 도전 과제 1 - 온라인 쇼핑몰 상품 (Product)
# ============================================================
# 조건:
    # Product class 만들기
        # 속성: name, price, quantity
        # __str__: "상품명: 가격원 (재고: 수량개)" 형태로 출력
        # __eq__: 상품명과 가격이 같으면 같은 상품으로 판단
        # __lt__: 가격 기준으로 비교 (sorted 가능하도록)
        # __add__: 같은 상품이면 수량을 합친 새 Product 반환
        #          다른 상품이면 "다른 상품은 합칠 수 없습니다" 출력 후 self 반환

    # 테스트:
        # Product 3개를 만들어 리스트에 넣고 가격순으로 정렬해서 출력하라.
        # 같은 상품 2개를 만들고 `+` 연산으로 새로운 상품을 만들어라.

# 

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}: {self.price}원 (재고: {self.quantity}개)"

    # def __repr__(self):
    #     return f"Product('{self.name}', {self.price}, {self.quantity})"

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __add__(self, other):
        if self == other: # if self.__eq__(other):
            return Product(self.name, self.price, self.quantity + other.quantity)
        else:
            print("다른 상품은 합칠 수 없습니다")
            return self

# 테스트
products = [
    Product("키보드", 89000, 5),
    Product("마우스", 35000, 10),
    Product("모니터", 350000, 3)
]

# 가격순 정렬
sorted_products = sorted(products) # __lt__가 있어야 가능하다.
print(sorted_products)
for p in sorted_products:
    print(p)

# __lt__() override가 없다면
# products.sort(key=lambda p: p.price, reverse=False)

# 출력:
# 마우스: 35000원 (재고: 10개)
# 키보드: 89000원 (재고: 5개)
# 모니터: 350000원 (재고: 3개)

# 같은 상품 합치기
stock1 = Product("키보드", 89000, 5)
stock2 = Product("키보드", 89000, 3)
merged = stock1 + stock2
print(merged)

# 출력:
# 키보드: 89000원 (재고: 8개)

# 다른 상품 합치기
stock3 = Product("마우스", 35000, 10)
result = stock1 + stock3
print(result)

# 출력:
# 다른 상품은 합칠 수 없습니다
# 키보드: 89000원 (재고: 5개)

