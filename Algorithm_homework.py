# 1
def two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] + arr[j] == target:
                return f'{i} and {j}'

    return 'There are no such integers'


list_1 = [0, 1, 3, 6]


print(two_sum(list_1, 9))


# 2
def profit(prices):
    return max(prices) - min(prices)


list_2 = [100, 20, 30, 60]


print(profit(list_2))

# 3
def prod(arr):
    answer = []
    for i in range(len(arr)):
        product = 1
        for j in range(len(arr)):
            if arr[j] != arr[i]:
                product *= arr[j]
        answer.append(product)

    return answer


print(prod([1, 2, 3, 4]))


# 4


# 5
def robber(houses):
    money = 0
    for i in range(0, len(houses), 2):
        for j in range(1, len(houses), 2):
            if houses[i] > houses[j]:
                money += houses[i]

            else:
                money += houses[j]
    return money


list_3 = [1, 2, 3, 1]
print(robber(list_3))
