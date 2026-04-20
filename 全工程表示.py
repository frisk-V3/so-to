def bubble_sort_visualized(arr):
    n = len(arr)
    print(f"初期状態: {arr}\n" + "-"*30)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"ステップ {i+1}-{j+1}: {arr}")
        if not swapped:
            break
    print("-"*30 + f"\n最終結果: {arr}")

data = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_visualized(data)
