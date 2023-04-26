Inițial, ne-am înscris că vom face doar un joc de Tetris.
Insă, după ce l-am facut pe acesta, ne-am dat seama că avem mai mult timp să facem ceva mai complex.
Astfel, am realizat o interfață care leagă trei jocuri: Tetris, Snake si Pong.
Toate jocurile au fost realizate cu ajutorul pygame.

### MAIN:
În main am făcut efectiv o pagină din care să îți alegi ce joc dorești să selectezi, apăsand tasta corespunzătoare.
Astfel, apare o interfață cu poze cu cele trei jocuri din care utilizatorul trebuie să aleagă unul.
Apoi, importând fișierele celorlaltor jocuri am pornit jocul selectat.

### TETRIS:

Avem:
    -o lista de culori pe care le folosim
    -o clasa care contine si gestioneaza figurile
    -clasa Tetris:
        * care contine functii cu toate mutarile pe care le poti face cu figurile in joc
        * retine dimensiunea "tablei de joc"
        * contine functia "start_tetris" care initializeaza interfata paginii de start, cea a jocului in sine si ce care apare atunci cand pierzi jocul; tot aici verificam daca poate sau nu sa inceapa jocul (la pagina de start, daca a fost apasata tasta "SPACE", jocul poate sa inceapa) si pornim jocul propiu-zis

#### Pagina de start:
    -doar un test care spune ce trebuie sa apesi pentru ca jocul sa inceapa

#### Pagina jocului propriu-zis:
    -un timer care iti spune de cate secunde joci
    -scorul care iti arata cate linii ai reusit sa distrugi
    -"tabla de joc" in care vor aparea figurile

#### Pagina de final:
    -text "Game over"
    -apoi apare scorul si timpul pe care l-ai avut
    -text cum poti incepe jocul din nou

#### Controale:
    SPACE - la pagina de start ca sa incepi jocul, dar si ca sa trimiti la pamant figura pe care o ai
    R sau UpArrow - roteste figura
    Left_Arrow - duce figura o patratica spre stanga
    Right_Arrow - duce figura o patratica spre dreapta
    ESC - da restart la joc (indiferent daca ai ajunsa la pagina de start sau nu)

### SNAKE:
Cand este ales jocul acesta, utilizatorului i se deschide jocul, aparand un patratel, capul sarpelui, care are ochi, pentru a putea face distinctia dintre capul si coada sa atunci camd sarpele se va mari. De asemenea, apare si primul mar, snack, pe care trebuie sa il "manance" sarpele ca sa creasca in lungime. Jocul se termina atunci cand utilizatorul intra in el insusi, incercand sa manance din sarpe, iar pe ecran apare un mesaj (intr-un message box) care anunta utilizatorul ca a pierdut, iar in consola apare lungimea sarpelui.


### PONG:
Incepe prin a oferi utilizatorului/utilizatorilor posibilitatea de a customiza elementele din joc (cele 2 paddle uri si bila). 
Cand acesta alege una dintre culori, elementul in discutie apare pe ecran pentru a ii oferi acestuia oportunitatea de a vizualiza aspectul sau. 
Cand decizia este finala, utilizatorul apasa SPACE pentru a seta culorea si a trece la urmatorul element. 
Dupa ce toate obiectele au o culoare definita, va incepe jocul (in cazul in care utilizatorul apasa SPACE fara a selecta anterior o culoare, atunci elementul respetiv va avea culoarea alba, cea standard). 
Pe masura ce bila este pasata de cele doua paddle uri, viteza acesteia va creste constat pentru a ridica nivelul de dificultate al jocului. 
Finalul este atins in momenul in care unul dintre jucatori ajunge la scorul de 10, puncte care pot fi dobandite in momentul in care bila atinge poarta adversarului - peretele din spatele paddle ului. 
Sfarsiul este accentual prin afisarea castigatorul pe ecran si oferirea posibilitatii reinceperii jocului.

## Controale :
- left paddle :
- w -> up
- s -> down 

- right paddle :
- UP ARROW -> up
- DOWN ARROW -> down


## Participanti proiect + contributii:
    * Almajanu Ana - jocul de Sanke
    * Dinu Ema - main, o parte din Tetris
    * Florescu Alexandra - jocul de Pong
    * Ionescu Cristina - Tetris, design aplicatie

