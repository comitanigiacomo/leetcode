from typing import List 

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        out = sentence.split(" ")
        for i in range(len(out)):
            for root in dictionary:
                if out[i].startswith(root):
                    out[i] = root
        return " ".join(out)
                          
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
sol1 = Solution()
print(sol1.replaceWords(dictionary,sentence))
        