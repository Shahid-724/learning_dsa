def minimumDifference(measurements): 
    # Step 1: Sort the input list 
    measurements.sort() 
     
    # Step 2: Calculate the minimum absolute difference 
    min_diff = float('inf')  # Initialize with a large value 
    for i in range(1, len(measurements)): 
        diff = measurements[i] - measurements[i - 1] 
        min_diff = min(min_diff, diff) 
     
    # Step 3: Identify all pairs with the minimum difference 
    for i in range(1, len(measurements)): 
        if measurements[i] - measurements[i - 1] == min_diff: 
            print(measurements[i - 1], measurements[i])