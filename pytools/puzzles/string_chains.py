def longest_chain(words):
    longest = 1
    for word in words:
        stack = [(word, 0)]
        chain = [word]
        while stack:
            word, i = stack.pop()
            if len(word) < 2:
                if longest < len(chain):
                    longest = len(chain)
                chain.pop()
            elif i < len(word):
                sub = word[:i] + word[i+1:]
                stack.append((word, i+1))
                stack.append((sub, 0))
                chain.append(sub)
            else:
                chain.pop()
    return longest



words = ['a', 'b', 'ba', 'bca', 'bcad']
print(longest_chain(words)) 