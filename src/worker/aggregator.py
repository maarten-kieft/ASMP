class Aggregator:
    """"Class responsible for aggregating the received messages"""



#1. je doet een groepering, 
#2. Je groeppeert op uur, pakt max van al die velden en avg van huidig.
#3. Je voegt die toe en verwijdert de source regels.
# dat doe je herhaal je tot er niks te doen is, daarna sleep je een uur
# di tmoet waars op een andere thread draaien