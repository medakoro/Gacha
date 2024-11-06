#imports
import random
import math
import sys

#試行回数(-1にしないとバグる)
count = -1
#確率0.6%
input_chance = 6
#凸回数
input_powerup = int(input("凸回数"))

if input_powerup < 0 or input_powerup > 6:
    print("エラー!:不明な凸回数:",input_powerup)
    sys.exit()
#何回シュミレートするか
input_count_simulate = int(input("何回繰り返しますか?"))

#-1回ってなんやねん
if input_count_simulate < 0:
    print("エラー!:不明な凸回数:",input_powerup)
    sys.exit()

#空白なら1回として
elif input_count_simulate == "" or input_count_simulate == 1:
    print("1回としてカウントします")
    input_count_simulate = 1
    bool_average = False

#必要時間(予想)
need_time = input_count_simulate * 0.1

print("カウント:リセット完了 確率:",input_chance/1000,"[%]",input_powerup,"[凸]","回数:",input_count_simulate,"予想必要時間:",need_time,"[sec]")
print("計算を開始します")

#Enterキー待機
input("Press Enter key")

#宣言
count_passing = 0
count_correct = 0
count_failure = 0
roof = 0
count_roof = 0
last_result = False
need_polychrome = 0
need_money = 0
count_simulate = input_count_simulate
count_powerup = input_powerup


#繰り返し処理
while count_simulate > 0:
    #凸の数だけ繰り返す
    while input_powerup >= 0:
        #回数増加
        count += 1
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
                print("\033[44m[!X]",input_chance/1000,"[%]が当選がすり抜けた\033[49m")
                #回数加算
                count_passing += 1
                #すり抜けが発生したため次回は必ず当選
                last_result = True

            else:
                print("\033[41m[!]",input_chance/1000,"[%]が当選\033[49m")
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
                    print("\033[42m[T!X]",input_chance/1000,"[%]が90天井で当選がすり抜けた\033[49m")
                    #回数加算
                    count_passing += 1
                    #すり抜けが発生したため次回は必ず当選
                    last_result = True

                else:
                    print("\033[43m[T!]",input_chance/1000,"[%]が90天井で当選\033[49m")
                    count_correct += 1
                    input_powerup -= 1
                    #当選したため次回不明
                    last_result = False

            #天井ではない
            else:
                #未当選
                print("\033[40m[X] 未当選\033[49m")
                count_failure += 1
                #残天井を減算
                roof += 1
    
    #凸回数を戻す
    input_powerup = count_powerup
    count_simulate -= 1
    print(count_simulate)

print("\033[49m集計終了 | 必要ガチャ回数:",count,"回 10連換算:",count/10,"回 すり抜け回数:",count_passing,"回 当選回数:",count_correct,"回 天井回数:",count_roof,"回\033[49m")
#ポリクローム(モノクローム計算) 1回あたり160ポリクローム必要
need_polychrome = 160 * count
#必要課金額(12000円で6480ポリクローム)
need_money = 12000 * math.ceil(need_polychrome/6480)
print("必要ポリクローム:約",need_polychrome,"個 必要課金額:約¥",need_money," 課金回数:約",math.ceil(need_polychrome/6480),"回\033[49m")

#繰り返し処理
if input_count_simulate >= 1:
    #平均
    print("=====================AVERAGE==================")
    print("\033[49m集計終了 試行回数:",input_count_simulate,"| 平均必要ガチャ回数:",count/input_count_simulate,"回 10連換算:",count/10/input_count_simulate,"回 平均すり抜け回数:",count_passing/input_count_simulate,"回 平均当選回数:",count_correct/input_count_simulate,"回 平均天井回数:",count_roof/input_count_simulate,"回\033[49m")
    print("平均必要ポリクローム:約",need_polychrome/input_count_simulate,"個 平均必要課金額:約¥",need_money/input_count_simulate," 平均課金回数:約",math.ceil(need_polychrome/6480/input_count_simulate),"回\033[49m")

