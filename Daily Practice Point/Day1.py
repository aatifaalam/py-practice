# # a = b = c = 1
# # print(a)

# # # a1 = "Hello"
# # print('Hello', "World")

# a = "Aalam"

# def Name():
#     a = "Khan"

# Name()
# print('Aatif' , a)

a = [1, 5, 10, 20, 40, 80]
b = [6, 7, 20, 80, 100]
c = [3, 4, 15, 20, 30, 70, 80, 120]

def findCommonElements(a, b, c):
    i = j = k = 0
    result = []

    while i < len(a) and j < len(b) and k < len(c):
        # Skip duplicates safely
        while i > 0 and i < len(a) and a[i] == a[i - 1]:
            i += 1
        while j > 0 and j < len(b) and b[j] == b[j - 1]:
            j += 1
        while k > 0 and k < len(c) and c[k] == c[k - 1]:
            k += 1

        if i >= len(a) or j >= len(b) or k >= len(c):
            break

        if a[i] == b[j] == c[k]:
            result.append(a[i])
            i += 1
            j += 1
            k += 1
        else:
            min_val = min(a[i], b[j], c[k])
            if a[i] == min_val:
                i += 1
            elif b[j] == min_val:
                j += 1
            else:
                k += 1

    return result
print(findCommonElements(a, b, c))