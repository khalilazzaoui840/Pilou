# Analyse financière des finalistes à 40 € et plus : rentabilité par commande, valeur client et budgets de test (état au 28/10/2026)

*Note du 28/10/2026 pour le nouveau rapport « produit animalier à 40 € minimum ». Elle chiffre, pour les 5 finalistes de la deuxième recherche, la rentabilité d’une commande, la valeur d’un client sur 12 mois et le budget minimal d’un test sérieux. C’est un travail de calcul sur les notes existantes : aucune recherche web (ni WebSearch, ni WebFetch, ni curl) n’a été faite pour cette note.*

**Méthode et limites (à lire avant d’utiliser un chiffre).**
1. **Données d’entrée.** Les intrants viennent des notes du dossier `Produit animalier à 40 euros minimum/` : `deep_harnais_levage_sourcing.md`, `deep_harnais_levage_marche.md`, `rescreen_etude_precedente.md`, `deep_peluche_replique.md`, `cadeaux_kits_bundles.md`, `deep_porte_chien_et_tente_chat.md`, `chien_balade_voyage_premium.md`, `chat_premium.md` et `chien_confort_senior_premium.md`. Chaque chiffre repris porte sa note et l’URL d’origine citée par cette note. Ces notes reposent sur des extraits de moteur de recherche (preuve indirecte) : il faut ouvrir l’URL avant de montrer un chiffre au client. Les prix fournisseurs sont des prix d’annonce, pas des devis.
2. **Même modèle que la première étude.** Les scripts de la première étude ont été copiés sans modification dans `/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance40/` (`model.py`, `report.py`, `fmt.py`), puis étendus par `model40.py` (nouveaux produits, nouvelles règles) et `report40.py` (tableaux de cette note). Tous les paramètres communs sont ceux de [`analyse_financiere_finalistes.md`](../Produit%20animalier%20gagnant%20pour%20la%20France/analyse_financiere_finalistes.md) §1 (H1 à H34) : TVA 20 %, mix de paiement Shopify Payments, Shopify et applications, Mondial Relay ou Colissimo par tranche de poids, 3PL, emballage et REP, retours 24 / 12 / 5 %, rétrofacturations, **CPA de 94,61 / 39,88 / 14,05 €** (prudent / intermédiaire / optimiste). Le tableau du §1 ne liste que ce qui diffère.
3. **Contrôles automatiques effectués** (dans `model40.py` et `report40.py`) :
   - l’extension reproduit au centime la première étude sur le kit L et la boîte chat, dans les 3 scénarios ;
   - la formule de coût rendu de la note harnais retrouve ses 18 valeurs publiées (3 tailles, mer et air, 3 scénarios) à 1 centime près ;
   - les coûts rendus publiés pour le sac (A1 à A3), l’enclos (B1 à B3), le lit (3 FOB) et le harnais repère (13,36 €) sont retrouvés ;
   - le repère de `deep_porte_chien_et_tente_chat.md` (harnais à 13,36 € de coût rendu, vendu 99,90 €, colis ≤ 1 kg) donne 49,84 € contre 49,83 € dans la note (arrondis intermédiaires) ;
   - Chaque tableau à 8 lignes et chaque budget est recalculé et vérifié : lignes arrondies au centime **avant** les totaux, sommes exactes au centime.
4. **Conventions.** Montants en **€ HT par commande**, sauf mention « TTC » ; la TVA collectée (TTC ÷ 6) n’est pas un revenu. Entreprise **assujettie à la TVA** (publicité Meta et Shopify facturées HT). 1 $ = 0,86 € (HYPOTHÈSE reprise de toutes les notes). **Prudent** = toutes les valeurs défavorables en même temps (test de résistance, pas un scénario probable) ; **intermédiaire** = scénario de référence pour décider ; **optimiste** = toutes les valeurs favorables. Le même CPA est appliqué aux 5 produits, faute de donnée par catégorie ; un panier plus cher convertit en général moins bien, ce que le modèle ne capte pas.
5. **Ce que les marges ne sont pas.** La « marge contributive » et la « marge après publicité » sont calculées **avant** les coûts fixes et de lancement (échantillons, essais, marque, contenus, stock invendu), avant l’impôt, les cotisations, la rémunération du dirigeant et le financement du stock. **Aucune n’est un bénéfice net.**
6. **Statuts.** **SOURCÉ** : chiffre repris d’une note (avec l’URL d’origine). **HYPOTHÈSE** : valeur non sourcée, avec sa raison. **CALCUL** : résultat d’une formule. **CPA observé de Pilou** : 96,61 € par achat en moyenne sur 4 achats (386,44 € de dépense), ou 80,19 € dans l’autre lecture des captures ; chaque tableau donne une ligne de sensibilité à ces deux niveaux.

## 1. Hypothèses qui diffèrent de la première étude

Tout le reste (H1 à H34 de la première étude) est inchangé. Les coûts rendus entrepôt sont **repris des notes produit** quand elles les ont calculés, comme la première étude l’avait fait pour le sac de litière (coût rendu de la note de faisabilité utilisé tel quel).

| # | Paramètre | Prudent | Intermédiaire | Optimiste | Statut | Source (note → URL d’origine) ou raisonnement |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| D1 | Harnais : coût rendu entrepôt par taille, groupage maritime (M / L / XL) | 22,14 / 24,13 / 27,14 € | 14,84 / 16,78 / 18,75 € | 8,91 / 9,87 / 10,84 € | SOURCÉ (calcul de la note) | `deep_harnais_levage_sourcing.md` Q1 : FOB M 9/14/20 $, L 10/16/22 $, XL 11/18/25 $ ancrés sur des fiches intégrales à 5,12–19,90 $ ([Made-in-China](https://www.made-in-china.com/products-search/hot-china-products/Lift_Safety_Harness_Price.html), [Altra](https://altrapet.en.alibaba.com/)) ; agent 5/7,5/10 % ; boîte 0,40/0,90/1,50 $ ; groupage 30/45/60 $/m³ ; contrôle 0/0,30/0,60 € ; droits 2,7 % en 4201 ([tariffnumber](https://www.tariffnumber.com/2026/harness)). Formule recalculée : les 18 valeurs sont retrouvées. |
| D2 | Harnais : coût rendu en aérien (M / L / XL) | 28,50 / 31,76 / 37,32 € | 19,79 / 22,72 / 26,68 € | 12,46 / 14,12 / 16,52 € | SOURCÉ (calcul de la note) | Même note : aérien DDP 5/7/9 $/kg sur le poids taxable max(réel, volume ÷ 6 000) ([Dantful](https://www.dantful.com/ddp-shipping-from-china-to-france/), [Weilong](https://www.weilong-sz.com/ddp-shipping-from-china-to-france/)). Utilisé au §4.2 et pour le premier lot. |
| D3 | Harnais : poids emballé et volume (M / L / XL) | 0,8 / 1,0 / 1,3 kg ; 0,005 / 0,006 / 0,008 m³ | idem | idem | HYPOTHÈSE de la note | Ancrés sur le PetSafe CareLift M et L ≈ 0,9 kg ([desertcart CY](https://www.desertcart.com.cy/products/5516606), [desertcart UY](https://www.desertcart.uy/products/317655031)). Avec le sachet d’expédition du modèle (+60/40/30 g), **M tient en ≤ 1 kg, L et XL passent en ≤ 2 kg** (la note supposait L ≤ 1 kg ; écart chiffré au §4.3). |
| D4 | Harnais : répartition des ventes par taille | M 50 % / L 35 % / XL 15 % | idem | idem | HYPOTHÈSE | Tailles de la note : M 20–36 kg, L 36–57 kg, XL 57–75 kg. Les races de grands chiens les plus identifiées (berger australien 1er, border collie 3e, golden 4e : [I-CAD 2025](https://www.i-cad.fr/uploads/CP_Chiens_Chats_preferes_2025.pdf)) pèsent surtout 20–36 kg ; aucune répartition des chiens par poids n’existe dans les notes. À remplacer par les ventes réelles. |
| D5 | Harnais : paire de poignées de marche (kit et commande additionnelle) | FOB 4,00 $ → 4,59 € | FOB 2,50 $ → 2,78 € | FOB 1,50 $ → 1,59 € | HYPOTHÈSE (coût) + SOURCÉ (repères) | Coût fournisseur non trouvé (note sourcing §2.7). Ancrage : un harnais standard complet coûte 3,40–3,95 $ ([Global Sources](https://www.globalsources.com/Pet-harness/dog-harness-1217432010p.htm), [Global Sources](https://www.globalsources.com/Pet-harness/Pet-harnesses-1196647494p.htm)) ; une paire de poignées utilise moins de matière. Prix de détail du leader : 22,50–26,50 $ ([helpemup](https://helpemup.com/products/walking-loop-handles)). Coût rendu par la formule de la note (D1), 0,15 kg. |
| D6 | Produits à tailles (harnais, sac) : taux de remboursement | 30 % | 12 % | 5 % | HYPOTHÈSE (30 %) + SOURCÉ (12 %, 24 %) | 12 % = animalerie ([Wisepim](https://wisepim.com/fr/ecommerce-industry-insights/pet-supplies)) ; 24 % = France tous secteurs, mode comprise ([blog Shopify citant la Fevad](https://www.shopify.com/fr/blog/retour-e-commerce)). Aucun taux propre à un produit en 3 tailles avant + arrière : le prudent ajoute 6 points au test de résistance de la première étude, pour le risque de taille. |
| D7 | Produits à tailles : échanges gratuits de taille (part des commandes) | 15 % | 8 % | 4 % | HYPOTHÈSE | La note sourcing recommande l’échange gratuit de la 1re taille comme principal levier contre le remboursement ; plaintes de taille chez le leader ([Trustpilot](https://www.trustpilot.com/review/www.helpemup.com), [K9 Mobility](https://www.trustpilot.com/review/k9mobility.co.uk)). Coût d’un échange = port aller + étiquette retour + préparation + emballage + part invendable de l’article rendu (H23). Absent de la première étude (aucun produit à tailles). |
| D8 | Peluche : fabrication à la pièce ; fret aérien groupé, droits et transitaire ; coffret | 65 € ; 12 € ; 1,50 € | 56 € ; 7 € ; 1,50 € | 45 € ; 5 € ; 1,50 € | SOURCÉ (56 €) + HYPOTHÈSE | 56 € ≈ 65 $ par réplique chez Pampanga Teddy Bear Factory (2023, [Aaj English / Reuters](https://english.aaj.tv/news/30317269)), voie principale de `deep_peluche_replique.md` ; 65 € = coûts pessimistes et 45 € = prix négocié visé (`cadeaux_kits_bundles.md` §2, `deep_peluche_replique.md` option A’). Fret, droits (≈ 4,7 % [CP] non vérifié) et coffret : hypothèses de `cadeaux_kits_bundles.md`. |
| D9 | Peluche : litiges de ressemblance (pas de droit de rétractation) | 12 % des commandes | 5 % | 2 % | SOURCÉ (2 %, exclusion) + HYPOTHÈSE | Bien « nettement personnalisé » exclu de la rétractation, art. L. 221-28, 3° ([donneespersonnelles.fr](https://donneespersonnelles.fr/commande-personnalisee-retractation), [Soulier Avocats](https://www.soulier-avocats.com/remboursement-du-consommateur-apres-exercice-de-son-droit-de-retractation-et-notion-de-bien-personnalise/?pdf=33802)) : on ne provisionne pas des retours mais des litiges de ressemblance, **soldés pour moitié par une refabrication et pour moitié par un remboursement sans récupération** (HYPOTHÈSE). 2 % : Cuddle Clones déclare moins de 2 % de remboursements ([Cuddle Clones FR](https://cuddleclones.com/fr/collections/best-sellers-2/products/custom-pet-memorial-plush-cuddle-clone)) ; 5 % et 12 % : `cadeaux_kits_bundles.md`. |
| D10 | Peluche : poids, colis et REP jouets | 0,9 kg ; coffret 35 × 25 × 18 cm (3,15 kg volumétrique) ; 0,50 € | 0,7 kg ; 0,20 € | 0,5 kg ; 0,10 € | HYPOTHÈSE | Peluche de 30–40 cm en coffret (`cadeaux_kits_bundles.md`) ; barème Ecomaison des jouets non trouvé ([Ecomaison, jouets](https://ecomaison.com/en/professionnels/nos-filieres/jouets/)). Passage court en entrepôt : stockage compté comme un article standard. |
| D11 | Sac porte-chien : coût rendu, FOB, volume, droits | 27,73 € (A3 : 25 + 2 $, 0,030 m³, 3,7 %) | 20,21 € (A2 : 18 + 1,5 $, 0,027 m³, 2,7 %) | 13,42 € (A1 : 12 + 1 $, 0,015 m³, 2,7 %) | SOURCÉ (calcul de la note) | `deep_porte_chien_et_tente_chat.md` §3.6 : Fuliya 18,75 $ ([Made-in-China](https://xtflybag.en.made-in-china.com/product-catalog/Pet-Carrier-1.html)), sac moto 17,19–18,63 $ ([Alibaba](https://www.alibaba.com/showroom/large-dog-carrier-motorcycle.html)) ; 4202 92 91 à 2,7 % ([agrégateur](https://custom-tariffs-seo.pages.dev/en/codes/4202-92-with-outer-surface-of-sheeting-of-plastics-or-of-textile-materials)). Valeurs retrouvées par la formule. |
| D12 | Sac porte-chien : poids emballé | 1,5 kg | 1,2 kg | 0,9 kg | HYPOTHÈSE | K9 Air 2 M ≈ 0,45–0,6 kg ([Walmart Business](https://business.walmart.com/ip/107713163)) ; un sac structuré avec ceinture de hanches est plus lourd. Sac de 37 × 13 × 57 cm ([desertcart](https://www.desertcart.tw/products/522349059-the-maxine-one-medium-dog-carrier-by-little-chonk-dog)) : 5,4 à 6,0 kg de poids volumétrique, appliqué en prudent. |
| D13 | Enclos-tente (kit tente + tunnel) : coût rendu, FOB, volume, droits, poids | 24,48 € (21,5 $, 0,036 m³, 12 %, 3,9 kg) | 17,55 € (16,5 $, 0,020 m³, 6,3 %, 1,2 kg) | 10,21 € (9 $, 0,020 m³, 6,3 %, 1,2 kg) | SOURCÉ (P, I) + CALCUL (O) | `deep_porte_chien_et_tente_chat.md` §3.6 : B2 (kit lourd, IKARE 3,9 kg, [Amazon](https://us.amazon.com/IKARE-Outdoor-Enclosure-Foldable-Playpen/dp/B0CG5LZYS6)) et B1 (kit léger, Naielfopet 1,2 kg, [Amazon](https://www.amazon.com/Naielfopet-Enclosures-Playground-Portable-Enclosure/dp/B0CRV43LDM)) ; FOB Kangna et Herui 14,19–21,90 $ (`chat_premium.md` §2.1, [Made-in-China](https://hapet123.en.made-in-china.com/product/dmDRwZHKyYVO/China-Outdoor-Cat-Enclosures-for-Indoor-Cats-Portable-Cat-Tent-Cat-Tunnel-Playhouse.html)). Optimiste : FOB favorable de 8 $ (`chat_premium.md` §2.4) + 1 $ de marquage, même formule. Droits 6,3 % ([Celna24](https://celna24.pl/en/customs-tariff/63079098)) ou 12 % [CP]. |
| D14 | Lit anti-mâchonnement : coût rendu, FOB ; poids emballé | 37,84 € (35 $) ; 6,0 kg | 30,02 € (27 $) ; 4,5 kg | 23,16 € (20 $) ; 3,5 kg | SOURCÉ (coût, calcul de la note) + HYPOTHÈSE (poids) | `chien_confort_senior_premium.md` Q2 : 0,06 m³ roulé ou compressé, droits 6,3 %, ancre à 20 $ pour un lit à mémoire de forme dès 300 pièces ([Alibaba](https://www.alibaba.com/product-introduction/Durable-Waterproof-Memory-Foam-Pet-Bed_60691877113.html)) ; poids dans la fourchette 3–7 kg de la note. Poids volumétrique de 12 kg, appliqué en prudent. |
| D15 | Lit : garantie anti-mâchonnement (lits remplacés) ; éco-participation Ecomaison | 10 % ; 2,00 € | 5 % ; 1,00 € | 2 % ; 0,50 € | HYPOTHÈSE (de la note pour l’intermédiaire) | Promesse de type « 120 Day Chew Proof » ([K9 Ballistics](https://k9ballistics.com/pages/about-us)) ; un lit 600D a été percé en 5 jours ([Chewy](https://www.chewy.com/happycare-textiles-durable-printed/dp/760398)). Montant Ecomaison non trouvé ([guide 2026](https://ecomaison.com/wp-content/uploads/2026/04/Ameublement_GUIDE-DE-LADHERENT_2026_FR.pdf)). Remplacement = coût rendu + port + préparation + emballage, sans retour du lit abîmé. |
| D16 | Transport au-delà de 5 kg (≤ 10 kg) | 24,00 € HT | 14,50 € HT | 14,50 € HT | SOURCÉ | `fr_couts_commerciaux.md` Q2 : Chrono 13 à domicile 3–10 kg (prudent) et Chrono Relais 13 3–10 kg ([La Poste Pro, Chronopost 2026](https://www.laposte.fr/professionnel/tarifs-chronopost)). **Aucun tarif au-delà de 10 kg** : 24,00 € est alors un plancher (lit en prudent). |
| D17 | Stockage des articles encombrants (règle H12 de la première étude, volume ÷ 0,006 m³) | inclus dans les 5,25 € de préparation | sac 1,04 € ; tente 0,77 € ; lit 2,30 € | sac 0,05 € ; tente 0,07 € ; lit 0,20 € | CALCUL | Les notes produit comptaient 0,23 € pour tous les articles (le lit : 1,50 € [H]) ; on applique la règle de la première étude, plus prudente pour les volumes. |
| D18 | Fret du stock en prudent | maritime à 60 $/m³ (valeurs des notes) | — | — | CALCUL (écart) | La première étude prenait le **ferroviaire à 450 $/m³** en prudent. Surcoût par unité s’il était retenu : harnais 1,72 € à 2,76 €, sac 10,43 €, tente 13,52 €, lit 21,39 € (droits compris). Non intégré au prudent, montré au §4.2 pour le harnais. |
| D19 | Commandes additionnelles (accessoire ou 2e peluche) : part des clients qui en passent au moins une en 12 mois | 5 % (peluche 2 %) | 10 % (peluche 5 %) | 20 % (peluche 10 %) | HYPOTHÈSE | Produits durables, sans consommable : même ordre de grandeur que les durables de la première étude (jouet 8/15/25 %, boîte chat 5/10/20 %). 2e commande chez 30 % des réacheteurs (mois 3 puis mois 9), remise de fidélité de 10 % et coût de relance (H30, H31). Détail au §3. |

**Formule de la provision pour retours et remboursements** (première étude, complétée) :
- Produits standard (enclos, accessoires) : taux de remboursement × [HT − (1 − part invendable) × coût rendu + part du port retour payée × port] + rétrofacturations (H22 à H25, inchangés).
- Produits à tailles (harnais, sac) : même remboursement (taux D6) **+ échanges** : taux D7 × [part invendable × coût rendu + 2 × port + préparation + emballage et REP].
- Peluche : **litiges** : taux D9 × [50 % × HT remboursé + 50 % × (refabrication : coût rendu + port + préparation + emballage et REP)] + rétrofacturations ; aucun retour au titre de la rétractation.
- Lit : remboursement standard (24 / 12 / 5 %) **+ garantie** : taux D15 × (coût rendu + port + préparation + emballage, REP et Ecomaison).

## 2. Rentabilité de la première commande : les 8 lignes demandées, par finaliste

**Définition des lignes** (identique à la première étude ; € HT par commande, sauf le prix) : 1. prix TTC payé, livraison en point relais offerte ; 2. chiffre d’affaires HT = TTC ÷ 1,2 ; 3. coût du produit livré = coût rendu entrepôt + préparation et stockage + emballage, encart et REP + transport ; 4. encaissement + Shopify et applications ; 5. provision pour retours, remboursements, échanges, litiges ou garantie, et rétrofacturations ; 6. marge contributive = 2 − 3 − 4 − 5, qui est aussi le **CPA d’équilibre** de la 1re commande ; 7. CPA du scénario ; 8. marge après publicité = 6 − 7, pour la **1re commande d’un nouveau client**. Sous chaque tableau : ROAS d’équilibre (CA TTC ÷ marge, le ROAS affiché par Meta en dessous duquel la publicité perd de l’argent) et **marge après publicité aux CPA observés de Pilou (80,19 € et 96,61 €)**.

### 2.1 Harnais de levage intégral pour grand chien âgé (modèle Help ’Em Up)

**Offres comparées** : « Harnais intégral » (avant + arrière, poignées) à **119 € TTC**, même prix pour M, L et XL, et « Kit mobilité » (harnais + paire de poignées de marche) à **139 € TTC**. Les marges sont des moyennes pondérées par le mix de tailles D4 (M 50 %, L 35 %, XL 15 %). Repères de prix en France (`deep_harnais_levage_marche.md` §2.5) : Help ’Em Up importé 98–173 € chez Zooplus ([Zooplus.fr](https://www.zooplus.fr/shop/chiens/laisses_colliers_chien/petit_chien/9980069045)) et dès 112,90 € chez Physioveto ([Physioveto](https://www.physioveto.com/harnais-portage-chien-help-em-up-harness.html)) ; PetSafe CareLift intégral 50,99–52,99 € ([PetSafe FR](https://www.petsafe.com/fr/p/harnais-de-levage-carelift-de-petsafe/PTV17-16879/)) ; Génia Handy Canis 61,99–78,90 € la seule partie arrière ([La Compagnie des Animaux](https://www.lacompagniedesanimaux.com/harnais-handy-canis-pattes-arrieres-xs.html)). Stock importé par mer et expédié depuis la France.

*Coût rendu entrepôt par taille (valeurs de la note sourcing, € HT par unité) :*

| Article | Mer · Prudent | Mer · Intermédiaire | Mer · Optimiste | Air · Prudent | Air · Intermédiaire | Air · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Taille M (20–36 kg) | 22,14 | 14,84 | 8,91 | 28,50 | 19,79 | 12,46 |
| Taille L (36–57 kg) | 24,13 | 16,78 | 9,87 | 31,76 | 22,72 | 14,12 |
| Taille XL (57–75 kg) | 27,14 | 18,75 | 10,84 | 37,32 | 26,68 | 16,52 |
| **Moyenne pondérée par le mix (50 / 35 / 15)** | **23,59** | **16,11** | **9,54** | **30,96** | **21,85** | **13,65** |
| Paire de poignées de marche (kit) | 4,59 | 2,78 | 1,59 | 5,76 | 3,68 | 2,24 |

*Les 8 lignes demandées, trois scénarios :*

| Ligne (€ par commande) | Harnais 119 € · Prudent | Harnais 119 € · Intermédiaire | Harnais 119 € · Optimiste | Kit harnais + poignées 139 € · Prudent | Kit harnais + poignées 139 € · Intermédiaire | Kit harnais + poignées 139 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 119,00 | 119,00 | 119,00 | 139,00 | 139,00 | 139,00 |
| 2. Chiffre d’affaires HT estimé par commande | 99,17 | 99,17 | 99,17 | 115,83 | 115,83 | 115,83 |
| 3. Coût du produit livré | 37,72 | 24,58 | 15,20 | 43,67 | 28,09 | 17,11 |
| 4. Frais de paiement et de plateforme | 4,95 | 3,13 | 2,34 | 5,48 | 3,49 | 2,64 |
| 5. Provision estimée pour retours et remboursements | 36,63 | 13,25 | 5,27 | 41,78 | 15,14 | 6,07 |
| **6. Marge contributive avant publicité** | **19,87** | **58,21** | **76,36** | **24,90** | **69,11** | **90,01** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−74,74** | **18,33** | **62,31** | **−69,71** | **29,23** | **75,96** |
| CPA d’équilibre (1re commande) | 19,87 | 58,21 | 76,36 | 24,90 | 69,11 | 90,01 |
| ROAS d’équilibre (CA TTC ÷ pub) | 5,99 | 2,04 | 1,56 | 5,58 | 2,01 | 1,54 |
| Marge après pub au CPA observé de 80,19 € | −60,32 | −21,98 | −3,83 | −55,29 | −11,08 | 9,82 |
| Marge après pub au CPA observé de 96,61 € | −76,74 | −38,40 | −20,25 | −71,71 | −27,50 | −6,60 |
| Marge contributive en % du CA HT | 20 % | 59 % | 77 % | 21 % | 60 % | 78 % |

*Détail des lignes 3 à 5 :*

| Détail (€ HT) | Harnais 119 € · Prudent | Harnais 119 € · Intermédiaire | Harnais 119 € · Optimiste | Kit harnais + poignées 139 € · Prudent | Kit harnais + poignées 139 € · Intermédiaire | Kit harnais + poignées 139 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 23,59 | 16,11 | 9,54 | 28,18 | 18,89 | 11,13 |
| Préparation et stockage | 5,25 | 1,99 | 1,02 | 5,95 | 2,72 | 1,34 |
| Emballage d’expédition, encart, REP (et éco-participation) | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 8,08 | 6,03 | 4,39 | 8,74 | 6,03 | 4,39 |
| **= Coût du produit livré** | **37,72** | **24,58** | **15,20** | **43,67** | **28,09** | **17,11** |
| Encaissement | 3,43 | 2,37 | 2,04 | 3,96 | 2,73 | 2,34 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **4,95** | **3,13** | **2,34** | **5,48** | **3,49** | **2,64** |
| Remboursements nets | 29,19 | 11,11 | 4,62 | 33,95 | 12,95 | 5,40 |
| Échanges de taille gratuits | 5,99 | 1,79 | 0,52 | 6,18 | 1,79 | 0,52 |
| Rétrofacturations | 1,45 | 0,35 | 0,13 | 1,65 | 0,40 | 0,15 |
| **= Provision retours, remboursements et échanges** | **36,63** | **13,25** | **5,27** | **41,78** | **15,14** | **6,07** |
| Poids d’expédition retenu et tranche | M ≤ 1 kg ; L ≤ 2 kg ; XL ≤ 2 kg | M ≤ 1 kg ; L ≤ 2 kg ; XL ≤ 2 kg | M ≤ 1 kg ; L ≤ 2 kg ; XL ≤ 2 kg | M ≤ 2 kg ; L ≤ 2 kg ; XL ≤ 2 kg | M ≤ 1 kg ; L ≤ 2 kg ; XL ≤ 2 kg | M ≤ 1 kg ; L ≤ 2 kg ; XL ≤ 2 kg |

*Prix testés (le §4 détaille la structure d’offre) :*

| Offre (prix TTC) | Marge contributive P / I / O | ROAS d’équilibre TTC (I) | Conversion d’équilibre (CPM 13 €, CTR 1,63 %) | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) | Après CPA 96,61 (coûts I) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Harnais intégral à 99,90 € | 9,42 / **44,59** / 61,54 | 2,24 | 1,79 % | 4,71 | −35,60 | −52,02 |
| Harnais intégral à 119 € | 19,87 / **58,21** / 76,36 | 2,04 | 1,37 % | 18,33 | −21,98 | −38,40 |
| Harnais intégral à 129 € | 25,34 / **65,34** / 84,12 | 1,97 | 1,22 % | 25,46 | −14,85 | −31,27 |
| Kit mobilité : harnais + poignées de marche à 139 € | 24,90 / **69,11** / 90,01 | 2,01 | 1,15 % | 29,23 | −11,08 | −27,50 |
| Kit mobilité : harnais + poignées de marche à 149 € | 30,38 / **76,25** / 97,77 | 1,95 | 1,05 % | 36,37 | −3,94 | −20,36 |

**Lecture.**
- **Harnais seul à 119 €** : 58,21 € de marge contributive en intermédiaire (59 % du HT), soit **+18,33 € par première commande** après un CPA de 39,88 €. Le CPA d’équilibre (58,21 €) vaut 1,46 fois le CPA central ; le ROAS d’équilibre est de 2,04.
- **Aux CPA observés de Pilou**, la première commande perd 21,98 € (80,19 €) à 38,40 € (96,61 €). Le kit à 139 € réduit la perte à 11,08 € et 27,50 € ; il dégage 10,90 € de marge de plus que le harnais seul pour 20 € de prix en plus.
- **En prudent**, la marge reste positive (19,87 € à 119 €) malgré 30 % de remboursements, 15 % d’échanges, le 3PL « coût complet » et Colissimo, mais le CPA de 94,61 € la rend très négative (−74,74 €).
- **Postes les plus lourds après le CPA** : la provision (13,25 €, dont 1,79 € d’échanges) et le transport (6,03 € en moyenne : L et XL passent en tranche de 2 kg). Le coût rendu (16,11 €) ne représente que 14 % du prix TTC.
- **Écart avec les notes** (49,83 € à 99,90 € dans `deep_porte_chien_et_tente_chat.md` ; ici 44,59 €) : coût rendu de 16,11 € en moyenne au lieu de 13,36 €, tranche de 2 kg pour L et XL, échanges de taille provisionnés, stockage volumique du XL. Le prix TTC qui donne 39,88 € de marge passe de 85,94 € (note) à 93,30 €.

### 2.2 Peluche réplique personnalisée (modèle Cuddle Clones)

**Offres comparées** : peluche réplique de 30–40 cm en coffret de marque à **169 € TTC** et à **199 € TTC** (149 € dans le tableau des prix). Fabrication à la pièce dans un atelier asiatique, envoi aérien groupé chaque semaine vers un 3PL français, contrôle, photo de validation, expédition en point relais. Repère : Cuddle Clones à 209,99 $ (≈ 181 €) hors port, **droits et taxes à la charge du client**, fabrication en 8 semaines ([Cuddle Clones FR](https://cuddleclones.com/fr/collections/best-sellers-2/products/custom-pet-memorial-plush-cuddle-clone)).

*Coût rendu entrepôt (€ HT par pièce) :*

| Poste | Prudent | Intermédiaire | Optimiste |
| :--- | ---: | ---: | ---: |
| Fabrication à la pièce | 65,00 | 56,00 | 45,00 |
| Fret aérien groupé, droits, transitaire | 12,00 | 7,00 | 5,00 |
| Coffret de marque et carte | 1,50 | 1,50 | 1,50 |
| **= Coût rendu entrepôt** | **78,50** | **64,50** | **51,50** |

| Ligne (€ par commande) | Peluche 169 € · Prudent | Peluche 169 € · Intermédiaire | Peluche 169 € · Optimiste | Peluche 199 € · Prudent | Peluche 199 € · Intermédiaire | Peluche 199 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 169,00 | 169,00 | 169,00 | 199,00 | 199,00 | 199,00 |
| 2. Chiffre d’affaires HT estimé par commande | 140,83 | 140,83 | 140,83 | 165,83 | 165,83 | 165,83 |
| 3. Coût du produit livré | 98,96 | 72,32 | 56,76 | 98,96 | 72,32 | 56,76 |
| 4. Frais de paiement et de plateforme | 6,27 | 4,02 | 3,08 | 7,06 | 4,55 | 3,54 |
| 5. Provision estimée pour retours et remboursements | 16,34 | 5,80 | 2,16 | 18,14 | 6,51 | 2,44 |
| **6. Marge contributive avant publicité** | **19,26** | **58,69** | **78,83** | **41,67** | **82,45** | **103,09** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−75,35** | **18,81** | **64,78** | **−52,94** | **42,57** | **89,04** |
| CPA d’équilibre (1re commande) | 19,26 | 58,69 | 78,83 | 41,67 | 82,45 | 103,09 |
| ROAS d’équilibre (CA TTC ÷ pub) | 8,77 | 2,88 | 2,14 | 4,78 | 2,41 | 1,93 |
| Marge après pub au CPA observé de 80,19 € | −60,93 | −21,50 | −1,36 | −38,52 | 2,26 | 22,90 |
| Marge après pub au CPA observé de 96,61 € | −77,35 | −37,92 | −17,78 | −54,94 | −14,16 | 6,48 |
| Marge contributive en % du CA HT | 14 % | 42 % | 56 % | 25 % | 50 % | 62 % |

| Détail (€ HT) | Peluche 169 € · Prudent | Peluche 169 € · Intermédiaire | Peluche 169 € · Optimiste | Peluche 199 € · Prudent | Peluche 199 € · Intermédiaire | Peluche 199 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 78,50 | 64,50 | 51,50 | 78,50 | 64,50 | 51,50 |
| Préparation et stockage | 5,25 | 1,98 | 1,02 | 5,25 | 1,98 | 1,02 |
| Emballage d’expédition, encart, REP (et éco-participation) | 1,30 | 0,65 | 0,35 | 1,30 | 0,65 | 0,35 |
| Transport jusqu’au client | 13,91 | 5,19 | 3,89 | 13,91 | 5,19 | 3,89 |
| **= Coût du produit livré** | **98,96** | **72,32** | **56,76** | **98,96** | **72,32** | **56,76** |
| Encaissement | 4,75 | 3,26 | 2,78 | 5,54 | 3,79 | 3,24 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **6,27** | **4,02** | **3,08** | **7,06** | **4,55** | **3,54** |
| Litiges de ressemblance (refabrication ou remboursement) | 14,39 | 5,32 | 1,98 | 15,89 | 5,95 | 2,23 |
| Rétrofacturations | 1,95 | 0,48 | 0,18 | 2,25 | 0,56 | 0,21 |
| **= Provision litiges et rétrofacturations** | **16,34** | **5,80** | **2,16** | **18,14** | **6,51** | **2,44** |
| Poids d’expédition retenu et tranche | 3,15 kg (≤ 5 kg) | 0,74 kg (≤ 1 kg) | 0,53 kg (≤ 1 kg) | 3,15 kg (≤ 5 kg) | 0,74 kg (≤ 1 kg) | 0,53 kg (≤ 1 kg) |

| Offre (prix TTC) | Marge contributive P / I / O | ROAS d’équilibre TTC (I) | Conversion d’équilibre (CPM 13 €, CTR 1,63 %) | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) | Après CPA 96,61 (coûts I) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Peluche réplique à 149 € | 4,33 / **42,85** / 62,65 | 3,48 | 1,86 % | 2,97 | −37,34 | −53,76 |
| Peluche réplique à 169 € | 19,26 / **58,69** / 78,83 | 2,88 | 1,36 % | 18,81 | −21,50 | −37,92 |
| Peluche réplique à 199 € | 41,67 / **82,45** / 103,09 | 2,41 | 0,97 % | 42,57 | 2,26 | −14,16 |

**Lecture.**
- **À 169 €**, la marge contributive intermédiaire est de 58,69 €, soit +18,81 € après un CPA de 39,88 €. **À 199 €**, elle monte à 82,45 € : c’est **la seule offre des cinq finalistes qui couvre le CPA observé de 80,19 €** en coûts intermédiaires (+2,26 €), sans couvrir 96,61 € (−14,16 €).
- **À 149 €** (prix central de `cadeaux_kits_bundles.md`), il ne reste que 42,85 € : le coût de fabrication retenu (56 €, prix public d’un atelier en 2023) est plus élevé que les 45 € de cette note, et les litiges remboursés sont comptés au prix HT.
- **Le coût de fabrication est le paramètre décisif** : ±10 € de fabrication déplacent la marge de 10,25 € (chaque euro de coût rendu retire 1 € plus la part de refabrication des litiges) ; à 45 € de fabrication (prix négocié visé), la marge à 169 € serait de 69,96 €. En prudent (65 € + 12 € de fret), la marge tombe à 19,26 € à 169 € ; en optimiste, elle atteint 78,83 €.
- Les litiges coûtent 5,32 € par commande au taux central de 5 % : la photo de validation avant expédition et une politique de retouche sont des leviers de marge directs.

### 2.3 Sac porte-chien frontal premium pour chiens de 8 à 22 kg (modèle Little Chonk)

**Offres comparées** : sac structuré avec ceinture de hanches à **99 € TTC** et à **119 € TTC** (89 € dans le tableau des prix). Repères : K9 Sport Sack ≈ 112–164 € sur Amazon.fr ([Amazon.fr](https://www.amazon.fr/K9-Sport-Backpack-Adjustable-Veterinarian/dp/B06X1BV1K3)), Ruffwear 116,90 € ([Hardloop](https://www.hardloop.fr/produit/84328-ruffwear-hitch-hiker-backpack-carrier-sac-a-dos-pour-chien-randonnee)), Little Chonk 120 $ ([Tubefilter](https://www.tubefilter.com/2022/01/10/tiktok-famous-corgi-maxine-dog-backpack-little-chonk/amp/)), génériques 15–40 €. Produit à tailles : règles D6 et D7.

| Coût rendu (€ HT, formule de la note) | Prudent (A3) | Intermédiaire (A2) | Optimiste (A1) |
| :--- | ---: | ---: | ---: |
| Achat (FOB × 0,86) | 23,22 | 16,77 | 11,18 |
| Commission d’agent (7,5 %) | 1,74 | 1,26 | 0,84 |
| Fret groupage (60 $/m³) | 1,55 | 1,39 | 0,77 |
| Dédouanement et frais fixes | 0,30 | 0,30 | 0,30 |
| Droits de douane | 0,92 | 0,49 | 0,33 |
| **= Coût rendu entrepôt** | **27,73** | **20,21** | **13,42** |

| Ligne (€ par commande) | Sac 99 € · Prudent | Sac 99 € · Intermédiaire | Sac 99 € · Optimiste | Sac 119 € · Prudent | Sac 119 € · Intermédiaire | Sac 119 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 99,00 | 99,00 | 99,00 | 119,00 | 119,00 | 119,00 |
| 2. Chiffre d’affaires HT estimé par commande | 82,50 | 82,50 | 82,50 | 99,17 | 99,17 | 99,17 |
| 3. Coût du produit livré | 57,78 | 30,31 | 18,61 | 57,78 | 30,31 | 18,61 |
| 4. Frais de paiement et de plateforme | 4,42 | 2,78 | 2,03 | 4,95 | 3,13 | 2,34 |
| 5. Provision estimée pour retours et remboursements | 38,75 | 11,27 | 4,29 | 43,95 | 13,32 | 5,14 |
| **6. Marge contributive avant publicité** | **−18,45** | **38,14** | **57,57** | **−7,51** | **52,41** | **73,08** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−113,06** | **−1,74** | **43,52** | **−102,12** | **12,53** | **59,03** |
| CPA d’équilibre (1re commande) | aucun (marge ≤ 0) | 38,14 | 57,57 | aucun (marge ≤ 0) | 52,41 | 73,08 |
| ROAS d’équilibre (CA TTC ÷ pub) | n.a. (marge ≤ 0) | 2,60 | 1,72 | n.a. (marge ≤ 0) | 2,27 | 1,63 |
| Marge après pub au CPA observé de 80,19 € | −98,64 | −42,05 | −22,62 | −87,70 | −27,78 | −7,11 |
| Marge après pub au CPA observé de 96,61 € | −115,06 | −58,47 | −39,04 | −104,12 | −44,20 | −23,53 |
| Marge contributive en % du CA HT | −22 % | 46 % | 70 % | −8 % | 53 % | 74 % |

| Détail (€ HT) | Sac 99 € · Prudent | Sac 99 € · Intermédiaire | Sac 99 € · Optimiste | Sac 119 € · Prudent | Sac 119 € · Intermédiaire | Sac 119 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 27,73 | 20,21 | 13,42 | 27,73 | 20,21 | 13,42 |
| Préparation et stockage | 5,25 | 2,79 | 1,05 | 5,25 | 2,79 | 1,05 |
| Emballage d’expédition, encart, REP (et éco-participation) | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 24,00 | 6,86 | 3,89 | 24,00 | 6,86 | 3,89 |
| **= Coût du produit livré** | **57,78** | **30,31** | **18,61** | **57,78** | **30,31** | **18,61** |
| Encaissement | 2,90 | 2,02 | 1,73 | 3,43 | 2,37 | 2,04 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **4,42** | **2,78** | **2,03** | **4,95** | **3,13** | **2,34** |
| Remboursements nets | 26,27 | 8,89 | 3,66 | 31,27 | 10,89 | 4,49 |
| Échanges de taille gratuits | 11,23 | 2,08 | 0,52 | 11,23 | 2,08 | 0,52 |
| Rétrofacturations | 1,25 | 0,30 | 0,11 | 1,45 | 0,35 | 0,13 |
| **= Provision retours, remboursements et échanges** | **38,75** | **11,27** | **4,29** | **43,95** | **13,32** | **5,14** |
| Poids d’expédition retenu et tranche | 6,00 kg (≤ 10 kg) | 1,24 kg (≤ 2 kg) | 0,93 kg (≤ 1 kg) | 6,00 kg (≤ 10 kg) | 1,24 kg (≤ 2 kg) | 0,93 kg (≤ 1 kg) |

| Offre (prix TTC) | Marge contributive P / I / O | ROAS d’équilibre TTC (I) | Conversion d’équilibre (CPM 13 €, CTR 1,63 %) | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) | Après CPA 96,61 (coûts I) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Sac porte-chien à 89 € | −23,91 / **31,02** / 49,81 | 2,87 | 2,57 % | −8,86 | −49,17 | −65,59 |
| Sac porte-chien à 99 € | −18,45 / **38,14** / 57,57 | 2,60 | 2,09 % | −1,74 | −42,05 | −58,47 |
| Sac porte-chien à 119 € | −7,51 / **52,41** / 73,08 | 2,27 | 1,52 % | 12,53 | −27,78 | −44,20 |

**Lecture.**
- **À 99 €**, la marge intermédiaire (38,14 €) est juste sous le CPA central : −1,74 € par première commande. Il faut **119 €** pour dégager +12,53 € ; le prix d’équilibre au CPA de 39,88 € est de 101,43 € TTC.
- **Écart avec la note** : à 99,90 €, ce modèle donne 38,79 € contre 41,67 € pour A2 ; l’écart vient du stockage au volume (1,04 € au lieu de 0,23 €) et des échanges de taille (2,08 €).
- **Le prudent est négatif avant toute publicité** (−18,45 € à 99 €) : le sac de 0,03 m³ pèse 6 kg en poids volumétrique et passe en tranche ≤ 10 kg (24,00 € HT), ce qui s’ajoute à 30 % de remboursements. Faire confirmer par le transporteur l’absence de supplément volumétrique est une condition d’entrée.

### 2.4 Enclos-tente pour chat d’intérieur, kit tente + tunnel (« catio nomade »)

**Offres comparées** : kit tente pop-up + tunnel à **94,90 € TTC** et à **109 € TTC** (84,90 € dans le tableau des prix). Repères : tente pop-up Jardiland ≈ 84,99 € ([Jardiland](https://www.jardiland.com/p/tente-chien-chat-polyester-jardin-camping-pop-up-protection-solaire-120cm-vert-comfortxl-pet-living-68da47c2a82c3a3df1cded34)), kits 2-en-1 de 57,07 € ([Amazon.fr](https://www.amazon.fr/NURCIX-dext%C3%A9rieur-Portables-Compagnie-Transport/dp/B0C7JVFKDJ)) à 139,99 € pour un 6-en-1 ([Amazon.fr](https://www.amazon.fr/PJDDP-dext%C3%A9rieur-cl%C3%B4tures-int%C3%A9rieure-ext%C3%A9rieure/dp/B0C2CTJLNS)). Une seule taille : règles de retour de la première étude (24 / 12 / 5 %).

| Coût rendu (€ HT, formule de la note) | Prudent (B2, kit lourd) | Intermédiaire (B1, kit léger) | Optimiste (kit léger, FOB bas) |
| :--- | ---: | ---: | ---: |
| Achat (FOB × 0,86) | 18,49 | 14,19 | 7,74 |
| Commission d’agent (7,5 %) | 1,39 | 1,07 | 0,58 |
| Fret groupage (60 $/m³) | 1,86 | 1,03 | 1,03 |
| Dédouanement et frais fixes | 0,30 | 0,30 | 0,30 |
| Droits de douane | 2,44 | 0,96 | 0,56 |
| **= Coût rendu entrepôt** | **24,48** | **17,55** | **10,21** |

| Ligne (€ par commande) | Kit tente 94,90 € · Prudent | Kit tente 94,90 € · Intermédiaire | Kit tente 94,90 € · Optimiste | Kit tente 109 € · Prudent | Kit tente 109 € · Intermédiaire | Kit tente 109 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 94,90 | 94,90 | 94,90 | 109,00 | 109,00 | 109,00 |
| 2. Chiffre d’affaires HT estimé par commande | 79,08 | 79,08 | 79,08 | 90,83 | 90,83 | 90,83 |
| 3. Coût du produit livré | 54,53 | 27,38 | 16,42 | 54,53 | 27,38 | 16,42 |
| 4. Frais de paiement et de plateforme | 4,31 | 2,70 | 1,97 | 4,68 | 2,95 | 2,19 |
| 5. Provision estimée pour retours et remboursements | 21,60 | 8,93 | 3,71 | 24,56 | 10,37 | 4,30 |
| **6. Marge contributive avant publicité** | **−1,36** | **40,07** | **56,98** | **7,06** | **50,13** | **67,92** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−95,97** | **0,19** | **42,93** | **−87,55** | **10,25** | **53,87** |
| CPA d’équilibre (1re commande) | aucun (marge ≤ 0) | 40,07 | 56,98 | 7,06 | 50,13 | 67,92 |
| ROAS d’équilibre (CA TTC ÷ pub) | n.a. (marge ≤ 0) | 2,37 | 1,67 | 15,44 | 2,17 | 1,60 |
| Marge après pub au CPA observé de 80,19 € | −81,55 | −40,12 | −23,21 | −73,13 | −30,06 | −12,27 |
| Marge après pub au CPA observé de 96,61 € | −97,97 | −56,54 | −39,63 | −89,55 | −46,48 | −28,69 |
| Marge contributive en % du CA HT | −2 % | 51 % | 72 % | 8 % | 55 % | 75 % |

| Détail (€ HT) | Kit tente 94,90 € · Prudent | Kit tente 94,90 € · Intermédiaire | Kit tente 94,90 € · Optimiste | Kit tente 109 € · Prudent | Kit tente 109 € · Intermédiaire | Kit tente 109 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 24,48 | 17,55 | 10,21 | 24,48 | 17,55 | 10,21 |
| Préparation et stockage | 5,25 | 2,52 | 1,07 | 5,25 | 2,52 | 1,07 |
| Emballage d’expédition, encart, REP (et éco-participation) | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 24,00 | 6,86 | 4,89 | 24,00 | 6,86 | 4,89 |
| **= Coût du produit livré** | **54,53** | **27,38** | **16,42** | **54,53** | **27,38** | **16,42** |
| Encaissement | 2,79 | 1,94 | 1,67 | 3,16 | 2,19 | 1,89 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **4,31** | **2,70** | **1,97** | **4,68** | **2,95** | **2,19** |
| Remboursements nets | 20,39 | 8,64 | 3,60 | 23,21 | 10,05 | 4,18 |
| Rétrofacturations | 1,21 | 0,29 | 0,11 | 1,35 | 0,32 | 0,12 |
| **= Provision retours et remboursements** | **21,60** | **8,93** | **3,71** | **24,56** | **10,37** | **4,30** |
| Poids d’expédition retenu et tranche | 7,20 kg (≤ 10 kg) | 1,24 kg (≤ 2 kg) | 1,23 kg (≤ 2 kg) | 7,20 kg (≤ 10 kg) | 1,24 kg (≤ 2 kg) | 1,23 kg (≤ 2 kg) |

| Offre (prix TTC) | Marge contributive P / I / O | ROAS d’équilibre TTC (I) | Conversion d’équilibre (CPM 13 €, CTR 1,63 %) | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) | Après CPA 96,61 (coûts I) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Kit tente + tunnel à 84,90 € | −7,33 / **32,94** / 49,23 | 2,58 | 2,42 % | −6,94 | −47,25 | −63,67 |
| Kit tente + tunnel à 94,90 € | −1,36 / **40,07** / 56,98 | 2,37 | 1,99 % | 0,19 | −40,12 | −56,54 |
| Kit tente + tunnel à 109 € | 7,06 / **50,13** / 67,92 | 2,17 | 1,59 % | 10,25 | −30,06 | −46,48 |

**Lecture.**
- **À 94,90 €**, la première commande est à l’équilibre au CPA central (+0,19 €) ; il faut **109 €** pour dégager +10,25 €. Le prix qui donne 39,88 € de marge est de 94,64 €, contre 93,87 € dans la note : l’écart vient du stockage volumique (0,54 € de plus).
- **Le kit lourd en prudent ne couvre pas ses coûts** (−1,36 € à 94,90 €) : 3,9 kg réels, 7,2 kg en poids volumétrique (tranche ≤ 10 kg) et 12 % de droits si la douane classe le kit en tente (6306 22, [CP]).
- Le produit vise des chats : aucune synergie avec la clientèle de Pilou, et une saisonnalité de printemps-été (HYPOTHÈSE de la note) qui concentre les ventes sur 5 à 6 mois.

### 2.5 Lit anti-mâchonnement pour grand chien destructeur (modèle K9 Ballistics ou Kuranda)

**Offres comparées** : lit en tissu balistique, roulé ou compressé, à **149 € TTC** et à **169 € TTC** (129 € dans le tableau des prix). Repères : Knuffelwuff « robuste » 104,95–166,90 € ([Zooplus.fr](https://www.zooplus.fr/shop/chiens/corbeilles_paniers_chien/knuffelwuff/9980008811)) ; lit 1680D à 79,99 $ aux États-Unis ([reach.dog](https://reach.dog/shop/dgs-pet-products-1/products/ninja-beds)). Colis lourd : 4,5 kg (≤ 5 kg) en intermédiaire.

| Coût rendu (€ HT, formule de la note) | Prudent (FOB 35 $) | Intermédiaire (FOB 27 $) | Optimiste (FOB 20 $) |
| :--- | ---: | ---: | ---: |
| Achat (FOB × 0,86) | 30,10 | 23,22 | 17,20 |
| Commission d’agent (7,5 %) | 2,25 | 1,74 | 1,29 |
| Fret groupage (60 $/m³) | 3,10 | 3,10 | 3,10 |
| Dédouanement et frais fixes | 0,30 | 0,30 | 0,30 |
| Droits de douane | 2,09 | 1,66 | 1,27 |
| **= Coût rendu entrepôt** | **37,84** | **30,02** | **23,16** |

| Ligne (€ par commande) | Lit 149 € · Prudent | Lit 149 € · Intermédiaire | Lit 149 € · Optimiste | Lit 169 € · Prudent | Lit 169 € · Intermédiaire | Lit 169 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 149,00 | 149,00 | 149,00 | 169,00 | 169,00 | 169,00 |
| 2. Chiffre d’affaires HT estimé par commande | 124,17 | 124,17 | 124,17 | 140,83 | 140,83 | 140,83 |
| 3. Coût du produit livré | 69,89 | 49,05 | 31,36 | 69,89 | 49,05 | 31,36 |
| 4. Frais de paiement et de plateforme | 5,74 | 3,66 | 2,79 | 6,27 | 4,02 | 3,08 |
| 5. Provision estimée pour retours et remboursements | 39,15 | 16,28 | 6,18 | 43,35 | 18,32 | 7,03 |
| **6. Marge contributive avant publicité** | **9,39** | **55,18** | **83,84** | **21,32** | **69,44** | **99,36** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−85,22** | **15,30** | **69,79** | **−73,29** | **29,56** | **85,31** |
| CPA d’équilibre (1re commande) | 9,39 | 55,18 | 83,84 | 21,32 | 69,44 | 99,36 |
| ROAS d’équilibre (CA TTC ÷ pub) | 15,87 | 2,70 | 1,78 | 7,93 | 2,43 | 1,70 |
| Marge après pub au CPA observé de 80,19 € | −70,80 | −25,01 | 3,65 | −58,87 | −10,75 | 19,17 |
| Marge après pub au CPA observé de 96,61 € | −87,22 | −41,43 | −12,77 | −75,29 | −27,17 | 2,75 |
| Marge contributive en % du CA HT | 8 % | 44 % | 68 % | 15 % | 49 % | 71 % |

| Détail (€ HT) | Lit 149 € · Prudent | Lit 149 € · Intermédiaire | Lit 149 € · Optimiste | Lit 169 € · Prudent | Lit 169 € · Intermédiaire | Lit 169 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 37,84 | 30,02 | 23,16 | 37,84 | 30,02 | 23,16 |
| Préparation et stockage | 5,25 | 4,05 | 1,20 | 5,25 | 4,05 | 1,20 |
| Emballage d’expédition, encart, REP (et éco-participation) | 2,80 | 1,45 | 0,75 | 2,80 | 1,45 | 0,75 |
| Transport jusqu’au client | 24,00 | 13,53 | 6,25 | 24,00 | 13,53 | 6,25 |
| **= Coût du produit livré** | **69,89** | **49,05** | **31,36** | **69,89** | **49,05** | **31,36** |
| Encaissement | 4,22 | 2,90 | 2,49 | 4,75 | 3,26 | 2,78 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **5,74** | **3,66** | **2,79** | **6,27** | **4,02** | **3,08** |
| Remboursements nets | 30,41 | 13,51 | 5,40 | 34,41 | 15,50 | 6,23 |
| Garantie anti-mâchonnement (remplacement) | 6,99 | 2,34 | 0,62 | 6,99 | 2,34 | 0,62 |
| Rétrofacturations | 1,75 | 0,43 | 0,16 | 1,95 | 0,48 | 0,18 |
| **= Provision retours, remboursements et garantie** | **39,15** | **16,28** | **6,18** | **43,35** | **18,32** | **7,03** |
| Poids d’expédition retenu et tranche | 12,00 kg (> 10 kg, tarif plancher) | 4,54 kg (≤ 5 kg) | 3,53 kg (≤ 5 kg) | 12,00 kg (> 10 kg, tarif plancher) | 4,54 kg (≤ 5 kg) | 3,53 kg (≤ 5 kg) |

| Offre (prix TTC) | Marge contributive P / I / O | ROAS d’équilibre TTC (I) | Conversion d’équilibre (CPM 13 €, CTR 1,63 %) | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) | Après CPA 96,61 (coûts I) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Lit anti-mâchonnement à 129 € | −2,55 / **40,93** / 68,34 | 3,15 | 1,95 % | 1,05 | −39,26 | −55,68 |
| Lit anti-mâchonnement à 149 € | 9,39 / **55,18** / 83,84 | 2,70 | 1,45 % | 15,30 | −25,01 | −41,43 |
| Lit anti-mâchonnement à 169 € | 21,32 / **69,44** / 99,36 | 2,43 | 1,15 % | 29,56 | −10,75 | −27,17 |

**Lecture.**
- **À 149 €**, la marge intermédiaire est de 55,18 €, soit +15,30 € après le CPA central ; à 129 €, elle n’est que de 40,93 €. La note trouvait 38,79 € à 129 € et un équilibre à 131 € ; ici l’équilibre au CPA central est à 127,53 € TTC, parce que la provision de la première étude déduit la valeur des lits retournés revendables (1,80 € par commande) et que l’emballage, la REP et l’éco-participation sont comptés 1,45 € au lieu de 2,50 €.
- **Le transport et le volume pèsent** : 13,53 € de port, 4,05 € de préparation et de stockage (10 fois le volume de référence), 2,34 € de garantie. En prudent, le poids volumétrique d’un rouleau de 0,06 m³ (12 kg) dépasse toutes les grilles sourcées : 24,00 € est un plancher.
- Le fret ferroviaire du prudent de la première étude ajouterait 21,39 € par lit (D18) : le lit impose un stock maritime.

## 3. Vue par client sur 12 mois : commandes additionnelles et récupération du coût d’acquisition

### 3.1 Hypothèses (toutes des HYPOTHÈSES, faute de donnée de rétention propre à ces produits)

Modèle de la première étude pour les produits durables : le client est acquis au mois 0 (CPA payé). Une part **p2** passe une commande additionnelle au mois 3 ; 30 % de ces clients en passent une seconde au mois 9. Chaque commande additionnelle rapporte la marge contributive de son offre, remise de fidélité de 10 % et coût de relance (2,00 / 1,00 / 0,50 €) déduits, avec les mêmes paramètres de coûts que la première commande. Aucun des cinq produits n’a de consommable : le réachat du produit principal lui-même est rare (un harnais ou un lit dure, un chien âgé a une espérance de vie limitée).

| Produit | Commande additionnelle (TTC) | Marge contributive de cette commande P / I / O (€) | p2 : part des clients P / I / O | Rythme | Fondement |
| :--- | :--- | ---: | ---: | :--- | :--- |
| Harnais de levage | Paire de poignées de marche (26,91 €) | −4,79 / 8,32 / 13,55 | 5 % / 10 % / 20 % | mois 3, puis mois 9 (30 % des réacheteurs) | Accessoire naturel du harnais : le leader les vend 22,50–26,50 $ ; coût D5. |
| Peluche réplique | 2e peluche à −10 % (152,10 €) | 4,65 / 44,31 / 64,66 | 2 % / 5 % / 10 % | mois 3, puis mois 9 (30 % des réacheteurs) | Autre animal du foyer, cadeau à un proche ou version mémorial ; produit cher et émotionnel : p2 plus bas. |
| Sac porte-chien | Housse de pluie ou ceinture de hanches (26,91 €) | −4,42 / 7,87 / 12,87 | 5 % / 10 % / 20 % | mois 3, puis mois 9 (30 % des réacheteurs) | Little Chonk vend la ceinture de hanches en accessoire ; FOB 2–4 $ [HYPOTHÈSE], 0,25 kg. |
| Enclos-tente chat | Tunnel supplémentaire (31,41 €) | −6,80 / 7,94 / 14,48 | 5 % / 10 % / 20 % | mois 3, puis mois 9 (30 % des réacheteurs) | Extension du parcours ; FOB 3–5 $ [HYPOTHÈSE ancrée sur des pop-up à 4,45–4,90 $, `chat_premium.md` §2.1], 0,6 kg. |
| Lit anti-mâchonnement | Housse de rechange balistique (44,91 €) | −4,82 / 11,41 / 21,23 | 5 % / 10 % / 20 % | mois 3, puis mois 9 (30 % des réacheteurs) | La housse porte l’essentiel du coût d’un lit ; FOB 6–12 $ [HYPOTHÈSE : environ un tiers du FOB du lit], 1,2 kg. |

### 3.2 Résultats par client acquis (offre principale en première commande)

| Produit et offre | Scénario | Marge 1re commande | CPA | Solde après 1re commande | Commandes additionnelles espérées sur 6 mois | Cumul par client à 6 mois | Commandes additionnelles espérées sur 12 mois | Cumul par client à 12 mois | Récupération du CPA | CPA maximal récupéré en 12 mois |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Harnais de levage — Harnais 119 € | Prudent | 19,87 | 94,61 | −74,74 | 0,050 | −74,98 | 0,065 | −75,05 | > 36 mois | 19,56 |
|  | Intermédiaire | 58,21 | 39,88 | 18,33 | 0,100 | 19,16 | 0,130 | 19,41 | dès la 1re commande | 59,29 |
|  | Optimiste | 76,36 | 14,05 | 62,31 | 0,200 | 65,02 | 0,260 | 65,83 | dès la 1re commande | 79,88 |
| Peluche réplique — Peluche 169 € | Prudent | 19,26 | 94,61 | −75,35 | 0,020 | −75,26 | 0,026 | −75,23 | > 36 mois | 19,38 |
|  | Intermédiaire | 58,69 | 39,88 | 18,81 | 0,050 | 21,03 | 0,065 | 21,69 | dès la 1re commande | 61,57 |
|  | Optimiste | 78,83 | 14,05 | 64,78 | 0,100 | 71,25 | 0,130 | 73,19 | dès la 1re commande | 87,24 |
| Sac porte-chien — Sac 99 € | Prudent | −18,45 | 94,61 | −113,06 | 0,050 | −113,28 | 0,065 | −113,35 | > 36 mois | −18,74 |
|  | Intermédiaire | 38,14 | 39,88 | −1,74 | 0,100 | −0,95 | 0,130 | −0,72 | > 36 mois | 39,16 |
|  | Optimiste | 57,57 | 14,05 | 43,52 | 0,200 | 46,09 | 0,260 | 46,87 | dès la 1re commande | 60,92 |
| Enclos-tente chat — Kit tente 94,90 € | Prudent | −1,36 | 94,61 | −95,97 | 0,050 | −96,31 | 0,065 | −96,41 | > 36 mois | −1,80 |
|  | Intermédiaire | 40,07 | 39,88 | 0,19 | 0,100 | 0,98 | 0,130 | 1,22 | dès la 1re commande | 41,10 |
|  | Optimiste | 56,98 | 14,05 | 42,93 | 0,200 | 45,83 | 0,260 | 46,69 | dès la 1re commande | 60,74 |
| Lit anti-mâchonnement — Lit 149 € | Prudent | 9,39 | 94,61 | −85,22 | 0,050 | −85,46 | 0,065 | −85,53 | > 36 mois | 9,08 |
|  | Intermédiaire | 55,18 | 39,88 | 15,30 | 0,100 | 16,44 | 0,130 | 16,78 | dès la 1re commande | 56,66 |
|  | Optimiste | 83,84 | 14,05 | 69,79 | 0,200 | 74,04 | 0,260 | 75,31 | dès la 1re commande | 89,36 |

« Cumul » = marge de la 1re commande − CPA + marges espérées des commandes additionnelles. « Récupération du CPA » = mois de la commande après laquelle le cumul espéré devient positif (horizon 36 mois). « CPA maximal récupéré en 12 mois » = CPA que la marge de 12 mois peut payer.

### 3.3 Variante : offre comparée en première commande, et CPA observés de Pilou (coûts intermédiaires)

| Produit | Offre comparée | Cumul à 12 mois, CPA 39,88 (offre comparée) | Récupération (offre comparée) | CPA maximal récupéré en 12 mois (offre comparée) | Offre principale : cumul à 12 mois au CPA de 80,19 € | … au CPA de 96,61 € | Offre principale : récupération à 80,19 € | Offre comparée : cumul à 12 mois à 80,19 € | … à 96,61 € | Offre comparée : récupération à 80,19 € |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Harnais de levage | Kit harnais + poignées 139 € | 30,31 | dès la 1re commande | 70,19 | −20,90 | −37,32 | > 36 mois | −10,00 | −26,42 | > 36 mois |
| Peluche réplique | Peluche 199 € | 45,45 | dès la 1re commande | 85,33 | −18,62 | −35,04 | > 36 mois | 5,14 | −11,28 | dès la 1re commande |
| Sac porte-chien | Sac 119 € | 13,55 | dès la 1re commande | 53,43 | −41,03 | −57,45 | > 36 mois | −26,76 | −43,18 | > 36 mois |
| Enclos-tente chat | Kit tente 109 € | 11,28 | dès la 1re commande | 51,16 | −39,09 | −55,51 | > 36 mois | −29,03 | −45,45 | > 36 mois |
| Lit anti-mâchonnement | Lit 169 € | 31,04 | dès la 1re commande | 70,92 | −23,53 | −39,95 | > 36 mois | −9,27 | −25,69 | > 36 mois |

**Lecture.**
- **Ces produits vivent de la première commande.** Les commandes additionnelles n’apportent que 1,02 € à 2,88 € par client acquis en 12 mois (coûts intermédiaires). L’écart entre « CPA d’équilibre de la 1re commande » et « CPA maximal récupéré en 12 mois » est donc de quelques euros, contre 10,18 € (additif litière) et 14,45 € (bouchées) pour les consommables de la première étude.
- **Au CPA central de 39,88 €**, le harnais à 119 €, la peluche à 169 € et le lit à 149 € récupèrent le coût d’acquisition **dès la première commande** ; l’enclos à 94,90 € y arrive de justesse ; le sac à 99 € ne le récupère pas, même en 36 mois (il faut 119 €).
- **Aux CPA observés de Pilou**, aucune offre principale ne récupère le coût d’acquisition, même en 36 mois. Parmi les offres comparées, seule la **peluche à 199 €** y parvient au CPA de 80,19 € (cumul de +5,14 € à 12 mois) ; le kit harnais à 139 € reste à −10,00 €.
- En prudent, aucun ne récupère un CPA de 94,61 € ; en optimiste, tous le récupèrent dès la première commande.

## 4. Harnais de levage : prix, structure d’offre, fret, tailles, remboursements et achats d’un test à 15 €/jour

### 4.1 Meilleur prix et structure d’offre

| Structure | Prix TTC (moyen) | Coût du produit livré (I) | Marge contributive P / I / O | ROAS d’équilibre TTC (I) | Conversion d’équilibre (I) | Conversion nécessaire par rapport à 119 € pour gagner autant par euro de pub | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) | Après CPA 96,61 (coûts I) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Harnais seul, 99,90 € | 99,90 | 24,58 | 9,42 / **44,59** / 61,54 | 2,24 | 1,79 % | +30,5 % | 4,71 | −35,60 | −52,02 |
| Harnais seul, 119 € (référence) | 119,00 | 24,58 | 19,87 / **58,21** / 76,36 | 2,04 | 1,37 % | référence | 18,33 | −21,98 | −38,40 |
| Harnais seul, 129 € | 129,00 | 24,58 | 25,34 / **65,34** / 84,12 | 1,97 | 1,22 % | −10,9 % | 25,46 | −14,85 | −31,27 |
| Prix par taille M 109 / L 119 / XL 129 € | 115,50 | 24,58 | 17,96 / **55,71** / 73,64 | 2,07 | 1,43 % | +4,5 % | 15,83 | −24,48 | −40,90 |
| Prix par taille M 119 / L 129 / XL 139 € | 125,50 | 24,58 | 23,42 / **62,83** / 81,39 | 2,00 | 1,27 % | −7,4 % | 22,95 | −17,36 | −33,78 |
| Kit harnais + poignées, 139 € | 139,00 | 28,09 | 24,90 / **69,11** / 90,01 | 2,01 | 1,15 % | −15,8 % | 29,23 | −11,08 | −27,50 |
| Kit harnais + poignées, 149 € | 149,00 | 28,09 | 30,38 / **76,25** / 97,77 | 1,95 | 1,05 % | −23,7 % | 36,37 | −3,94 | −20,36 |

**Lecture et recommandation.**
- **Chaque palier de 10 € TTC ajoute ≈ 7,13 € de marge** (le prix HT moins l’encaissement et la provision). À 99,90 €, il faudrait convertir 31 % de mieux qu’à 119 € pour gagner autant par euro de publicité ; à 129 €, une baisse de conversion jusqu’à 11 % reste neutre.
- **Le kit à 139 € est la meilleure structure** : +10,90 € de marge pour +20 € de prix, parce que les poignées coûtent 2,78 € rendues et ne changent pas la tranche de poids de M. Avec 30 % de clients qui prennent le kit [HYPOTHÈSE de lecture], la marge moyenne de première commande passe de 58,21 € à 61,48 €.
- **Prix par taille** : l’échelle M 109 / L 119 / XL 129 € suit les coûts (le XL coûte plus cher et pèse plus), mais baisse le panier moyen avec un mix centré sur M ; l’échelle du leader (+15 $ par taille) transposée à M 119 / L 129 / XL 139 € rapporte davantage, au prix d’un message publicitaire moins simple (« à partir de 119 € »).
- **Recommandation** : harnais à **119 €** pour toutes les tailles en prix d’entrée (sous Help ’Em Up importé, 98 à 173 € selon la taille et le style chez Zooplus et dès 112,90 € chez Physioveto ; à 2,3 fois CareLift, qu’il faut justifier par l’ajustement, la charge testée et le service de taille), **kit mobilité à 139 € mis en avant** (« le plus choisi »), et test de 129 € contre 119 € en phase B (§5.2). 99,90 € ne se justifie qu’en prix de lancement daté, car il exige 31 % de conversion en plus.

### 4.2 Fret maritime ou aérien (et ferroviaire en test de résistance)

| Mode du stock | Coût rendu moyen P / I / O (mix) | Marge contributive à 119 € P / I / O | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) |
| :--- | ---: | ---: | ---: | ---: |
| Groupage maritime (valeurs de la note) | 23,59 / 16,11 / 9,54 | 19,87 / 58,21 / 76,36 | 18,33 | −21,98 |
| Aérien DDP (valeurs de la note) | 30,96 / 21,85 / 13,65 | 12,23 / 52,59 / 72,34 | 12,71 | −27,60 |
| Prudent avec fret ferroviaire à 450 $/m³ (première étude) | 25,59 (P) | 17,80 (P) | — | — |

- **L’aérien coûte 5,74 € de plus par harnais vendu** en moyenne (de 4,95 € en M à 7,93 € en XL) : la marge à 119 € passe de 58,21 € à 52,59 €. Sur le premier lot central (M 100, L 75, XL 50), cela représente **1 337 €** (3 680 € par mer contre 5 017 € par air).
- **Délai** (calendrier de la note sourcing) : ≈ 20,5 semaines en central par mer, ≈ 16,5 semaines par air, du premier contact au stock en France. Un premier contact fin octobre 2026 place la production vers février 2027, au Nouvel An chinois (06/02/2027) : l’aérien n’est qu’une assurance de 4 semaines, à réserver au premier lot ou à la taille M.
- **Le ferroviaire du prudent de la première étude** ajouterait 1,72 € à 2,76 € par harnais : marge prudente de 17,80 € au lieu de 19,87 €. Le harnais, petit et léger, y est peu sensible (contre 21,39 € pour le lit).

### 4.3 Mix de tailles

| Répartition des ventes | Coût rendu P / I / O | Tranches (I) | Transport (I) | Marge contributive à 119 € P / I / O | Après CPA 39,88 (I) | Après CPA 80,19 (coûts I) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 100 % M | 22,14 / 14,84 / 8,91 | M ≤ 1 kg | 5,19 | 22,35 / 60,46 / 77,51 | 20,58 | −19,73 |
| 100 % L | 24,13 / 16,78 / 9,87 | L ≤ 2 kg | 6,86 | 18,36 / 56,58 / 75,50 | 16,70 | −23,61 |
| 100 % XL | 27,14 / 18,75 / 10,84 | XL ≤ 2 kg | 6,86 | 15,23 / 54,57 / 74,54 | 14,69 | −25,62 |
| Mix de référence M 50 / L 35 / XL 15 | 23,59 / 16,11 / 9,54 | M ≤ 1 kg ; L ≤ 2 kg ; XL ≤ 2 kg | 6,03 | 19,87 / 58,21 / 76,36 | 18,33 | −21,98 |
| Mix « grands gabarits » M 30 / L 40 / XL 30 | 24,44 / 16,79 / 9,87 | M ≤ 1 kg ; L ≤ 2 kg ; XL ≤ 2 kg | 6,36 | 18,61 / 57,14 / 75,82 | 17,26 | −23,05 |
| Mix de référence, L tenu sous 1 kg (emballage allégé) | 23,59 / 16,11 / 9,54 | M ≤ 1 kg ; L ≤ 1 kg ; XL ≤ 2 kg | 5,44 | 19,87 / 58,91 / 76,74 | 19,03 | −21,28 |

- **Chaque taille plus grande coûte ≈ 2 € de produit et le passage en tranche de 2 kg** : la marge à 119 € va de 60,46 € (M) à 54,57 € (XL). Un mix plus lourd (30 / 40 / 30) retire 1,07 € par commande ; tenir la taille L sous 1 kg (sachet imprimé au lieu d’une boîte, recommandation de la note) en rapporte 0,70 €.

*Écoulement d’un stock acheté à quantités égales par taille, au rythme du test (3 ensembles de publicités à 15 €/jour, soit 1 368,90 € par mois) :*

| CPA | Commandes par mois | Mois pour vendre 100 M | Mois pour vendre 100 L | Mois pour vendre 100 XL |
| :--- | ---: | ---: | ---: | ---: |
| CPA 14,05 € | 97,4 | 2,1 | 2,9 | 6,8 |
| CPA 39,88 € | 34,3 | 5,8 | 8,3 | 19,4 |
| CPA 80,19 € | 17,1 | 11,7 | 16,7 | 39,1 |
| CPA 96,61 € | 14,2 | 14,1 | 20,2 | 47,0 |

- **Acheter 100 pièces par taille immobilise 5 037 €** (mer), dont un stock XL qui mettrait 19 mois à s’écouler au CPA central. Un premier lot proportionnel au mix, avec un plancher au minimum de commande (M 100, L 75, XL 50 ; MOQ de 20 à 100 par taille selon les fournisseurs : OKEYPETS 20 par taille, [PR Newswire](https://en.prnasia.com/releases/global/dog-harness-manufacturer-okeypets-launches-neoprene-and-air-mesh-harness-collections-for-global-pet-brands-541277.shtml) ; Altra 50 à 100) immobilise 3 680 €. C’est l’hypothèse du budget central (§5.1).

### 4.4 Remboursements à 24 % (et 30 %) et échanges de taille

| Taux de remboursement ↓ / échanges de taille → | 0 % | 4 % | 8 % (référence) | 15 % |
| :--- | ---: | ---: | ---: | ---: |
| 5 % | 66,48 | 65,59 | 64,69 | 63,13 |
| 12 % | 60,00 | 59,11 | **58,21** | 56,65 |
| 24 % | 48,88 | 47,99 | 47,09 | 45,53 |
| 30 % | 43,32 | 42,43 | 41,53 | 39,97 |

*Marge contributive à 119 €, coûts intermédiaires, mix de référence. En gras : le scénario intermédiaire.*

- **Passer de 12 % à 24 % de remboursements coûte 11,12 € par commande** (19 % de la marge) : la marge tombe à 47,09 €, encore au-dessus du CPA central (+7,21 € après publicité). Avec les taux du prudent (30 % de remboursements, 15 % d’échanges) mais des coûts intermédiaires, elle tombe à 39,97 €, soit +0,09 € après un CPA de 39,88 €.
- **Un échange coûte moins qu’un remboursement** : chaque point de commandes échangées coûte ≈ 0,22 € de marge, chaque point remboursé ≈ 0,93 €. Transformer des remboursements en échanges (guide en 3 cotes, vidéo de mesure, envoi de la nouvelle taille avant réception de l’ancienne) est donc rentable dès qu’il évite un remboursement pour 4,1 échanges.

### 4.5 Ce qu’apporte un test à 15 €/jour pendant 30 jours

| Niveau de CPA | CPA (€) | Achats attendus pour 450 € (15 €/jour × 30 jours) | Intervalle à 95 % du vrai CPA (multiple du CPA observé, Poisson) | Soit, si ce CPA est observé |
| :--- | ---: | ---: | ---: | ---: |
| CPA optimiste | 14,05 | 32,0 | 0,71 × à 1,46 × | 10 € à 21 € |
| CPA central | 39,88 | 11,3 | 0,56 × à 2,00 × | 22 € à 80 € |
| CPA d’équilibre du harnais à 119 € | 58,21 | 7,7 | 0,51 × à 2,32 × | 30 € à 135 € |
| CPA d’équilibre du kit à 139 € | 69,11 | 6,5 | 0,49 × à 2,49 × | 34 € à 172 € |
| CPA observé de Pilou (lecture basse) | 80,19 | 5,6 | 0,46 × à 2,72 × | 37 € à 219 € |
| CPA prudent | 94,61 | 4,8 | 0,43 × à 3,08 × | 41 € à 291 € |
| CPA observé de Pilou (lecture haute) | 96,61 | 4,7 | 0,43 × à 3,08 × | 41 € à 298 € |

- **Un mois à 15 €/jour ne permet pas de conclure** : avec ≈ 8 achats au CPA d’équilibre, le vrai CPA peut être deux fois plus haut ou deux fois plus bas que le CPA observé. Il sert à détecter un échec net (aucun achat après 175 €, soit 3 CPA d’équilibre dépensés : cela n’arrive que 5 fois sur 100 si le vrai CPA est à l’équilibre).
- **Pour distinguer l’équilibre (58,21 €) d’un CPA 1,5 fois plus élevé** avec 5 % d’erreur et 80 % de puissance, il faut ≈ 46,5 achats attendus, soit ≈ 2 707 € de publicité ; d’un CPA 2 fois plus élevé : 19,5 achats, ≈ 1 135 € ; 3 fois : 9,5 achats, ≈ 553 €.
- **Phase d’apprentissage de Meta** (≈ 50 événements en 7 jours, [CP] de la première étude) : il faudrait ≈ 285 € par jour au CPA central. Au budget du client, optimiser d’abord sur l’ajout au panier ou regrouper le budget dans un seul ensemble (Advantage+).

## 5. Budget minimal d’un test sérieux

Le budget est une **sortie de trésorerie** (€ HT) : échantillons, essais, propriété intellectuelle, stock, emballage, contenus, outils et publicité. Une partie revient par les ventes du test (marge contributive des commandes) ; le stock non vendu reste un actif, sous réserve de l’interdiction de détruire les invendus (loi AGEC).

### 5.1 Harnais de levage : budget détaillé

Trois niveaux : **bas** = test de demande sur un modèle de catalogue avec logo (50 pièces par taille, pas de développement) ; **central** = test sérieux sur un harnais à cahier des charges propre (patron, 2 arrières, essais de charge en laboratoire), 225 pièces ; **haut** = spécification haute, 300 pièces, avis complet de liberté d’exploitation. Délai de l’échantillon au stock (note sourcing) : ≈ 10,5 à 30 semaines par mer, ≈ 9 à 24,5 par air.

| Poste (€ HT) | Bas | Central | Haut | Statut | Détail et source |
| :--- | ---: | ---: | ---: | :--- | :--- |
| Échantillons catalogue (3 tailles par fournisseur, port express) | 259,80 | 741,00 | 2 246,78 | SOURCÉ (prix) + HYPOTHÈSE | 3 / 5 / 8 fournisseurs (Altra, Furvorite, Huchong, OKEYPETS…, note sourcing §1.1) × 3 tailles × 20 $ (haut des fiches intégrales 14,90–19,90 $) / 40 $ (≈ 2 × FOB, HYPOTHÈSE) / 85,60 $ (échantillon d’un ensemble rembourré, [Pietra](https://pietrastudio.com/sourcing/products/adjustable-padded-dog-harness-set-yi77)) + port express 35 / 45 / 60 € par fournisseur (HYPOTHÈSE de la première étude). |
| Prototype sur mesure : patron, 2 arrières (standard et mâle), logo, 1 à 2 itérations | 0,00 | 802,80 | 1 603,39 | HYPOTHÈSE | Bas : modèle de catalogue avec logo. Central et haut : 2 itérations × 6 pièces (3 tailles × 2 arrières) au prix d’échantillon + frais de patron 300 / 600 € + 2 envois express. Coût du patron non trouvé : à demander dans la demande de devis (note sourcing Q1). |
| Essais de charge (5 × le poids maximal de chaque taille, par poignée et ensemble ; boucles, D-rings, coutures ; 20 lavages puis nouvel essai) | 200,37 | 1 651,11 | 3 302,22 | HYPOTHÈSE (aucun prix trouvé) | Protocole de la note : 180 kg en M, 285 kg en L, 375 kg en XL, sur le modèle Kohl’s 1500-E ([Kohl’s](https://link.kohls.com/content/dam/klink/pdfs/Protocol_1500-E-February_2024.pdf)). Bas : en interne (peson ou dynamomètre, charges : 150 €) + 1 harnais détruit par taille ; central : laboratoire tiers (SGS, Intertek, TÜV, BV) 1 500 € + 3 harnais détruits par taille ; haut : 3 000 € + 2 séries. Harnais détruits au coût rendu moyen de 16,79 €. |
| Essais chimiques REACH (azoïques et NPE sur textiles ; HAP et phtalates sur plastiques et mousses ; PFAS en haut) | 281,00 | 1 424,60 | 2 756,40 | SOURCÉ (HAP, phtalates) + HYPOTHÈSE (azoïques, NPE, PFAS) | Essai HAP 184 € HT par échantillon + 97 € par commande ([Measurlabs](https://measurlabs.com/products/polycyclic-aromatic-hydrocarbons-pahs-in-plastic-and-rubber-reach)) ; phtalates 130 $ ([CAPLINQ](https://caplinq.com/reach-svhc-testing-pricelist.html)) ; azoïques et NPE supposés au prix de l’essai HAP (aucun prix dans les notes) ; PFAS 300 €. Bas : rapports REACH du fournisseur sur l’échantillon validé + 1 contrôle ; central : 2 matières textiles et 2 pièces plastiques ; haut : 4 matières, 3 pièces et un dépistage PFAS. |
| Essais sur chiens (5 à 10 chiens par taille : recul, rotation, port de 2 à 4 h, enfilage sur chien couché) | 0,00 | 300,00 | 900,00 | HYPOTHÈSE | Harnais pris dans les échantillons ; dédommagement et port des volontaires (clients Pilou, kinésithérapeutes vétérinaires). |
| Étude de liberté d’exploitation (brevets et dessins) par un conseil en propriété industrielle — ligne estimée | 1 000,00 | 2 500,00 | 5 000,00 | HYPOTHÈSE (aucun prix trouvé) | Statut et validation française d’EP 2 965 620 ([EPO](https://data.epo.org/publication-server/rest/v1.2/patents/EP2965620NWA3/document.html)), revendications des suites US 11 464 201 et US 12 414 538 ([USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11464201), [USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12414538)) sur la liaison avant-arrière et la U-band, dessin US D1079145 ([Justia](https://patents.justia.com/patent/D1079145)) et dessins UE (EUIPO). Bas : vérification de statut et recherche de dessins ; central : avis écrit limité à cette famille ; haut : avis complet et pistes de contournement. **Risque juridique n° 1 du projet** (note sourcing Q3). |
| Autres frais de conformité (Citeo, assurance RC produits, dépôt de marque INPI, relecture juridique des allégations, de la notice GPSR et des CGV) | 270,00 | 1 040,00 | 1 980,00 | SOURCÉ (Citeo) + HYPOTHÈSE (reste) | Citeo 80 / 110 / 110 € ([Citeo](https://bo.citeo.com/sites/default/files/2025-04/20241219_MAJ_Tarif_EM_2025-FR.pdf)) ; RC produits 0 / 400 / 800 €, INPI 190 / 230 / 270 €, relecture 0 / 300 / 800 € (HYPOTHÈSES de la première étude). Étiquetage de composition non obligatoire (annexe V du règlement 1007/2011, à confirmer) ; RTC gratuit sur la position 4201. |
| Premier stock par taille (groupage maritime) | 2 668,50 | 4 066,00 | 8 013,00 | CALCUL sur SOURCÉ + HYPOTHÈSE | Bas : M 50 / L 50 / XL 50 au coût rendu central (catalogue avec logo, MOQ 50 chez Altra), 2 518,50 € + 150 € de dossier. Central : **M 100 / L 75 / XL 50** (proportionnel au mix, plancher au MOQ, §4.3), 3 680,00 € + 300 € de dossier + 1 jour d’inspection AQL (≈ 100 $, [Epic Sourcing](https://www.epicsourcing.co.uk/post/china-sourcing-agent-cost-uk-2026)) ; par air : 5 017,00 €, soit 1 337,00 € de plus. Haut : spécification haute (FOB 20–25 $), 100 par taille (haut de la fourchette de 50 à 100 de la note), 7 341,00 € + 500 € + 2 jours d’AQL. |
| Emballage de marque (création graphique + boîtes d’expédition imprimées) | 30,00 | 1 012,80 | 2 325,60 | SOURCÉ (boîtes) + HYPOTHÈSE (création) | Boîtes d’expédition avec logo 0,19–0,96 $ (MOQ 500, [Made-in-China](https://www.made-in-china.com/products-search/hot-china-products/Mailer_Boxes.html)), haut de fourchette retenu ; création 0 / 600 / 1 500 € (HYPOTHÈSE de la première étude). La boîte de vente et la notice sont dans le coût rendu (0,40 à 1,50 $). |
| Photos et vidéos UGC (grands chiens âgés) | 982,15 | 2 790,45 | 4 956,90 | SOURCÉ (UGC) + HYPOTHÈSE (photos, envois) | 5 vidéos × 170 € / 8 × 250 € / 10 × 320 €, + 12 / 15 / 18 % de coûts cachés ([Plateya](https://www.plateya.fr/blog/detail/couts-moyens-createur-ugc-2026-grille-tarifaire-plateya), [Takema](https://takema-studio.com/marques/prix-video-ugc-en-france-le-guide-complet-pour-2026)) ; photos 0 / 400 / 1 000 € ; harnais offerts à 5 / 15 / 30 créateurs (pris dans le stock, port de 6,03 €). Démonstration « avant / après » dans l’escalier ou à la montée en voiture. |
| Shopify, applications, domaine et thème (3 mois) | 123,00 | 243,00 | 980,00 | SOURCÉ (Shopify) + HYPOTHÈSE | Basic 36 €/mois / Basic + 40 € d’applications / Grow 105 € + 100 € ([Kanal](https://getkanal.com/fr/blog/prix-shopify)) ; domaine 15 €, thème 350 € (HYPOTHÈSES de la première étude). |
| Publicité de test (plan par phases au §5.2) | 630,00 | 2 520,00 | 4 270,00 | CALCUL | Plans ci-dessous. |
| Imprévus (10 %) | 644,48 | 1 909,18 | 3 833,43 | HYPOTHÈSE | Réexpéditions, casse, essai supplémentaire, frais bancaires. |
| **Total** | **7 089,30** | **21 000,94** | **42 167,72** |  |  |

- **Ce qui revient pendant le test** (budget central) : 63 commandes attendues au CPA central, soit ≈ 3 678 € de marge contributive (harnais à 119 €, coûts intermédiaires) ; 179 commandes et ≈ 13 696 € en optimiste ; 31 commandes et ≈ 1 829 € au CPA observé de 80,19 €. La trésorerie réellement exposée est le total moins ce montant, moins la valeur du stock restant (147 harnais au CPA central, après les 15 offerts aux créateurs).
- **Version minimale sans stock** : échantillons de catalogue, visuels tournés avec eux, page de précommande ou liste d’attente (délai affiché), et 630 € de publicité : ≈ 2 842 € avec l’étude de brevets minimale. Elle mesure le coût par ajout au panier ou par précommande, pas un vrai CPA.
- **Postes propres au harnais**, absents des budgets de la première étude : essais de charge (1 651 € en central) et étude de liberté d’exploitation (2 500 €) ; ensemble, ≈ 20 % du budget central.

### 5.2 Plan publicitaire par phases (harnais)

| Budget | Phase | Ensembles de publicités | Budget par jour et par ensemble | Jours | Dépense (€) | Achats (CPA 14,05) | Achats (CPA 39,88) | Achats (CPA 80,19) | Achats (CPA 94,61) | Achats (CPA 96,61) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bas | Angles créatifs (escalier, voiture, se relever, dos du maître) | 2 | 15 € | 21 | 630 | 44,8 | 15,8 | 7,9 | 6,7 | 6,5 |
| **Bas : total** |  |  |  |  | **630** | **45** | **16** | **8** | **7** | **7** |
| Central | A. Tri des angles créatifs | 3 | 15 € | 14 | 630 | 44,8 | 15,8 | 7,9 | 6,7 | 6,5 |
| Central | B. Test d’offre : harnais 119 € contre kit 139 € (ou 119 € contre 129 €) | 2 | 30 € | 21 | 1 260 | 89,7 | 31,6 | 15,7 | 13,3 | 13,0 |
| Central | C. Validation sur l’angle et l’offre gagnants | 1 | 45 € | 14 | 630 | 44,8 | 15,8 | 7,9 | 6,7 | 6,5 |
| **Central : total** |  |  |  |  | **2 520** | **179** | **63** | **31** | **27** | **26** |
| Haut | A. Tri des angles créatifs | 4 | 20 € | 14 | 1 120 | 79,7 | 28,1 | 14,0 | 11,8 | 11,6 |
| Haut | B. Test de prix 99,90 / 119 / 129 € | 3 | 30 € | 21 | 1 890 | 134,5 | 47,4 | 23,6 | 20,0 | 19,6 |
| Haut | C. Validation et premier passage à l’échelle | 1 | 60 € | 21 | 1 260 | 89,7 | 31,6 | 15,7 | 13,3 | 13,0 |
| **Haut : total** |  |  |  |  | **4 270** | **304** | **107** | **53** | **45** | **44** |

**Règles de décision proposées (inférences du calcul).**
- **Couper un ensemble** qui a dépensé 3 fois le CPA d’équilibre sans achat : ≈ 175 € pour le harnais à 119 € (5 chances sur 100 de se tromper si le vrai CPA est à l’équilibre).
- **Juger un angle** après 15 à 20 achats ; **juger une offre ou un prix** après 40 à 50 achats par variante (§4.5).
- **Décision finale** : poursuivre si, après ≈ 50 achats, le CPA observé reste sous ≈ 58 € (équilibre du harnais à 119 €) ou ≈ 69 € si la moitié des clients prend le kit ; entre ces seuils et ≈ 80 €, retravailler l’offre (kit par défaut, 129 €, preuve de charge en vidéo) ; au-delà de ≈ 80 €, le niveau actuel des campagnes Pilou, arrêter ou changer d’angle. Le seuil d’équilibre du harnais (≈ 58 €) est 4,1 à 5,7 fois celui des offres principales de la première étude (10,26 € à 14,26 €) : un CPA proche du marché (39,88 €) suffit, alors que les campagnes actuelles ressortent à 1,4 à 1,7 fois l’équilibre.

### 5.3 Peluche réplique : version courte (campagne d’échantillons auprès de 5 à 6 ateliers)

| Poste (€ HT) | Bas | Central | Haut | Statut | Détail et source |
| :--- | ---: | ---: | ---: | :--- | :--- |
| Campagne d’échantillons : même jeu de photos (pelage uni, bicolore, tacheté) envoyé à 5–6 ateliers | 1 465,00 | 1 869,60 | 2 836,80 | SOURCÉ (prix) + HYPOTHÈSE (port) | 5 ateliers × 2 animaux × 150 $ / 6 × 2 × 155 $ / 6 × 3 × 160 $ : échantillons sur mesure à 150 $ ([Fourthwall](https://products.fourthwall.com/custom-plushie)) et 160 $ ([Xuzhou Gaopeng](https://www.alibaba.com/product-detail/Custom-Plushies-Cute-Soft-Plush-Dolls_1600256277019.html)), plan de `deep_peluche_replique.md` §1 (≈ 1 800–1 900 $ hors port) ; ateliers : Pampanga, Xuzhou Gaopeng, Hebei Yerong, Yangzhou Dixin, Custom Plush Maker, artisans Etsy. |
| Essais EN 71-1, -2, -3 sur un « type » standardisé et dossier CE (statut de jouet probable) | 600,00 | 1 200,00 | 2 500,00 | HYPOTHÈSE (coût non cherché dans les notes) | Matières, yeux, coutures, garnissage ; le positionnement « objet décoratif 14 ans et plus » est fragile (guide n° 20 de la Commission, `deep_peluche_replique.md` §1.6). |
| Conformité : Citeo, REP jouets (Ecomaison), RC produits, marque INPI, relecture (CGV sans rétractation, RGPD des photos, GPSR) | 270,00 | 1 340,00 | 2 380,00 | SOURCÉ (Citeo) + HYPOTHÈSE | Citeo ([Citeo](https://bo.citeo.com/sites/default/files/2025-04/20241219_MAJ_Tarif_EM_2025-FR.pdf)) ; adhésion Ecomaison jouets 0 / 100 / 200 € (barème non trouvé) ; RC 0 / 400 / 800 € ; INPI 190 / 230 / 270 € ; relecture 0 / 500 / 1 000 € (plus lourde que pour un accessoire : exclusion de la rétractation à rédiger, contrat de sous-traitance RGPD avec l’atelier). |
| Coffrets de marque (création + premier lot de coffrets) | 150,00 | 1 050,00 | 2 250,00 | HYPOTHÈSE | Création 0 / 600 / 1 500 € ; 100 / 300 / 500 coffrets à 1,50 € (coût par pièce de `cadeaux_kits_bundles.md`). |
| Répliques de démonstration (animaux de créateurs) et vidéos UGC de réaction | 1 145,50 | 3 022,50 | 5 292,00 | SOURCÉ (UGC) + CALCUL | 3 / 5 / 8 répliques au coût rendu intermédiaire (64,50 €) + UGC comme le harnais ([Plateya](https://www.plateya.fr/blog/detail/couts-moyens-createur-ugc-2026-grille-tarifaire-plateya)) + photos 0 / 400 / 1 000 €. Formats « réaction au déballage » et « il rencontre son jumeau » (`deep_peluche_replique.md` §2.5). |
| Shopify, application de personnalisation (envoi de photos), domaine et thème (3 mois) | 183,00 | 303,00 | 1 040,00 | SOURCÉ (Shopify) + HYPOTHÈSE | Comme le harnais, + 20 €/mois d’application de personnalisation (HYPOTHÈSE) ([Kanal](https://getkanal.com/fr/blog/prix-shopify)). |
| Publicité de test (mêmes plans que le harnais ; phase B : 169 € contre 199 €) | 630,00 | 2 520,00 | 4 270,00 | CALCUL | Ton sobre pour le registre « mémorial » ; format « jumeau » pour l’échelle. |
| Imprévus (10 %) | 444,35 | 1 130,51 | 2 056,88 | HYPOTHÈSE | Réexpéditions, casse, essai supplémentaire, frais bancaires. |
| **Total** | **4 887,85** | **12 435,61** | **22 625,68** |  |  |

- **Pas de stock** : chaque peluche est fabriquée après la commande, payée d’avance par le client ; le risque de trésorerie se limite aux échantillons, aux coffrets et à la publicité. En contrepartie, il faut réserver de la capacité pour novembre (atelier de 20 personnes, ≈ 1 pièce par ouvrière et par jour, `deep_peluche_replique.md` §1).
- **Ce qui revient** (budget central) : 63 commandes au CPA central, ≈ 3 709 € de marge contributive à 169 € ; au CPA de 80,19 €, 31 commandes et ≈ 1 844 €.
- **Condition de passage** : au moins 2 ateliers qui tiennent la ressemblance (note à l’aveugle par les propriétaires), un prix ferme ≤ 56 € par pièce et un délai porte à porte de 3 à 4 semaines. Sans cela, le budget publicitaire ne doit pas être engagé.

## 6. Comparaison des 5 finalistes

### 6.1 Tableau comparatif (première commande, coûts intermédiaires sauf mention)

| Finaliste | Offre principale / comparée | Marge contributive de l’offre principale P / I / O | Marge après pub au CPA 39,88 (I) : offre / comparée | CPA d’équilibre 1re commande (I) : offre / comparée | ROAS d’équilibre TTC (I) : offre / comparée | Offre principale après CPA 80,19 / 96,61 (coûts I) | Mois pour récupérer le CPA : à 39,88 / à 80,19 (offre principale, I) | Prix TTC nécessaire pour couvrir un CPA de 39,88 / 80,19 / 96,61 (I) | Trésorerie du premier stock |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Harnais de levage | Harnais 119 € / Kit harnais + poignées 139 € | 19,87 / **58,21** / 76,36 | **18,33** / 29,23 | 58,21 / 69,11 | 2,04 / 2,01 | −21,98 / −38,40 | dès la 1re commande / > 36 mois | 93,30 / 149,84 / 172,86 | 3 680 € (225 pièces, mer) |
| Peluche réplique | Peluche 169 € / Peluche 199 € | 19,26 / **58,69** / 78,83 | **18,81** / 42,57 | 58,69 / 82,45 | 2,88 / 2,41 | −21,50 / −37,92 | dès la 1re commande / > 36 mois | 145,26 / 196,14 / 216,85 | ≈ 0 € (fabrication à la commande) |
| Sac porte-chien | Sac 99 € / Sac 119 € | −18,45 / **38,14** / 57,57 | **−1,74** / 12,53 | 38,14 / 52,41 | 2,60 / 2,27 | −42,05 / −58,47 | > 36 mois / > 36 mois | 101,43 / 157,97 / 180,99 | 1 010 € à 10 105 € |
| Enclos-tente chat | Kit tente 94,90 € / Kit tente 109 € | −1,36 / **40,07** / 56,98 | **0,19** / 10,25 | 40,07 / 50,13 | 2,37 / 2,17 | −40,12 / −56,54 | dès la 1re commande / > 36 mois | 94,64 / 151,16 / 174,19 | 1 755 € à 8 775 € |
| Lit anti-mâchonnement | Lit 149 € / Lit 169 € | 9,39 / **55,18** / 83,84 | **15,30** / 29,56 | 55,18 / 69,44 | 2,70 / 2,43 | −25,01 / −41,43 | dès la 1re commande / > 36 mois | 127,53 / 184,07 / 207,09 | 9 006 € à 15 010 € |

**Lecture.**
- **Au CPA central de 39,88 €, trois offres principales sont rentables dès la première commande** (coûts intermédiaires) : la peluche à 169 € (+18,81 €), le harnais à 119 € (+18,33 €) et le lit à 149 € (+15,30 €) ; l’enclos à 94,90 € est à l’équilibre (+0,19 €) et le sac à 99 € juste en dessous (−1,74 €). C’est un changement net par rapport à la première étude, où aucune offre principale n’était rentable à ce CPA (−25,62 € au mieux).
- **Aux CPA observés de Pilou, aucune offre principale n’est rentable** : il faudrait vendre le harnais 149,84 € TTC pour couvrir 80,19 €. Seule la **peluche à 199 €** couvre 80,19 € (+2,26 €). Le projet reste donc un pari sur la baisse du CPA, mais l’écart à combler est passé de 4 à 8 fois le seuil du jouet de la première étude à 1,4 à 1,7 fois celui du harnais.
- **Le harnais combine une marge du niveau de la peluche et le moindre risque logistique des produits stockés** : colis ≤ 1–2 kg, coût rendu de 16,11 €, peu sensible au fret ; il vise exactement la clientèle de Pilou. La peluche a une marge supérieure à 169–199 € et aucun stock, mais un coût de fabrication non coté et un verrou de production. Le lit et l’enclos sont pénalisés par le volume ; le sac par les tailles et le poids volumétrique.
- **Lecture pour le choix (inférence)** : sur les seuls chiffres, le harnais et la peluche sont en tête. Le harnais l’emporte sur la logistique, la synergie avec la clientèle de Pilou et le volume possible ; la peluche, sur la marge par commande (82,45 € à 199 €) et l’absence de stock, mais elle reste une niche (quelques milliers de commandes par an selon `cadeaux_kits_bundles.md` §3) et dépend d’un atelier qui reste à trouver et à tester.

### 6.2 Principaux risques financiers

| Finaliste | Remboursements, échanges, litiges | Guerre des prix | Transport | Trésorerie (MOQ, stock) | Réglementaire et propriété intellectuelle |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Harnais de levage | Tailles : 12 % → 24 % de remboursements = −11,12 € ; 30 % + 15 % d’échanges = marge de 39,97 €. Responsabilité si une sangle cède (essais de charge obligatoires). | CareLift ≈ 51 € et génériques 12–60 € ; copie facile si les publicités marchent ; Help ’Em Up importé 98–173 €. | M ≤ 1 kg, L et XL ≤ 2 kg (+1,67 € HT) ; peu sensible au fret (aérien +4,95 à +7,93 € par pièce). | Stock par taille : 100 XL = 19 mois de ventes au CPA central ; premier lot de 2 518 € à 7 341 € hors frais. | Brevets Help ’Em Up (EP 2 965 620 et suites US) : étude de liberté d’exploitation avant de figer le patron ; allégations santé à proscrire. |
| Peluche réplique | Litiges de ressemblance : 5,32 € par commande à 5 % ; 14,39 € à 12 % (prudent). | Cuddle Clones en français (≈ 181 € + port et taxes) ; artisans Etsy de 80–85 € (PetyChery) à 179–215 $ ; imprimé bon marché sur Amazon.fr. | Colis léger, mais coffret volumineux (3,15 kg volumétrique en prudent) ; fret aérien hebdomadaire. | Aucun stock ; capacité de pointe en novembre à réserver ; dépendance à un atelier. | Jouet probable (EN 71, CE, REP jouets) ; RGPD des photos ; ciblage du deuil délicat sur Meta. |
| Sac porte-chien | Tailles et confort : 30 % + 15 % en prudent ; la marge prudente est négative (−18,45 €). | K9 à 112–164 € et Ruffwear à 116,90 € ; 107 offres ventrales ; Little Chonk importé. | Poids volumétrique 5,4–6,0 kg : tranche ≤ 10 kg (24,00 € HT en prudent) ; fret ferroviaire +10,43 €. | MOQ 500 chez Fuliya : ≈ 10 105 €. | Sécurité (chute, chaleur, dos) ; FOB d’un sac capable de porter 20 kg non documenté. |
| Enclos-tente chat | Chat qui refuse la tente, fuite : retours d’articles utilisés (part invendable 50 %). | Génériques identiques de 18 à 140 € sur 6 canaux ; Jardiland 84,99 €. | Kit lourd : 3,9 kg réels, 7,2 kg volumétriques ; tube de 89 cm ; fret ferroviaire +13,52 €. | Saisonnalité de printemps-été : stock à écouler en 5–6 mois. | Droits 6,3 % ou 12 % selon le classement (RTC) ; aucune synergie avec Pilou. |
| Lit anti-mâchonnement | Garantie : 2,34 € par commande à 5 % de lits remplacés ; promesse « anti-mâchonnement » déçue = avis négatifs. | Knuffelwuff 105–167 € ; génériques « indestructibles » probables sur Amazon.fr. | Colis de 4,5–6 kg (13,53 € HT ; 24,00 € plancher en prudent) ; fret ferroviaire +21,39 € ; retour à 13 € et plus. | MOQ 300 : ≈ 9 006 € et 18 m³ de stock. | Ecomaison (montant inconnu) ; ingestion de tissu si le lit est percé. |

## 7. Limites et vérifications qui changeraient les chiffres

1. **Le CPA réel** reste le paramètre décisif ; il est supposé identique pour les 5 produits. Un panier de 119 à 199 € convertit en général moins bien qu’un panier de 30 à 40 € : la conversion d’équilibre du harnais à 119 € (1,37 % au CPM et au CTR de référence) est à comparer aux 0,83 à 0,99 % implicites des campagnes Pilou (`rescreen_etude_precedente.md` §1.1).
2. **Les devis** : aucun coût rendu n’est un devis. Le plus incertain est la peluche (56 € = prix public d’un atelier en 2023), puis le sac (FOB d’un sac porteur de 20 kg) et le lit. Pour le harnais, exiger poids et dimensions pliées par taille : ils décident de la tranche de 1 ou 2 kg.
3. **Les taux de remboursement, d’échange et de litige** propres à ces produits sont des hypothèses ; seuls 12 % (animalerie), 24 % (France tous secteurs) et < 2 % (Cuddle Clones, déclaré) sont sourcés.
4. **Le transport** : poids volumétrique réellement appliqué par Mondial Relay, tarifs au-delà de 5 kg et de 10 kg, hausse 2027 (Arcep).
5. **La douane** : RTC pour le harnais (4201, 2,7 %), le sac (4202 ou 4201) et l’enclos (6306 22 ou 6307 90).
6. **La propriété intellectuelle du harnais** : statut d’EP 2 965 620 en France ; c’est une condition avant tout stock.
7. **Les postes de budget sans prix sourcé** (essais de charge, étude de liberté d’exploitation, essais EN 71, patron, adhésion REP jouets) sont des estimations : demander au moins deux devis pour chacun avant d’engager le budget.
8. **Le mix de tailles et la répartition entre harnais seul et kit** sont des hypothèses : les remplacer par les ventes réelles dès les 50 premières commandes, avant le réassort.

## 8. Synthèse

- **Harnais de levage** : à 119 €, 58,21 € de marge contributive en intermédiaire, soit **+18,33 € par première commande** au CPA de 39,88 € ; le **kit avec poignées à 139 €** fait 69,11 € (+29,23 €). Aux CPA observés de Pilou, −21,98 € à −38,40 € (harnais) et −11,08 € à −27,50 € (kit). CPA d’équilibre 58,21 €, ROAS d’équilibre 2,04. Recommandation : 119 € toutes tailles, kit à 139 € mis en avant, test de 129 €.
- **Sensibilités du harnais** : l’aérien coûte 5,74 € par pièce (1 337 € sur le premier lot) ; un mix plus lourd retire ≈ 1 € ; 24 % de remboursements retirent 11,12 € ; un test à 15 €/jour sur 30 jours n’apporte que 11,3 achats au CPA central et 4,7 au CPA observé haut, trop peu pour conclure autre chose qu’un échec net.
- **Budget de test du harnais** : 7 089,30 € (bas), **21 000,94 € (central)**, 42 167,72 € (haut), dont l’étude de liberté d’exploitation (1 000 à 5 000 €, estimée) et les essais de charge. **Peluche** : 4 887,85 € / 12 435,61 € / 22 625,68 €, sans stock, avec une campagne d’échantillons de 5 à 6 ateliers comme condition de passage.
- **Classement à la première commande (CPA 39,88 €, intermédiaire)** : peluche 169 € (+18,81 €), harnais 119 € (+18,33 €), lit 149 € (+15,30 €), enclos 94,90 € (+0,19 €), sac 99 € (−1,74 €). Les commandes additionnelles ajoutent moins de 3 € par client en 12 mois : ce sont des produits de première commande.
- **Aucun de ces montants n’est un bénéfice net** : coûts de lancement, impôts, cotisations et rémunération du dirigeant restent à couvrir, et le CPA réel ne sera connu que par le test.

---

*Fichiers de calcul : `/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance40/model.py` (modèle de la première étude, copié sans modification), `/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance40/model40.py` (extension et contrôles) et `/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance40/report40.py` (tableaux). Aucune recherche web pour cette note.*
