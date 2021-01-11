############### Blackjack Project 
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    select_cards = random.choice(cards)
    return select_cards

user_cards = []
computer_cards = []
for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())



def calculate_score(game_cards):
    '''Take a list of cards and return 計算完的分數'''
    score = 0
    for cards_score in game_cards:
        score += cards_score
    if score > 21 and 11 in game_cards: ## 增加驗證判斷11(Ace)實際的分數
        game_cards.remove(11)
        game_cards.append(1)
        score = 0 
        for cards_score in game_cards:
            score += cards_score
    else: 
        score = 0 
        for cards_score in game_cards:
            score += cards_score
    return score

def add_newcards(current_cards):
    while calculate_score(current_cards) < 17:
        current_cards.append(deal_card())
    return current_cards

#電腦增加卡片跟彼此的現階段計分
computer_score = calculate_score(computer_cards)
user_score = calculate_score(user_cards)

#用戶根據一剛開始的兩張卡和電腦一張卡判斷要不要加,以及遊戲是否繼續
is_game_over = False

while not (is_game_over):
    user_score = calculate_score(user_cards)
    print(f"Your cards:{user_cards}, current score:{user_score}")
    print(f"Computer's first card:{computer_cards[0]}")
    if computer_score == 21 and len(computer_cards) == 2:
        print("computer win the game directly due to blackjack")
        is_game_over = True
    elif user_score == 21 and len(user_cards) == 2:
        print("User win the game directly due to blackjack")
        is_game_over = True
    elif user_score > 21:
        print("User's score is bust, computer win the game")
        is_game_over = True
    else:
        user_should_deal = input("如果你要加牌請回答'y'不要就答'n'. ")
        print(user_should_deal)
        if user_should_deal == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

add_newcards(computer_cards)# 電腦根據卡片狀況決定要不要加卡片


#電腦增加卡片跟更新彼此的現階段計分
computer_score = calculate_score(computer_cards)
user_score = calculate_score(user_cards)


#遊戲最後結果判定
if computer_score > 21: 
    print("User win the game because computer over 21")
elif user_score >21:
    print("Computer win the game because User over 21")
elif computer_score >= user_score or computer_score ==21:
    print("computer win the game")
elif computer_score == user_score:
    print("Draw,平手")

else:
    print("user win the game")

#檢視最終卡片的狀況和分數

print(f"Your cards:{user_cards}, final score:{user_score}")
print(f"Comnputer cards:{computer_cards}, final score:{computer_score}")


