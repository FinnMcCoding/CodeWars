
def order_weight(strng):
    input_nums = strng.split()
    input_sums = []
    for number in input_nums:
        sum = 0
        for digit in number:
            sum += int(digit)
        input_sums.append(sum)

    ref_dict = {}

    n = 0
    for sum in input_sums:
        try:
            ref_dict[sum] = [*ref_dict[sum], input_nums[n]]

        except KeyError:
            ref_dict[sum] = [input_nums[n]]
        n+=1

    for key in ref_dict:
        ref_dict[key].sort()

    captured_keys = []
    input_sums.sort()
    fully_sorted = []
    for val in input_sums:
        if val not in captured_keys:
            for reference in ref_dict[val]:
                fully_sorted.append(reference)
            captured_keys.append(val)
        else:
            pass
    return ' '.join(fully_sorted)



order_weight("103 123 35 44 4444 99 2000 20")