import random
import time


eng_words = ['Hi','Bye','Task', 'Programm'] #Burada değişkenler oluşturulmuş.
tr_words = ['Merhaba','Hoşça kalın','Görev', 'Program']
score = 0

mode = input("Bir mod seçin: Yeni kelimeler eklemek için 0, çeviri yapmak için 1: \n") # Kullanıcının girdiği bilgiyi değişkene atamış
while ((mode != '0') and (mode != '1')):
    mode = input("Geçersiz sembol! Sadece 0 veya 1 yazın (Yeni kelimeler eklemek için 0, çeviri yapmak için 1) \n") #mode değişkeninin 1 veya 0 değilse kullanıcıdan yeni değer girmesini istemiş

if mode == "1": #eğer girilen değer 1 ise aşağıdaki kodları çalıştırır
    print("Çevirebildiğiniz kadar kelime çevirin! 10 hakkınız var!")
    for i in range(10): #aşağıdaki kodu 10 kez tekrarlar
        number = random.randint(0, len(eng_words)-1)
        print("Tercümesi bu şekilde olmalı: " + eng_words[number])
        if input() == tr_words[number]:
            print("Harika!!!")
            score += 1
        else:
            print("Bir yanlışlık var... Doğru kelime - " + eng_words[number])
else: #eğer değer 0 ise aşağıdaki kodu çalıştırır
    word = input("İngilizce bir kelime yazın: ")
    translate = input("Kelimenin tercümesini yazın: ")
    if len(word) > 0 and len(translate) > 0:
        eng_words.append(word)
        tr_words.append(translate)
        print("Kelime başarıyla eklendi!")
