# Coûts commerciaux d'une petite marque française d'accessoires chien/chat sur Shopify : paramètres sourcés pour les scénarios de rentabilité par commande (état au 27/10/2026)

**Note de méthode (à lire avant usage).**
1. **Objet.** Ce fichier complète le tableau des paramètres du tour 1 (`fr_costs_regulation.md`, Livrable 1). Toutes les lignes commerciales de ce tableau (n° 7 à 27) y étaient des hypothèses [H], faute de budget de recherche. Je ne reprends pas ce que le tour 1 a déjà sourcé : TVA, droit UE de 3 €, taxe française suspendue, droits ad valorem, conformité et REP. Seule exception : le statut des frais de traitement UE de 2 €, revérifié par une requête de confirmation (Q4).
2. **Accès aux sources.** Je n'ai ouvert aucune page directement : WebFetch, curl et téléchargements sont exclus dans cet environnement. **Toutes les constatations viennent des résumés de résultats WebSearch. Ce sont des preuves indirectes.** Plusieurs résumés agrègent plusieurs pages. Quand je ne peux pas rattacher un chiffre à une page précise, je l'écris (« rattachement non isolé »). Il faut relire chaque page avant publication.
3. **Budget.** J'ai utilisé les 40 requêtes WebSearch autorisées, dont 3 en mode « extended ». Le journal complet figure en fin de fichier (section Livrable, Gaps).
4. **Marqueurs.**
   - [S] : source primaire (page tarifaire de l'opérateur, administration).
   - [S2] : source secondaire (blog, comparateur, agence, prestataire concurrent, outil tiers).
   - [calc] : calcul du chercheur à partir de chiffres sourcés.
   - [H] : hypothèse non sourcée.
   - [CP] : connaissance préalable non revérifiée.
   - « Historique » : donnée antérieure à 2024.
5. **Conventions.**
   - « HT calc » = TTC ÷ 1,2. Ce calcul ne vaut que si la TVA est facturée et récupérable. Un micro-entrepreneur en franchise en base raisonne en TTC.
   - Les montants en dollars restent en dollars. Quand un calcul exige une conversion, j'utilise **1 $ = 0,86 € [H]**. Ce taux n'est pas sourcé dans cette session ; il faut le remplacer par le taux BCE du jour.
   - « Bas / central / haut » désigne le **niveau de coût**, et **bas = favorable**. La colonne « bas » contient donc les CTR, taux de conversion et paniers les plus élevés.

## Q1 : Shopify et encaissement en France (abonnements, Shopify Payments, passerelles tierces, PayPal, Alma, Klarna)

### Takeaway
- **Abonnements 2026.** Les blogs tiers concordent ; la page officielle n'a pas été lue. Basic coûte **36 €/mois** (27 € en annuel), Grow **105 €** (79 €), Advanced **384 €** (289 €).
- **Shopify Payments France.**
  - Carte « standard » : **1,5 % + 0,25 €** sur Basic, 1,3 % sur Grow, 1,1 % sur Advanced.
  - Carte « internationale » : **2,7 % + 0,25 €** sur Basic.
  - Avec une passerelle tierce, Shopify ajoute **2 % (Basic), 1 % (Grow) ou 0,6 % (Advanced)** de frais de transaction.
- **PayPal France : 2,90 % + 0,35 €.** Le taux et le fixe viennent de deux extraits distincts de la page officielle.
- **Paiement fractionné.**
  - Alma : **3,6 à 4,8 % HT** selon le nombre d'échéances, environ 3,8 % en 3x.
  - **Klarna via Shopify Payments : 4,99 % + 0,35 €.**
  - Le paiement fractionné relève du crédit à la consommation à partir du **20/11/2026**, ce qui impose une mention obligatoire dans la publicité.
- **Ordre de grandeur [calc].** À 40 € TTC, l'encaissement coûte de 0,85 € (carte via Shopify Payments) à 2,35 € (Klarna). Un mix central [H] donne environ **0,97 €, soit 2,4 %**.

### Cited Findings
**Abonnements Shopify**
- **Grille mensuelle.** Basic 36 €, Grow 105 €, Advanced 384 € par mois en paiement mensuel. Plus démarre à 2 100 €, et Starter coûte 5 €.
- **Grille annuelle.** Un guide indique 27 €, 79 € et 289 € par mois ; un autre calcule 27 €, 78,75 € et 288 €.
- **Statut et dates.** Les prix sont affichés en euros, sans mention HT ou TTC. [S2], relevés de juillet à octobre 2026 selon les pages.
- **Sources** (rattachement exact des montants annuels non isolé) : [Kanal, prix Shopify 2026](https://getkanal.com/fr/blog/prix-shopify) ; [Sellfy, tarifs Shopify 2026](https://sellfy.com/fr/blog/tarifs-shopify/) ; [La Fabrique du Net, Shopify prix 2026](https://www.lafabriquedunet.fr/logiciels/tendances/shopify-prix-quels-tarifs-pour-creer-un-site-shopify) ; [Digismoothie](https://www.digismoothie.com/fr/blog/shopify-pricing-plans).
- **Nom des plans.** Le plan « Shopify » cité dans le brief correspond au plan **Grow**, après le renommage des forfaits [CP].

**Shopify Payments (France)**
- **Taux par forfait.** Le tableau France, par forfait (Basic, Grow, Advanced, Plus), donne :
  - « Carte standard | 1,5 % + 0,25 € | 1,3 % + 0,25 € | 1,1 % + 0,25 € | 1 % + 0,25 € » ;
  - « Carte internationale | 2,7 % + 0,25 € | 2,6 % + 0,25 € | 2,4 % + 0,25 € | 2,3 % + 0,25 € ».
  - « La page ne précise pas si ces montants sont hors taxes ou toutes taxes comprises ».
  - [S2], relevé du 07/10/2026 : [Kanal, Shopify Payments : frais, versements et conditions en France](https://getkanal.com/fr/blog/shopify-payments-frais).
- **Correspondance avec l'EEE.** Les extraits ne confirment pas que « standard » désigne les cartes émises dans l'EEE ni qu'« internationale » désigne les cartes hors EEE. Trueprofit indique que les cartes American Express et les cartes internationales coûtent « généralement environ 1 % de plus que le taux national ». Ses chiffres sont surtout américains. [S2, date non visible] : [Trueprofit](https://trueprofit.io/fr/blog/shopify-payment-fees).
- **Passerelle tierce.** Sans Shopify Payments, les frais de transaction Shopify sont de 2 %, 1 %, 0,6 % ou 0,2 % selon le forfait (Basic, Grow, Advanced, Plus). [S2, 2026] : [Kanal](https://getkanal.com/fr/blog/prix-shopify) ; [Sellfy](https://sellfy.com/fr/blog/tarifs-shopify/).
- **Frais de rétrofacturation.**
  - Le blog Shopify en français parle de « frais aux fournisseurs de services marchands pour enquêter et résoudre les rétrofacturations. Ces frais, environ 15 € par incident ». Il vise les prestataires en général, pas spécifiquement Shopify Payments en France. [S2 éditeur, date non visible] : [blog Shopify FR](https://shopify.com/fr/blog/retrofacturation).
  - Selon l'aide Shopify, le montant contesté et les frais sont prélevés immédiatement sur le solde ou les versements. Shopify « peut vous rembourser les frais de rétrofacturation en fonction de votre pays ou de votre région » si le litige est gagné. [S, date non visible] : [aide Shopify](https://help.shopify.com/fr/manual/payments/chargebacks/chargeback-process).
  - Chargeflow cite des frais habituels de 20 à 30 $ par litige, facturés que l'on gagne ou non, avec un délai de réponse de 7 à 21 jours. [S2, page du 13/04/2026] : [Chargeflow, guide](https://www.chargeflow.io/fr/blog/shopify-chargebacks-guide) ; [Chargeflow, litiges Shopify](https://www.chargeflow.io/fr/chargebacks-101/shopify-dispute).

**PayPal France**
- **Taux.** La page indique un taux de **2,90 %** plus une commission fixe pour les transactions commerciales courantes, et 1,10 % pour les paiements par QR code. Elle définit le domestique par un expéditeur et un destinataire résidant dans l'EEE. [S, version non datée dans l'extrait] : [PayPal FR, Tarification pour les marchands](https://www.paypal.com/fr/business/paypal-business-fees).
- **Commission fixe.** La grille française affiche **0,35 EUR** pour les transactions commerciales en euros. Pour le QR code, le fixe est de 0,10 € au-delà de 10 € et de 0,05 € jusqu'à 10 €. [S, date non visible] : [PayPal FR, merchant-fees](https://www.paypal.com/fr/webapps/mpp/merchant-fees).
- **Autres versions de la grille.**
  - Une grille PDF « rest of world » en français, datée du 28/09/2026, existe. Ce n'est pas la grille France. [S] : [PDF PayPal du 28/09/2026](https://www.paypalobjects.com/marketing/ua/pdf/row/row-fr-merchant-fees-28-september-2026.pdf).
  - Une version de juillet 2026 d'une page d'outre-mer formule différemment la notion de « même marché ». [S] : [PayPal (gp)](https://www.paypal.com/gp/webapps/mpp/merchant-fees).

**Paiement fractionné**
- **Alma, extraits non datés ou anciens** (rattachement exact non isolé) :
  - « taux standard tout compris est de 3,8 % » ;
  - « 3,8 % du prix de la vente pour le paiement en plusieurs fois et 0,75 % pour le paiement comptant », avec des tarifs dégressifs selon le volume ;
  - environ 3,6 % HT en 2x, 3,8 % HT en 3x et jusqu'à 4,2 % HT en 4x ;
  - « à partir de 3,60 % HT » ;
  - ni frais de dossier, ni frais d'installation, ni abonnement ; le marchand est payé immédiatement et les impayés sont couverts par Alma.
  - [S2] : [Appvizer](https://www.appvizer.fr/finance-comptabilite/gestion-des-paiements/alma) ; [Blog du Modérateur](https://www.blogdumoderateur.com/tools/alma/) ; [La Fabrique du Net, Alma](https://www.lafabriquedunet.fr/logiciel/alma) ; [La Fabrique du Net, alternatives à Alma](https://www.lafabriquedunet.fr/logiciels/alternatives/alternative-alma).
- **Comparatif 2026.** « Klarna via Shopify Payments coûte 4,99 % + 0,35 € par transaction, et Alma publie de 3,60 % HT à 4,80 % HT ». [S2, 2026] : [Kanal, paiement en plusieurs fois sur Shopify](https://getkanal.com/fr/blog/paiement-plusieurs-fois-shopify.md).
- **Modèle d'Alma.** Alma n'applique aucune pénalité de retard ; son modèle repose uniquement sur les commissions versées par les commerçants. [S2, bilan 2025] : [Ecommerce Nation](https://www.ecommerce-nation.fr/?p=125991).
- **Klarna en contrat direct.** Je n'ai trouvé aucune grille marchande. Klarna perçoit « un pourcentage des frais d'interchange sous forme de commission » en plus des frais habituels. [S2, **historique** : article de l'arrivée de Klarna en France] : [FranceTransactions](https://www.francetransactions.com/actus/news-banques/klarna-debarque-en-france-le-paiement-differe-gratuit-3-fois-sans-frais-devrait.html). Le paiement en 3 fois est sans frais pour l'acheteur s'il paie à temps, et le marchand est payé immédiatement : [FAQ Klarna « Payer en 3 fois sans frais »](https://docs.klarna.com/assets/objects/920f1a65-88ed-4305-bd32-95a48185e451/FAQ+-+Payer+en+3+fois+sans+frais.pdf).
- **Scalapay et Oney.** Scalapay annonçait une « commission de 4,2 % maximum (dégressif en fonction des volumes) ». [S2, **historique, vers 2021**] : [JDN](https://www.journaldunet.com/fintech/1498261-paiement-fractionne-l-italien-scalapay-veut-s-imposer-en-france). Je n'ai trouvé aucun tarif marchand Oney.
- **Évolution réglementaire.** Selon un guide d'octobre 2026, « à partir du 20 novembre 2026, le paiement fractionné entre dans le crédit à la consommation, avec une mention obligatoire dans la publicité ». [S2] Attribution probable au guide Kanal cité plus haut. C'est cohérent avec l'application de la directive (UE) 2023/2225 (CCD2) au 20/11/2026 [CP].

### Inferences
- **Coût d'encaissement par commande [calc].** Les taux ci-dessus sont appliqués au montant TTC encaissé.

| Moyen de paiement | Taux | 25 € | 40 € | 60 € |
|---|---|---|---|---|
| Shopify Payments, carte standard (Basic) | 1,5 % + 0,25 € | 0,63 € | 0,85 € | 1,15 € |
| Shopify Payments, carte standard (Grow) | 1,3 % + 0,25 € | 0,58 € | 0,77 € | 1,03 € |
| Shopify Payments, carte internationale (Basic) | 2,7 % + 0,25 € | 0,93 € | 1,33 € | 1,87 € |
| PayPal | 2,90 % + 0,35 € | 1,08 € | 1,51 € | 2,09 € |
| PayPal + frais Shopify de passerelle tierce de 2 % (Basic), **si applicables** | 4,90 % + 0,35 € | 1,58 € | 2,31 € | 3,29 € |
| Klarna via Shopify Payments | 4,99 % + 0,35 € | 1,60 € | 2,35 € | 3,34 € |
| Alma 3x (HT) | 3,8 % | 0,95 € | 1,52 € | 2,28 € |
| Alma 3x + frais Shopify de passerelle tierce de 2 % (Basic), si applicables | 5,8 % | 1,45 € | 2,32 € | 3,48 € |

- **Taux effectif selon le mix de moyens de paiement [calc sur un mix H], à 40 € TTC.**
  - **Bas** : 100 % carte standard via Shopify Payments, soit 0,85 € (2,1 %).
  - **Central** : 80 % carte standard, 5 % carte internationale et 15 % PayPal, soit **0,97 € (2,4 %)**.
  - **Haut** : 60 % carte standard, 10 % carte internationale, 25 % PayPal avec 2 % de frais Shopify et 5 % Klarna, soit 1,34 € (3,3 %).
  - Le central du tour 1 (2,0 % + 0,25 €, soit 1,05 € à 39,90 €) est donc **cohérent**.
- **PayPal.** Il coûte environ 0,66 € de plus qu'une carte via Shopify Payments à 40 € (1,51 € contre 0,85 €). L'écart atteint environ 1,46 € si les frais de passerelle tierce s'appliquent [calc]. Il faut limiter sa part, ou passer au forfait Grow si le volume le justifie.
- **Paiement fractionné.** Il coûte 1,8 à 2,8 fois le prix d'une carte [calc] et sert surtout aux achats de plus de 500 € (Kantar, cité dans `fr_market_landscape.md`). Pour un panier de 25 à 60 €, son intérêt est faible, d'autant que la mention obligatoire de crédit à partir du 20/11/2026 alourdit les publicités. **Il vaut mieux le réserver à un produit de plus de 100 €** (inférence).
- **Abonnement ramené à la commande [calc].** 36 € ÷ 50, 100 ou 250 commandes par mois donne 0,72 €, 0,36 € ou 0,14 € par commande.
- **Franchise en base de TVA.** Shopify facture depuis l'Irlande [CP]. Le service est alors soumis à une TVA de 20 % autoliquidée et non déductible, ce qui renchérit l'abonnement de 20 % [CP] (voir le tour 1, Q1). Les commissions de paiement sont en principe des services financiers exonérés [CP].

### Gaps
- **Shopify.** La page officielle de Shopify France (tarifs et Shopify Payments) n'a pas été lue. La correspondance entre « standard / internationale » et « EEE / hors EEE » n'est pas confirmée. Les frais de conversion de devise n'ont pas été recherchés.
- **Frais de passerelle tierce sur PayPal et Alma.** On ne sait pas si Shopify les facture sur les commandes PayPal ou Alma quand Shopify Payments est actif. Ce point n'est pas vérifié. Le scénario prudent retient que oui (+2 % sur Basic) [H].
- **PayPal.** Les frais transfrontaliers pour les acheteurs hors EEE et les frais de litige PayPal n'ont pas été trouvés.
- **Paiement fractionné.**
  - Aucune grille marchande 2026 n'a été trouvée pour Klarna en contrat direct, Oney, Floa, Younited Pay ou PayPal 4X.
  - Pour Alma, le panier minimum, la dégressivité et l'application de la TVA à la commission (affichée « HT ») ne sont pas vérifiés.
- **Rétrofacturation.** Le montant exact des frais Shopify Payments en France et les conditions de leur remboursement en cas de litige gagné ne sont pas confirmés.

## Q2 : Transport de colis en France (Colissimo, Mondial Relay, Chronopost, Relais Colis, agrégateurs Boxtal et Sendcloud)

### Takeaway
- **Les grilles publiques 2026 sont sourcées de 0,25 à 5 kg.**
  - **Colissimo domicile** (La Poste, TTC au 01/01/2026) : 5,49 € à 250 g, **7,59 € à 500 g**, **9,59 € à 1 kg**, 11,19 € à 2 kg, 17,39 € à 5 kg.
  - **Mondial Relay point relais** (grille du 15/06/2026) : **4,15 € jusqu'à 500 g**, **5,99 € à 1 kg**, 7,99 € à 2 kg, 15,99 € à 5 kg.
  - **Relais Colis** : 4,20 €, 4,50 €, 6,25 € et 9,20 € selon le poids. Cette grille vient d'une source unique et reste à vérifier.
  - **Chronopost** : Chrono Relais 13 à **9,00 € HT** (0 à 1 kg) et Chrono 13 à domicile à **19,50 € HT** (0 à 1 kg).
- **Tarifs professionnels.** Ils ne sont pas publiés. On ne dispose que de prix d'appel : Boxtal « à partir de 3,60 € HT », Mondial Relay pro « démarre à 3,89 € ».
- **Écart entre point relais et domicile [calc].** Mondial Relay en point relais coûte environ 45 % de moins que Colissimo à domicile à 500 g et 38 % de moins à 1 kg. L'écart tombe à 29 % à 2 kg et à 8 % à 5 kg. **Pour un produit léger, le point relais par défaut économise environ 2,90 € HT par commande.**

### Cited Findings
**Grille publique 2026, en € TTC sauf mention contraire**

| Poids | Colissimo domicile | Colissimo point de retrait | Mondial Relay point relais ou locker | Mondial Relay domicile | Relais Colis (relais) | Chrono Relais 13 | Chrono 13 (domicile, lendemain avant 13 h) |
|---|---|---|---|---|---|---|---|
| 250 g | 5,49 | 4,79 | 4,15 (tranche jusqu'à 500 g, « à partir de ») | 7,49 (tranche jusqu'à 500 g, inférence) | 4,20 (moins de 500 g) | 9,00 HT / 10,80 TTC (0-1 kg) | 19,50 HT / 23,40 TTC (0-1 kg) |
| 500 g | 7,59 | 6,89 | 4,15 | 7,49 | 4,20 | 9,00 HT / 10,80 TTC | 19,50 HT / 23,40 TTC |
| 1 kg | 9,59 | 8,89 | 5,99 | 9,49 | 4,50 | 9,00 HT / 10,80 TTC | 19,50 HT / 23,40 TTC |
| 2 kg | 11,19 | 10,49 | 7,99 | 10,99 | 6,25 | 10,60 HT / 12,72 TTC (1-3 kg) | 21,00 HT / 25,20 TTC (1-3 kg) |
| 5 kg | 17,39 | 16,69 | 15,99 | 16,39 | 9,20 | 14,50 HT / 17,40 TTC (3-10 kg) | 24,00 HT / 28,80 TTC (3-10 kg) |
| Statut, date | [S] 01/01/2026 | [S] 01/01/2026 | [S2] grille du 15/06/2026 | [S2] grille du 15/06/2026 | [S2] 2026, source unique | [S] 01/01/2026 | [S] 01/01/2026 |

- **Colissimo.** La Poste publie les tarifs 2026 pour 250 g, 500 g, 750 g (9,29 €), 1 kg, 2 kg et 5 kg, à domicile et en point de retrait. Elle précise : « Les prix affichés ci-après sont nets en vigueur à partir du 1er janvier 2026 ».
  - Les tarifs pros négociés sont inférieurs, mais leurs grilles ne sont pas publiées dans les extraits.
  - Les grilles ne mentionnent pas de livraison « sans signature ».
  - [S] : [La Poste, tarifs Colissimo en ligne 2026](https://www.laposte.fr/colissimo-en-ligne/tarifs) ; [La Poste, principaux tarifs colis 2026](https://www.laposte.fr/tarifs-postaux-colis) ; [La Poste Pro, tarifs Colissimo 2026](https://www.laposte.fr/professionnel/tarif-colissimo) ; [La Poste Pro, tarifs colis](https://www.laposte.fr/professionnel/tarifs-postaux-colis). Repris par [ShippyPro](https://www.shippypro.com/blog/fr/envoyer-un-colis-prix-et-tarifs-2026-des-transporteurs-en-france) et [24matins](https://www.24matins.fr/en-2026-la-poste-revoit-fortement-ses-tarifs-timbres-colissimo-chronopost-tous-les-prix-reveles-1400859).
- **Hausse 2026.** Les tarifs Colissimo augmentent en moyenne de **3,4 %** en 2026, toutes destinations confondues. [S2] : [tarif-lettre.com](https://www.tarif-lettre.com/info/hausse-des-tarifs-la-poste-en-2026-ce-qui-change-pour-les-particuliers-et-les-entreprises).
- **Encadrement par l'Arcep.** L'Arcep a fixé l'évolution nominale des tarifs du service universel postal à **7,5 % par an en moyenne** sur 2026-2029, avec un plafond de 10 % par an. Le dossier tarifaire concerne aussi les modifications prévues au **1er janvier 2027**. [S, 2026] : [Arcep, avis 26-1295](https://www.arcep.fr/uploads/tx_gsavis/26-1295.pdf).
- **Carnet d'étiquettes.** Un carnet de 2 étiquettes prépayées pour colis jusqu'à 1 kg coûte 17,80 €, soit 8,90 € par colis au lieu de 9,59 €. [S2, 2026] : [tarifs-postaux.fr](https://tarifs-postaux.fr/tarif-colissimo.htm).
- **Colissimo vers l'Europe** (pour mémoire) : 14,99 € à 500 g, 19,39 € à 1 kg, 22,19 € à 2 kg. [S2, 2026] : [tarif-lettre.com, Colissimo 2026](https://www.tarif-lettre.com/tarif-colissimo-2026).
- **Mondial Relay.**
  - La grille est celle « publiés par Mondial Relay pour les envois en France depuis le 15 juin 2026 », avec un délai moyen de 3 à 5 jours ouvrés.
  - Le prix est « identique en Point Relais et en locker », seules les dimensions maximales changent. Les envois partent « à partir de 4,15 € en Point Relais ».
  - [S2] : [ShippyPro, tarifs 2026](https://www.shippypro.com/blog/fr/envoyer-un-colis-prix-et-tarifs-2026-des-transporteurs-en-france). Les valeurs de 2 kg et 5 kg figurent déjà dans `fr_deep_litiere_indicatrice_sante.md`.
- **Estimations de revendeur (Margeo, juillet 2026).** Pour la tranche de 500 g à 1 kg : Mondial Relay de 4,49 à 5,49 €, Colissimo de 8,50 à 9,50 €. Margeo estime les frais de service de Packlink ou Sendcloud à 0,10 à 0,30 € par colis, sans source officielle. [S2] : [Margeo, calculateur 2026](https://margeoapp.com/blog/calculateur-frais-mondial-relay-colissimo-2026) ; [Margeo, Mondial Relay ou Colissimo](https://margeoapp.com/blog/mondial-relay-vs-colissimo-revendeur) ; [Margeo, grille Mondial Relay 2026](https://margeoapp.com/blog/tarifs-mondial-relay-2026) (tableau non visible dans l'extrait).
- **Écart moyen.** Mondial Relay serait « en moyenne 20 % moins cher » que Colissimo. [S2, 2026] : [Eurosender](https://www.eurosender.com/fr/cvc/mondial-relay-colissimo). Un autre guide 2026 situe Mondial Relay entre 4,50 et 12,80 € pour 1 à 5 kg. [S2] : [iambeezy](https://blog.iambeezy.app/fr/envoyer-colis-pas-cher-france-2026-comparatif-tarifs-transporteurs/).
- **Mondial Relay pro.** Ces tarifs sont tirés de comptes pros anonymisés. Ce n'est pas une source officielle. [S2] : [artisansdeuxpointzero.fr](https://artisansdeuxpointzero.fr/mondial-relay-tarif-pro-artisan).
  - Le tarif pro « démarre à 3,89 € » pour l'envoi qui coûte 5,99 € au tarif public à 1 kg. Il exige un SIRET et un dépôt.
  - Tarifs HT « observés en février 2026 sur des comptes pro actifs » :
    - 4,89 € de 1 à 2 kg, sous 25 colis par mois ;
    - 6,25 € de 2 à 5 kg.
- **Relais Colis.** Moins de 500 g : 4,20 € ; moins de 1 kg : 4,50 € ; moins de 2 kg : 6,25 € ; moins de 5 kg : 9,20 €. Le colis reste 10 jours en relais, puis le retour est gratuit. [S2, 2026, page tierce unique ; grille officielle non trouvée] : [tarif-lettre.com, Relais Colis](https://www.tarif-lettre.com/relais-colis-tarif).
- **Chronopost.**
  - Grille professionnelle HT : Chrono 13 à 19,50 € (0 à 1 kg), 21,00 € (1 à 3 kg) et 24,00 € (3 à 10 kg). Chrono Relais 13 à 9,00 €, 10,60 € et 14,50 €.
  - Les prix TTC valent HT × 1,2. Ils sont en vigueur depuis le 01/01/2026.
  - L'offre Shop2Shop (2 à 4 jours) existe, mais son prix n'apparaît pas dans les extraits.
  - [S] : [La Poste Pro, tarifs Chronopost 2026](https://www.laposte.fr/professionnel/tarifs-chronopost) ; [La Poste, tarifs Chronopost](https://www.laposte.fr/tarif-chronopost).
- **Boxtal.**
  - Shop2Shop de Chronopost ou CPourToi de Mondial Relay sont proposés « à partir de 3,60 € HT pour les professionnels, négocié pour vous par Boxtal ».
  - Pour Colissimo, le marchand peut « bénéficier de notre contrat » ou utiliser le sien.
  - [S, PDF de l'opérateur **non daté**] : [grille Boxtal](https://resource.boxtal.com/documents/tarifs/tarifs-boxtal.pdf).
- **Sendcloud.**
  - Mondial Relay en point relais de 500 g à 1 kg « à partir de 4,18 € », 3,34 € avec la remise de 20 %. [S2, page promotionnelle **2024**] : [Sendcloud](https://www.sendcloud.com/fr/2024-campaign/).
  - Le poids volumétrique (L × l × h ÷ 5 000) peut entraîner un supplément s'il dépasse la tranche choisie. [S2, aide Sendcloud, date non visible] : [Sendcloud, suppléments Mondial Relay](https://support.sendcloud.com/hc/fr/articles/360036521531-Mondial-Relay-Suppl%C3%A9ments-Tarifaires-et-Restrictions).
- **Autre fourchette Colissimo.** Un comparatif commercial cite 6,84 à 10,48 € pour un colis Colissimo France de moins de 2 kg. La base (public ou pro, HT ou TTC) n'est pas précisée. [S2, 2026] : [Zunapro](https://www.zunapro.com/france/pt/blog/logistique-ecommerce-france-transporteurs).

### Inferences
- **Prix HT calculés (TTC ÷ 1,2), à utiliser si la TVA est récupérable.**

| Poids | Colissimo domicile | Colissimo retrait | Mondial Relay relais | Mondial Relay domicile | Relais Colis | Chrono Relais 13 | Chrono 13 |
|---|---|---|---|---|---|---|---|
| 250 g | 4,58 | 3,99 | 3,46 | 6,24 | 3,50 | 9,00 | 19,50 |
| 500 g | 6,33 | 5,74 | 3,46 | 6,24 | 3,50 | 9,00 | 19,50 |
| 1 kg | 7,99 | 7,41 | 4,99 | 7,91 | 3,75 | 9,00 | 19,50 |
| 2 kg | 9,33 | 8,74 | 6,66 | 9,16 | 5,21 | 10,60 | 21,00 |
| 5 kg | 14,49 | 13,91 | 13,33 | 13,66 | 7,67 | 14,50 | 24,00 |

  Le statut de TVA des tarifs publics Colissimo (prix « nets ») n'est pas vérifié : voir Gaps. S'ils sont exonérés, HT = TTC.
- **Point relais par défaut [calc].** Pour un produit de 500 g ou moins, le point relais coûte environ 3,46 € HT contre 6,33 € HT pour Colissimo à domicile, soit **environ 2,90 € d'économie par commande**. La livraison à domicile peut être proposée en option payante.
- **Seuil des 500 g [calc].** Passer de 500 g à 1 kg coûte +1,84 € TTC en Mondial Relay point relais (de 4,15 à 5,99 €) et +2,00 € en Colissimo domicile (de 7,59 à 9,59 €). **Il faut concevoir l'emballage pour rester sous 500 g** chaque fois que c'est possible. Les produits volumineux (couchages, par exemple) sont pénalisés par le poids volumétrique.
- **Comparaison avec le tour 1.**
  - Le point relais central [H] de 4,50 € est cohérent : 4,15 € TTC jusqu'à 500 g, 5,99 € à 1 kg.
  - Le domicile central [H] de 6,50 € était **sous-estimé** : il faut compter 7,59 € TTC à 500 g et 9,59 € à 1 kg.
  - L'express central [H] de 11 € correspond à Chrono Relais 13 (9,00 € HT, 10,80 € TTC). Chrono 13 à domicile coûte près du double.
- **Risque de hausse au 01/01/2027.** Le cadre de l'Arcep (+7,5 % par an en moyenne) et le dossier tarifaire 2027 rendent une nouvelle hausse de Colissimo plausible. Pour un scénario 2027, majorer de 3 à 7,5 % (inférence).
- **Relais Colis.** Il serait le moins cher au-delà de 1 kg : 9,20 € à 5 kg contre 15,99 € chez Mondial Relay. L'écart est inhabituel et repose sur une source unique ; il faut le vérifier avant de s'en servir.

### Gaps
- **Colissimo pro.** Les grilles professionnelles (contrats Facilité, Privilège ou entreprise) ne sont pas trouvées. L'écart de prix entre « Domicile sans signature » et « Domicile avec signature », distinction des offres pros [CP], est inconnu. Les grilles publiques ne mentionnent pas la signature.
- **Grilles 2026 non trouvées.** Boxtal, Sendcloud et Packlink, la grille officielle Mondial Relay pro, la grille officielle Relais Colis, le prix de Shop2Shop et Colis Privé.
- **TVA des tarifs publics Colissimo.** On ignore s'il s'agit d'un service universel exonéré ou de prix soumis à la TVA de 20 %. Ce point n'est pas confirmé.
- **Suppléments.** Carburant, haute saison, zones (Corse, montagne) et tailles hors normes n'ont pas été recherchés.

## Q3 : Logistique externalisée (3PL) en France pour une petite marque (préparation, article supplémentaire, stockage, réception)

### Takeaway
- **Pas de grille publique chez Cubyn ni chez Bigblue.** Les prix passent par un devis ou un simulateur. Bigblue vise **500 à 150 000 commandes par mois** et indique qu'une marque sous 500 commandes par mois serait mieux servie par un autre partenaire.
- **Pages commerciales françaises 2025-2026.** Elles convergent vers les fourchettes suivantes, toutes HT :
  - préparation : **1 à 2,50 € par commande d'un article**, plus **0,30 à 0,70 € par article supplémentaire** ;
  - coût complet hors affranchissement : **3,50 à 7 € par commande** (4 à 8 € en Île-de-France) ;
  - stockage : **6 à 25 € par palette et par mois**, le plus souvent 15 à 20 € ;
  - réception : **3,50 à 30 € par palette**.
- **Indice européen 2026.** Il situe la préparation à 2 à 4 € pour 1 ou 2 articles, et l'exécution complète hors affranchissement à 4 à 7 €.

### Cited Findings
- **Stockage.**
  - Pour une palette standard, la fourchette va d'environ 6 à 25 € par mois.
  - Un site situe le « tarif moyen constaté en France entre 12 € et 25 € par palette et par mois », la fourchette la plus fréquente étant de 15 à 20 €.
  - D'autres annoncent de 6 à 12 € par palette et par mois, ou de 8 à 15 € selon les prestataires et les régions.
  - La province facture de 12 à 16 € par palette et par mois, l'Île-de-France de 18 à 25 €.
  - Le petit format au casier coûte de 0,15 à 0,50 € par mois.
  - [S2, pages de prestataires 2025-2026, rattachement exact non isolé] : [tarif-logistique.fr, prix du stockage palette par mois 2025-2026](https://tarif-logistique.fr/prix-stockage-palette-mois/) ; [tarif-logistique.fr, Île-de-France 2026](https://tarif-logistique.fr/logistique-ecommerce-ile-de-france/) ; [logistique-ecommerce.com, coût du stockage 2026](https://logistique-ecommerce.com/blog/cout-stockage-ecommerce/) ; [Acolyt, 2026](https://www.acolyt.co/actualites/stockage-logistique-ecommerce/) ; [HR Associés](https://www.hr-associes.fr/blog/stockage-e-commerce).
- **Réception.** Les montants divergent : « 8 à 15 €/palette » pour une réception standard, 3,50 € par palette, ou 15 à 30 € par palette reçue. [S2, mêmes pages] : [Logily, grille 2026](https://logily.fr/tarif-logistique-ecommerce-2026/) ; [Logily, par secteur](https://logily.fr/tarif-logistique-e-commerce/) ; [JCD Logistique](https://www.jcd-logistique.fr/tarifs-logistique-e-commerce/).
- **Préparation de commande.**
  - Les fourchettes courantes tournent autour de 1 à 2,50 € par commande de base pour un seul article. Chaque article supplémentaire ajoute environ 0,30 à 0,70 €.
  - Le coût complet est « souvent annoncé autour de 3,50 et 7 euros par commande traitée, hors frais de port », et de 4 à 8 € en Île-de-France.
  - Le contenu exact de ce « coût complet » n'est pas détaillé : emballage, stockage, réception ?
  - [S2] : [Logily](https://logily.fr/tarif-logistique-ecommerce-2026/) ; [Alolog](https://alolog.fr/cout-externalisation-logistique-ecommerce/) ; [tarif-logistique.fr, Île-de-France](https://tarif-logistique.fr/logistique-ecommerce-ile-de-france/).
- **Indice européen.** Un indice 2026 situe la préparation d'une commande simple d'un ou deux articles entre environ 2 et 4 €, et l'exécution complète hors affranchissement autour de 4 à 7 €. Il n'est pas propre à la France. [S2, 2026] : [EightX, EU 3PL Cost Index](https://eightx.co/blog/eu-3pl-cost-index).
- **Prix d'appel.** Une offre est annoncée « à partir de 0,95 € par pick ». C'est une page commerciale. [S2, 2026] : [Zunapro](https://www.zunapro.com/france/pt/blog/logistique-ecommerce-france-transporteurs).
- **Bigblue.**
  - Le devis comprend un tarif par commande (préparation, emballage, expédition), qui « baisse avec le volume », plus le stockage au m³, un abonnement au logiciel Bigblue et des packs optionnels, hors TVA.
  - Bigblue cible 500 à 150 000 commandes par mois, et les marques de moins de 500 commandes par mois « seraient mieux servies par un partenaire spécialisé dans les jeunes marques ».
  - L'application Shopify facture en dollars.
  - Un concurrent (La Fabrique du Net) affirme que la facture devient difficile à justifier au-delà de 3 000 commandes par mois. Cette affirmation vient d'une source intéressée et n'est pas vérifiée.
  - [S, date non visible] : [Bigblue, tarifs](https://www.bigblue.co/fr/tarifs) ; [application Shopify Bigblue](https://apps.shopify.com/bigblue?locale=fr) ; [S2] : [La Fabrique du Net](https://www.lafabriquedunet.fr/logiciels/alternatives/alternative-bigblue).
- **Cubyn.**
  - Je n'ai trouvé aucun barème public. Cubyn facture un montant mensuel qui couvre réception, stockage, traitement, livraison et retours.
  - Le centre d'aide de Cubyn donne un exemple : une facture de 112 518,06 € sur un mois pour plus de 15 000 commandes. C'est un client sans rapport avec une petite marque.
  - Packlink parle de « quelques euros par objet ».
  - Cubyn revendique une réduction de 30 % des coûts logistiques ; c'est une affirmation de l'entreprise.
  - [S2, dates non visibles] : [Expertmarket](https://www.expertmarket.com/fr/logistique-ecommerce/cubyn-avis) ; [Packlink](https://www.packlink.com/fr-FR/transporteurs/cubyn/) ; [FrenchWeb](https://www.frenchweb.fr/cubyn-leve-35-millions-deuros-pour-batir-un-reseau-logistique-independant-des-marketplaces/417925).

### Inferences
- **Deux lectures du coût par commande, à trancher sur devis.**
  - **Par composants [calc + H].** Préparation 1,75 € (milieu de 1 à 2,50 €), stockage et réception ramenés à l'unité 0,23 € (voir plus bas), emballage 0,35 € [H] : environ **2,30 € HT**.
  - **Coût complet annoncé.** 3,50 à 7 €, milieu **5,25 € HT** [calc].
  - Le tour 1 retenait 3,20 € (2,50 + 0,30 + 0,40 [H]). Sa valeur se situe donc entre les deux lectures, mais **sous le bas de la fourchette « coût complet »**.
- **Stockage et réception ramenés à l'unité [calc + H].** La formule est : (stockage par palette et par mois × mois de rotation + réception par palette) ÷ unités par palette.
  - **Exemple central** : (17,50 € × 2 mois + 11,50 €) ÷ 200 unités = **0,23 € par unité**. Le nombre d'unités par palette et la rotation de 2 mois sont des hypothèses [H].
  - **Cas défavorable** : (25 € × 4 mois + 30 €) ÷ 100 unités = 1,30 € par unité. Un stock qui tourne lentement multiplie ce coût par plus de 5.
- **Volume et minimums.** Sous 500 commandes par mois, une marque n'est explicitement pas la cible de Bigblue. Les minimums mensuels et frais d'entrée des petits 3PL ne sont pas publiés de façon uniforme. **Au lancement, à 2 à 10 commandes par jour, un forfait minimum peut dominer le coût par commande** (inférence, montant non sourcé).

### Gaps
- **Grilles des 3PL.** Ni Cubyn ni Bigblue ne publient de grille. Les minimums mensuels, frais d'intégration, coûts de retour (réception, contrôle, remise en stock) et prix des emballages fournis par le 3PL n'ont pas été trouvés.
- **Contenu du « coût complet ».** On ignore ce que recouvre exactement la fourchette de 3,50 à 7 €.
- **Autres prestataires.** Aucun autre prestataire nommé et travaillant avec des marchands Shopify n'a de grille publique dans les extraits.

## Q4 : Sourcing en Chine (agents, fret aérien, maritime et ferroviaire, lignes de dropshipping, frais UE de 2 €)

### Takeaway
- **Agents de sourcing.** Ils prennent **3 à 10 % de la commande** ; 5 à 10 % est la fourchette la plus citée. La commission peut atteindre 15 % sur les petites commandes, et les agents du marché de Yiwu prennent 3 à 5 %. L'inspection est souvent incluse dans un forfait (5 %, minimum 100 $, inspection AQL 2,5 comprise chez un agent).
- **Fret aérien.**
  - L'indice Freightos Chine vers Europe du Nord atteint environ **4,88 $/kg dans la semaine du 08/09/2026**, contre 3,52 $/kg au 31/12/2025. Ce tarif s'entend d'aéroport à aéroport, hors frais annexes.
  - Les transitaires annoncent 5 à 9 $/kg en « air DDP » et **7,75 $/kg en express (octobre 2026)**.
- **Fret maritime.**
  - L'indice Drewry Shanghai-Rotterdam est passé de 2 773 à **3 944 $ par conteneur de 40 pieds** entre la fin mai et le 08/07/2026. Je n'ai pas trouvé de relevé d'octobre.
  - Le groupage maritime (LCL) coûte 30 à 60 $/m³ pour le fret seul, avec 15 à 45 jours de transit.
  - Le ferroviaire coûterait 250 à 450 $/m³, mais la source se contredit.
- **Lignes de dropshipping.** Le délai CJPacket « Euro Ordinary » vers la France est de **6 à 14 jours**. **Aucun prix 2026 n'a été trouvé** pour YunExpress ou CJPacket : la ligne reste en hypothèse [H].
- **Frais de traitement UE de 2 €.** L'administration fiscale irlandaise annonce, le 29/09/2026, leur application **au 1er novembre 2026**, à hauteur de 2 € « per distinct item ». **La publication au Journal officiel n'est pas vérifiée.**

### Cited Findings
**Frais de traitement UE de 2 € (une requête de confirmation)**
- **Annonce irlandaise.** Revenue écrit le 29/09/2026 : « From 1 November 2026, the EU will introduce a new Union Handling Fee of €2 per distinct item, which businesses that file Customs declarations for eCommerce packages will pay. » [S, administration fiscale et douanière irlandaise] : [Revenue (Irlande), communiqué du 29/09/2026](https://www.revenue.ie/en/corporate/press-office/press-releases/2026/pr-092926-handling-fee.aspx).
- **Acte délégué.** « The handling fee is a customs charge of €2 "per item" […] set by the European Commission in delegated regulation C(2026) 6694 of September 21. It applies from the tenth day after publication in the Official Journal of the EU, with November 1 as the deadline written into the new Union Customs Code. » [S2, date non visible] : [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/18538/eu-handling-fee-2-euro-non-eu-parcels).
- **Versions divergentes.**
  - Un site ukrainien non daté écrit que « the 2-euro amount is still undergoing a formal approval procedure ». [S2] : [kurs.com.ua](https://kurs.com.ua/en/novost/1481261-evrosojuz-zaprovadit-novii-zbir-na-posilki-z-za-mezh-bloku).
  - RSM Belgique parle d'une « expected EU harmonization as from November 2026, with earlier national implementations possible ». [S2] : [RSM](https://www.rsm.global/belgium/en/insights/eu-introduces-new-charges-low-value-imports).
  - DHL (Royaume-Uni) indique « €2 per parcel (TBC) ». [S2] : [DHL](https://www.dhl.com/gb-en/ecommerce/uk/international-parcel-delivery/eu-customs-changes-2026.html).

**Agents de sourcing**
- **Commissions.** La plupart des sources situent la commission entre 3 et 10 % de la valeur de la commande. Un guide britannique retient 5 à 10 % et jusqu'à 15 % pour les petites commandes ; pour les grosses commandes (plus de 50 000 £), la fourchette tombe à 3 à 6 %. Les agents du marché de Yiwu prennent 3 à 5 %.
- **Forfaits.** Les forfaits mensuels vont de 500 à 3 000 $ (sources américaines) ou de 800 à 3 000 £ (source britannique). Un projet ponctuel coûte 300 à 1 500 $, ou 500 à 2 000 £.
- **Exemples d'agences.**
  - Supplyia : 5 à 10 %, plus environ 100 $ par jour de visite d'usine.
  - Sourcing Allies : 100 $ par audit de fournisseur, et un forfait à 500 $ par mois.
  - JingSourcing Basic : 5 % de la valeur produit (minimum 100 $), inspection AQL 2,5 incluse.
- **Mises en garde.** Certains agents se rémunèrent aussi auprès de l'usine, ce qui peut gonfler les prix unitaires de 30 à 40 %. Il faut vérifier la base de calcul de la commission (EXW, FOB ou facture).
- **Sources.** [S2, guides 2026, rattachement exact non isolé] : [Epic Sourcing, guide Royaume-Uni 2026](https://www.epicsourcing.co.uk/post/china-sourcing-agent-cost-uk-2026) ; [Epic Sourcing, États-Unis 2026](https://www.epicsourcing.co/post/sourcing-agent-fees-usa-2026) ; [Supplyia](https://www.supplyia.com/China-sourcing-agent/) ; [Maple Sourcing](https://www.maplesourcing.com/china-sourcing-agent-fees-complete-cost-breakdown.html?page=7) ; [Tianwen, guide du 27/07/2026](https://tianwenwangluo.com/en/china-sourcing-agent/).

**Fret aérien**
- **Indice Freightos (Freightos Air Index), Chine vers Europe du Nord.**
  - Environ **4,88 $/kg dans la semaine du 08/09/2026**, contre 3,52 $/kg au 31/12/2025, soit environ +39 %.
  - Ce sont des tarifs « airport-to-airport » : enlèvement, dédouanement, droits et livraison s'ajoutent.
  - Je n'ai trouvé aucun relevé d'octobre 2026.
  - [S2, reprise de l'indice] : [DocShipper (EN)](https://china.docshipper.com/en/?p=30165) ; [DocShipper (FR)](https://china.docshipper.com/fr/?p=25032).
- **Mise à jour d'octobre 2026.** Un transitaire indique « Express: $7.75/kg (flat versus September) ». [S2, page mise à jour en octobre 2026] : [Sino-Shipping, Chine-France](https://www.sino-shipping.com/country-guides/shipping-from-china-to-france/).
- **Tarifs « air DDP ».**
  - « Indicative DDP cost: $5-9/kg above 100 kg palletized, or from $6/kg for small parcels ».
  - 5,70 à 6,40 $/kg à partir de 45 kg, en 8 à 10 jours.
  - Environ 11,35 $/kg en express, selon un guide de juin 2026.
  - [S2, guides 2026, rattachement non isolé] : [Dantful, DDP](https://www.dantful.com/ddp-shipping-from-china-to-france/) ; [Dantful, tarifs](https://www.dantful.com/shipping-rates-from-china-to-france/) ; [Weilong](https://www.weilong-sz.com/ddp-shipping-from-china-to-france/) ; [Goodhope Freight](https://www.goodhopefreight.com/freight/freight-price-list-from-china-to-france.html) ; [Viputrans](https://www.viputrans.com/shipping-from-china-to-france-2026-guide-to-importing-goods.html).

**Fret maritime et ferroviaire**
- **Indice Drewry (World Container Index), Shanghai-Rotterdam, conteneur de 40 pieds.**
  - Semaine 21 de 2026 : +15 %, à **2 773 $**.
  - Semaine 24 : +5 %, à **3 768 $**.
  - 08/07/2026 : -7 %, à **3 944 $**. L'indice composite est alors à 3 493 $.
  - [S2, reprises de Drewry] : [The Logistics World, 08/07/2026](https://thelogisticsworld.com/actualidad-logistica/world-container-index-de-drewry-se-mantiene-a-la-baja) ; [WLA, semaine 24](https://wla.us.com/?p=48761) ; [WLA, semaine 21](https://wla.us.com/?p=48103).
  - Je n'ai trouvé **aucun relevé de septembre ou d'octobre 2026** (deux requêtes).
- **Fourchettes d'un transitaire.** [S2, prestataire] : [Sino-Shipping, vue d'ensemble des coûts](https://www.sino-shipping.com/fr/freight-costs-from-china/overview/) ; [Sino-Shipping, coûts](https://www.sino-shipping.com/fr/shipping-from-china/costs-overview/).
  - Conteneur de 20 pieds Shanghai-Europe : 1 500 à 4 500 $ au 2e trimestre 2026.
  - Groupage (LCL) Chine-Europe : **30 à 60 $/m³**, en 15 à 45 jours, avec une hausse de plus de 30 % en haute saison (août à octobre).
  - Ferroviaire : **250 à 450 $/m³**, présenté comme 60 à 70 % moins cher que l'aérien. Le même acteur décrit ailleurs le rail comme « 30-40 % de plus que maritime », ce qui est contradictoire.
- **Tension en juin 2026.** Un bulletin de mai 2026 signale une forte tension sur le maritime Chine-Europe début juin, avec un indice conteneurisé en hausse de plus de 34 % sur un mois. Depuis le 01/01/2026, les compagnies doivent couvrir 100 % de leurs émissions dans le cadre de l'EU ETS, ce qui alourdit les surcharges. [S2] : [DocShipper, bulletin de mai 2026](https://china.docshipper.com/fr/?p=24957).
- **Volumes ferroviaires.**
  - Au 1er trimestre 2026 : 5 460 trains (+29 %) et 546 000 conteneurs (+22 %), selon China State Railway Group. [S2, 17/04/2026] : [China Services Info](https://www.chinaservicesinfo.com/s/202604/17/WS69e1a8d2498e36855033bfbb/china-europe-freight-train-services-surge-in-q1-2026.html).
  - En 2025, les volumes Europe vers Chine ont chuté de 22,7 %, à 38 422 EVP. [S2, 2025] : [Trans.info](https://trans.info/fr/fret-maritime-moins-cher-le-rail-eurasien-perd-du-terrain-en-2025-467116).

**Lignes de dropshipping (colis de 0,3 à 1 kg vers la France)**
- **CJPacket « Euro Ordinary », délais.** Environ 7 à 10 jours vers la France, « many in 7 days ». Un autre guide indique 7 à 14 jours. Ship24 affiche 6 à 12 jours. La ligne YW (Yanwen) est plus lente : 15 à 25 jours.
  - Les numéros de suivi CJP sont internes ; le colis reçoit ensuite le numéro du transporteur (Yanwen, Yun Express, SFC…).
  - [S2, sites de suivi, contenu non daté ou ancien] : [TrackingMore](https://www.trackingmore.com/review-cj-dropshipping.html?p=10) ; [Ship24](https://ship24.com/couriers/cjpacket-tracking) ; [ParcelsApp](https://parcelsapp.com/en/carriers/cjpacket).
- **CJPacket, prix.** Aucun prix 2026 par colis vers la France n'a été trouvé (trois requêtes). Le seul commentaire tarifaire vient d'un billet CJ de 2019 sur la ligne États-Unis. [S, **historique**] : [blog CJ](https://blog.cjdropshipping.cn/detail/growing-cjpacket-best-reliable-china-us-shipping-option).
- **Seul prix de ligne trouvé, qui n'est pas un tarif marchand.** Le calculateur d'un agent d'achat grand public affiche « FR Economic General Small Parcel (charged by actual weight) | $24.26 ¥152 | $38.62 ¥242 | $52.99 ¥332 | $81.72 ¥512 | 12-20 », soit de 1 kg à 5 kg environ, en 12 à 20 jours. Le statut DDP et l'inclusion des 3 € et 2 € ne sont pas précisés. [S2, date non visible] : [Fishgoo](https://blog.fishgoo.com/china-shipping-cost-estimator/).
- **Pages de transitaires 2026 dépassées.** Certaines présentent encore la taxe française de 2 € « effective March 1, 2026 » sans mentionner sa suspension au 01/07/2026 (voir le tour 1). D'autres hésitent entre un droit de 3 € « per HS code » et « per item ». [S2] : mêmes pages que l'aérien.

### Inferences
- **Frais de 2 € au 01/11/2026.** Ils sont annoncés par une administration nationale (l'Irlande, le 29/09/2026), et les sources secondaires concordent sur la date et le montant. Pour les scénarios, je les retiens comme **applicables depuis le 01/11/2026** (2 € par article distinct). Il faut confirmer la publication au JO et l'absence d'objection.
  - L'expression « per distinct item » suggère la même logique que pour le droit de 3 € : par article distinct, et non par unité. C'est une inférence à confirmer.
  - Les frais sont payés par le déclarant (transporteur ou plateforme), qui les répercutera vraisemblablement sur le vendeur.
- **Fret à l'unité, modèle stock [calc].** Hypothèses [H] : produit emballé de 0,4 kg taxable et de 0,002 m³. Taux : 1 $ = 0,86 € [H].
  - Aérien DDP de 5, 6 ou 9 $/kg : 1,72 €, 2,06 € ou 3,10 € par unité.
  - Indice Freightos à 4,88 $/kg : 1,68 €, hors frais annexes.
  - Express de 7,75 à 11,35 $/kg : 2,67 à 3,90 €.
  - Groupage maritime de 30 à 60 $/m³ (fret seul) : 0,05 à 0,10 € par unité, plus les **frais fixes d'origine, de destination et de dédouanement, non sourcés**, qui dominent sur un petit envoi.
  - Ferroviaire de 250 à 450 $/m³ : 0,43 à 0,77 €.
  - Contrôle de cohérence : un conteneur de 40 pieds à 3 944 $ pour environ 67 m³ utiles [CP] revient à environ 59 $/m³, soit la même zone que le haut du groupage.
- **Dropshipping.** Faute de prix de ligne sourcé, le coût par commande reste « prix de la ligne [H] + 3 € + 2 € », plus le produit.
  - Le prix [H] du tour 1 (4,50 à 8 €) n'est ni confirmé ni infirmé.
  - Le calculateur Fishgoo (24 $ pour 1 kg) concerne un agent d'achat grand public : je ne le retiens pas comme tarif marchand.
  - **Le délai de 6 à 14 jours est compatible avec l'obligation d'afficher un délai de livraison** (voir le tour 1, Q5), mais il reste au-dessus des 2 à 5 jours d'un stock en France.
- **Agent.** Pour une première commande de petite taille, il faut compter **5 à 10 % du coût produit**, et jusqu'à 15 %. L'inspection AQL est à prévoir dans le forfait ou en sus, environ 100 $ par jour.

### Gaps
- **Prix des lignes.** Les prix par colis de 0,3 à 1 kg vers la France de YunExpress, CJPacket, 4PX et Yanwen n'ont pas été trouvés en trois requêtes. On ignore aussi si ces lignes sont DDP ou IOSS, si elles incluent les 3 € et 2 €, et quelle est la redevance par colis.
- **Groupage et douane.** Le coût porte-à-porte d'un groupage Chine-France (frais d'origine, de port, de dédouanement, de livraison) et les honoraires de transitaire ou de commissionnaire en douane n'ont pas été trouvés.
- **Relevés d'octobre 2026.** Il manque l'indice Drewry, l'indice FBX Asie-Europe du Nord et l'indice aérien Freightos.
- **Inspection.** Le prix d'une inspection indépendante, par exemple QIMA à la journée-homme, n'a pas été trouvé.
- **Frais de 2 €.** La publication au JO de l'acte C(2026) 6694, la fin du délai d'objection et la définition de l'« item » restent à vérifier.

## Q5 : Benchmarks publicitaires Meta et TikTok en France (CPM, CTR, CPC, conversion, CPA, ROAS)

### Takeaway
- **Il n'existe pas de benchmark officiel Meta**, et je n'ai trouvé **aucune donnée France propre aux animaux**. Les repères français 2026 sont les suivants :
  - **CPM Meta : 8 à 18 €** (La Fabrique du Net), ou 12 à 20 € (Adintime).
  - **Série Superads** : CPM médian moyen d'environ 8 (probablement en $) de juillet 2025 à juillet 2026, avec un **pic à 21,74 en juillet 2026**.
  - **CPC : 0,40 à 1,80 €**, et un CPC médian d'environ 0,62 $ selon Superads.
- **Catégorie animaux (WordStream 2025, campagnes de trafic) :** **CPC de 0,78 $** et **CTR de 1,63 %**, contre 0,70 $ et 1,51 % toutes industries.
- **Conversion du site.** Environ **2 % en France**, 1,4 à 1,8 % sur Shopify, et **2,6 % pour l'animalerie** (2,2 % sur mobile) selon Wisepim.
- **ROAS Meta médian.** Environ **1,8 pour l'animalerie**, non vérifié, contre 2,19 toutes industries (Varos, avril 2025).
- **CPA [calc] : environ 14 € (favorable), environ 40 € (central) et environ 95 € (défavorable).** Le central est corroboré par deux calculs indépendants, l'un à partir du coût des impressions, l'autre à partir du panier moyen et du ROAS.
- **TikTok France.** Une seule source donne un CPM de **3 à 8 €** ; il n'y a pas de CPA français.

### Cited Findings
**Meta, France**
- **CPM (série Superads).** L'échantillon de Superads n'est pas décrit (« données publicitaires »). [S2, période de juillet 2025 à juillet 2026] : [Superads, CPM France](https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/france).
  - « France started the period at a CPM of about 7.47 and finished at 21.74, a roughly +191% change from July 2025 to July 2026. Across the full period France's median CPM averaged approximately 8.06 ».
  - Les CPM français ont été nettement inférieurs au benchmark mondial sur la majeure partie de la période, avec un creux en février 2026 et un pic brutal en juillet 2026.
  - L'unité n'est pas précisée dans l'extrait ; il s'agit probablement de dollars.
- **CPC (série Superads).** « France's median CPC for all industries averaged about $0.62 versus a global baseline of roughly $1.05. By July 2026 France had swung to roughly 105% above the global benchmark. » [S2] : [Superads, CPC France](https://www.superads.ai/facebook-ads-costs/cpc-cost-per-click/france).
- **Chiffres statiques 2026 (rattachement non isolé, méthodologie inconnue).** [S2]
  - CPM France de 6,95 $ : probablement [PaceAds](https://paceads.com/research/meta-ads-statistics-2026).
  - « France $8.05 $1.15 $6.50–$9.50 » (CPM moyen, CPC moyen, fourchette de CPM) : probablement [Adamigo, par pays](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026).
- **Repères en euros (La Fabrique du Net, 2026).** Pour Facebook : CPM de 8 à 18 €, CPC de 0,40 à 1,80 €, coût par lead de 15 à 45 €. Ailleurs dans l'article : « CPM moyen : 10 € à 20 € », toutes plateformes. L'échantillon n'est pas précisé. [S2] : [La Fabrique du Net, prix d'une pub en 2026](https://www.lafabriquedunet.fr/logiciels/tendances/facebook-linkedin-instagram-twitter-quel-est-le-cout-dune-annonce).
- **Comparaison Meta-TikTok.** « Average CPM in France: €3 to €8, which is 40% to 60% cheaper than Meta Ads (€12-20) ». [S2, date non visible] : [Adintime](https://adintime.com/en/blog?id=311).

**Meta, repères mondiaux et e-commerce**
- **WebFX 2026.** Taux de clic de 0,72 à 1,49 % sur Facebook et de 0,22 à 0,88 % sur le fil Instagram. CPC de 1,06 à 1,72 $ sur Facebook, 3,35 $ sur le fil Instagram et 1,83 $ sur les stories. CPM de 7,47 $ sur Facebook et de 6,25 à 7,68 $ sur Instagram. [S2] : [WebFX](https://www.webfx.com/blog/social-media/meta-benchmarks/).
- **AdKit, septembre 2026.** Médianes Meta tous placements : **CPM 9,08 $, CPC 0,36 $, CTR 2,46 %**. AdKit publie aussi les 25e et 75e percentiles. Le type de CTR (lien ou tous clics) n'est pas précisé. [S2] : [AdKit](https://adkit.so/benchmarks).
- **CPM e-commerce.** Le CPM médian Meta des marques e-commerce clientes de Triple Whale est de **15,06 $**, en hausse de 13,2 % sur un an. [S2, date non visible ; relayé dans les résultats, rattachement non isolé] : [Digital Applied](https://www.digitalapplied.com/blog/facebook-ads-benchmarks-2026-cpc-cpm-ctr-industry) / [Orange MonkE](https://orangemonke.com/blogs/facebook-ads-benchmarks/).
- **CTR par objectif.** CTR médian de **2,19 % pour l'e-commerce**, contre 1,71 % pour le trafic et 2,59 % pour les leads. [S2, 2026, rattachement probable] : [Adamigo, par objectif et placement](https://www.adamigo.ai/blog/meta-ads-benchmarks-2026-by-objective-and-placement).
- **Absence de référence officielle.** Il n'existe pas de benchmark officiel de Meta. Beaucoup de « CPC moyens » partagés sont anciens ou sans source. [S2] : [Digital Applied](https://www.digitalapplied.com/blog/facebook-ads-benchmarks-2026-cpc-cpm-ctr-industry).
- **Influee (données d'octobre 2025).**
  - CPM Facebook de 8 à 11 $ en moyenne : d'environ 2 $ pour de la notoriété sur audience froide à plus de 30 $ pour du retargeting chaud au 4e trimestre.
  - CPC de 0,70 $ pour le trafic et de 1,92 $ pour les leads. Les Reels coûtent environ la moitié du fil Facebook.
  - [S2] : [Influee, bon CPM](https://influee.co/fr/blog/good-cpm-facebook-ads) ; [Influee, coût des Facebook Ads](https://influee.co/fr/blog/how-much-do-facebook-ads-cost).

**Catégorie animaux**
- **WordStream 2025 (campagnes de trafic).** CPC moyen de 0,70 $ toutes industries et de **« Animals & Pets $0.78 »**. La taille de l'échantillon n'est pas visible dans l'extrait. [S2, 2025] : [WordStream, Facebook Ads Benchmarks 2025](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025).
- **Taux de clic, catégorie animaux.**
  - **Animals & Pets : 1,63 %**, contre 1,51 % en moyenne pour les campagnes de trafic. Ce tableau reprend vraisemblablement WordStream 2025 ; sa date n'est pas visible. [S2] : [MegaDigital](https://megadigital.ai/en/blog/facebook-ad-benchmarks/).
  - La page WordStream non datée donne 1,68 % pour les animaux. Le chiffre est probablement ancien (historique probable). [S2] : [WordStream](https://www.wordstream.com/facebook-ad-benchmarks).
- **Chiffres animaux inexploitables.**
  - Influee 2026 donne « pets » à 2,19 % et 38,18 $, mais les colonnes ne sont pas identifiables dans l'extrait. [S2] : [Influee](https://influee.co/blog/facebook-ads-benchmarks).
  - La page Varos « Facebook Ads CVR For Pets Subscriptions » ne contenait aucun chiffre dans l'extrait. [S2] : [Varos](https://www.varos.com/benchmarks/facebook-cvr-for-pets-subscriptions).
- **ROAS Meta médian.**
  - **« Pet Supplies » : 1,78** dans un récapitulatif, et **environ 1,80x** dans un autre, parmi les catégories « difficiles ». Ce n'est pas vérifié sur des données primaires. Rattachement non isolé entre [Superscale (mis à jour le 23/07/2026)](https://superscale.ai/learn/roas-benchmarks-by-industry/), [GoMarble](https://www.gomarble.ai/roas-benchmarks), [Hawky](https://hawky.ai/blog/roas-benchmarks-by-industry) et [CorePPC](https://coreppc-website.pages.dev/blog/average-roas-by-industry-2026/).
  - **2,19x sur 28 industries** (Varos, données mises à jour en avril 2025). Résumé relayé, rattachement non isolé : [Flable](https://flable.ai/blog/meta-ads-profitability-benchmarks-d2c) ou [Ryze](https://www.get-ryze.ai/blog/meta-ads-cost-ecommerce-average-spend-roas).
- **Coût d'acquisition client par panier.** Lebesgue publie un CAC « Food, Beverage & Pet » d'environ **17 à 18 $ pour un panier de moins de 100 $**, et d'environ 45 $ pour 100 à 200 $. Ce n'est pas une médiane Varos ou Triple Whale, et la page ne distingue pas les animaux. [S2, 2026] : [Lebesgue](https://lebesgue.io/facebook-ads/meta-ads-benchmarks-by-industry-and-aov).
- **Google Ads, pour mémoire.** Triple Whale donne, toutes industries, un CPA médian de 28,14 $ et un ROAS de 3,27. Ses médianes par catégorie ne sont visibles que dans son outil. [S2] : [Triple Whale](https://www.triplewhale.com/blog/google-ads-benchmarks.md).

**Taux de conversion du site**
- **France.** « En France, la moyenne constatée se situe plutôt dans le bas de cette fourchette [2 % à 3 %], autour de 2 % ». [S2, 2026] : [La Fabrique du Net](https://www.lafabriquedunet.fr/logiciels/tendances/taux-de-conversion-ecommerce-statistiques-et-benchmarks).
- **Shopify.** « La moyenne globale sur Shopify se situe autour de 1,4 % à 1,8 % ». [S2, 2026] : [Launchtip](https://www.launchtip.com/fr/blog/benchmarks-taux-conversion-shopify-par-secteur-2026-statistiques-fourchettes-bon).
- **Tendance.** Le taux de conversion e-commerce a reculé de 5 % sur un an. Le desktop convertit à 3,4 %, soit 74 % de plus que le mobile. [S2, benchmark 2026] : [Contentsquare](https://contentsquare.com/fr-fr/blog/taux-transformation/).
- **Animalerie.** Taux de conversion de **2,6 %** (moyenne e-commerce 2,3 %), **2,2 % sur mobile**, et abandon de panier de 63,5 %. Le périmètre géographique et l'échantillon ne sont pas précisés. [S2, page du 07/05/2026] : [Wisepim, animalerie](https://wisepim.com/fr/ecommerce-industry-insights/pet-supplies).

**TikTok**
- **France.** CPM de **3 à 8 €**. C'est une source unique (Adintime, voir plus haut).
- **Repères mondiaux.**
  - CPM d'environ 6,16 à 6,21 $ et CPC de 0,99 $ en 2026. [S2] : [MegaDigital](https://megadigital.ai/en/blog/how-much-do-tiktok-ads-cost/).
  - CPM de 4,20 à 9,00 $ et CPC de 0,17 à 1,00 $. **CPA médian de 32,74 $**, la plupart des secteurs acquérant un client pour moins de 22 $. En 2025, le CPM a augmenté de 16 % et le taux de conversion a baissé de 6,2 %. [S2, 2026] : [Influee, coût](https://influee.co/fr/blog/tiktok-ads-cost) ; [Influee, benchmarks](https://influee.co/fr/blog/tiktok-ads-benchmarks).
  - In-Feed Ads : CPM de 8 à 15 $ et CPC de 0,10 à 0,30 $. [S2, 2026] : [TrendTrack](https://www.trendtrack.io/fr/blog-post/couts-publicitaires-tiktok-guide-complet-des-tarifs-et-calculateur-2026).

### Inferences
- **CPA Meta reconstruit [calc]** avec la formule CPA = CPM ÷ (1 000 × CTR × taux de conversion). Chaque entrée est sourcée, mais elles viennent de sources différentes.

| Scénario | CPM | CTR | Conversion | CPA |
|---|---|---|---|---|
| Favorable | 8 € (bas de La Fabrique du Net, environ la médiane Superads) | 2,19 % (médiane e-commerce) | 2,6 % (animalerie, Wisepim) | **14,0 €** |
| Central | 13 € (milieu de 8 à 18 €) | 1,63 % (animaux, trafic, 2025) | 2,0 % (France) | **39,9 €** |
| Défavorable | 20 € (haut d'Adintime ou de La Fabrique du Net ; pic Superads de juillet 2026 à 21,74) | 1,51 % (moyenne toutes industries) | 1,4 % (bas Shopify) | **94,6 €** |

  - **Contrôle par le CPC.** CPA = CPC ÷ taux de conversion.
    - Avec 0,40 € et 2,6 %, on obtient 15,4 €.
    - Avec le CPC animaux de 0,78 $ (environ 0,67 €) et 2 %, on obtient **33,5 €**.
    - Avec 1,80 € et 1,4 %, on obtient 128,6 €.
  - **Contrôle par le panier moyen et le ROAS.** CPA = panier moyen ÷ ROAS.
    - Avec 71 € et un ROAS de 2,19, on obtient 32,4 €.
    - Avec 71 € et un ROAS de 1,78 (animaux), on obtient **39,9 €**.
  - Le CPA favorable de 14 € est cohérent avec le CAC Lebesgue de 17 à 18 $ (environ 15 €).
  - Des créations sous la moyenne (CTR de 0,72 à 1,0 %, bas de la fourchette WebFX) porteraient le CPA à 100 à 200 €.
- **Budget du client [calc].** Avec 15 € par jour et par ensemble de publicités, on obtient environ **1,1 achat par jour** dans le cas favorable, **0,38 en central** et 0,16 en défavorable. Cela fait environ **7,5, 2,6 et 1,1 achats par semaine**, très loin des quelque 50 événements par semaine nécessaires pour sortir de la phase d'apprentissage [CP, voir le tour 1].
  - En central, un ensemble de publicités produit environ 1 150 impressions, 19 clics et 0,4 achat par jour.
  - **Il faut regrouper le budget sur moins d'ensembles**, ou optimiser sur un événement plus fréquent pendant le test, par exemple l'ajout au panier (inférence).
- **Rentabilité dès la première commande.** Le CPA central d'environ 40 € **dépasse les marges de contribution avant publicité du tour 1** à 39,90 € (11,30 € en dropshipping, 15,68 € en stock).
  - Pour un produit vendu à l'unité entre 25 et 60 €, la **rentabilité dès la première commande sur trafic froid est improbable** au benchmark central.
  - Il faut donc soit un CPA réel proche du scénario favorable (14 à 15 €), soit un panier relevé par des lots, soit la récurrence d'achat.
  - Cela rejoint la préférence du client pour un produit à réachat.
- **Saisonnalité.** Le CPM augmente au 4e trimestre (retargeting au-delà de 30 $ chez Influee), et la série Superads montre un pic en juillet 2026. **Un lancement en novembre ou décembre 2026 (Black Friday, Noël) se fera au CPM haut** (inférence).
- **TikTok.** Son CPM français est plus bas (3 à 8 €) mais repose sur une source unique, et il n'existe ni CPA ni taux de conversion français. Il est à tester en parallèle, sans le substituer à Meta dans les scénarios.

### Gaps
- **Données propres aux animaux en France.** Aucun CPM, CTR, taux de conversion ou CPA Meta n'a été trouvé pour cette catégorie.
- **Méthodologie des séries.** L'échantillon et la devise de Superads ne sont pas précisés, et son pic de juillet 2026 n'est pas recoupé. Le type de CTR (lien ou tous clics) n'est pas précisé chez AdKit ni pour la médiane e-commerce.
- **Taux de conversion du trafic Meta.** Le taux de conversion des pages d'atterrissage depuis Meta, distinct du taux moyen du site, n'a pas été trouvé.
- **Médianes par catégorie.** Les médianes Varos ou Triple Whale pour l'animalerie ne sont accessibles que dans leurs outils.
- **TikTok en France.** Aucun CTR, taux de conversion, CPA ni ROAS n'a été trouvé.
- **Phase d'apprentissage.** Le seuil de Meta (environ 50 événements en 7 jours) n'a pas été revérifié [CP].

## Q6 : Retours, remboursements, rétrofacturations et panier moyen (animalerie, France)

### Takeaway
- **Animalerie.** Taux de retour de **12 %** (moyenne e-commerce : 17,5 %), panier moyen de **71 €** (moyenne : 119 €), réachat de **72 %** (moyenne : 28,5 %), selon Wisepim (07/05/2026). Le périmètre géographique n'est pas précisé.
- **France, tous secteurs.** Taux de retour moyen de **24 % en 2023-2024**, chiffre attribué à la Fevad mais non vérifié. Panier moyen e-commerce de **62 €** (Fevad 2025, déjà sourcé dans `fr_market_landscape.md`).
- **Rétrofacturations.** Taux moyen de **0,26 % des transactions** au 3e trimestre 2025, toutes industries (Sift). Le seuil du programme Mastercard ECM est fixé à **1,5 % et 100 litiges par mois**. Les seuils Visa VAMP sont contradictoires selon les sources.

### Cited Findings
- **Animalerie (Wisepim).** « Le panier moyen du secteur animalerie et soins est de 71 € (moyenne e-commerce 119 €) » ; « Taux de conversion de 2,6 % (moyenne e-commerce 2,3 %) » ; « Taux de retour de 12 % (moyenne e-commerce 17,5 %) » ; « Taux de réachat de 72 % (moyenne e-commerce 28,5 %) : le levier de la LTV ». Le même tableau donne une conversion mobile de 2,2 % et un abandon de panier de 63,5 %.
  - La page ne précise ni l'échantillon, ni le pays, ni la définition du réachat (période, base).
  - Sa moyenne e-commerce de 119 € diverge de celle de la Fevad pour la France (62 €). Le périmètre est donc vraisemblablement **non français ou non comparable**.
  - [S2, page du 07/05/2026] : [Wisepim, animalerie](https://wisepim.com/fr/ecommerce-industry-insights/pet-supplies).
- **France, tous secteurs.** « Le taux moyen de retour e-commerce en France s'élevait à 24 % en 2023-2024 ». Ce chiffre est attribué à un rapport Fevad relayé par un autre site ; le rapport original n'a pas été vérifié. [S2, blog Shopify, date non visible] : [Shopify FR, retours e-commerce](https://www.shopify.com/fr/blog/retour-e-commerce).
- **Comparaisons internationales.** États-Unis : 19,3 % des ventes en ligne en 2025 (NRF). Pays-Bas : 11,4 % en 2025. Allemagne : 24,2 % des colis en 2021 (**historique**). Il n'existe pas de moyenne unique. [S2] : [Wisepim, statistiques de retours](https://wisepim.com/fr/ecommerce-return-rate-statistics).
- **Sondage Statista (avril 2021 à mars 2022, historique).** 39 % des internautes français avaient renvoyé au moins un article en 12 mois. [S2] : [L'Écho du Mardi](https://www.echodumardi.com/economie/e-commerce-le-taux-de-retour-des-colis-par-pays/?print=pdf).
- **Contexte Fevad.** Les ventes en ligne atteignent 196,4 Md€ en 2025 (+7 %) et 50,1 Md€ au 1er trimestre 2026 (+4,7 %). [S2] : [Ecommerce Nation, bilan 2025](https://www.ecommerce-nation.fr/bilan-e-commerce-top-sites-fevad/) ; [Ecommerce Nation, 1er trimestre 2026](https://www.ecommerce-nation.fr/?p=126941). Le panier moyen de 62 € (-3 %) en 2025 est sourcé dans le tour 1 : [Le Journal des Entreprises](https://www.lejournaldesentreprises.com/article/e-commerce-nouveau-record-des-ventes-en-ligne-en-2025-2146033).
- **Magasins physiques.** Une source commerciale (éditeur de business plans) donne un panier moyen de 25 à 45 € par visite et un marché français de 7 Md€ en 2025, en estimation secondaire. Ce n'est pas un chiffre en ligne. [S2] : [modelesdebusinessplan.com](https://modelesdebusinessplan.com/blogs/infos/business-plan-animalerie).
- **Enseignes en ligne.** Je n'ai trouvé **aucun panier moyen publié** pour Zooplus, Wanimo ou Zoomalia (une requête).
- **Taux moyen de rétrofacturation.** Il est de 0,26 % des transactions au 3e trimestre 2025, toutes industries confondues, en hausse de 24 % sur un an (0,21 %), selon Sift. [S2] : [chargeback.io](https://www.chargeback.io/fr/blog/average-e-commerce-chargeback-rate) ; [SeamlessChex, 2026](https://seamlesschex.com/blog/chargeback-protection-for-merchants-2026-benchmarks).
- **Seuils Mastercard.** Le programme Excessive Chargeback Merchant (ECM) démarre à 100 rétrofacturations et 1,5 % ; le niveau supérieur (HECM) à 300 et 3,00 %. Il faut trois mois conformes consécutifs pour en sortir. Une source plus ancienne indiquait 1 % et 100 par mois. [S2, date non visible] : [chargeback.io, guide Mastercard](https://www.chargeback.io/fr/blog/mastercard-chargeback-guide) ; [Chargebacks911](https://chargebacks911.com/mastercard-chargeback-threshold/) ; [Sift](https://sift.com/blog/mastercard-chargebacks/).
- **Seuils Visa VAMP (sources contradictoires).**
  - Version 1 : 2,2 % pour un marchand américain, abaissé à 1,5 % le 01/04/2026.
  - Version 2 : 0,9 % et 100 litiges par mois en surveillance standard ; 1,8 % et 1 000 litiges par mois en « Excessive ».
  - [S2, rattachement non isolé] : [chargeback.io](https://www.chargeback.io/fr/blog/average-e-commerce-chargeback-rate) ; [Chargeback Gurus](https://www.chargebackgurus.com/blog/chargeback-thresholds-what-they-mean-for-your-business).
- **Frais par rétrofacturation.** Environ 15 € (blog Shopify FR) ou 20 à 30 $ (Chargeflow) : voir Q1.

### Inferences
- **Provision de retours.** La formule du tour 1 est conservée : taux × perte nette par retour. Paramètres :
  - **central 12 %**, soit le chiffre de l'animalerie (Wisepim) ;
  - **haut 24 %**, soit la France tous secteurs, mode compris (stress-test) ;
  - **bas 5 % [H]**, pour un accessoire non textile dont les frais de retour sont à la charge du client, s'il en est informé (art. L. 221-23 [CP]).
  - Le central du tour 1 (5 %) était donc probablement **optimiste**, d'un facteur proche de 2,4.
- **Rétrofacturations.** Le central passe de 0,5 % [H] à **0,26 %**. Les frais de 15 € par litige sont confirmés (source secondaire).
  - [calc] À 40 €, la provision vaut 0,26 % × (40 + 15) = **0,14 € par commande**.
  - En dropshipping, les délais longs sont un facteur connu de litiges « produit non reçu » [CP]. Le scénario haut (1 %) y est plus probable, mais reste sous le seuil Mastercard de 1,5 %.
- **Panier moyen.**
  - Les repères ne doivent pas servir à fixer le prix, que le produit détermine. Ils situent l'objectif d'un panier relevé par les lots : **62 € (France, tous secteurs) à 71 € (animalerie)**.
  - Un produit à 25-35 € a donc intérêt à des lots de 2 ou 3 pour atteindre ce niveau. C'est aussi le levier qui dilue le transport, l'encaissement et le droit de 3 € (une seule fois pour des unités identiques, voir le tour 1).
- **Réachat de 72 %.** Ce chiffre, s'il se confirme, confirme que la valeur client se joue sur la récurrence en animalerie. Sa définition n'est pas précisée : il ne faut donc pas l'utiliser comme taux de réachat d'une marque mono-produit sans test (inférence).

### Gaps
- **Retours.** Le taux propre à l'animalerie en France n'a pas été trouvé ; le chiffre Wisepim n'a pas de périmètre géographique. Le rapport Fevad sur les retours n'a pas été lu.
- **Rétrofacturations.** Le taux propre aux animaux n'a pas été trouvé. Les seuils officiels Visa VAMP 2026 n'ont pas été vérifiés.
- **Paniers.** Les paniers moyens de Zooplus, Wanimo, Zoomalia ou Animalis ne sont pas publiés dans les extraits. Le nombre d'articles par commande n'a pas été trouvé.

## Livrable : tableau des paramètres pour les scénarios par commande (produit de 25 à 60 € TTC)

### Takeaway
Ce tableau remplace les lignes [H] n° 7 à 27 du tableau du tour 1 par des valeurs sourcées ou calculées, à l'exception de cinq postes : applications Shopify, emballage, prix de la ligne de dropshipping, dédouanement et transitaire, et articles par commande.

En central, les relevés modifient les hypothèses du tour 1 dans les deux sens :
- **plus coûteux** : livraison à domicile (+1 à +3 €), 3PL en lecture « coût complet » (+2 €), taux de retour (×2,4) et CPA (environ 40 € contre 20 à 33 €) ;
- **moins coûteux ou équivalents** : point relais, encaissement, abonnement Shopify et rétrofacturations.

### Cited Findings
Montants en € HT sauf mention contraire. « Bas » désigne la valeur favorable. Les sources et dates détaillées figurent dans les sections Q1 à Q6. « Réf. tour 1 » renvoie au numéro de ligne du Livrable 1 de `fr_costs_regulation.md`.

| # | Paramètre (unité) | Bas (favorable) | Central | Haut (défavorable) | Statut | Source et date | Réf. tour 1 et écart |
|---|---|---|---|---|---|---|---|
| P1 | Abonnement Shopify (€ par mois) | 27 (Basic, annuel) | 36 (Basic, mensuel) | 105 (Grow, mensuel) | [S2] | Kanal, Sellfy, La Fabrique du Net (juillet à octobre 2026) | L7 : inchangé, [H] devient [S2] |
| P2 | Abonnement par commande (calcul P1 ÷ commandes par mois) | 0,14 (36 € ÷ 250) | 0,36 (36 € ÷ 100) | 0,72 (36 € ÷ 50) | [calc], volume [H] | — | L7 |
| P3 | Applications Shopify (€ par mois) | 0 | 40 | 100 | **[H]** | Non sourcé | L8 : inchangé |
| P4 | Shopify Payments, carte « standard » | 1,1 % + 0,25 € (Advanced) | 1,5 % + 0,25 € (Basic) | 1,5 % + 0,25 € (Basic) | [S2] | Kanal, relevé du 07/10/2026 | L9 |
| P5 | Shopify Payments, carte « internationale » | 2,4 % + 0,25 € (Advanced) | 2,7 % + 0,25 € (Basic) | 2,7 % + 0,25 € (Basic) | [S2] | Kanal, relevé du 07/10/2026 | L9 |
| P6 | PayPal France | 2,90 % + 0,35 € | 2,90 % + 0,35 € | 2,90 % + 0,35 €, plus 2 % de frais Shopify si applicables | [S] (fixe), [S] (taux) | Pages PayPal FR (version non datée ; grille ROW du 28/09/2026) | L9 : confirmé |
| P7 | **Encaissement, taux effectif au panier de 40 € TTC** | 2,1 % (0,85 €) | **2,4 % (0,97 €)** | 3,3 % (1,34 €) | [calc] sur [S]/[S2] ; mix [H] | Q1, Inferences | L9 : 1,05 € devient 0,97 € |
| P8 | Frais Shopify en cas de passerelle tierce | 0,6 % (Advanced) | 1 % (Grow) | 2 % (Basic) | [S2] | Kanal, Sellfy (2026) | L10 : inchangé |
| P9 | Paiement fractionné, commission marchand | 3,6 % HT (Alma 2x) | 3,8 % HT (Alma 3x) | 4,99 % + 0,35 € (Klarna via Shopify Payments) ; Alma jusqu'à 4,8 % HT | [S2] | Kanal 2026 ; Appvizer, BDM, La Fabrique du Net (dates variées) | L11 : environ 3 à 4,5 % devient 3,6 à 5 % |
| P10 | Frais par rétrofacturation | 15 € | 15 € | environ 26 € (30 $) | [S2] | Blog Shopify FR (date non visible) ; Chargeflow (2026) | L26 : 15 € confirmé |
| P11 | Colis France, point relais, jusqu'à 500 g | 3,46 (Mondial Relay 4,15 TTC) | 3,66 (Mondial Relay + 0,20 € d'agrégateur [S2 estim.]) | 5,74 (Colissimo retrait 6,89 TTC) | [calc] sur [S]/[S2] | Mondial Relay 15/06/2026 ; La Poste 01/01/2026 ; Margeo 07/2026 | L12 : 4,5 € [H] devient 3,5 à 3,7 € HT |
| P12 | Colis France, point relais, 1 kg | 3,75 (Relais Colis 4,50 TTC, source unique) ; Mondial Relay pro « dès 3,89 » | 4,99 (Mondial Relay 5,99 TTC) | 7,41 (Colissimo retrait 8,89 TTC) | [calc] sur [S]/[S2] | Idem ; tarif-lettre.com ; artisansdeuxpointzero (02/2026) | L12 |
| P13 | Colis France, domicile, 500 g | 6,24 (Mondial Relay domicile 7,49 TTC) | 6,33 (Colissimo 7,59 TTC) | 7,59 (TTC, TVA non récupérable) | [calc] sur [S]/[S2] | La Poste 01/01/2026 ; Mondial Relay 15/06/2026 | L13 : 6,5 € [H] ; TTC sous-estimé d'environ 1,1 € |
| P14 | Colis France, domicile, 1 kg | 7,91 (Mondial Relay 9,49 TTC) | 7,99 (Colissimo 9,59 TTC) | 9,59 (TTC) | [calc] sur [S]/[S2] | Idem | L13 : TTC sous-estimé d'environ 3,1 € |
| P15 | Colis France, 2 kg (relais / domicile) | 5,21 (Relais Colis) | 6,66 (Mondial Relay relais) | 9,33 (Colissimo domicile) | [calc] sur [S]/[S2] | Idem | L12-13 |
| P16 | Colis France, 5 kg (relais / domicile) | 7,67 (Relais Colis, à vérifier) | 13,33 (Mondial Relay relais) | 14,49 (Colissimo domicile) | [calc] sur [S]/[S2] | Idem | — |
| P17 | Express | 9,00 (Chrono Relais 13, 0-1 kg) | 10,60 (Chrono Relais 13, 1-3 kg) | 19,50 à 21,00 (Chrono 13 domicile, 0-1 kg / 1-3 kg) | [S] | La Poste, grille Chronopost du 01/01/2026 | L14 : 11 € [H] confirmé pour le relais |
| P18 | 3PL, préparation du premier article | 1,00 | 1,75 (milieu de fourchette) | 2,50 (indice UE : 2 à 4 €) | [S2], [calc] | Logily, Alolog, tarif-logistique.fr (2026) ; EightX (2026) | L15 : 2,50 € devient 1,75 € |
| P19 | 3PL, article supplémentaire | 0,30 | 0,50 (milieu) | 0,70 | [S2], [calc] | Idem | L15 : 0,2 à 0,6 € [H] confirmé |
| P20 | 3PL, coût complet par commande hors affranchissement (variante de P18 + P21 + P23) | 3,50 | 5,25 (milieu) | 7,00 (Île-de-France jusqu'à 8) | [S2], [calc] | Idem ; contenu exact non détaillé | L15-17 : 3,20 € devient 5,25 € selon cette lecture |
| P21 | Stockage (€ par palette et par mois) | 6 | 17,50 (milieu de 15-20, fourchette la plus fréquente) | 25 | [S2] | tarif-logistique.fr, logistique-ecommerce.com, Acolyt (2025-2026) | L16 |
| P22 | Réception (€ par palette) | 3,50 | 11,50 (milieu de 8-15) | 30 | [S2] | Logily, JCD Logistique, tarif-logistique.fr | L16 |
| P23 | Stockage et réception ramenés à l'unité | 0,02 (6 € × 1 mois + 3,50 €, ÷ 400 unités) | 0,23 (17,50 € × 2 mois + 11,50 €, ÷ 200 unités) | 1,30 (25 € × 4 mois + 30 €, ÷ 100 unités) | [calc], unités et rotation [H] | — | L16 : 0,30 € [H], du même ordre |
| P24 | Emballage et encart | 0,20 | 0,30 à 0,40 | 0,60 | **[H]** | Non sourcé | L17 : inchangé |
| P25 | Agent de sourcing (% du coût produit) | 3 % | 7,5 % (milieu de 5-10) | 15 % (petites commandes) | [S2] | Epic Sourcing, Supplyia, Maple Sourcing (2026) | L21 : 5/7/10 % devient 3/7,5/15 % |
| P26 | Inspection ou visite d'usine | Incluse (forfait de 5 %, minimum 100 $) | environ 100 $ par jour | n.d. | [S2] | Supplyia, JingSourcing (via guides 2026) | — |
| P27 | Fret international par unité (0,4 kg ; 0,002 m³ [H]) | 0,10 (groupage maritime, fret seul, sans frais fixes) | 0,77 (ferroviaire à 450 $/m³) | 3,10 (aérien DDP à 9 $/kg) | [calc] sur [S2] | Sino-Shipping (2e trim. et oct. 2026) ; Dantful, Weilong (2026) ; Freightos 4,88 $/kg (sem. du 08/09/2026) | L19 : 0,40/1,00/2,50 € devient 0,10/0,77/3,10 € |
| P28 | Dédouanement, transitaire et frais fixes de groupage, par unité | 0,10 | 0,30 | 0,60 | **[H]** | Non sourcé | L20 : inchangé |
| P29 | Ligne de dropshipping Chine-France, 0,3 à 1 kg (hors 3 € et 2 €) | 4,50 | 6,50 | 8,00 | **[H]** ; délai [S2] | Prix non trouvé ; délai CJPacket « Euro Ordinary » de 6 à 14 jours (TrackingMore, Ship24) | L18 : inchangé |
| P30 | Droit UE de 3 € et frais de 2 € (envoi direct) | 5 € par article distinct | 5 € | 5 € (voire par unité pour les 2 € ?) | [S] | Tour 1 (règlement 2026/382) ; Revenue Irlande (29/09/2026) : 2 € à partir du 01/11/2026 | L3-4 : 2 € confirmés au 01/11, JO non vérifié |
| P31 | CPM Meta France | 8 € | 13 € (milieu de 8-18) | 20 € (pic Superads de juillet 2026 : 21,74) | [S2], [calc] | La Fabrique du Net 2026 ; Adintime ; Superads (juillet 2025 à juillet 2026) | Nouveau (L24) |
| P32 | CTR Meta | 2,19 % (médiane e-commerce) | 1,63 % (animaux, trafic 2025) | 1,51 % (moyenne toutes industries) ; jusqu'à 0,72 % (WebFX) | [S2] | Adamigo (probable), MegaDigital/WordStream 2025, WebFX 2026 | Nouveau (L24) |
| P33 | CPC Meta | 0,40 € | 0,67 € (0,78 $, animaux) | 1,80 € | [S2] | La Fabrique du Net 2026 ; WordStream 2025 | Nouveau (L24) |
| P34 | Taux de conversion du site | 2,6 % (animalerie ; mobile 2,2 %) | 2,0 % (France) | 1,4 % (bas Shopify) | [S2] | Wisepim 07/05/2026 ; La Fabrique du Net 2026 ; Launchtip 2026 | Nouveau (L24) |
| P35 | **CPA Meta** | **14,0 €** | **39,9 €** | **94,6 €** | [calc] sur [S2] | P31 ÷ (1 000 × P32 × P34) ; recoupé par CPC ÷ conversion (33,5 €) et panier ÷ ROAS (32,4 à 39,9 €) | L24 : 20 à 33 € [H] devient environ 40 € |
| P36 | ROAS Meta médian (repère) | 2,19 (toutes industries, Varos 04/2025) | 1,78 à 1,80 (animalerie, non vérifié) | — | [S2] | Superscale (23/07/2026), GoMarble, Hawky, CorePPC | Nouveau |
| P37 | CPM TikTok France | 3 € | 5,50 € (milieu) | 8 € | [S2], source unique | Adintime (date non visible) ; CPA médian mondial 32,74 $ (Influee 2026) | Nouveau |
| P38 | Taux de retour ou de remboursement | 5 % | **12 %** (animalerie) | 24 % (France, tous secteurs, 2023-2024) | [H] / [S2] / [S2] | Wisepim 07/05/2026 ; blog Shopify citant la Fevad | L25 : 5 % devient 12 % |
| P39 | Taux de rétrofacturation | 0,1 % | **0,26 %** | 1,0 % (seuil Mastercard ECM : 1,5 %) | [H] / [S2] / [H] | Sift, 3e trim. 2025 (via chargeback.io) | L26 : 0,5 % devient 0,26 % |
| P40 | Panier moyen (repère) | 71 € (animalerie) | 62 € (France, tous secteurs) | — | [S2] | Wisepim 07/05/2026 ; Fevad 2025 (tour 1) | L27 : n.d. devient sourcé |
| P41 | Articles par commande | 1,3 | 1,15 | 1,0 | **[H]** | Non sourcé | — |
| P42 | Réachat, animalerie (repère) | 72 % (définition non précisée) | — | — | [S2] | Wisepim 07/05/2026 | Nouveau |

### Inferences
- **Changements qui comptent le plus par rapport au tour 1, en central.**
  1. **CPA** : environ 40 € au lieu de 20 à 33 €. À lui seul, il rend négative la contribution après publicité des deux modèles du tour 1 à 39,90 €.
  2. **Taux de retour** : 12 % au lieu de 5 %. La provision du modèle B passe de 0,43 € à environ 1 à 1,3 €, selon la base retenue [calc].
  3. **3PL** : si la fourchette « coût complet » de 3,50 à 7 € s'applique au cas du client, il faut ajouter environ 2 € par commande au modèle B. Si la lecture par composants (environ 2,30 €) est la bonne, le coût baisse d'environ 0,9 €. **Il faut trancher par deux devis.**
  4. **Livraison à domicile** : 1 à 3 € de plus que l'hypothèse du tour 1. Le **point relais par défaut** reste à environ 3,5 € HT jusqu'à 500 g.
  5. **Encaissement et rétrofacturations** : légèrement inférieurs à l'hypothèse du tour 1 (0,97 € et 0,14 € à 40 €).
- **Seuils structurants [calc].** Ces paliers sont fixes par colis ou par article, si bien que le panier relevé (lots) est le levier le plus puissant :
  - le point de poids de 500 g (environ +1,8 à +2,0 € au-delà) ;
  - le premier article d'une préparation 3PL (environ 1,75 €, puis 0,50 € par article supplémentaire) ;
  - le droit de 3 € par article distinct en dropshipping.
- **Sensibilité au volume.** L'abonnement Shopify et les applications pèsent environ 0,76 € par commande à 100 commandes par mois (36 € + 40 € [H]), et environ 1,52 € à 50 commandes [calc]. Ce poste fixe compte au lancement.
- **Microentreprise en franchise de TVA.** Il faut utiliser les colonnes TTC pour le transport. Les services facturés depuis l'étranger (Meta, Shopify) supportent alors une TVA non déductible de 20 % [CP, tour 1].

### Gaps
**Paramètres non sourcés après ce tour (à obtenir par devis ou par test)**
- **Coûts restés en hypothèse.** Prix des lignes de dropshipping (YunExpress, CJPacket) ; frais fixes de groupage et de dédouanement ; emballage ; applications Shopify ; articles par commande.
- **Grilles et données non trouvées.** Grilles pros Colissimo, Boxtal, Sendcloud et Relais Colis ; minimums des 3PL ; grilles marchandes Klarna en direct et Oney ; frais transfrontaliers PayPal ; taux de conversion des pages d'atterrissage Meta ; CTR, conversion et CPA TikTok en France ; taux de retour de l'animalerie en France ; seuils Visa VAMP officiels ; paniers moyens Zooplus, Wanimo et Zoomalia ; relevés d'octobre 2026 des indices Drewry, FBX et Freightos aérien.
- **Taux de change.** Le taux EUR/USD (1 $ = 0,86 € [H]) n'est pas sourcé ; il est à remplacer par le taux BCE du jour.
- **Requêtes envisagées mais non lancées (budget épuisé).**
  - « Oney commission marchand 3x 4x 2026 » ;
  - « Klarna tarif marchand France contrat direct » ;
  - « Colissimo Facilité grille HT 2026 domicile sans signature » ;
  - « Sendcloud tarifs Colissimo Mondial Relay 2026 grille » ;
  - « YunExpress France rate card 2026 » ;
  - « LCL Chine France porte à porte prix m3 frais fixes 2026 » ;
  - « QIMA inspection price man-day 2026 » ;
  - « Visa VAMP thresholds official 2026 » ;
  - « Drewry WCI 23 October 2026 » ;
  - « Varos pet Meta CVR » ;
  - « TikTok ads France CTR conversion 2026 » ;
  - « coût emballage e-commerce carton par colis ».

#### Journal des 40 requêtes WebSearch (dans l'ordre, verbatim, avec le résultat utile)
1. « Shopify tarifs France 2026 Basic Grow Advanced prix par mois euros » (standard). Blogs tiers : Basic 36 €, Grow 105 €, Advanced 384 € (27, 79 et 289 € en annuel).
2. « Shopify Payments France frais cartes européennes internationales taux 2026 » (standard). Kanal (07/10/2026) : 1,5 % + 0,25 € pour la carte standard et 2,7 % + 0,25 € pour la carte internationale (Basic).
3. « PayPal France commission vendeur 2026 transaction nationale 2,90 % 0,35 € » (standard). Page PayPal FR : 2,90 % plus un fixe non visible ; QR code 1,10 % ; grille ROW du 28/09/2026.
4. « Alma frais marchand paiement 3x 4x commission pourcentage Shopify » (standard). 3,6 à 4,2 % HT, 3,8 % standard, 0,75 % au comptant.
5. « Klarna France frais marchand paiement en 3 fois commission tarif e-commerçant » (standard). Aucune grille marchande.
6. « tarif Colissimo 2026 250 g 500 g 1 kg 2 kg 5 kg France domicile sans signature prix » (standard). Grille La Poste du 01/01/2026.
7. « Colissimo entreprise tarifs 2026 grille professionnels contrat Facilité Privilège prix colis » (standard). Pas de grille pro ; hausse de 3,4 % ; cadre Arcep.
8. « Mondial Relay tarif juin 2026 500 g 1 kg point relais domicile prix grille » (standard). Grille ShippyPro du 15/06/2026.
9. « Chronopost tarifs 2026 Chrono 13 Chrono Relais 1 kg 2 kg 5 kg prix » (standard). Grille La Poste HT et TTC.
10. « Boxtal Sendcloud tarifs 2026 Mondial Relay Colissimo Relais Colis prix colis 500 g 1 kg e-commerçant » (standard). Estimations Margeo ; promotion Sendcloud 2024 ; ni Boxtal ni Relais Colis.
11. « Relais Colis tarif 2026 prix envoi colis 500 g 1 kg 2 kg Shop2Shop Chronopost prix » (standard). Rien sur Relais Colis ni Shop2Shop ; Colissimo Europe ; carnet d'étiquettes.
12. « Boxtal tarif professionnel 2026 Mondial Relay Colissimo prix négocié abonnement e-commerce » (standard). PDF Boxtal « à partir de 3,60 € HT » ; Mondial Relay pro 3,89 €.
13. « Cubyn tarifs logistique e-commerce prix préparation commande stockage » (standard). Aucune grille publique.
14. « Bigblue tarifs logistique e-commerce prix par commande stockage Shopify » (standard). Structure tarifaire, sans montants.
15. « prix logisticien e-commerce France 2026 pick and pack par commande article supplémentaire stockage palette mois réception » (standard). Indice EightX : 2 à 4 € ; 0,95 € par pick.
16. « EU €2 customs handling fee e-commerce parcels 1 November 2026 confirmed apply delegated act » (standard). Revenue Irlande (29/09/2026) ; publication au JO non confirmée.
17. « China sourcing agent fees commission percentage of order 2026 inspection fee » (standard). Commissions de 3 à 10 % ; forfaits ; exemples d'agences.
18. « Freightos Air Index China to Europe air freight rate per kg October 2026 » (standard). 4,88 $/kg (semaine du 08/09/2026) ; 3,52 $/kg (31/12/2025).
19. « Drewry World Container Index Shanghai Rotterdam 40ft October 2026 » (standard). 3 944 $ (08/07/2026) ; pas de relevé d'octobre.
20. « YunExpress CJ Packet France shipping cost 2026 0.5 kg delivery time days » (standard). Rien d'exploitable (pages Easyship).
21. « Meta Facebook Instagram ads benchmarks France 2026 CPM CPC CTR by country e-commerce » (**extended**). Séries Superads France, WebFX, AdKit, Triple Whale.
22. « Facebook ads benchmarks pets animals industry CTR CPC conversion rate cost per lead 2025 WordStream LocaliQ » (standard). Animaux : CPC 0,78 $ et CTR 1,63 %.
23. « TikTok Ads France CPM CPC coût moyen 2026 e-commerce benchmark » (standard). Adintime (France) : CPM de 3 à 8 € ; repères mondiaux.
24. « taux de conversion e-commerce France 2025 2026 moyen boutique Shopify benchmark secteur animalerie » (standard). France environ 2 % ; Shopify 1,4 à 1,8 %.
25. « Meta ads ROAS benchmark 2026 ecommerce median CPA pet supplies Varos Triple Whale » (standard). ROAS animalerie de 1,78 ; Varos 2,19 ; CAC Lebesgue.
26. « taux de retour e-commerce France 2025 2026 étude produits retournés pourcentage commandes Fevad » (standard). 24 % (relayé) ; NRF 19,3 %.
27. « average chargeback rate ecommerce 2025 2026 benchmark Visa VAMP threshold Mastercard excessive chargeback 1.5% » (standard). Sift : 0,26 % ; Mastercard ECM : 1,5 % ; VAMP contradictoire.
28. « panier moyen animalerie en ligne France Zooplus Wanimo Zoomalia panier moyen euros 2025 » (standard). Wisepim : 71 € ; rien pour les enseignes.
29. « CJPacket ordinary YunExpress Europe ligne France tarif délai livraison dropshipping 2026 colis 500 g prix » (standard). Rien.
30. « fret ferroviaire Chine Europe prix 2026 conteneur groupage LCL prix par m3 Chine France maritime » (standard). Groupage 30 à 60 $/m³ ; ferroviaire 250 à 450 $/m³ ; volumes ferroviaires.
31. « tarifs logistique e-commerce petite marque France stockage palette par mois réception marchandise prix préparation commande grille publique 2026 » (**extended**). Fourchettes 3PL françaises.
32. « Freightos FBX Asia North Europe container rate October 2026 air freight China Europe per kg » (standard). Rien pour 2026 (articles de 2025).
33. « CJdropshipping shipping to France CJPacket delivery days price per order 2026 YunExpress Global Direct Line France » (standard). Délais de 6 à 14 jours ; pas de prix.
34. « Shopify Payments France frais de rétrofacturation litige 15 € PayPal France commission fixe 0,35 EUR transactions nationales » (standard). Environ 15 € (blog Shopify) ; 20 à 30 $ (Chargeflow).
35. « comparatif paiement fractionné marchands 2026 Alma Klarna Oney Scalapay frais commerçant 3x 4x pourcentage » (standard). Klarna via Shopify Payments : 4,99 % + 0,35 € ; Alma 3,60 à 4,80 % HT ; échéance du 20/11/2026.
36. « CPM moyen Facebook Ads France 2026 euros coût par clic Meta Ads France agence » (standard). La Fabrique du Net : CPM de 8 à 18 €, CPC de 0,40 à 1,80 €.
37. « wisepim animalerie e-commerce benchmark taux de retour taux de conversion panier moyen 71 € » (standard). Wisepim animalerie : retours 12 %, conversion 2,6 %, réachat 72 %.
38. « "PayPal" France tarification marchands 2026 commission fixe "0,35" EUR paiements nationaux 2,90 % » (standard). Fixe de 0,35 EUR confirmé.
39. « Relais Colis tarifs 2026 envoi particulier e-commerçant prix 1 kg 2 kg 5 kg point relais » (standard). tarif-lettre.com : 4,20 / 4,50 / 6,25 / 9,20 €.
40. « China to France ecommerce small parcel line price 2026 YunExpress 4PX Yanwen per kg plus registration fee 0.5 kg DDP IOSS » (**extended**). Aucune grille de transporteur ; express à 7,75 $/kg (octobre 2026) ; calculateur Fishgoo.
