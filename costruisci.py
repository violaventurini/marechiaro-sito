# -*- coding: utf-8 -*-
"""Genera le pagine interne riusando testa, navigazione e footer della home."""
import io, os, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
home = io.open(os.path.join(BASE,'index.html'), encoding='utf-8').read()

NAV = re.search(r'<nav class="nav">.*?</nav>', home, re.S).group(0)
FOOT = re.search(r'<footer>.*?</div>\s*<script', home, re.S).group(0).replace('<script','')

def testa(titolo, descr, path, path_en):
    return '''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="https://marechiaroostia.it%s">
<link rel="alternate" hreflang="it" href="https://marechiaroostia.it%s">
<link rel="alternate" hreflang="en" href="https://marechiaroostia.it%s">
<link rel="alternate" hreflang="x-default" href="https://marechiaroostia.it%s">
<meta name="theme-color" content="#FBF7EF">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:locale" content="it_IT">
<meta property="og:site_name" content="Marechiaro Ostia">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="https://marechiaroostia.it%s">
<meta property="og:image" content="https://marechiaroostia.it/img/og-marechiaro.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,300..600,60..100&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/avorio.css">
</head>
<body>
''' % (titolo, descr, path, path, path_en, path, titolo, descr, path)

def pagina(file, titolo, descr, path, path_en, corpo, schema=''):
    h = testa(titolo, descr, path, path_en)
    h += NAV + '\n' + corpo + '\n' + FOOT + '\n<script src="/avorio.js"></script>\n'
    if schema: h += schema + '\n'
    h += '</body>\n</html>\n'
    io.open(os.path.join(BASE, file), 'w', encoding='utf-8').write(h)
    print('scritto', file, '(%d byte)' % len(h))
