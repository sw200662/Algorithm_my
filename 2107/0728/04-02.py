def fee(minute, distance):
    total_fee = 0
    total_fee += minute * 120
    miunte_insure = minute // 30
    if minute % 30 == 0:
        total_fee += miunte_insure * 525
    else:
        total_fee += (miunte_insure + 1) * 525
    
    if distance <= 100:
        total_fee += distance * 170
    else:
        total_fee += 100 * 170 + (distance - 100) * 85

    return total_fee

# 아래의 코드를 실행하여 출력된 결과를 확인하시오.
print(fee(600, 50))
print(fee(600, 110))