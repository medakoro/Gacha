#imports
import random
import math

#試行回数(-1にしないとバグる)
count = -1
#確率0.6%
input_chance = 6
#凸回数
input_powerup = 0
print("カウント:リセット完了 確率:",input_chance/1000,"[%]",input_powerup,"[凸]")
print("計算を開始します")

#宣言
count_passing = 0
count_correct = 0
count_failure = 0
roof = 0
count_roof = 0
last_result = False
need_polychrome = 0
need_money = 0

#凸の数だけ繰り返す
while input_powerup >= 0:
        #回数増加
        count += 1
        #debug
        print(count)
        #1000(0.1%単位で計算)
        result = random.randint(0,1000)

        #当選時
        if result <= input_chance:
            #S級キャラ確定なので天井をリセット
            roof = 1
            count_roof += 1

            #すり抜け判定
            result = random.randint(0,100)

            if (result <= 51) and (last_result == False):
                #すり抜け
                print("[!X]",input_chance/1000,"[%]が当選がすり抜けた")
                #回数加算
                count_passing += 1
                #すり抜けが発生したため次回は必ず当選
                last_result = True

            else:
                print("[!]",input_chance/1000,"[%]が当選")
                count_correct += 1
                input_powerup -= 1
                #当選したため次回不明
                last_result = False

        else:
            #天井判定(90連)
            if roof >= 90:
                #すり抜け判定
                result = random.randint(0,100)
                count_roof += 1
                #天井をリセット
                roof = 1

                if (result <= 51) and (last_result == False):
                    #すり抜け
                    print("[T!X]",input_chance/1000,"[%]が90天井で当選がすり抜けた")
                    #回数加算
                    count_passing += 1
                    #すり抜けが発生したため次回は必ず当選
                    last_result = True

                else:
                    print("[T!]",input_chance/1000,"[%]が90天井で当選")
                    count_correct += 1
                    input_powerup -= 1
                    #当選したため次回不明
                    last_result = False

            #天井ではない
            else:
                #未当選
                print("[X] 未当選")
                count_failure += 1
                #残天井を減算
                roof += 1

print("集計終了 | 必要ガチャ回数:",count,"回 10連換算:",count/10,"回 すり抜け回数:",count_passing,"回 当選回数:",count_correct,"回 天井回数:",count_roof,"回")
#ポリクローム(モノクローム計算) 1回あたり160ポリクローム必要
need_polychrome = 160 * count
#必要課金額(12000円で6480ポリクローム)
need_money = 12000 * math.ceil(need_polychrome/6480)
print("必要ポリクローム:約",need_polychrome,"個 必要課金額:約¥",need_money," 課金回数:約",math.ceil(need_polychrome/6480),"回")
