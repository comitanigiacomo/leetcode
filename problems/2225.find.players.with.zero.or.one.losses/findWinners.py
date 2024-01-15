from pstats import SortKey
from typing import List  

# voglio in pos 0 tutti quelli che non hanno perso neanche un match
# voglio in pos 1 tutti che hanno perso esattamente un match  

# pos 0 : associo ad ogni elemento che incontro per la prima volta un contatore, e metto l'elemento nella lista di pos 1. nel momento in cui re-incontro il contatore, quindi il contatore associato mi va a 1, elimino l'elemento dalla lista ( tengo il contatore per i controlli successivi)
# pos 1:  stessa concetto: associo ad ogni elemento un contatore a zero, che incremento nel momento in cui li incontro che hanno perso. se il contatore è > di zero elimino gli elementi dalla lista 

# ho quindi bisogno di di una struttura dati ausiliaria: combino le due condizioni di pos0 e pos1, e utilizzo una mappa da elemento a intero che mi conta quanti match ha perso.
# eseguo una prima scansione per aggiornare i contatori, successivamente itero sulla mappa e, dove la condizione viene rispettata, aggiungo l'elemento nella lista di pos0 e/o nella lista di pos 1
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        counter = {}
        answer = []
        answer.append([])
        answer.append([])
        for i in range(0,len(matches)) :
            if matches[i][1] not in counter :
                counter[matches[i][1]] = 0
            if matches[i][0] not in counter :
                counter[matches[i][0]] = 0
            counter[matches[i][1]] += 1
        for elem in counter:
            if counter[elem] == 0: 
                answer[0].append(elem)
            elif counter[elem] == 1: 
                answer[1].append(elem)
        answer[0].sort()
        answer[1].sort()
        return(answer)
            
                 
matches = [[2,3],[1,3],[5,4],[6,4]]
sol1 = Solution()
result = sol1.findWinners(matches)
print(result)