class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        return " ".join([word +'ma'+ 'a'*(index+1) if word[0].lower() in ['a', 'e', 'i', 'o', 'u'] else word[1:]+word[:1] +'ma'+ 'a'*(index+1) for index, word in enumerate(sentence.split())])
        
