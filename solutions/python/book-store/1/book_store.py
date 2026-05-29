"""discounted book basket"""
def total(basket):
    """discounted book basket"""
    receipt = [set()]
    discounts = [0,0,0.05,0.1,0.2,0.25]

    for book in basket:
        for index, group in enumerate(receipt):
            if book not in group:
                group.add(book)
                break
            elif index+1 == len(receipt):
                new_set = {book}
                receipt.append(new_set)
                break

    fives = [group for group in receipt if len(group) == 5]
    threes = [group for group in receipt if len(group) == 3]
    
    for five, three in zip(fives, threes):
        move = (five - three).pop()
        five.remove(move)
        three.add(move)
    
    return int(sum(len(group) * 800 * (1-discounts[len(group)]) for group in receipt))