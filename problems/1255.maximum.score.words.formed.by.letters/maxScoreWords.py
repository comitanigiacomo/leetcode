from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        def can_form(word, freq):
            word_freq = {}
            for char in word:
                if char not in freq or word_freq.get(char, 0) >= freq[char]:
                    return False
                word_freq[char] = word_freq.get(char, 0) + 1
            return True
        
        def calculate_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)
        
        def backtrack(index, current_score, freq):
            if index == len(words):
                return current_score
            
            max_score = current_score
            
            if can_form(words[index], freq):
                
                word_freq = {}
                for char in words[index]:
                    freq[char] -= 1
                    word_freq[char] = word_freq.get(char, 0) + 1
                
                max_score = max(max_score, backtrack(index + 1, current_score + calculate_score(words[index]), freq))
                
                
                for char in words[index]:
                    freq[char] += 1
            
           
            max_score = max(max_score, backtrack(index + 1, current_score, freq))
            
            return max_score
        
        freq = {}
        for letter in letters:
            freq[letter] = freq.get(letter, 0) + 1
        
        return backtrack(0, 0, freq)

words = ["dog", "cat", "dad", "good"]
letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
