from collections import Counter

if __name__ == '__main__':
    s = input()
    counter = Counter(list(s)).most_common()
    ## -x[1] for ascending count like -3, -2, -1
    sort_counter = sorted(counter, key=lambda x: (-x[1], x[0]), reverse=False) 
    for char, count in sort_counter[:3]:
        print(char, count)