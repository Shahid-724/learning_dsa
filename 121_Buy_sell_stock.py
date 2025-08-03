def max_profit(arr):
    buy = 0
    profit = 0
    for sell in range(1, len(arr)):
        profit = max(profit, arr[sell] - arr[buy])
        if arr[sell] < arr[buy]:
            buy = sell
    return profit

print(max_profit([7,6,4,3,1]))