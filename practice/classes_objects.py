lottery_player_dict = {
    'name': "Vivek",
    'lottery_num': (11, 22, 33, 44)
}

print(lottery_player_dict.get('name'))
print(lottery_player_dict.get('lottery_num'))


class LotteryPlayer:
    def __init__(self):
        self.name = "Vivek Kumar"
        self.lottery_num = (11, 22, 33, 44, 55, 66)

    def total(self):
        return sum(self.lottery_num)  # Always self.lottery.num


player_one = LotteryPlayer()
player_two = LotteryPlayer()

print(player_one == player_two)  # False, because both are different instance of LotteryPlayer object
print(player_two.name == player_one.name)  # Returns True


class LotteryPlayerWithVariables:
    def __init__(self, name, lottery_num):
        self.name = name
        self.lottery_num = lottery_num

    def total(self):
        return sum(self.lottery_num)


player_type_one = LotteryPlayerWithVariables("Vivek", (22, 33, 55))
player_type_two = LotteryPlayerWithVariables("Harsha", (66, 77, 88))
