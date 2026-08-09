# -*- coding: utf-8 -*-
"""Tutte le carte del Marechiaro. Unica fonte per italiano e inglese.
   (nome_it, nome_en, descr_it, descr_en, prezzo, allergeni)   '' = assente
   L'asterisco nel nome segnala il prodotto surgelato all'origine."""

PROPOSTE = [
 ("Insalata di mare","Seafood salad","","","15,00",""),
 ("Spaghetti con i lupini","Spaghetti with lupin clams","","","16,00","1, 14"),
 ("Paccheri con puttanesca di tonno","Paccheri with tuna puttanesca","","","14,00","1, 4"),
 ("Saut&eacute; di cozze","Saut&eacute;ed mussels","","","12,00","1, 14"),
 ("Frittura di calamari e gamberi*","Fried squid and prawns*","","","18,00","1, 14"),
 ("Tagliata di tonno con rucola e grana","Sliced tuna with rocket and Grana","","","20,00","4, 7"),
 ("Tartare di tonno","Tuna tartare","","","14,00","4"),
]
SFIZI = [
 ("Moscardino fritto*","Fried baby octopus*","Cartoccio di moscardini, maionese al limone.","Baby octopus in a cone, lemon mayonnaise.","16,00","1, 3, 7"),
 ("Orto","Orto","Tempura di verdure, maionese al prezzemolo.","Vegetable tempura, parsley mayonnaise.","10,00","3"),
 ("Minions*","Minions*","Suppl&igrave;, panzerotto e crocchetta.","Suppl&igrave;, panzerotto and croquette.","8,00","1, 3, 7"),
 ("Chips Marechiaro","Chips Marechiaro","Patate sfoglia fritte e maionese della casa.","Crispy sliced potatoes, house mayonnaise.","6,00","3"),
 ("Poldo*","Poldo*","Alette di pollo con salsa buffalo.","Chicken wings with buffalo sauce.","12,00","7, 9, 10, 12"),
]
INSALATE = [
 ("Capri","Capri","Burratina, pomodori, pesto di basilico e olive di Gaeta.","Burrata, tomatoes, basil pesto and Gaeta olives.","10,00","7"),
 ("Tirreno","Tirreno","Panzanella, cipolle agrodolci, datterini e gamberi.","Panzanella, sweet-and-sour onions, cherry tomatoes and prawns.","8,00","1, 4, 7, 9, 12"),
 ("Contadina","Contadina","Pollo marinato, lattuga romana, grana padano e pane croccante.","Marinated chicken, romaine lettuce, Grana Padano and crispy bread.","12,00","1, 3, 7, 10, 12"),
 ("Riviera","Riviera","Misticanza, tonno, fagiolini, patate, datterini, uovo, olive di Gaeta e vinaigrette.","Mixed leaves, tuna, green beans, potatoes, cherry tomatoes, egg, Gaeta olives and vinaigrette.","12,00","3, 4, 10"),
 ("Marechiaro","Marechiaro","Misticanza, mazzancolle*, avocado, variazione di pomodori.","Mixed leaves, king prawns*, avocado, tomato variations.","14,00","2, 3, 9, 10"),
]
PANINI = [
 ("B.L.T.","B.L.T.","Pane bianco, bacon croccante, lattuga, pomodori e maionese.","White bread, crispy bacon, lettuce, tomatoes and mayonnaise.","9,00","1, 3, 10"),
 ("Tradizionale","Tradizionale","Schiacciata, crudo dolce, mozzarella di bufala, pomodori e pesto di basilico.","Schiacciata, sweet prosciutto crudo, buffalo mozzarella, tomatoes and basil pesto.","11,00","1, 3, 7"),
 ("Americano","Americano","Pane bun, hamburger, lattuga, pomodoro, salse e chips. Aggiunte: cheddar 1,50&nbsp;&euro; &middot; bacon 2&nbsp;&euro;.","Bun, hamburger, lettuce, tomato, sauces and chips. Add: cheddar &euro;1.50 &middot; bacon &euro;2.","16,00","1, 3, 7, 10"),
 ("Ortolano","Ortolano","Panino morbido, frittata, zucchine e fior di latte.","Soft roll, omelette, courgettes and fior di latte.","9,00","1, 3, 7"),
]
_PIZZE_PRANZO_SEGNAPOSTO = []
DOLCI_PRANZO = [
 ("Cheesecake ai frutti di bosco","Berry cheesecake","","","6,00","1, 3, 7"),
 ("Trecciocolati","Trecciocolati","","","6,00","1, 3, 7"),
 ("Ricotta e pere","Ricotta and pear","","","6,00","1, 3, 7, 8"),
 ("Frutta","Fresh fruit","","","5,00",""),
 ("Sorbetto al limone","Lemon sorbet","","","5,00","7"),
]

# ---------------- CENA ----------------
CENA_ANTIPASTI = [
 ("Insalata di mare","Seafood salad","","","15,00",""),
 ("Moscardini fritti*","Fried baby octopus*","","","16,00",""),
 ("Tartare di tonno","Tuna tartare","","","14,00",""),
 ("Catalana","Catalana","Mazzancolle*, pomodoro e cipolla di Tropea.","King prawns*, tomato and Tropea onion.","13,00",""),
 ("Contadina","Contadina","Pollo marinato, lattuga romana, grana padano e pane croccante.","Marinated chicken, romaine lettuce, Grana Padano and crispy bread.","12,00","1, 3, 7, 10, 12"),
 ("Capri","Capri","Burratina, pomodori, pesto di basilico e olive di Gaeta.","Burrata, tomatoes, basil pesto and Gaeta olives.","10,00","7"),
]
CENA_PRIMI = [
 ("Spaghetti con i lupini","Spaghetti with lupin clams","","","16,00","1, 14"),
 ("Pacchero con pachino e gamberi rossi","Paccheri with cherry tomatoes and red prawns","","","17,00","1, 2"),
 ("Risotto alla crema di scampi","Risotto with scampi cream","","","18,00","2, 7"),
]
CENA_SECONDI = [
 ("Tagliata di tonno","Sliced tuna","","","20,00","4"),
 ("Frittura di calamari e gamberi*","Fried squid and prawns*","","","18,00","1, 2, 14"),
 ("Polpo rosticciato","Roasted octopus","","","18,00","14"),
 ("Pesce spada alla griglia","Grilled swordfish","","","18,00","4"),
]
DOLCI_CENA = [
 ("Cheesecake ai frutti di bosco","Berry cheesecake","","","8,00","1, 3, 7"),
 ("Trecciocolati","Trecciocolati","","","8,00","1, 3, 7"),
 ("Ricotta e pere","Ricotta and pear","","","8,00","1, 3, 7, 8"),
 ("Sorbetto al limone","Lemon sorbet","","","8,00","7"),
 ("Bab&agrave;","Bab&agrave;","","","6,00","1, 3, 7"),
 ("Frutta","Fresh fruit","","","6,00",""),
]

# ---------------- APERITIVO ----------------
COCKTAIL = [
 ("Spritz","Spritz","Aperol, Campari, Hugo o Limoncello.","Aperol, Campari, Hugo or Limoncello.","",""),
 ("Mojito","Mojito","","","",""),
 ("Moscow Mule","Moscow Mule","","","",""),
 ("Margarita","Margarita","","","",""),
 ("Paloma","Paloma","","","",""),
 ("Bellini","Bellini","","","",""),
 ("Mimosa","Mimosa","","","",""),
 ("Garibaldi","Garibaldi","","","",""),
 ("Gin tonic","Gin and tonic","","","",""),
 ("Gin lemon","Gin lemon","","","",""),
 ("Vodka lemon","Vodka lemon","","","",""),
 ("J&auml;ger Bomb","J&auml;ger Bomb","","","",""),
]
VINI = [
 ("Falanghina","Falanghina","","","18,00",""),
 ("Chardonnay","Chardonnay","","","18,00",""),
 ("Greco","Greco","","","20,00",""),
 ("Ribolla Gialla","Ribolla Gialla","","","20,00",""),
 ("Prosecco","Prosecco","","","20,00",""),
 ("Traminer","Traminer","","","22,00",""),
 ("Millesimato","Millesimato","","","22,00",""),
 ("Bellavista La Scala","Bellavista La Scala","","","90,00",""),
 ("Ruinart Ros&eacute;","Ruinart Ros&eacute;","","","120,00",""),
]


# ---------------- FORMULE APERITIVO ----------------
FORMULE_APERITIVO = [
 ("Menu fritti aperitivo","Aperitivo fried menu",
  "Un cocktail a scelta dalla carta e i fritti della casa.",
  "One cocktail of your choice from the list and the house fried bites.","15,00",""),
 ("Menu tagliere","Board menu",
  "Un cocktail a scelta dalla carta e il tagliere di salumi e formaggi.",
  "One cocktail of your choice and a board of cured meats and cheeses.","20,00",""),
]

# ---------------- DA CONDIVIDERE (aperitivo) ----------------
CONDIVIDERE = [
 ("Tagliere","Board","Salumi e formaggi, da mettere in mezzo al tavolo.",
  "Cured meats and cheeses, for the middle of the table.","",""),
] + SFIZI

# ---------------- PIZZERIA (sera) ----------------
PIZZE_SERA = [
 ("Bianca","Bianca","Fior di latte e olio EVO.","Fior di latte and EVO oil.","5,00","1, 7"),
 ("Rossa","Rossa","Pomodoro, origano e olio EVO.","Tomato, oregano and EVO oil.","6,00","1"),
 ("Marinara","Marinara","Pomodoro, aglio, origano, alici e olio EVO.","Tomato, garlic, oregano, anchovies and EVO oil.","7,00","1, 4"),
 ("Margherita","Margherita","Pomodoro, fior di latte, basilico e olio EVO.","Tomato, fior di latte, basil and EVO oil.","9,00","1, 7"),
 ("Funghi","Funghi","Pomodoro, fior di latte, funghi e olio EVO.","Tomato, fior di latte, mushrooms and EVO oil.","9,00","1, 7"),
 ("Crostino","Crostino","Fior di latte, prosciutto cotto e olio EVO.","Fior di latte, cooked ham and EVO oil.","9,00","1, 7"),
 ("Boscaiola","Boscaiola","Fior di latte, funghi, salsiccia e olio EVO.","Fior di latte, mushrooms, sausage and EVO oil.","9,50","1, 7"),
 ("Diavolina","Diavolina","Pomodoro, fior di latte, salame, peperoncino, basilico e olio EVO.","Tomato, fior di latte, salami, chilli, basil and EVO oil.","9,50","1, 7"),
 ("Vegetariana","Vegetariana","Fior di latte, zucchine, melanzane, peperoni, funghi e olio EVO.","Fior di latte, courgettes, aubergines, peppers, mushrooms and EVO oil.","9,50","1, 7"),
 ("Napoli","Napoli","Pomodoro, fior di latte, alici, origano e olio EVO.","Tomato, fior di latte, anchovies, oregano and EVO oil.","10,00","1, 4, 7"),
 ("Capricciosa","Capricciosa","Pomodoro, fior di latte, funghi, olive, uovo sodo, prosciutto cotto, basilico e olio EVO.","Tomato, fior di latte, mushrooms, olives, boiled egg, cooked ham, basil and EVO oil.","10,00","1, 3, 7"),
 ("Fiori e alici","Fiori e alici","Fior di latte, fiori di zucca, alici e olio EVO.","Fior di latte, courgette flowers, anchovies and EVO oil.","10,00","1, 4, 7"),
 ("Sfizio di pomodori","Sfizio di pomodori","Pomodoro giallo, pachino, pomodorini secchi, mozzarella di bufala, basilico e olio EVO.","Yellow tomato, Pachino tomatoes, sun-dried cherry tomatoes, buffalo mozzarella, basil and EVO oil.","10,50","1, 7"),
 ("Bufalina","Bufalina","Pomodoro, mozzarella di bufala, basilico e olio EVO.","Tomato, buffalo mozzarella, basil and EVO oil.","11,00","1, 7"),
 ("Bresaola","Bresaola","Fior di latte, bresaola, rucola, grana e olio EVO.","Fior di latte, bresaola, rocket, grana cheese and EVO oil.","11,00","1, 7"),
 ("Primavera","Primavera","Base focaccia, mozzarella di bufala, pomodorini, rucola, scaglie di grana e olio EVO.","Focaccia base, buffalo mozzarella, cherry tomatoes, rocket, grana shavings and EVO oil.","11,00","1, 7"),
 ("Pinna gialla*","Pinna gialla*","Pomodoro giallo, tartare di tonno, stracciata di bufala e rucola.","Yellow tomato, tuna tartare, buffalo stracciata and rocket.","13,00","1, 4, 7"),
]
FRITTI = [
 ("Zeppola fritta*","Fried zeppola*","","","3,00","1, 3, 7"),
 ("Suppl&igrave;*","Suppl&igrave;*","","","3,50","1, 3, 7"),
 ("Montanara*","Montanara*","","","3,50","1, 7"),
 ("Olive ascolane*","Ascolana olives*","","","3,50","1, 3, 7"),
 ("Fiori di zucca*","Courgette flowers*","","","4,00","1, 3, 4, 7"),
 ("Crocch&egrave;*","Crocch&egrave;*","","","8,00","1, 3, 7"),
 ("Cestino fritto*","Fried basket*","","","8,00","1, 3, 7"),
]
FORMULA_PIZZA = [
 ("Menu pizza","Pizza menu",
  "Antipasto di fritti con suppl&igrave;, chips fatte in casa e zeppola. Una pizza a scelta e una bibita analcolica.",
  "Fried starters with suppl&igrave;, home-made crisps and zeppola. One pizza of your choice and a soft drink.","16,00",""),
]


# le pizze del pranzo sono un estratto della carta della pizzeria: stessi prezzi
_SCELTE = ("Marinara","Margherita","Funghi","Capricciosa")
PIZZE = [p for n in _SCELTE for p in PIZZE_SERA if p[0] == n]
