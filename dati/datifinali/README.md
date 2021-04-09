## Dati
I test sono stati divisi in diverse directory per facilitare le diverse tipologie di esecuzioni.

## dati1NewGLPK
In questa cartella sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK.

## dati1NewCbc
In questa cartella sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver CBC.

## dati1NewLAGRANGE
In questa cartella sono presenti tutte le istanze necessarie per il lancio degli esperimenti del duale Lagrangiano con il solver GLPK in cui abbiamo rilassato la formulazione del problema spostando i vincoli di capacità nella funzione obiettivo.

## dati1NEWVALID
In questa cartella sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK con l'aggiunta di vincoli di valid inequalities che impediscano la creazione di percorsi che usano lo stesso collegamento per una data commodity, ossia impedisce la generazione di soluzioni aventi cicli di lunghezza 2.
 
## dati1NewColGen
In questa cartella sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui abbiamo selezionato solo i nodi di partenza e destinazione di tutte le commodity. Questo è un sotto-problema ammissibile nel problema originale.

## dati1NewColGenGap0 &  dati1NewColGenGapSi
In queste cartelle sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui sono presenti le istanze della cartella qui sopra in cui il gap nel problema ridotto è 0 e > 0 e inoltre ad ogni istanza abbiamo aggiunto incrementalmente i 10 nodi strada a costo minimo non ancora inclusi.

## dati1NewColGenBoth
In queste cartelle sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui sono presenti le istanze della cartella ## dati1NewColGen  e inoltre ad ogni istanza abbiamo aggiunto incrementalmente i 10 nodi strada o ferrovia a costo minimo non ancora inclusi.

## dati1NewColGenFerrovie
In queste cartelle sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui sono presenti le istanze della cartella ## dati1NewColGen  e inoltre ad ogni istanza abbiamo aggiunto incrementalmente i 10 nodi ferrovia a costo minimo non ancora inclusi.

## dati1NewColGen25Misto
In queste cartelle sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui sono presenti le istanze della cartella ## dati1NewColGen  e inoltre ad ogni istanza abbiamo aggiunto incrementalmente i 5 nodi strada e 10 ferrovia, 5 nodi strada e 15 ferrovia, 5 nodi strada e 20 ferrovia a costo minimo non ancora inclusi.

## dati1NewColGen25Ferrovie
In queste cartelle sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui sono presenti le istanze della cartella ## dati1NewColGen  e inoltre ad ogni istanza abbiamo aggiunto incrementalmente i 25 nodi ferrovia a costo minimo non ancora inclusi.

## dati1NewColGen25Strade
In queste cartelle sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui sono presenti le istanze della cartella ## dati1NewColGen  e inoltre ad ogni istanza abbiamo aggiunto incrementalmente i 25 nodi strada a costo minimo non ancora inclusi.


## dati1NewColGen20Misto
In queste cartelle sono presenti tutte le istanze necessarie per il lancio degli esperimenti con il solver GLPK in cui sono presenti le istanze della cartella ## dati1NewColGen  e inoltre ad ogni istanza abbiamo aggiunto incrementalmente i 10 nodi strada e 10 ferrovia a costo minimo non ancora inclusi.



