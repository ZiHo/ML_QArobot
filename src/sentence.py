
import jieba.posseg as pseg
import synonyms
import random


def generate_synon(sentence):
    sentence_syno =""
    words = pseg.cut(sentence)
    for word, flag in words:
        if(flag == "eng"):
            sentence_syno += word
            continue
        list_synonyms = synonyms.nearby(word)[0]
        if(len(list_synonyms) == 0):
            sentence_syno += word
        else:
            num = random.randint(0,len(list_synonyms)-1)
            sentence_syno += list_synonyms[num]
    similarity = synonyms.compare(sentence, sentence_syno, seg=True)
    sentence_pair = [sentence_syno, similarity]
    return sentence_pair


def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, l, r):
    x = array[r][1]
    i = l - 1
    for j in range(l, r):
        if array[j][1] >= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


words="你们学校是一所什么样的大学？"
sentence_set =[]
for i in range(0,10):
    sentence_set.append(generate_synon(words))
quick_sort(sentence_set,0,len(sentence_set)-1)
print(sentence_set)