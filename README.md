# Pseudo-Web Scraper in Brainf**k

1. Python used to scrape URL
2. Text converted to ASCII
3. ASCII converted into bf operations

ASCII -> bf logic compares three approaches for each ASCII code:
1. 'Naive' - "+" * ASCII_code
2. Factorisation - finding a,b when a*b = ASCII_code

    * bf code -> "+"*a + "[>]" + "+"*b + "<-]>"
3. Near factorisation - for when there isn't a convenient a,b

We then compare the length of the resulting code for each approach and choose the shortest
NB. There are ***many*** optimisations that could be made to this approach
