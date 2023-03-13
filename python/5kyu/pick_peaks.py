# https://www.codewars.com/kata/5279f6fe5ab7f447890006a7

def pick_peaks(arr):
    def is_this_peak(i):
        if arr[i - 1] < (peak := arr[i]):
            return peak > arr[i + 1] or \
                   (peak == arr[i + 1] and peak > next(v for v in arr[i:] + [peak + 1] if v != peak))

    pos = [i for i in range(1, len(arr) - 1) if is_this_peak(i)]
    return {'pos': pos, 'peaks': [arr[i] for i in pos]}


print(pick_peaks([1, 2, 3, 6, 4, 1, 2, 3, 2, 1]), {"pos": [3, 7], "peaks": [6, 3]}, sep='\n', end='\n\n')

print(pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 3]), {'pos': [2, 7, 14, 20], 'peaks': [5, 6, 5, 5]}, sep='\n', end='\n\n')

print(pick_peaks([2, 1, 3, 1, 2, 2, 2, 2]), {"pos": [2], "peaks": [3]}, sep='\n', end='\n\n')
