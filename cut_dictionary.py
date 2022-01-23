def cut_dictionary(input: str, d: set):
    M = [False]*(len(input)+1)
    M[0] = True
    for i in range(1, len(input)+1):
        for j in range(0, i):
            if M[j] and input[j:i] in d:
                M[i] = True
                break
    print(M)
    return M[len(input)]

if __name__ == "__main__":
    print(cut_dictionary("bcoabt", {"bob", "cat", "rob"}))
    print(cut_dictionary("bobcatrob", {"bob", "cat", "rob"}))
