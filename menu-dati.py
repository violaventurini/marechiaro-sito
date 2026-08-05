# -*- coding: utf-8 -*-
"""Il menu vero, trascritto dal PDF A5 bilingue. Unica fonte per IT ed EN."""

# (nome_it, nome_en, descr_it, descr_en, prezzo, allergeni)
PROPOSTE = [
 ("Spaghetti con i lupini","Spaghetti with lupin clams","","","16","1, 14"),
 ("Spaghetti al pomodoro fresco e basilico","Spaghetti with fresh tomato and basil","","","14",""),
 ("Paccheri con puttanesca di tonno","Paccheri with tuna puttanesca","","","14","1, 4"),
 ("Saut&eacute; di cozze","Saut&eacute;ed mussels","","","12","1, 14"),
 ("Insalata di mare","Seafood salad","","","13",""),
 ("Frittura di calamari e gamberi","Fried squid and prawns","","","18","1, 14"),
 ("Tagliata di tonno con rucola e grana","Sliced tuna with rocket and Grana","","","20","4, 7"),
 ("Tartare di tonno con avocado","Tuna tartare with avocado","","","16","4"),
]

SFIZI = [
 ("Moscardino","Moscardino","Cartoccio di moscardini, maionese al limone.","Baby octopus in a cone, lemon mayonnaise.","12","1, 3, 7"),
 ("Orto","Orto","Tempura di verdure, maionese al prezzemolo.","Vegetable tempura, parsley mayonnaise.","10","3"),
 ("Minions","Minions","Suppl&igrave;, panzerotto e crocchetta (1 pz).","Suppl&igrave;, panzerotto and croquette (1 pc).","8","1, 3, 7"),
 ("Chips Marechiaro","Chips Marechiaro","Patate sfoglia fritte e maionese della casa.","Crispy sliced potatoes, house mayonnaise.","6","3"),
 ("Poldo","Poldo","Alette di pollo con salsa buffalo.","Chicken wings with buffalo sauce.","12","7, 9, 10, 12"),
]

PANINI = [
 ("B.L.T.","B.L.T.","Pane bianco, bacon croccante, lattuga, pomodori e maionese.","White bread, crispy bacon, lettuce, tomatoes and mayonnaise.","9","1, 3, 10"),
 ("Tradizionale","Tradizionale","Schiacciata, crudo dolce, mozzarella di bufala, pomodori e pesto di basilico.","Schiacciata, sweet prosciutto crudo, buffalo mozzarella, tomatoes and basil pesto.","11","1, 3, 7"),
 ("Americano","Americano","Pane bun, hamburger, lattuga, pomodoro, salse e chips. Aggiunte: Cheddar 1,50&euro; &middot; Bacon 2&euro;.","Bun, hamburger, lettuce, tomato, sauces and chips. Add: Cheddar 1.50&euro; &middot; Bacon 2&euro;.","11","1, 3, 7, 10"),
 ("Ortolano","Ortolano","Panino morbido, frittata, zucchine e fior di latte.","Soft roll, omelette, courgettes and fior di latte.","9","1, 3, 7"),
]

INSALATE = [
 ("Capri","Capri","Burratina, pomodori, pesto di basilico e olive di Gaeta.","Burrata, tomatoes, basil pesto and Gaeta olives.","10","7"),
 ("Tirreno","Tirreno","Panzanella, cipolle agrodolci, datterini e gamberi.","Panzanella, sweet-and-sour onions, cherry tomatoes and prawns.","8","1, 4, 7, 9, 12"),
 ("Contadina","Contadina","Pollo marinato, lattuga romana, grana padano e pane croccante.","Marinated chicken, romaine lettuce, Grana Padano and crispy bread.","12","1, 3, 7, 10, 12"),
 ("Riviera","Riviera","Misticanza, tonno, fagiolini, patate, datterini, uovo, olive di Gaeta e vinaigrette.","Mixed leaves, tuna, green beans, potatoes, cherry tomatoes, egg, Gaeta olives and vinaigrette.","12","3, 4, 10"),
 ("Marechiaro","Marechiaro","Misticanza, mazzancolle, avocado, variazione di pomodori.","Mixed leaves, king prawns, avocado, tomato variations.","14","2, 3, 9, 10"),
]

PIZZE = [
 ("Margherita","Margherita","Pomodoro, fior di latte, basilico e olio EVO.","Tomato, fior di latte, basil and EVO oil.","","1, 7"),
 ("Diavola","Diavola","Pomodoro, fior di latte, salame e peperoncino.","Tomato, fior di latte, salami and chilli.","","1, 7"),
 ("Marinara","Marinara","Pomodoro, aglio, origano e olio EVO.","Tomato, garlic, oregano and EVO oil.","","1"),
 ("Napoli","Napoli","Pomodoro, fior di latte, acciughe, origano e olio EVO.","Tomato, fior di latte, anchovies, oregano and EVO oil.","","1, 4, 7"),
]

DOLCI = [
 ("Cheesecake ai frutti di bosco","Berry cheesecake","","","6","1, 3, 7"),
 ("Trecciocolati","Trecciocolati","","","6","1, 3, 7"),
 ("Ricotta e pere","Ricotta and pear","","","6","1, 3, 7, 8"),
 ("Frutta","Fresh fruit","","","5",""),
 ("Sorbetto al limone","Lemon sorbet","","","5","7"),
]

# ---- MENU DELLA SERA (nome_it, nome_en, descr_it, descr_en, prezzo, allergeni) ----
SERA_ANTIPASTI = [
 ("Insalata di mare","Seafood salad","","","",""),
 ("Tartare di tonno","Tuna tartare","","","",""),
 ("Catalana di mazzancolle","King prawn catalana","","","",""),
 ("Polpo e patate","Octopus and potatoes","In alternativa: salmone marinato.","Alternative: marinated salmon.","",""),
 ("Salmone marinato","Marinated salmon","","","",""),
 ("Tris mix di mare","Seafood trio","","","",""),
]
SERA_PRIMI = [
 ("Spaghetto con le vongole","Spaghetti with clams","","","",""),
 ("Risotto alla crema di scampi","Risotto with scampi cream","","","",""),
 ("Gnocchetto gamberi e pecorino","Gnocchetti with prawns and pecorino","","","",""),
]
SERA_SECONDI = [
 ("Frittura di calamari e gamberi","Fried squid and prawns","","","",""),
 ("Polpo rosticciato","Roasted octopus","","","",""),
 ("Pesce spada alla piastra","Grilled swordfish","","","",""),
]
