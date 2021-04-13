## Requisiti
Il lavoro è stato svolto su sistema operativo windows 10.
E' necessario avere a disposizione tra le variabili d'ambiente un riferimento all'eseguibile di almeno un ottimizzatore : GLPK o CBC e
ad un interprete python che abbia a disposizione la libreria di calcolo numpy. \
Gli script che sotto linux sarebbero stati sviluppati in bash, sono stati scritti per la powershell di windows e hanno estensione .ps1

## Generazione delle istanze
Il file [generator](generator.py) prevede tre argomenti necessari alla generazione delle istanze.cmpl
-   -nodes: lista contenente il numero di nodi da creare (lo script può generare più istanze in sequenza)
-   -pferr: percentuale di attivazione di collegamenti ferroviari.
-   -p: path della folder nel quale le istanze verranno create. Il filename dell'istanza è generato in automatico. 
Le altri costanti necessarie alla creazione del problema, come demand e K, vengono calcolati in automatico in base al numero di nodi che vengono generati.
Per ogni istanza vengono inoltre generate 4 istanze con diversi valori di K.
Lanciando lo script come di seguito :
```console
user@pc:~$ python generator.py -nodes 100 -pferr 0.9 -p pathToExperimentFolder
```

## Valutazione dei risulati
L'ottimizzazione delle istanze *.cmpl* sono state eseguite tramite script powershell lanciando direttamente il solver GLPK o CBC, quindi senza utilizzare wrapper in python o altri linguaggi. Gli script powershell prendono in input una cartella *MainFolder* che deve essere così formata:

- MainFolder/SubFolder/InstanceFolder/Instance1.cmpl ... InstanceN.cmpl

Gli script powershell [Automatize_cmplGLPK.ps1](Automatize_cmplGLPK.ps1) e [Automatize_cmplCBC.ps1](Automatize_cmplCBC.ps1) non necessitano di argomenti e possono essere lanciati come eseguibili,
generandp all'interno di *SubFolder* un .csv per ogni *InstanceFolder* che contiene per ogni Instance.cmpl le seguenti informazioni:

| Name  | Value |
| ------------- | ------------- |
| Istance  | glpkEXEC\inst2\inst_50_01_4\inst_50_01_4_1;glpkEXEC\inst2\inst_50_01_4\inst_50_01_4_2;  |
| gap  | 0.9; 0.0  |
| low  | 18000; 19000  |
| mem  | 276; 51  |
| time  | 304; 18  |
| sol  | 18200; 19000  |

Sono stati necessari due script diversi per GLPK e CBC in quanto i due solver hanno output diversi.

Una volta ottenuti i .csv nella maniera sopra riportata è possibile calcolare media e std delle esecuzioni lanciando lo script [media](media.py) con argomento *-p* il path della folder : *MainFolder*.
L'output di questo script sarà un ulteriore .csv con le seguenti informazioni:

| instance | gap_mean | gap_std |low_mean |low_std |mem_mean | mem_std |sol_mean| sol_std | time_mean | time_std |
| ------------- | ------------- | -------------|------------- |------------- | ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| inst_50_01_4  | 0.45 | 0.45 | 18500 | 500 | 163.5 | 103.5 | 19600 | 400 | 161 | 143|

## Script ausiliari
Lo script [eval_activation](eval_activation.py) prende in input un file .xml contenente la soluzione trovata dal solver e ne stampa il risulato in termini di attivazioni di strade e ferrovie.
## Generazione nuove istanze : Lowering upper bound
Gli script python [colgenGap](colgenGap.py), [colgenCap20](colgenGap20.py) e [colgenGap25](colgengap25.py) prendono in input una istanza .cmpl e ne generano altre utilizzando la tecnica di aggiunta di nuovi nodi a partire da una più piccola soluzione ammissibile, descritta nella relazione a pagina [TODO:pagina].

Una volta generate è possibile lanciare lo script powershell [Automatize_cmplGLPK.ps1](Automatize_cmplGLPK.ps1) per eseguire in batch tutte le ottimizzazioni.

## Generazione nuove istanze: Increasing lower bound 
Lo script python [lagrange](lagrange.py) prende in input due parametri che sono:
-   -p : path al problema .cmpl
-   -l : path alla soluzione .xml generata dal solver per il corrispondente rilassamento
L'output dello script è la scrittura a terminale della soluzione intera ottenuta nel problema originale ma usando gli archi selezionati dalla risoluzione del rilassamento lagrangeano.

## Script per l'esecuzione condizionale del solver
Lo script powershell [solver](solverProblem.ps1) ha due argomenti posizionali:
-   arg1 : path alla cartella dove risiede il problema .cmpl da analizzare
-   arg2 : threshold per esecuzione condizionale dell'istanza ridotta
-   arg3 : path al generatore di istanza modificata per column generation - [colgenTest](colgenTest.py)
\
Lo script nel caso in cui il gap del problema originale sia >= di arg2, creerà un istanza ridotta del problema e risolverà quella.
\
Infine, verrà generato un .csv contenente i risultati del problema originale e di quello ridotto.
\
Per eseguire il test su una singola istanza è necessario lanciare lo script nella maniera seguente, dopo essersi posizionati nella cartella /src:
```console
user@pc:~$ ./solveProblem.ps1 ../dati/test/ 0.8 colgenTest.py
```
