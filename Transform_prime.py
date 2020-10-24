
def minimum_number(numbers):
    overall = sum(numbers)
    prime_nums = [3,5]
    for num in range(overall,overall+1000):
        g = 0
        if len(prime_nums)== 3:
            break
        for i in range(2,num//2):
            if num%i == 0:
                g += 1
                pass
            elif i == (num//2)-1 and g == 0:
                prime_nums.append(num)
    small_prime = min(prime_nums, key=lambda x: abs(x - overall))
    if overall < small_prime:
        return small_prime-overall
    elif overall == small_prime:
        return 0
    else:
        index_prime = prime_nums.index(small_prime)+1
        return prime_nums[index_prime] - overall



print(minimum_number([2,12,8,4,6]))