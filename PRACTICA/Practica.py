inputArray =[3, 6, -2, -5, 7, 3]
def solution(inputArray):
    product = []
    for i in inputArray:
        if product:
            product.append(i)
        else: 
            product.append(product[i-1]*i)
        
    
    return max(product)

solution(inputArray)