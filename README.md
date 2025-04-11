# Kursat-Matte-2-Oblig
I dette standardprosjektet ser vi på tilnæringer for dervierte til f ved partielle differentiallikninger, hvor store feil forskjellige metoder gir for tilnærminger, også skal vi vurdere hvilke metoder som er best å bruke i forskjellige situasjoner. 

1. Vi ser her at I starten (f.eks. h = 0.1), får du en grov, men grei tilnærming. Etter hvert som h blir mindre, forbedres tilnærmingen.
Men når h blir for liten (rundt 10^{-8} og mindre), begynner avrundingsfeil å ødelegge nøyaktigheten pga begrenset presisjon i floating-point-tall. 

2. Nå bruker vi sentraldifferanse i steden for framover. Denne gir en bedre numerisk tilnærming, med feil av orden O(h^2) istedenfor O(h). Vi ser dette hvis vi ser på taylor-utvikling på f(x+h) og f(x-h)(Se vedlegg av utregningen). Når man trekker de sammen og deler på 2h ser man at feilen er proposjonal med h^{2}. Det betyr at feilen synker raskere når du reduserer h. For eksempel h = 10^{-1} til 10^{-6}), synker feilen som h^{2}, veldig raskt. Men når h blir for liten (rundt 10^{-8}), kommer avrundingsfeil igjen. Dette er fordi maskinen må regne med forskjellen mellom to nesten like tall.

3. 4-punkts setnraldiffernase er enda bedre og gir enda lavere feil. Feilen minker veldig raskt når h blir mindre, men så møter man på avrundingsfeil igjen. Ved å bruke Taylor-utvidelser for f(x +- h) og f(x +- 2h) og setter disse inn vil førsteordensfeilene og andreordensfeilene kansellere hverandre ut. 

4. Ut ifra testing ser man at h = k er ofte ustabilt. Når k<<h^{2} blir alpha << 0.5 og metoden blir stabil og trygg, men det blir mange tidssteg.
    Når k >> h^2: Da blir alpha > 0.5 og da blir løsningen ustabil. Du får tall som eksploderer, eller helt feil resultat.

5. Implisitt er bra fordi den er stabil uansett hvor stor alpha er. Man kan da bruke større tidssteg. h = 0.1, k = 0.01 gir liten alpha, h = 0.1, k = 0.1 gir alpha = 10, men den blir fortsatt stabil. h = 0.01, k = 0.1  gir alpha = 1000 som fortsatt er stabil.

6.Vi tar et gjennomsnitt av eksplisitt og implisitt, dette gir tridiagonale matriser A og B. Denne metoden er stabil og 2.ordens nøyaktighet, og mest nøyaktig.

PS: Noen av kodene fungerte først, men når jeg kjørte litt etterpå skrev ikke kodene ut noe selv om det ikke var feilmelding, dette gjelder f.eks opgv 6 og 4.
