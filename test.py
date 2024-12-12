tab = [4, 8, 1, 5]

def quicksort(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab)//2]

    left = []
    right = []
    middle = []

    for element in tab:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            middle.append(element)
    return quicksort(left) + middle + quicksort(right)
     

print(f"Resultat : {quicksort(tab)}")