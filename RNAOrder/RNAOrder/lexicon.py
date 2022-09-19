a = input("Please enter the first thing.")
b = input("Please enter the second thing.")
c = input("Please enter the third thing.")

list = [a, b, c]
answer = [a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a]

for q in range(0, 3):
    answer[0] = list[q]
    for w in range(0, 3):
        answer[1] = list[w]
        for e in range(0, 3):
            answer[2] = list[e]
            for r in range(0, 3):
                answer[3] = list[r]
                for t in range(0, 3):
                    answer[4] = list[t]
                    for y in range(0, 3):
                        answer[5] = list[y]
                        for u in range(0, 3):
                            answer[6] = list[u]
                            for i in range(0, 3):
                                answer[7] = list[i]
                                for o in range(0, 3):
                                    answer[8] = list[o]
                                    for p in range(0, 3):
                                        answer[9] = list[p]
                                        for a in range(0, 3):
                                            answer[10] = list[a]
                                            for s in range(0, 3):
                                                answer[11] = list[s]
                                                for d in range(0, 3):
                                                    answer[12] = list[d]
                                                    for f in range(0, 3):
                                                        answer[13] = list[f]
                                                        for g in range(0, 3):
                                                            answer[14] = list[g]
                                                            for h in range(0, 3):
                                                                answer[15] = list[h]
                                                                for j in range(0, 3):
                                                                    answer[16] = list[j]
                                                                    print(''.join(answer))

            

# while n != 0:
#     for i in range(0, n):
#         for j in range(0, 3):
#             answer[i] = list[j]
#             print(answer)
#     n -= 1


# n = int(input("Please enter the amount of things."))
# m = int(input("Please enter the number of arrays you want."))

# for i in range(0, m):
#     for j in range(0, n):
#         result = []
#         result.append(list[j])
#         print(''.join(list))