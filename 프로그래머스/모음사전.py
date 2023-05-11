def solution(word):
    alpa_dict = {'A':0,'E':1,'I':2,'O':3,'U':4}
    word_li = list(word)
    count = 0
    for idx, w in enumerate(word_li):
        #각 자리마다 1+ 알파벳숫자 * 공비수열의 합(1-5^n)/(1-5)
        count += 1 + alpa_dict[w]*((1-5**(5-idx))/(1-5))       
    return count