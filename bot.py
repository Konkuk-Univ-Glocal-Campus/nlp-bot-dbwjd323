import random

# 랜덤 응답 리스트에 한국어 응답을 추가합니다.
random_responses = ["그거 정말 흥미로워요. 더 말씀해주세요.",
                    "그렇군요. 계속 이야기해주세요.",
                    "왜 그렇게 말하시나요?",
                    "요즘 날씨 정말 이상하죠?",
                    "주제를 바꿔볼까요?",
                    "어제 경기 보셨나요?"]

print("안녕하세요, 저는 Marvin이라고 합니다. 단순한 로봇입니다.")
print("언제든지 '안녕'을 입력하여 대화를 종료할 수 있습니다.")
print("각 응답을 입력한 후 '엔터' 키를 눌러주세요.")
print("오늘은 어떠신가요?")

while True:
    user_input = input("> ")
    if user_input == "안녕":
        break
    else:
        response = random.choice(random_responses)
    print(response)

print("대화해 주셔서 감사합니다. 안녕히 가세요!")
