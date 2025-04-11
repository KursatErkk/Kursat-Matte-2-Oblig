# Kursat-Matte-2-Oblig
I dette standardprosjektet ser vi på tilnæringer for dervierte til f ved partielle differentiallikninger, hvor store feil forskjellige metoder gir for tilnærminger, også skal vi vurdere hvilke metoder som er best å bruke i forskjellige situasjoner. 

1. Vi ser her at I starten (f.eks. h = 0.1), får du en grov, men grei tilnærming. Etter hvert som h blir mindre, forbedres tilnærmingen.
Men når h blir for liten (rundt 10^{-8} og mindre), begynner avrundingsfeil å ødelegge nøyaktigheten pga begrenset presisjon i floating-point-tall. 

2. Nå bruker vi sentraldifferanse i steden for framover. Denne gir en bedre numerisk tilnærming, med feil av orden O(h^2) istedenfor O(h). Vi ser dette hvis vi ser på taylor-utvikling på f(x+h) og f(x-h)(Se vedlegg av utregningen). Når man trekker de sammen og deler på 2h ser man at feilen er proposjonal med h^{2}. Det betyr at feilen synker raskere når du reduserer h. For eksempel h = 10^{-1} til 10^{-6}), synker feilen som h^{2}, veldig raskt. Men når h blir for liten (rundt 10^{-8}), kommer avrundingsfeil igjen. Dette er fordi maskinen må regne med forskjellen mellom to nesten like tall.

3. 4-punkts setnraldiffernase er enda bedre og gir enda lavere feil. Feilen minker veldig raskt når h blir mindre, men så møter man på avrundingsfeil igjen. Ved å bruke Taylor-utvidelser for f(x +- h) og f(x +- 2h) og setter disse inn vil førsteordensfeilene og andreordensfeilene kansellere hverandre ut. 
