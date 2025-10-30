def metal_rod(prices, n):

    """
    Calculation the maximum revenue from 
    cutting a rod into small pieces
    """  
    if n<=0:
        raise ValueError ("n must b>=0")
                          
    best_value = [0] * (n + 1)     
    best_pieces = []                    
    for i in range(n + 1):
        best_pieces.append([])

    for r in range(1, n + 1):
        for c in range(1, r + 1):
            if c <= len(prices):
                current_value = prices[c - 1] + best_value[r - c]
                if current_value > best_value[r]:
                    best_value[r] = current_value
                    best_pieces[r] = [c] + best_pieces[r - c]

    return best_pieces[n], best_value[n]


prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8

pieces, money = metal_rod(prices, n)

print("list of lengths:", pieces)
print("total money gained:", money)