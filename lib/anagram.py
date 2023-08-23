# your code goes here!
# pseudocode
#create a class Anagram that takes a word on initialization
#define a function match that takes a list of possible anagrams 
#check which of them is an  anagram
#if there is no match it should return an empty list

class Anagram:
    def __init__(self,word):
        self.word=word

    def match(self,list=[]):
        given_letters=[letter for letter in self.word]
        matched=[]
        for word in list:
            letters=[letter for letter in word]
            if sorted(given_letters) == sorted (letters):
                 matched.append(word)
        return matched    

listen=Anagram("listen")   
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
word=Anagram("word")
print(word.match(["hello","goodbye"]))
two=Anagram("enlist")
print(two.match(["listen", "silent", "hippopotamus"]))
