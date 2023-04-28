def sliceRect(rect, ratio, direction):
    
    # parameter description
    ## rect: (pos_x, pox_y, size_x, size_y)
    ## ratio: [rate_1, rate_2, ....]
    ## direction: 'horizontal' or 'vertical'
    
    result = []
    
    sumRatio = sum(ratio)
    ratio_ = [x/sumRatio for x in ratio]
    
    
    if direction == 'horizontal': # 가로로 나눔
        for i in range(len(ratio_)):
            pos_x, pos_y, size_x, size_y = rect
            size_y = int(size_y *ratio_[i])
            if i > 0:
                pos_y = int(result[i-1][1] + result[i-1][3])
            result.append((pos_x, pos_y, size_x, size_y))
            
    elif direction == 'vertical': # 세로로 나눔
        for i in range(len(ratio_)):
            pos_x, pos_y, size_x, size_y = rect
            size_x = int(size_x * ratio_[i])
            if i > 0:
                pos_x = int(result[i-1][0] + result[i-1][2])
            result.append((pos_x, pos_y, size_x, size_y))
    
    return result