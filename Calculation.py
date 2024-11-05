#imports
import random

#思考回数
count = 0
#確率0.6%
input_chance = 6
#凸回数
input_powerup = input("何回の凸をしますか?")
print("カウント:リセット完了 確率:",input_chance/1000,"[%]",input_powerup,"[凸]")

print("計算を開始します")
#天井180回まで繰り返す
while count < 180:
    #1000(0.1%単位で計算)
    result = random.randint(0,1000)
    #当選時
    if result <= input_chance:
        input("[!]",input_chance/1000,"[%]が当選")
    else:
        input("[X] 未当選")
    count += 1
