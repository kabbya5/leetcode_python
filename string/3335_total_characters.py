def stringLengthAfterTransrofamtions(s,t):
    MOD = 10**9 + 7
    freq = [0] * 26

    for ch in s:
        freq[ord(ch) - ord('a')] += 1

    for _ in range(t):
        new_freq = [0] * 26
        for i in range(26):
            if i == 25:  # 'z'
                new_freq[0] = (new_freq[0] + freq[i]) % MOD
                new_freq[1] = (new_freq[1] + freq[i]) % MOD
            else:
                new_freq[i + 1] = (new_freq[i + 1] + freq[i]) % MOD
        freq = new_freq

    return sum(freq) % MOD


s = "abcyy"
t = 2

print(stringLengthAfterTransrofamtions(s,t))