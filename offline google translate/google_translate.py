from translate import Translator

translator= Translator(to_lang="ja")

try:
    with open("./test.txt", mode="r") as f:
        k=f.read()
        print(k)
        translation = translator.translate(f.read())
        print(translation)
        with open("./translated_file.txt",mode="w") as f2:
           f2.write(translation)
        
except FileNotFoundError as er:
    print("check it")
    print(er)
 
    
    
