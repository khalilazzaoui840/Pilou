# Bow Wow Buddy (support qui empêche le chien d'avaler le dernier morceau de nerf de bœuf) : vérification US, test approfondi France, sourcing, réglementation, potentiel publicitaire et économie du panier (état au 2026-10-28)

_Notes du 2026-10-28. Lectures préalables : `us_decouverte_marques_meconnues.md` (en entier), `fr_costs_regulation.md` (TVA, douane, GPSR), `fr_couts_commerciaux.md` (paramètres P1 à P42, dont le CPA Meta central de 39,9 €), et, pour la réglementation des aliments pour animaux, `sourcing_jouet_lechage.md` et `fr_deep_glandes_anales.md`._

_Méthode et limites (valables pour tout le document) :_
- _**45 appels WebSearch sur 45** : 44 en mode « standard », 1 en mode « extended » (n° 25). Le budget est épuisé. WebFetch et curl sont interdits. **Toutes les données viennent des titres, extraits et synthèses du moteur de recherche** : ce sont des preuves indirectes. Il faut ouvrir chaque URL avant publication. La synthèse du moteur attribue parfois mal un chiffre à une page : je le signale quand l'attribution est incertaine._
- _Le moteur est « US-only ». Le filtre `allowed_domains` remplace l'opérateur `site:`. Un résultat vide ne prouve jamais une absence : j'écris « non trouvé dans ce criblage ». Une source inaccessible est notée « non vérifié (accès impossible) »._
- _Meta Ad Library, TikTok Creative Center, Google Trends, Espacenet, EDGAR (recherche plein texte) et les pages Amazon elles-mêmes n'ont pas pu être consultés._
- _Types de chiffres : CA DÉCLARÉ, RÉSULTAT DÉCLARÉ, CA ESTIMÉ (outil nommé), FINANCEMENT, PROJECTION, TRAFIC, VUES/ENGAGEMENT, UNITÉS, AVIS, CLASSEMENT, PRIX. Je ne convertis jamais un type en un autre. « HISTORIQUE » signale une donnée antérieure à 2024. « CA non confirmé » signale l'absence de chiffre fiable._
- _Marqueurs : [S] source officielle ; [S2] source secondaire ; [H] hypothèse non sourcée ; [CP] connaissance préalable non revérifiée en ligne ; [calc] calcul de l'auteur. Taux de change : 1 $ = 0,86 € [H], repris de `fr_couts_commerciaux.md`._
- _Les requêtes France du tour précédent (FR-A1 à FR-A6, consignées dans `us_decouverte_marques_meconnues.md`) sont reprises dans le tableau 2.5 pour étayer tout constat d'absence._

## 1. Le succès US de Bow Wow Labs est-il documenté par des dépôts fiables, et croît-il encore en 2024–2026 ?

### Takeaway
**Oui pour 2022–2023, non démontré pour 2024–2026.** Les seuls chiffres financiers sont ceux déclarés dans l'offre de financement participatif réglementée (Reg CF) publiée sur Wefunder en 2023 :
- **CA DÉCLARÉ** de 5,12 M$ (2022) puis 6,01 M$ (2023), soit +17 % ;
- marge brute passée de 48,4 % à 50,6 % ;
- **perte nette** passée de −0,34 M$ à **−1,22 M$**, soit −20 % du CA en 2023.

Ces chiffres sont HISTORIQUES et, selon la synthèse du moteur, non audités. Aucun dépôt ultérieur (rapport annuel Form C-AR) n'a été trouvé : **CA 2024–2026 non confirmé**.

Les signaux 2024–2026 montrent une entreprise **active qui investit** :
- Inc. 5000 2024, pour la 2e année ;
- produit refondu en 2024 ;
- nouveau brevet US en 2025 ;
- lancement dans environ 700 magasins Pet Supplies Plus en août 2025 ;
- effectif passé de 12 à 15 personnes (décembre 2024) ;
- test Dogster mis à jour en juillet 2026.

Ces signaux ne prouvent pas une croissance. Aucune actualité 2026 et aucune présence aux Inc. 5000 2025 ou 2026 n'ont été trouvées. La croissance 2023 a ralenti (+17 %) : la projection de plus de 7,5 M$ annualisés, annoncée en janvier 2023, n'a pas été atteinte, et l'année a été déficitaire.

### Cited Findings

#### 1.1 Dépôts financiers (Wefunder, SEC, Regulation Crowdfunding)
- **Exercice 2023** (page de détails Wefunder) :
  - **CA DÉCLARÉ de 6 013 347 $** (+17 %) ;
  - **RÉSULTAT NET DÉCLARÉ de −1 223 084 $** (marge nette −20 %) ;
  - marge brute de 51 % (50,57 % relevé au tour précédent) ;
  - coût des ventes moyen sur les trois derniers mois : 281 357 $ par mois ;
  - trésorerie de 450 000 $ en janvier 2024.
  - HISTORIQUE. Source : [Wefunder, détails](https://wefunder.com/bowwowlabs/details)
- **Exercice 2022** (HISTORIQUE) :
  - CA DÉCLARÉ de 5 115 333 $ ;
  - coût des ventes de 2 641 833 $ ;
  - RÉSULTAT NET DÉCLARÉ de −340 260 $ ([KingsCrowd](https://kingscrowd.com/bow-wow-labs-on-wefunder-2023/)) ;
  - Wefunder indique « Operating Income positive for FY '22 » ([Wefunder, détails](https://wefunder.com/bowwowlabs/details)).
  - [calc] Marge brute 2022 = (5 115 333 − 2 641 833) / 5 115 333 = **48,35 %**, cohérente avec le tour précédent. Croissance 2023 = +17,6 %. CA mensuel moyen 2023 ≈ 501 000 $.
- **Campagne Wefunder** (FINANCEMENT, HISTORIQUE) :
  - selon KingsCrowd : ouverture le 12/01/2023, clôture le 18/05/2023 ; objectif minimum de 100 001 $ et maximum de 1 235 000 $ ; prix de 0,38 $ par action ; « Invested this round: $548,961 » ([KingsCrowd](https://kingscrowd.com/bow-wow-labs-on-wefunder-2023/)) ;
  - P2P Market Data : 536 811 $ levés auprès de 190 investisseurs, « fundraise ended on April 29, 2024 ». **Cette date contredit la clôture de mai 2023** ([P2P Market Data](https://p2pmarketdata.com/investments/bow-wow-labs-on-wefunder-2023)) ;
  - CB Insights : 540 k$ en deux tours, dernier tour « Angel » de 0,54 M$ le 18/05/2023 ([CB Insights](https://www.cbinsights.com/company/bow-wow-labs/financials)) ;
  - valorisation de 23,3 M$ (tour précédent, [KingsCrowd](https://kingscrowd.com/bow-wow-labs-on-wefunder-2023/)) ;
  - usage des fonds : « marketing, new product development, increasing inventory, and mold production » ; « launch two exciting, innovative new products » (synthèse de [KingsCrowd](https://kingscrowd.com/bow-wow-labs-on-wefunder-2023/) et [Pet Insight, 2023](https://pet-insight.com/?p=26603)).
- **UNITÉS DÉCLARÉES** (campagne 2023, HISTORIQUE, tour précédent) : « Sold over 200,000 Bow Wow Buddy™ safety devices, 1.6 million bully sticks » ([Wefunder](https://wefunder.com/bowwowlabs)).
- **EDGAR** :
  - un **Form C/A** (amendement d'offre) a été déposé le 26/04/2023 (n° d'enregistrement 0001670254-23-000415, CIK 1954010, adresse à Novato, Californie). Le nom de l'émetteur n'apparaît pas dans l'extrait : **rattachement à Bow Wow Labs non confirmé** ([SEC](https://www.sec.gov/Archives/edgar/data/1954010/000167025423000415/0001670254-23-000415-index.htm)) ;
  - **aucun Form C-AR (rapport annuel) de Bow Wow Labs trouvé** (requête n° 1). Les autres résultats concernaient d'autres sociétés.
- **Qualité des états financiers** :
  - le tour précédent les décrit comme « non audités de manière indépendante », selon la synthèse du moteur ;
  - [CP] En Reg CF, au-delà de 124 000 $ levés, les états doivent être au minimum revus par un expert-comptable indépendant. Pour un premier émetteur levant jusqu'à 1,235 M$, une revue suffit, sans audit. Niveau exact (revue ou audit) non vérifié.

#### 1.2 Chiffres de presse et estimations tierces
- **CA DÉCLARÉ via presse** (Pet Insight, 2023, HISTORIQUE) :
  - « record monthly revenue exceeding $600,000 » en novembre et en décembre (2022) ;
  - PROJECTION de plus de 7,5 M$ annualisés.
  - Synthèse du moteur, attribution probable à [Pet Insight (mars 2023)](https://pet-insight.com/?p=26847).
  - [calc] Le CA 2023 réel (6,01 M$) est **20 % sous cette projection**.
- **CA DÉCLARÉ via presse** (HISTORIQUE) : titre « Bow Wow Labs Reaches $500,000 in Monthly Revenue Selling Dog Products ». Selon la synthèse, ce niveau aurait été atteint « by January 2021 » : date à vérifier. Le même article évoque un projet Kickstarter de 2018 qui aurait levé « over $50,000 » auprès de « more than 1,000 backers » (FINANCEMENT participatif, HISTORIQUE). Source : [Startup Savant](https://startupsavant.com/news/bow-wow-labs)
- **Estimations tierces** (non fiables, contradictoires, non datées) :
  - CA ESTIMÉ (LeadIQ) de **10 à 25 M$** ; « founded in 2016 » ; effectif de 2 à 10 ([LeadIQ](https://leadiq.com/c/bow-wow-labs-inc/5b3e72e7360000ac00a2a392)) ;
  - CA ESTIMÉ (Prospeo) de **1 112 215 $**, calculé par une formule de CA par employé ([Prospeo](https://prospeo.io/c/bow-wow-labs)) ;
  - CA ESTIMÉ (BrandSearch) d'environ 394 k$ par mois et TRAFIC ESTIMÉ (BrandSearch) d'environ 44 000 visites par mois sur bowwowlabs.com ([BrandSearch](https://brandsearch.co/brands/bowwowlabs.com)).
- **Effectif** : 12 puis 15 salariés à décembre 2024 (+25 % sur le trimestre) selon Caplight ([Caplight](https://www.caplight.com/company/bowwowlabs)).

#### 1.3 Classements Inc.
- **Inc. 5000 2023** : n° 684 (CLASSEMENT, HISTORIQUE).
- **Inc. 5000 2024** : « recognized and awarded for the second year in a row to the 2024 Inc. 5,000, ranked 181 in Consumer Products and one of only 10 pet nutrition companies » (communiqué de l'entreprise).
- Un autre média donnait le rang 684 pour 2024 (contradiction relevée au tour précédent).
- **Vet100** : n° 63 (tour précédent).
- Sources : [Bow Wow Labs](https://www.bowwowlabs.com/blogs/in-the-news/bow-wow-labs-named-to-inc-5000-list-of-americas-fastest-growing-private-companies) ; [Pet Insight](https://pet-insight.com/?p=27710) ; [Pets+](https://petsplusmag.com/?p=48711)
- **Inc. 5000 2025 et 2026** : **non trouvé** (requête n° 26). Une seule requête ne prouve pas l'absence.
- [CP] L'Inc. 5000 2024 mesure la croissance du CA de 2020 à 2023. Il ne prouve donc pas une croissance en 2024.

#### 1.4 Statut 2024–2026 : produit, distribution, communication
- **2024, refonte du produit** :
  - « reengineered in 2024 with an improved Twist Screw » ;
  - vis « with two teeth and four points of contact » ;
  - nouvelles fiches Amazon US : « Buddy® SafeFit™ Bully Stick Holder for Dogs, Small (16-30 Lbs) » ([B0DFX3PCZ4](https://www.amazon.com/clp/B0DFX3PCZ4)) et « Redesigned … Dishwasher » ([B0DFX69Q8C](https://www.amazon.com/Bow-Wow-Labs-Redesigned-Dishwasher/dp/B0DFX69Q8C)) ;
  - fiche miroir « newly redesigned » ([desertcart](https://www.desertcart.com.ar/products/667447284-bow-wow-labs-buddy-safety-device-newly-redesigned-bully-stick)).
- **2024, étude commanditée par l'entreprise** : « more than 5.5 million dogs swallow an unchewed portion of a chew stick each year ». C'est une donnée d'entreprise, non indépendante ([finanzen.net, communiqué](https://www.finanzen.net/nachricht/aktien/bow-wow-labs-partners-with-pet-supplies-plus-to-bring-vet-recommended-safety-chew-device-to-pet-parents-nationwide-14675973)).
- **2025, sondage vétérinaire commandité** : « 4 out of 5 veterinarians surveyed recommend the Bow Wow Buddy ». Source sponsorisée ([Pets+](https://petsplusmag.com/4-out-of-5-veterinarians-surveyed-recommend-the-bow-wow-buddy-for-safer-chewing/)).
- **Partenariat Pet Supplies Plus, annoncé le 31/07/2025** :
  - environ **700 magasins** (en propre et franchisés) à partir d'août 2025 ;
  - **6 références** : Bow Wow Buddy en 3 tailles et bâtonnets SafeFit ;
  - décrit par la synthèse comme le « first major move into brick-and-mortar stores ».
  - Sources : [finanzen.net](https://www.finanzen.net/nachricht/aktien/bow-wow-labs-partners-with-pet-supplies-plus-to-bring-vet-recommended-safety-chew-device-to-pet-parents-nationwide-14675973) ; [Pet Insight, 31/07/2025](https://pet-insight.com/?p=31061) ; [Pets+](https://petsplusmag.com/bow-wow-labs-partners-with-pet-supplies-plus/) ; [Pet Age](https://www.petage.com/?p=496332)
- **2026** : **aucune actualité trouvée** (requête n° 39). Seul signal : un test Dogster « updated July 2026 », note éditoriale de 4,75/5 ([Dogster](https://www.dogster.com/lifestyle/bow-wow-labs-bow-wow-buddy-review/)).
- **Distribution US relevée** (fiches actives à des dates inconnues) :
  - **Amazon US**, boutique de marque ([Amazon](https://www.amazon.com/stores/BowWowLabs/BowWowBuddy/page/830B2CC2-490B-40D1-9328-02983129AECD)) ;
  - **Chewy** : support S et L, kits XS et S ([S](https://www.chewy.com/bow-wow-labs-buddy-safety-device/dp/1441758), [L](https://www.chewy.com/bow-wow-labs-buddy-safety-device/dp/1441774), [kit XS](https://www.chewy.com/bow-wow-labs-buddy-starter-kit-anti/dp/1392422), [kit S](https://www.chewy.com/bow-wow-labs-buddy-starter-kit-anti/dp/1392414)) ;
  - **Walmart** : M, XL et kit XXL ([M](https://www.walmart.com/ip/376205768), [XL](https://www.walmart.com/ip/Bow-Wow-Labs-Bow-Wow-Buddy-XL-Bully-Stick-Holder/633612694), [kit XXL](https://www.walmart.com/ip/533075359)) ;
  - **Target** ([A-89789163](https://www.target.com/p/bow-wow-buddy-safety-device-holder-for-dog-bully-sticks-and-chews/-/A-89789163)) ;
  - **Pet Supplies Plus** ;
  - **Reach.dog** ([kit](https://reach.dog/shop/bow-wow-labs/products/bow-wow-buddy-starter-kit)) ;
  - **shop.app** ([bundle](https://shop.app/products/14670275248494/smart-bully-stick-bundle)) ;
  - indépendants : Happy Hound, Dr. Judy Morgan (tour précédent) ;
  - vente en gros de bully sticks aux détaillants ([Pets+](https://petsplusmag.com/bow-wow-labs-inc-announces-bully-sticks-in-bulk-offer-to-u-s-pet-retailers/)).
  - Hors US : Amazon.fr (section 2.3), revente sur eBay.de ([eBay.de](https://www.ebay.de/itm/205664518114)), miroirs desertcart.
- **Comptes sociaux** : « bowwowlabs » sur Instagram, Facebook, TikTok, YouTube, Twitter et LinkedIn, d'après un communiqué ([Pets+](https://petsplusmag.com/bow-wow-labs-inc-announces-bully-sticks-in-bulk-offer-to-u-s-pet-retailers/)). Nombres d'abonnés : **non trouvés**.
- **Histoire fondatrice** : « the founder's dog, Finn, choked on a piece of a bully stick and was taken to the emergency vet, inspiring the invention of the Bow Wow Buddy » ([À propos, Bow Wow Labs](https://bowwowlabs.com/pages/about)).

#### 1.5 Gamme, tailles pour grands chiens et prix
- **Tailles** :
  - de XS (moins de 15 lb, soit moins de 6,8 kg) à L (51–75 lb, soit 23–34 kg) ;
  - une fiche Amazon US vise les chiens de « 76+ lbs » (34,5 kg et plus) ;
  - XL ([Walmart](https://www.walmart.com/ip/Bow-Wow-Labs-Bow-Wow-Buddy-XL-Bully-Stick-Holder/633612694)) et kit XXL ([Walmart](https://www.walmart.com/ip/533075359)) ;
  - kit L « 6" Thick, Large (51-75 Lbs) » ([Amazon B0CK3PD5S2](https://www.amazon.com/clp/B0CK3PD5S2)).
  - **Nombre de tailles contradictoire** : « five sizes » selon la synthèse du communiqué Pet Supplies Plus ; « 3 sizes for dogs from under 15 lbs to 100+ lbs » selon la page À propos ([Bow Wow Labs](https://bowwowlabs.com/pages/about)). Les pages datent probablement d'époques différentes.
  - Conversions [calc] : 1 lb = 0,4536 kg.
- **Caractéristiques** :
  - « made in the USA », nylon « BPA-free », lavable au lave-vaisselle ;
  - « a safety device, not a toy … should be removed promptly after the dog finishes the chew » ;
  - fonctionne mieux avec les bâtonnets SafeFit de la marque : « other bully stick brands may be too wide or narrow » ;
  - bâtonnets droits uniquement.
  - Sources : [Amazon B0DFX69Q8C](https://www.amazon.com/Bow-Wow-Labs-Redesigned-Dishwasher/dp/B0DFX69Q8C) ; [Amazon B0CK3K3C31](https://www.amazon.com/Bow-Wow-Labs-Buddy-Starter/dp/B0CK3K3C31)
- **Gamme** :
  - supports ;
  - bâtonnets SafeFit : 6 pouces, et « 12" SafeFit 100% Beef Bully Sticks - 10 Pack (Jumbo) » ([Amazon B08FNTPL7P](https://www.amazon.com/Bow-Wow-Labs-Bully-Sticks/dp/B08FNTPL7P)) ;
  - kits de démarrage (5 bâtonnets SafeFit et un bocal) et kit des fêtes ;
  - abonnement ;
  - vente en gros aux détaillants ;
  - friandises au collagène et hygiène bucco-dentaire, d'après `us_pet_dtc_revenue_evidence.md`.
- **PRIX US** (relevés le 2026-10-28 via les extraits ; dates de capture inconnues) :
  - **support** : 29,95 $ (Bow Wow Labs), 27,95 $ (Reach), 34,95 $ (Happy Hound), 33,99 $ (Target) au tour précédent. Whole Dog Journal : « nearly $28 for the extra small size, and nearly $38 for the extra large » ([WDJ](https://www.whole-dog-journal.com/?p=582533)) ;
  - **bâtonnets SafeFit** : 28,95 $ (auparavant 27,95 $), contenance du lot non relevée ([Reach](https://reach.dog/shop/bow-wow-labs/products/bully-sticks)) ;
  - **kit des fêtes** : 44,95 $, avec un historique de prix alternant entre 29,95 $ et 44,95 $ ; « five SafeFit™ Bully Sticks and a stay-fresh jar » ([Reach](https://reach.dog/shop/bow-wow-labs/products/bow-wow-buddy-starter-kit)) ;
  - **Chewy** : kit XS à 47,88 $ (45,49 $ en livraison programmée, 31,12 $ pour la première) ; kit S à 53,95 $ (35,07 $ pour la première livraison programmée) ([kit XS](https://www.chewy.com/bow-wow-labs-buddy-starter-kit-anti/dp/1392422) ; [kit S](https://www.chewy.com/bow-wow-labs-buddy-starter-kit-anti/dp/1392414)) ;
  - **abonnement « Subscribe + Save »** : « 30% off the first shipment, 10% off every shipment after », port forfaitaire de 3 $. Une autre version de la page promet 10 % et le port offert ([Bow Wow Labs](https://bowwowlabs.com/products/bully-sticks)).

#### 1.6 Avis (AVIS) et « bought in past month »
- **Amazon US, support** : note et nombre d'avis **non visibles dans les extraits**, donc **non vérifié (accès impossible)**. Le badge « bought in past month » est lui aussi **non vérifié (accès impossible)**.
- **Meilleur indicateur disponible** :
  - l'ancienne version XS a le même ASIN B082YJHTYN sur amazon.com ([Amazon US](https://www.amazon.com/Bow-Wow-Labs-Safety-Device/dp/B082YJHTYN)) et sur amazon.fr ;
  - Amazon.fr y affiche 4,3/5 sur **7 021** (AVIS, global ratings probables, relevé du tour précédent) ([Amazon.fr](https://www.amazon.fr/Bow-Wow-Labs-Dispositif-s%C3%A9curit%C3%A9/dp/B082YJHTYN)).
  - [inférence] Ces avis viennent sans doute surtout d'acheteurs US.
- **Bâtonnets SafeFit 12" Jumbo, lot de 10** : 4,2/5 sur **1 311** (AVIS, Amazon US) ([B08FNTPL7P](https://www.amazon.com/Bow-Wow-Labs-Bully-Sticks/dp/B08FNTPL7P)).
- **Autres sites** :
  - Chewy (support) : 4,1/5 sur 198 ([Chewy](https://www.chewy.com/bow-wow-labs-buddy-safety-device/dp/1441774)) ;
  - Walmart (M) : 4,5/5 sur 13 ([Walmart](https://www.walmart.com/ip/376205768)) ;
  - shop.app (bundle) : 4,8/5 sur 29 ([shop.app](https://shop.app/products/14670275248494/smart-bully-stick-bundle)) ;
  - desertcart, taille L (51–75 lb) : **3,7/5 sur 217**, miroir non daté ([desertcart](https://www.desertcart.co.th/products/592196318)).
- **Tests éditoriaux** : Dogster, 4,75/5, mis à jour en juillet 2026 ([Dogster](https://www.dogster.com/lifestyle/bow-wow-labs-bow-wow-buddy-review/)) ; Hepper, test 2024 avec avantages et inconvénients ([Hepper](https://www.hepper.com/bow-wow-labs-bow-wow-buddy-review/)) ; Whole Dog Journal ([WDJ](https://www.whole-dog-journal.com/?p=582533)).

#### 1.7 Brevets, marques et actions contre les copies
- **US 10,015,951 B2**, « Pet treat holder and safety device » :
  - dépôt le 01/05/2015, délivrance le 10/07/2018 ; publication US 2015/0313184 ;
  - inventeurs J. Scott Woolwine et Julie Hackett ; cessionnaire Bow Wow Labs, Inc. ;
  - objet : des bras mobiles entre deux positions forment une cavité pour l'extrémité d'une friandise allongée, et une bague filetée (« twist ring ») les serre.
  - Sources : [Justia](https://patents.justia.com/patent/10015951) ; [Justia, cessionnaire](https://patents.justia.com/assignee/bow-wow-labs-inc)
- **US 10,856,528 B2**, même titre et mêmes inventeurs : dépôt le 09/07/2018 (demande 16/030,806), délivrance le 08/12/2020. Objet : une tête, des bras opposables articulés et une bague de serrage ([9235.net](https://www.9235.net/patent/US10856528B2.html) ; [Justia](https://patents.justia.com/patent/10856528)).
- **US 12,317,863 B1** (2025), « Pet treat holder and safety device », même famille selon la synthèse Google Patents et Justia. Objet : un corps à parois internes autour d'un vide, des éléments antidérapants et un élément de retenue mobile. Il couvre probablement la version refondue (inférence). Source : [Justia, cessionnaire](https://patents.justia.com/assignee/bow-wow-labs-inc)
  - Un PDF USPTO n° 12317862 porte le même titre, mais son cessionnaire n'est pas visible : confusion de numéro possible ([USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12317862)).
- **Documents non rattachés** :
  - US 11,997,986 B2, « Pet treat holder » : cessionnaire non visible ([Google Patents](https://patents.google.com/patent/US11997986)) ;
  - **WO 2020/102719 A1**, cité dans la famille d'après la liste de citations Google Patents : **rattachement non vérifié** ;
  - US 6,470,830, US 7,278,374 (WO 2004/043142, inventeur Charles D. Mann), US 2009/0217885 et US 9,675,050 sont attribués à Bow Wow Labs par la synthèse du moteur. **Attribution douteuse**, probablement des métadonnées erronées. Ne pas s'y fier ([Google Patents](https://patents.google.com/patent/US7278374B2/en)).
- **Brevet européen (EP)** : **aucun trouvé** (requêtes n° 6, 9 et 35), donc **non vérifié (Espacenet non consultable)**. Dessins et modèles EUIPO : non recherchés.
- **Marque** : opposition TTAB n° 91255536 (HISTORIQUE).
  - Premier Pet Products, titulaire des marques BUSY BUDDY, s'est opposé à la demande BULLY BUDDY de Bow Wow Labs.
  - La procédure a été suspendue fin 2021 pour négocier.
  - Elle a été rejetée sans préjudice en janvier 2022, après le **retrait de la demande** ([Gleanmark](https://gleanmark.com/ttab/proceeding/91255536)).
  - Communiqué de 2022 : « Bully Sticks Buddy is now Bow Wow Buddy » ([Pets+](https://petsplusmag.com/bow-wow-labs-favorite-bully-sticks-buddy-is-now-bow-wow-buddy/)). Le lien de cause à effet avec l'opposition est une inférence.
- **Actions contre les copies** : **aucune trouvée** (requête n° 10). Les annonces eBay relevées sont des reventes de produits authentiques.
- [CP] Un brevet d'invention US dure 20 ans à compter du dépôt, sous réserve du paiement des annuités. Le brevet de 2015 courrait jusqu'à environ mai 2035.

#### 1.8 Plaintes récurrentes dans les avis négatifs (deliverable 2)
1. **Le bâtonnet glisse ou le chien l'extrait** :
   - Chewy, 1 étoile : « the bully stick slipped out after my dog start chewing it for a bit » ([Chewy](https://www.chewy.com/bow-wow-labs-buddy-safety-device/dp/1441774)) ;
   - Amazon US : le chien l'a sorti « in about five minutes » ([Amazon](https://www.amazon.com/Bow-Wow-Labs-Safety-Device/dp/B082YJHTYN)) ;
   - certains chiens ont extrait le dernier morceau ([desertcart](https://www.desertcart.nl/products/122254124)) ;
   - acheteur du kit M au tour précédent : la marque a évoqué une pièce défectueuse.
2. **Compatibilité des diamètres** :
   - test WDJ intitulé « Bow Wow Buddy Works Best With Thick Sticks » ; le testeur voudrait l'utiliser avec des bâtonnets plus fins ([WDJ](https://www.whole-dog-journal.com/?p=582533)) ;
   - questions-réponses Amazon : « Would this work with curly bully sticks? » ([Amazon Q&A](https://www.amazon.com/ask/questions/Tx18C17TKI80PGK/ref=ask_ql_ql_al_hza)) et « What size is best to fit Costco's Cadet 12" Bully sticks? » ([Amazon Q&A](https://www.amazon.com/ask/questions/Tx25MG3MIK2YEBB/ref=ask_ql_ql_al_hza)) ;
   - la marque elle-même « cannot guarantee » l'ajustement (tour précédent).
3. **Usure** :
   - Amazon.fr : les dents en plastique se sont un peu usées après une seule utilisation ([Amazon.fr B0DFX3NHT4](https://www.amazon.fr/Bow-Wow-Labs-dintimidation-lave-vaisselle/dp/B0DFX3NHT4)) ;
   - supports rayés ou mâchés (desertcart, modèles bon marché). Un acheteur note qu'un chien qui ronge le support signale surtout un bâtonnet laissé trop court ([desertcart](https://www.desertcart.nl/products/122254124)).
4. **Ergonomie** : le support glisse sur le parquet, un défaut cité par Dogster ([Dogster](https://www.dogster.com/lifestyle/bow-wow-labs-bow-wow-buddy-review/)). Il est trop lourd pour qu'un petit chien le traîne (Amazon US).
5. **Prix** : environ 28 à 38 $ selon la taille (WDJ). Les acheteurs jugent toutefois que le modèle plus cher à dents métalliques vaut son prix ([desertcart](https://www.desertcart.nl/products/122254124)).
6. **Ruptures** : sur Amazon.fr, XS « Currently unavailable » et kit XL sans date de retour (tour précédent).
7. **Service après-vente** : un client a été facturé pour quatre supports non voulus. Anecdote non datée ([desertcart](https://www.desertcart.co.th/products/592196318)).

#### 1.9 Concurrents US : une catégorie validée, mais encombrée
- **Woof BullySafe** :
  - **confirmé comme produit de Woof**, la marque du Pupsicle : il figure dans le blog Woof et dans des lots avec le Pupsicle ([mywoof](https://mywoof.com/blogs/articles/woof-pet-products)) ;
  - nylon, lave-vaisselle ; on dévisse, on insère la friandise, on revisse ;
  - **19,99 $** chez PetSmart, Chewy et Jeffers (24,99 $ barré) ; 26,99 $ chez The Hungry Pooch ;
  - une boutique britannique, wooof.co.uk, liste un « Woof BullySafe Bully Stick Pizzle Chew Holder ». **Identité de cette boutique non vérifiée.**
  - Sources : [PetSmart](https://www.petsmart.com/5363397.html) ; [Chewy](https://www.chewy.com/woof-bullysafe-dog-chew-treat-holder/dp/1363134) ; [Jeffers](https://jefferspet.com/es/products/bullysafe) ; [The Hungry Pooch](https://thehungrypooch.com/product-tag/chew-holder/) ; [wooof.co.uk](https://wooof.co.uk/products/woof-bullysafe-bully-stick-pizzle-chew-holder)
  - Woof a été racheté par The Farmer's Dog en août 2026 (tour précédent, [CB Insights](https://www.cbinsights.com/investor/woof-2)).
- **Bully Grip** :
  - fondatrice Vaso Karras ; la marque est née après que le chien Tesla « swallowed too large a piece of a bully stick and landed us in the ER » ([Faire](https://www.faire.com/brand/b_5qrfxvey9d)) ;
  - AVIS : Amazon 4,2/5 sur **1 714** ; Walmart 3,9/5 sur 20 ([Walmart](https://www.walmart.com/ip/777575223)) ;
  - matière : silicone selon Cuteness, caoutchouc naturel selon une fiche Amazon.fr.
- **PetClan Chewise** :
  - nylon avec dents métalliques, chiens de plus de 20 lb ;
  - kit avec « nubs collector, emergency stickers, travel bag » ;
  - origine Chine, première mise en vente le **10/08/2024** ;
  - AVIS de 4,5/5 sur **1 429** ou **1 370** selon les miroirs.
  - Sources : [desertcart](https://www.desertcart.ae/products/654838619-chewise-bully-stick-holder-improved-bully-sticks-holder-ultimate-secure.md) ; [desertcart HR](https://www.desertcart.hr/products/666286063-petclan-chewise-bully-stick-holder-ultimate-secure-heavy-duty-improved.md)
- **Autres** :
  - EverChew : « pin-locking mechanism », dit « patent-pending » ou « patented » selon les pages ([CB Insights](https://www.cbinsights.com/compare/bow-wow-labs-vs-everchew)) ;
  - Tall Tails Bully Stick Holders (Pet Age, 01/05/2024) ([Pet Age](https://www.petage.com/product/tall-tails-bully-stick-holders/)) ;
  - ChewEasy ([Fido Friendly](https://www.fidofriendly.com/blog/the-best-bully-stick-holder-for-fido/)) ;
  - Best Bully Sticks : support à 19,99 $ en « food-grade nylon » ([bullystick.com](https://www.bullystick.com/products/bully-stick-holder)) ;
  - Bully Stick Companion ([desertcart](https://www.desertcart.co.za/products/428876563-bully-stick-companion-locks-onto-bully-stick-prevents-choking-keeps)) ;
  - Mighty Chewz (tour précédent).

### Inferences
- **Fiabilité.** Les chiffres 2022–2023 viennent d'une offre réglementée par la SEC (Reg CF). Ils sont donc plus solides qu'un agrégateur, mais restent **déclaratifs et HISTORIQUES**. Pour 2024–2026, il n'existe que des estimations contradictoires (LeadIQ de 10 à 25 M$, Prospeo à 1,1 M$) : **CA non confirmé**.
- **Dynamique.** L'entreprise vit, innove et élargit sa distribution : refonte 2024, brevet 2025, environ 700 magasins depuis août 2025, effectif de 15 personnes. Mais la croissance de 2023 était déjà **lente et déficitaire** (+17 %, −20 % de marge nette). L'entrée en magasin en 2025 peut traduire soit un succès, soit un plafonnement de la vente directe. C'est une hypothèse, non tranchable.
- **Modèle économique** [calc, ordre de grandeur] : 200 000 supports à 28–35 $ représentent environ 5,6 à 7,0 M$ cumulés en valeur de vente, sur plusieurs années. C'est moins que le seul CA 2022–2023 (11,1 M$). Le CA récurrent repose donc vraisemblablement sur les **bully sticks** (le consommable), et le support sert de produit d'appel (inférence).
- **Catégorie validée aux US mais encombrée.** On compte au moins 8 concurrents, dont Woof (adossé à The Farmer's Dog depuis 2026) et PetClan Chewise, qui a accumulé environ 1 400 avis depuis août 2024. Un nouvel entrant peut donc percer vite, ce qui montre aussi la faible barrière à l'entrée.
- **Les plaintes portent sur la conception, pas sur le concept** : bâtonnet qui glisse, diamètres, dents en plastique, glissement au sol. Ce sont autant d'axes de différenciation pour une marque française (section 3).

### Gaps
- **Form C-AR 2024 et 2025, et toute mise à jour Wefunder postérieure à janvier 2024 : non trouvés.** EDGAR plein texte non consultable.
- **CA 2024, 2025 et 2026 : CA non confirmé.**
- Inc. 5000 2025 et 2026 : non trouvé, une seule requête.
- Amazon US : nombre d'avis des nouvelles fiches (B0DFX…, B0CK…) et badge « bought in past month » : **non vérifié (accès impossible)**.
- Conflit sur la date de clôture Wefunder (mai 2023 ou 29/04/2024) : non résolu.
- Famille de brevets hors US (WO 2020/102719, EP) et rattachement de US 11,997,986 et US 12,317,862 : **non vérifiés (Espacenet et USPTO non consultables)**.
- Part du support dans le CA : inconnue.

## 2. Le support de bully stick est-il vraiment sous-exploité en France, et la demande française est-elle crédible ?

### Takeaway
**La demande de fond est réelle, le support reste à éduquer.**

Le **nerf de bœuf** est une friandise courante en France :
- toutes les grandes enseignes en vendent : Zooplus, Maxi Zoo, Zoomalia, Animalis, Truffaut, Bricomarché, La Compagnie des Animaux, Amazon.fr ;
- elles proposent des marques propres (MultiFit) et des marques françaises (Nutrivet Inne, Bubimex) ;
- les prix vont d'environ 1,4 € la pièce à 54 € le kilo ;
- certaines fiches dépassent 600 avis (636 sur Amazon.fr).

Le **risque d'étouffement et d'occlusion** est décrit dans des contenus français (conseils-animaux.fr, SantéVet, PetsCare FR, avis Zoomalia). En revanche, la **solution « support » n'apparaît presque jamais** dans les contenus en français.

**Offre de supports accessible en France** :
- Bow Wow Labs (Amazon.fr, ruptures fréquentes) ;
- PetClan Chewise (environ 35,10 € sur Amazon.fr) ;
- **PetTribes « Support Bâton Mordant Chien Grand Format » sur Zooplus.fr**. **Correction du tour précédent : au moins une enseigne vend un support en France** ;
- des fiches de type Bully Grip, Agelux (métal) et des génériques sur Amazon.fr ;
- Fruugo, Temu et AliExpress.

**Aucune marque française ni boutique Shopify française n'a été trouvée**, et aucune publicité n'a pu être vérifiée.

**Verdict : concurrence moyenne sur l'offre, sous-exploité côté marque et contenu en français.**

### Cited Findings

#### 2.1 Le nerf de bœuf en France : noms, enseignes, prix et avis (indicateurs de demande)
- **Noms employés par les vendeurs français** :
  - « nerf de bœuf » (dominant) ;
  - « pénis de bœuf » (Maxi Zoo, MultiFit) ;
  - « 100% verge de taureau » (Zoomalia) ;
  - « Bully Sticks Chien » et « Tendon de Bœuf » (titre Amazon.fr de Natural Dog Treats) ;
  - « Best Bully Sticks » (classement echoduconsommateur.fr) ;
  - « nerfs de veau » (Caniland, Zooplus).
  - Sources : [Maxi Zoo](https://www.maxizoo.fr/p/multifit-nerf-de-buf-native-1-pice-1006999/) ; [Zoomalia, nerf entier](https://www.zoomalia.com/animalerie/nerf-de-b-uf-entier-pour-chien-p-142710.html) ; [Amazon.fr](https://www.amazon.fr/product-reviews/B077XRG6M3/ref=dp_prsubs_1) ; [Zooplus, Caniland](https://www.zooplus.fr/shop/chiens/friandises_chien/friandises_chien_boeuf/autres_friandises_boeuf/405409)
  - Définition (source US) : le pizzle est le pénis du taureau ; on parle aussi de « steer sticks », « pizzle sticks », « bull pizzles » ([ScienceABC](https://www.scienceabc.com/nature/animals/what-are-beef-pizzles) ; [bullystick.com](https://www.bullystick.com/what-is-a-bully-stick)).
- **PRIX TTC** (relevés le 2026-10-28 via les extraits) :
  - **Maxi Zoo, MultiFit native** : 1 pièce à environ 9,59 € ; 350 g à 22,99 €, soit environ 65,7 €/kg [calc] ; 1 kg à 53,99 € ([1 pièce](https://www.maxizoo.fr/p/multifit-nerf-de-buf-native-1-pice-1006999/) ; [350 g](https://www.maxizoo.fr/p/multifit-native-nerf-de-buf-350-g-1006989/) ; [1 kg](https://www.maxizoo.fr/p/multifit-native-nerfs-de-buf-1kg-1009268/)) ;
  - **Zoomalia** : Trixie 12 cm par 8 à environ 10,99 €, soit environ 1,37 € la pièce [calc] ; nerf entier de 90 cm entre 15,49 et 15,99 € ([Trixie](https://www.zoomalia.com/animalerie/trixie-nerf-de-b-uf-a-macher-pour-chien-p-13761.html) ; [nerf entier](https://www.zoomalia.com/animalerie/nerf-de-b-uf-entier-pour-chien-p-142710.html)) ;
  - **Animalis** : Trixie 70–80 cm à 8,16 € ([Animalis](https://www.animalis.com/trixie-nerfs-de-boeuf-pour-chien-70-80cm-809965_M.html)) ;
  - **Truffaut** : nerfs à l'unité en S, M, L et XL, avec la mention « Origine France Garantie : Non » ([Truffaut](https://www.truffaut.com/nerf-de-boeuf.html)) ;
  - **Bricomarché** : Bubimex 65 cm, prix non relevé ([Bricomarché](https://www.bricomarche.com/p/nerf-de-boeuf-entier-1x-65cm/4250078907169)) ;
  - **La Compagnie des Animaux** : Trixie en 12 cm par 50 et en 100 g ([12 cm x50](https://www.lacompagniedesanimaux.com/trixie-nerf-de-boeuf-pour-chien-12-cm-x50.html)) ;
  - **Zooplus.fr**, prix non relevés : « Nerfs de bœuf 8 pièces » ([lien](https://www.zooplus.fr/shop/chiens/friandises_chien/friandises_chien_boeuf/9980003822)), Nutrivet Inne ([lien](https://www.zooplus.fr/shop/chiens/friandises_chien/friandises_chien_boeuf/autres_friandises_boeuf/2100531)), MAIKAI ([lien](https://www.zooplus.fr/shop/chiens/friandises_chien/bois_corne_sabot/9980010537)), Yuccana 12 cm par 5 (URL non attribuable) et le revendeur Zoomici.
- **AVIS (indicateurs de demande)** :
  - Amazon.fr, **Natural Dog Treats 15 cm par 5** (B077XRG6M3) : **4,4/5 sur 636** (62 % de 5 étoiles, 5 % de 1 étoile ; global ratings probables) ([Amazon.fr](https://www.amazon.fr/product-reviews/B077XRG6M3/ref=dp_prsubs_1)) ;
  - Amazon.fr, 4DOGS Original 15 cm : 4,0/5 sur 17 ;
  - Zoomalia, **Dailys 8 pièces** : 4,8/5 sur **106** ([Zoomalia](https://www.zoomalia.com/animalerie/nerfs-de-boeuf-pour-chien-dailys-8-pieces-p-138474.html)) ;
  - Zoomalia, Trixie tresse à mâcher aux nerfs de bœuf : 4,7/5 sur 90 ([Zoomalia](https://www.zoomalia.com/animalerie/trixie-tresse-a-macher-avec-nerfs-de-b-uf-en-vrac-p-124132.html)) ;
  - Zoomalia, nerfs de 15 cm : 4,8/5 sur 21 ([Zoomalia](https://www.zoomalia.com/animalerie/nerfs-de-b-uf-15cm-p-140699.html)) ; nerf entier : 4,91/5 sur 11.
- **Contenu des avis** :
  - pièces trop fines ou mal calibrées ;
  - trop chères pour la durée de mastication ;
  - avalées en quelques minutes par les gros chiens ;
  - odeur forte ;
  - un cas isolé de diarrhée (MultiFit 350 g).
  - Sources : [Zoomalia, avis](https://www.zoomalia.com/animalerie/avis/nerf-de-b-uf-a-macher-pour-chien-av-13761.html) ; [Maxi Zoo](https://www.maxizoo.fr/p/multifit-native-nerf-de-buf-350-g-1006989/)
- **Usage** : une fiche Zooplus conseille 1 friandise par jour pour un chien de 10 à 30 kg, et 1,5 au-delà de 30 kg. Des clients glissent des morceaux dans un Kong ([Zooplus](https://www.zooplus.fr/shop/chiens/friandises_chien/friandises_chien_boeuf/9980003822)).
- **Marques et origine** :
  - **Nutrivet Inne** est présentée comme « Fabrication française » ([Zoomalia](https://www.zoomalia.com/animalerie/nutrivet-inne-friandise-naturelle-nerfs-de-boeuf-pour-chien-p-156691.html)) ;
  - Bubimex, Vadigran ([Zoomalia](https://www.zoomalia.com/animalerie/vadigran-friandise-naturelle-nerfs-de-b-uf-p-70752.html)), Trixie, MultiFit (marque propre de Maxi Zoo), Dailys ;
  - M'Gourmand, vendeur de Champagne-Ardenne ([comdewouf](https://comdewouf.fr/?p=11702), synthèse).
- **Contexte de mastication de masse** : Action vend des « bâtonnets à mâcher pour chien » et des « friandises à mâcher pour chien » ([Action](https://www.action.com/fr-fr/p/2580366/friandises-a-macher-pour-chien/)).

#### 2.2 Conscience du risque : contenus vétérinaires et médias français
- **conseils-animaux.fr** :
  - « le principal danger reste ici l'éventualité d'un étouffement en raison d'une mauvaise ingestion » (tour précédent, [page mastication](https://conseils-animaux.fr/alimentation/nourriture-pour-chien/friandises/mastication/nerf-boeuf/)) ;
  - le nerf ingéré peut aussi provoquer une **occlusion gastrique ou intestinale** ; des fragments durs peuvent perforer l'intestin et imposer une chirurgie ;
  - le risque augmente chez un chien glouton ou avec une friandise trop petite ([page friandises naturelles](https://conseils-animaux.fr/alimentation/nourriture-pour-chien/friandises/naturelles/nerf-boeuf/)).
- **PetsCare (version française)** :
  - surveiller le chien ;
  - « utiliser un porte-bâton pour éviter qu'il avale le dernier morceau » (formulation de la synthèse) ;
  - retirer la friandise quand elle devient assez petite pour être avalée ;
  - risques cités : « étouffement, obstruction œsophagienne, blocage intestinal, perforation ».
  - Sources : [PetsCare, guide](https://www.petscare.com/fr/news/post/dog-swallowed-bully-stick-guide) ; [PetsCare](https://www.petscare.com/fr/news/post/are-bully-sticks-good-for-dogs)
  - **C'est le seul contenu en français trouvé qui recommande un support.**
- **SantéVet** (assureur santé animale), contenus généraux sur l'ingestion de corps étrangers :
  - urgence, ne pas faire vomir ;
  - symptômes d'occlusion ;
  - taux de survie de 80 à 90 % si l'intervention est rapide.
  - Ces articles ne portent pas sur le nerf de bœuf en particulier ([SantéVet](https://www.santevet.com/articles/pourquoi-mon-chien-mange-des-chaussettes) ; [SantéVet](https://www.santevet.com/articles/puis-je-donner-un-os-de-poulet-a-mon-chien)).
- **Avis clients** :
  - Zoomalia (Trixie grandes tailles) : un client conseille de retirer le petit morceau restant pour éviter les étouffements (tour précédent) ;
  - Zooplus : témoignages d'étouffement avec des friandises molles ou collantes, et conseil de surveiller les chiens qui mâchent trop vite ([Zooplus, avis](https://www.zooplus.fr/feedback/shop/chiens/friandises_chien/friandises_os_chien/soin_dentaire/184117)).
- **Sensibilisation voisine** : Zoomalia, « Lancer un bâton à votre chien peut lui coûter la vie » ([Zoomalia](https://www.zoomalia.com/blog/article/lancer-baton-chien-peut-lui-couter-la-vie.html)) ; Paris Match Belgique, 29/07/2022, HISTORIQUE ([Paris Match](https://www.parismatch.be/actualites/environnement/2022/07/29/pourquoi-vous-devez-absolument-arreter-de-jeter-des-batons-a-votre-chien-EFEA6ITIWZCHXHSXM46YNLRDUM/)).
- **Wamiz et 30 Millions d'Amis** : **aucun article trouvé** (requête n° 14, une seule).
- **Classement d'affiliation en français** : « Les 10 Meilleurs Best Bully Sticks en France » (juin 2026) classe **PetClan Chewise 3e** ([echoduconsommateur.fr](https://reviews.echoduconsommateur.fr/product/best-bully-sticks/)). Valeur probante faible : page probablement générée automatiquement (inférence).
- **Source US** : bullystick.com recommande de retirer le bâtonnet à 2,5–3 pouces (6–8 cm) ([bullystick.com](https://www.bullystick.com/what-is-a-bully-stick)) ; Core77 décrit le risque du bout avalé ([Core77](https://www.core77.com/posts/137392)).

#### 2.3 Inventaire des supports vendus ou accessibles en France (relevé le 2026-10-28)

| # | Offre | Canal en France | Marque, origine | Prix TTC | Avis | Langue de la fiche | Source |
|---|---|---|---|---|---|---|---|
| 1 | Bow Wow Buddy, ancienne version XS | Amazon.fr B082YJHTYN | Bow Wow Labs (US) | non relevé | 4,3/5 sur 7 021 (global) ; « Currently unavailable » | anglais / traduction partielle | [Amazon.fr](https://www.amazon.fr/Bow-Wow-Labs-Dispositif-s%C3%A9curit%C3%A9/dp/B082YJHTYN) |
| 2 | Buddy Safety Device, nouvelle version (grande taille 23–34 kg) | Amazon.fr B0DFX3NHT4 | Bow Wow Labs | non relevé | avis : dents en plastique usées après une utilisation | traduction automatique (« dintimidation » dans l'URL) | [Amazon.fr](https://www.amazon.fr/Bow-Wow-Labs-dintimidation-lave-vaisselle/dp/B0DFX3NHT4) |
| 3 | Kits Bow Wow Buddy et Bully Buddy, Starter Kit S | Amazon.fr B0881ZN7P9, B0882LN8MF, B0CK3K3C31 | Bow Wow Labs | non relevé | kit « indisponible » (synthèse) | anglais | [B0881ZN7P9](https://www.amazon.fr/Bow-Wow-Labs-Bully-d%C3%A9marrage/dp/B0881ZN7P9) ; [B0882LN8MF](https://www.amazon.fr/-/en/Bow-Wow-Labs/dp/B0882LN8MF) ; [B0CK3K3C31](https://www.amazon.fr/Bow-Wow-Labs-Buddy-d%C3%A9marrage/dp/B0CK3K3C31) |
| 4 | **PetClan Chewise** (nylon sans BPA, dents en métal, plus de 9 kg, garantie de 2 ans) | Amazon.fr B0CQX8TRL2 (et B0F7H8XWXD) | PetClan (origine Chine, lancé en 08/2024) | **environ 35,10 €** | « très rassurant » ; une note de 3 étoiles doute de la durabilité ; environ 1 400 avis à l'international | anglais | [Amazon.fr](https://www.amazon.fr/Dispositif-s%C3%A9curis%C3%A9-l%C3%A9touffement-Compatible-b%C3%A2tonnets/dp/B0CQX8TRL2) |
| 5 | **PetTribes « Support Bâton Mordant Chien Grand Format »** (nylon, « anti-étouffement », grands chiens, rinçage à l'eau claire) | **Zooplus.fr** 9980073117 | PetTribes, marque générique multi-catégories (bandanas, cordes à 18,99 € et 21,59 €) | non relevé | non relevés | français | [Zooplus.fr](https://www.zooplus.fr/shop/chiens/jouets_sport_chien/jouets_chien_occupation/9980073117) ; [PetTribes, corde](https://www.zooplus.fr/shop/chiens/jouets_sport_chien/cordes_jeu_chien/9980060161) |
| 6 | « Bully Stick Holder », « Bully Stick Dog Stand » (M et S). La synthèse cite un « Bully Grip » en caoutchouc naturel, pour chiens jusqu'à 50 lb, jugé « difficile à utiliser » | Amazon.fr B07YNYFXTP, B0827D3SCV, B0827F2SSL | **Bully Grip probable** (US ; inférence d'après les titres identiques aux fiches Bully Grip) | non relevé | non relevés | anglais | [B07YNYFXTP](https://www.amazon.fr/Support-pour-b%C3%A2ton-taureau-interactif/dp/B07YNYFXTP) ; [B0827D3SCV](https://www.amazon.fr/Bully-Stick-Holder-alimentation-distributeur/dp/B0827D3SCV) ; [B0827F2SSL](https://www.amazon.fr/Bully-Stick-Support-pour-chiens/dp/B0827F2SSL) |
| 7 | Agelux, support en métal | Amazon.fr B0CBBD92V2 | Agelux | non relevé | non relevés | français approximatif | [Amazon.fr](https://www.amazon.fr/Agelux-Support-b%C3%A2ton-bully-chiens/dp/B0CBBD92V2) (tour précédent) |
| 8 | Générique « Bully Stick Holder Interactive Container » | Amazon.fr B0GZWBR5QR | inconnue | non relevé | non relevés | anglais | [Amazon.fr](https://www.amazon.fr/Bully-Stick-Holder-Interactive-Container/dp/B0GZWBR5QR) (tour précédent) |
| 9 | « Bully Stick Holder … anti-choking … 3-in-1 » (plusieurs annonces) | **Fruugo.fr** | vendeurs transfrontaliers | **environ 18–28 €** | non relevés | anglais | [Fruugo](https://www.fruugo.fr/bully-stick-holder-durable-dog-chew-holder-for-safe-anti-choking-chew-toy-for-aggressive-chewers-3-in-1-dog-enrichment-toy-dishwasher-safe/p-433628060-910266805) (tour précédent) |
| 10 | « bully stick holder … prevent choking safety device long enough screw to lock » | **Temu** (livraison en France non vérifiée) | génériques chinois | non relevé | non relevés | anglais | [Temu](https://www.temu.com/bully-stick-holder-for-dogs-durable-chew-toy-chew-holder-prevent-choking-safety-device-long-enough-screw-to-lock-g-601099847629620.html) |
| 11 | Plusieurs supports, articles « wiki », support All For Paws | **AliExpress** (fr.aliexpress.com) | génériques chinois | non relevé | non relevés | anglais ou traduction automatique | [AliExpress FR](https://fr.aliexpress.com/w/wholesale-kong-bully-stick-holder.html) ; [AliExpress, article](https://www.aliexpress.com/s/wiki-ssr/article/bully-stick-holder-dog) |
| 12 | Revente de Bow Wow Buddy (« Sicherheitsvorrichtung … mittelgroße Hunde ») | eBay.de | Bow Wow Labs | non relevé | — | allemand | [eBay.de](https://www.ebay.de/itm/205664518114) |

- **Non trouvé dans ce criblage** :
  - Cdiscount, ManoMano, Rakuten et Fnac (requête n° 16, et FR-A1 et FR-A6 pour Cdiscount) ;
  - Maxi Zoo, Zoomalia, Wanimo et Animalis (FR-A1, FR-A6, n° 12) ;
  - **boutiques Shopify françaises** (FR-A5, n° 17, n° 37) ;
  - Woof BullySafe en France (n° 36 : seule une boutique britannique apparaît).

#### 2.4 Publicités actives
- **Meta Ad Library (France et US) et TikTok Creative Center : non vérifié (accès impossible).**
- Les recherches n'ont fait remonter **aucune publicité française**, aucun créateur français et aucune boutique française. Cela ne prouve pas l'absence de publicités.

#### 2.5 Requêtes « France » et ce qu'elles ont renvoyé (preuve à l'appui de tout constat d'absence)
Les requêtes FR-A1 à FR-A6 datent du tour précédent (`us_decouverte_marques_meconnues.md`). Les numéros 11 à 45 sont ceux de ce tour.

| Angle | Requête (verbatim) | Domaines | Résultat |
|---|---|---|---|
| Nom anglais, marque | FR-A1 `Bow Wow Buddy bully stick holder` | amazon.fr, cdiscount.com, zooplus.fr, zoomalia.com, wanimo.com | Original et au moins 6 copies sur Amazon.fr ; rien ailleurs |
| Nom anglais | n° 15 `Bully Stick Holder chien support anti-étouffement` | amazon.fr | Bow Wow Labs (4 ASIN), PetClan Chewise (environ 35,10 €), Bully Grip, génériques |
| Nom anglais | n° 16 `bully stick holder chien support` | cdiscount.com, manomano.fr, fr.shopping.rakuten.com, fnac.com, temu.com, aliexpress.com | Temu et AliExpress seulement ; **rien** chez Cdiscount, ManoMano, Rakuten ou Fnac |
| Nom français | FR-A2 `support nerf de boeuf chien` | amazon.fr | Nerfs seulement |
| Nom français | FR-A3 `porte nerf de boeuf chien anti étouffement` | — | Aucun produit ; avis Zoomalia « retirer le petit morceau » |
| Nom français | FR-A6 `support pour bâton à mâcher chien anti-étouffement` | cdiscount.com, zooplus.fr, zoomalia.com, wanimo.com, maxizoo.fr, animalis.com, fruugo.fr | Bâtonnets seulement |
| Nom français | n° 17 `porte-friandise à mâcher chien empêche d'avaler le dernier morceau` | — | Aucun support ; friandises Zooplus et Action |
| Nom français | n° 37 `porte-bâton à mâcher chien nerf de bœuf support sécurité acheter` | — | **PetTribes sur Zooplus.fr** ; classement echoduconsommateur (Chewise) ; nerfs |
| Formulation des concurrents | n° 41 `"support bâton mordant" chien` | — | PetTribes sur Zooplus.fr (seul résultat) ; bâtons IntiMeg |
| Formulation des concurrents | n° 42 `PetTribes support bâton mordant chien prix avis` | zooplus.fr | Fiche du support non renvoyée ; cordes PetTribes à 18,99 et 21,59 €, sans avis |
| Boutiques | FR-A5 `support bully stick chien sécurité boutique en ligne` | — | Fruugo.fr à 18–28 € ; aucune boutique française |
| Problème | FR-A4 `nerf de boeuf chien danger étouffement dernier morceau` | — | conseils-animaux.fr, PetsCare FR |
| Problème | n° 13 `chien a avalé morceau nerf de boeuf vétérinaire occlusion étouffement` | — | conseils-animaux.fr (occlusion), SantéVet |
| Problème | n° 14 `wamiz OR "30 millions d'amis" friandise à mâcher chien étouffement surveiller dernier morceau` | — | PetsCare FR (« porte-bâton ») ; avis Zooplus ; rien de Wamiz ni de 30 Millions d'Amis |
| Synonymes | n° 38 `bully stick c'est quoi chien nerf de boeuf pizzle` | — | Définitions US (pizzle, steer sticks) |
| Demande | n° 11 `nerf de boeuf chien` | zooplus.fr | Au moins 5 références |
| Demande | n° 12 `nerf de boeuf chien prix avis` | maxizoo.fr, zoomalia.com, wanimo.com, animalis.com | Prix MultiFit, Trixie, nerf entier ; **rien chez Wanimo** |
| Demande | n° 28 `nerf de boeuf origine France friandise naturelle chien marque française` | — | Nutrivet Inne (fabrication française) ; Truffaut |
| Demande | n° 45 `nerfs de bœuf chien à mâcher naturel évaluations note sur 5` | amazon.fr, zooplus.fr, zoomalia.com | 636 avis (Amazon.fr), 106 et 90 (Zoomalia) |
| Fournisseurs | n° 43 `nerf de boeuf grossiste fournisseur professionnel friandises chien marque blanche` | — | Aucun grossiste en marque blanche (section 3.4) |
| Concurrent US | n° 36 `"Woof" BullySafe bully stick holder brand Pupsicle` | — | US et une boutique britannique ; rien en France |

### Inferences

#### Verdict sur les 7 points

| Point | Verdict | Justification |
|---|---|---|
| 1. Concurrents directs accessibles en France | **Au moins 8 offres** (au moins 12 ASIN sur Amazon.fr, 1 sur Zooplus.fr, Fruugo, Temu, AliExpress) ; **0 marque française** | Tableau 2.3 |
| 2. Marques | Bow Wow Labs (US), **PetClan Chewise** (CN, la plus « marque » : 35 €, garantie, kit), **PetTribes** (générique, Zooplus.fr), Bully Grip (US, probable), Agelux, génériques | Tableau 2.3 |
| 3. Publicités actives | **Non vérifié (accès impossible)** ; aucune trouvée par recherche | Section 2.4 |
| 4. Niveau | **Concurrence moyenne** pour l'offre ; **sous-exploité** pour la marque, le contenu en français, la vente physique et l'adaptation aux nerfs vendus en France | Fiches en anglais ou mal traduites ; vocabulaire non stabilisé (« bâton mordant », « bâton taureau », « bully stick holder ») ; aucune boutique française |
| 5. Conscience des consommateurs | **Risque connu (moyenne), solution peu connue (faible)** | conseils-animaux.fr, SantéVet, avis Zoomalia ; un seul contenu en français recommande un « porte-bâton » (PetsCare) |
| 6. Demande française | **Forte pour le nerf de bœuf** (toutes les enseignes, marques propres, jusqu'à 636 avis par fiche) ; **non mesurée pour le support** | Section 2.1 ; Google Trends et Ad Library non consultés |
| 7. Avantage concurrentiel ou facilité de copie | **Facile à copier** (usines à 1–3 $, MOQ de 20 à 1 000, brevets uniquement US) ; différenciation possible par la marque, la compatibilité avec les nerfs français, les kits et le contenu | Sections 1.7, 1.8 et 3.1 |

- **Correction par rapport au tour précédent.** « Aucune enseigne française » n'est plus exact : Zooplus.fr référence un support (PetTribes). Il s'agit vraisemblablement d'un vendeur partenaire et d'une marque générique (inférence). Cela confirme la catégorie sans établir de marque.
- **Ce qui est sous-exploité, ce n'est pas l'offre mais le positionnement.** Personne ne vend en français un « kit de mastication sécurisée » adapté aux nerfs de bœuf des enseignes françaises (Trixie, MultiFit, Nutrivet Inne), avec un guide des tailles par race et un contenu éducatif. Or les avis français se plaignent de **nerfs « trop fins ou mal calibrés »**, et le leader US reconnaît ne pas garantir l'ajustement.
- **Revers de la faible notoriété** : la publicité devra éduquer (problème, puis solution), ce qui pèse sur le CPA.
- **Menaces d'entrée** : Woof (BullySafe à 19,99 $, propriété de The Farmer's Dog en 2026, Pupsicle déjà sur Amazon.fr selon le tour 1) ; PetClan, déjà présent sur Amazon.fr ; Bow Wow Labs, s'il ouvrait l'Europe. Hypothèses non vérifiées.

### Gaps
- Prix et avis de PetTribes sur Zooplus.fr, prix Amazon.fr de Bow Wow Labs, Bully Grip, Agelux et des génériques : **non relevés** (extraits incomplets).
- Meta Ad Library FR, TikTok FR, Google Trends (« nerf de bœuf », « bully stick ») : **non vérifié (accès impossible)**.
- Wanimo : aucune fiche de nerf renvoyée ; une seule requête filtrée, donc non concluant.
- Leboncoin, Vinted, Instagram FR et les groupes Facebook de propriétaires de chiens : non recherchés.
- Volume des ventes de nerfs en France : aucune donnée de marché ; seuls des comptes d'avis servent d'indicateur.
- Formulations non testées : `bâton de taureau support`, `porte-os chien`, `support os à mâcher chien`, `bully stick holder` sur Zooplus.de ou Amazon.de (demande européenne).

## 3. Une marque française peut-elle sourcer, différencier et vendre ce support avec profit, seul ou en kit, sans charge réglementaire lourde ?

### Takeaway
**Sourcing : facile.** Au moins 6 usines chinoises affichent des supports entre 0,95 et 3,19 $ FOB, avec des MOQ de 20 à 1 000 pièces. On trouve du nylon, du nylon avec dents en métal, du silicone et du caoutchouc. Le logo et l'emballage personnalisés sont courants.

**Brevets : risque faible en France, sous réserve d'une vérification sur Espacenet.** Seuls des brevets US ont été trouvés.

**Réglementation : légère pour le support seul.** C'est un produit de consommation soumis au GPSR. Elle devient **moyenne si l'on ajoute des nerfs** en marque propre : sous-produits animaux, étiquetage selon le règlement 767/2009, questions d'enregistrement auprès de la DDPP. Elle devient **lourde en cas d'import direct de pizzles hors UE** : certificat sanitaire, poste de contrôle frontalier.

**Potentiel publicitaire : qualitativement fort.** Histoires fondatrices (« mon chien s'est étouffé »), démonstration en 3 gestes, exposition TikTok de Bully Grip. Mais **aucune preuve chiffrée** d'engagement ou de rentabilité n'a été trouvée, et Bow Wow Labs perdait 20 % de son CA en 2023.

**Économie : non rentable au premier achat au CPA central de 39,9 €.**
- La contribution avant publicité va de 13 € (support seul à 29,90 €) à 27,50 € (kit duo à 69,90 €).
- Après publicité, chaque commande perd donc de 12 à 26 €.
- Il faut l'une de ces conditions : un CPA inférieur ou égal à 13–28 € ; un panier d'au moins 96 € TTC ; ou un modèle de réachat (recharges de nerfs à environ 6 € de contribution par commande) appuyé sur la base clients Pilou.

### Cited Findings

#### 3.1 Sourcing : fournisseurs, matériaux, prix, MOQ, échantillons, personnalisation
- **Listings Alibaba et Made-in-China** (PRIX FOB indicatifs en USD, relevés le 2026-10-28 via la synthèse du moteur ; attribution fournisseur par URL incertaine, sauf pour le premier) :
  - **Dongguan Hongzhou Technology** (Guangdong) : « Bully Stick Bolt », plastique, modèle HZ-B054Q, avec housse en silicone pour protéger le sol. **MOQ de 500 ; 1,67–2,08 $** ; fournisseur présent depuis 6 ans ([Alibaba](https://www.alibaba.com/product-detail/Bully-Stick-Bolt-for-Dogs-Dog_1601152729471.html)) ;
  - **Ningbo Sincere Holding Group** : « AFP Heavy Duty », nylon, « Anti-Choking BPA-Free Nylon Toy ». **0,95–1,60 $, MOQ de 24**. AFP désigne probablement la marque All For Paws (inférence) ;
  - **Guangzhou Zuowu Pet Product** : silicone « 2 In1 », support et distributeur de friandises. **2,46–2,82 $, MOQ de 20** ;
  - **Qingdao Yuanche International Trade** : bague remplaçable. **1,99–3,19 $, MOQ de 300** ;
  - **Shenzhen Ultra Eagex Tech** : « Dog Bully Stick Holder Anti-Choking Adjustable ». **2,85 $, MOQ de 1 000** ;
  - **Jiangxi Welton Pet Products** : forme d'os. **2–2,50 $, MOQ de 500**.
  - Pages : [Alibaba, chew stick holder](https://www.alibaba.com/wholesale/chew-stick-holder-dog.html) ; [Alibaba showroom](https://www.alibaba.com/showroom/bulli-stick-hold.html) ; [guide d'achat Alibaba](https://sonusgear.alibaba.com/buyingguides/bully-stick-holder)
- **Personnalisation** (repère indirect) : sur un autre produit Alibaba (porte-sacs en toile), « Customized logo (Min. Order: 1000 pieces) », avec des prix dégressifs de 1,49 $ (2–99 pièces) à 0,79 $ (10 000 pièces et plus) ([Alibaba](https://www.alibaba.com/product-introduction/Custom-Logo-Printing-Portable-Canvas-Dog_1601102483705.html)).
- **Échantillons** : avec des MOQ de 20 à 24 pièces (Zuowu, Ningbo Sincere), on peut commander de **petites séries d'essai** pour un coût marchandise de quelques dizaines de dollars [calc : 24 × 0,95–1,60 $ = 23–38 $, hors port]. Le coût réel des échantillons et du port n'a pas été relevé.
- **Repères de prix de détail** :
  - Apasiri sur eBay, « US $5.10 or Best Offer » ; une autre annonce à 7,75 $ (URL exacte non attribuable : [eBay.de](https://www.ebay.de/itm/396376994903), [eBay.com.au](https://www.ebay.com.au/itm/257525935478), [Apasiri](https://deals.christianpost.com/deal/apasiri-bully-stick-holder-for-medium-large-dogs-safe-and-durable)) ;
  - **Bully Lok** sur Faire UK : prix conseillé de 18,64 £, commande minimum de 97,10 £ ; corps en caoutchouc, vis en nylon ([Faire](https://www.faire.com/en-gb/product/p_turugc92zt)) ;
  - Woof BullySafe 19,99 $ ; Best Bully Sticks 19,99 $ ; Bow Wow Buddy 28–38 $ ; Chewise environ 35,10 € sur Amazon.fr.
- **Matériaux constatés** :
  - nylon « BPA-free » (Bow Wow Labs, fabriqué aux USA ; Woof) ;
  - nylon avec dents en métal (Chewise) ;
  - caoutchouc naturel ou silicone (Bully Grip) ;
  - silicone (Zuowu) ;
  - métal (Agelux).
- **Fabrication Bow Wow Labs** : aux USA, avec un poste « mold production » dans l'usage des fonds de 2023 ([KingsCrowd](https://kingscrowd.com/bow-wow-labs-on-wefunder-2023/)).

#### 3.2 Risque brevet et marque pour une marque française
- Brevets trouvés : **uniquement US** (US 10,015,951 ; 10,856,528 ; 12,317,863). Aucun EP n'a été trouvé (section 1.7).
- [CP] Un brevet US ne produit aucun effet en France.
- [CP] Si la demande PCT WO 2020/102719 appartient à Bow Wow Labs, l'entrée en phase européenne devait intervenir vers 2021 (31 mois après la priorité). Elle serait visible sur Espacenet. **À vérifier avant tout lancement.**
- Vendre sur Amazon US un modèle à bague filetée et bras serrants exposerait en revanche à une contrefaçon (inférence).
- **Marque** : éviter « Buddy ». L'opposition TTAB entre BUSY BUDDY (Premier Pet, marque PetSafe) et BULLY BUDDY montre la sensibilité de ce terme. Or les recharges PetSafe Busy Buddy sont vendues en France, chez Zoomalia ([Zoomalia](https://www.zoomalia.com/animalerie/recharge-friandises-pour-jouet-bristle-et-bouncy-bone-p-23795.html), repris de `sourcing_jouet_lechage.md`). Éviter aussi « SafeFit ».
- **Modèles chinois** : ils peuvent eux-mêmes reprendre des dessins protégés ailleurs. Dessins et modèles EUIPO non recherchés. Recommandation [CP] : une recherche de liberté d'exploitation (Espacenet et EUIPO) par un conseil en propriété industrielle, coût non sourcé.

#### 3.3 Réglementation du support seul
- **GPSR (UE) 2023/988**, applicable depuis le 13/12/2024. La fiche en ligne doit indiquer :
  - le fabricant ou la personne responsable dans l'UE, avec ses adresses postale et électronique ;
  - l'identification du produit ;
  - les **avertissements de sécurité en français**, sur la page produit elle-même.
  - Repris de `fr_costs_regulation.md` : [eugpsr.de](https://eugpsr.de/en/blog/gpsr-online-sales-required-info) ; [Xictron](https://www.xictron.com/en/blog/gpsr-product-safety-regulation-online-shop-2026/) ; [TÜV SÜD, 05/2026](https://www.tuvsud.com/en/newsroom/press-releases/2026/may/tuev-sued-eu-requirements-enhance-safety-and-transparency-for-consumers)
- **REACH** pour les plastiques et caoutchoucs (substances SVHC, phtalates, HAP), repris de `fr_costs_regulation.md`.
- [CP] Le règlement (CE) 1935/2004 sur le contact alimentaire vise les denrées destinées à l'homme. Les mentions « BPA-free » ou « qualité alimentaire » doivent cependant être étayées par une déclaration du fournisseur.
- **Douane** (repris de `fr_costs_regulation.md`, [S2]) :
  - article en plastique, position 3926 90 97 probable : **6,5 %**, à confirmer par un renseignement tarifaire contraignant ;
  - en envoi direct de Chine (dropshipping) : **3 € par article** depuis le 01/07/2026 (règlement (UE) 2026/382), plus **2 € de frais de traitement par article** attendus au 01/11/2026. Ce surcoût de 5 € pénalise un support à 29,90 € et plaide pour un stock importé en France ([guide de la Commission](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)).
- **Responsabilité** : le produit se présente comme un dispositif de sécurité, ce qui expose davantage la marque s'il cède. Il faut prévoir une assurance responsabilité civile produit [CP], des tests d'arrachement et d'usure et des instructions claires. Coûts non sourcés.

#### 3.4 Réglementation si des nerfs sont vendus en kit (deliverable 5)
- **Statut** : un nerf de bœuf séché est un **« dog chew »** au sens de l'annexe I du règlement (UE) 142/2011 : « products for pet animals to chew, produced from untanned hides and skins of ungulates or from other material of animal origin ». Il relève du cadre des **sous-produits animaux** : règlement (CE) 1069/2009, appliqué par le règlement (UE) 142/2011 ([legislation.gov.uk, art. 23 et annexes](https://www.legislation.gov.uk/eur/2011/142/article/23/data.pdf)).
- **Matières premières** : catégorie 3 (art. 35, a, i). À l'import, certaines matières de catégorie 1 issues d'animaux soumis à un traitement illégal sont admises (art. 35, a, ii). Exigences de production : annexe XIII, chapitre II ([legislation.gov.uk, annexe XIII ch. II](https://www.legislation.gov.uk/eur/2011/142/annex/XIII/chapter/II/data.pdf)).
- **Import depuis un pays tiers** : annexe XIV, chapitre II, section 1, **tableau 2, ligne 12** (modifiée par le règlement d'exécution (UE) 2020/207). Les produits doivent venir d'un pays listé et respecter l'annexe XIII, chapitre II ([règl. 2020/207](https://www.legislation.gov.uk/eur/2020/207/data.html)).
  - Le Royaume-Uni est un pays tiers : le certificat vétérinaire britannique **8325NFG** sert à exporter des dog chews vers l'UE ou l'Irlande du Nord (versions décembre 2023 v6, juin 2025 v7, novembre 2025 v9) ([Defra, Nov25 v9](https://assets.publishing.service.gov.uk/media/6841c046fa0289a17a3e87c8/8325NFG_Nov25_v9.pdf)).
  - Exemple de guide d'export étranger : [ACIA Canada](https://inspection.canada.ca/en/animal-health/terrestrial-animals/exports/pet-food/2009-7).
  - Attention : les textes consultés sont des versions britanniques (legislation.gov.uk) datées de 2013 à 2020. **Il faut relire la version consolidée sur EUR-Lex.**
- **France, filière des sous-produits animaux (SPAn)** :
  - « Tous les opérateurs de la filière des sous-produits animaux doivent au moins être enregistrés » ;
  - un **agrément préfectoral** est requis pour la transformation, l'entreposage et la **fabrication d'aliments pour animaux familiers** ;
  - la DD(CS)PP délivre une notification d'enregistrement et renseigne SIGAL ou RESYTAL.
  - Sources : [Préfecture de la Haute-Garonne](https://www.haute-garonne.gouv.fr/index.php/Actions-de-l-Etat/Agriculture-elevage-et-developpement-rural/Informations-par-type-d-activite/Sous-produits-animaux/Les-sous-produits-animaux-SPAN) ; [arrêté du 8 décembre 2011, Légifrance](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000025056078/) ; [agriculture.gouv.fr](https://agriculture.gouv.fr/les-sous-produits-animaux-et-les-produits-qui-en-sont-derives-valorisation-et-elimination)
  - Une instruction DGAL vers 2018 réserve aux bouchers et volaillers la cession au détail de SPAn **crus** (« os pour chien ») ; elle ne vise pas les friandises transformées ([instruction 2018-716](https://info.agriculture.gouv.fr/gedei/site/bo-agri/instruction-2018-716/telechargement)).
  - Un guide commercial affirme que « tout exploitant du secteur de l'alimentation animale, y compris les vendeurs en ligne, doit être enregistré ou agréé ». Ce n'est pas une source officielle ([L'union fait la friandise](https://lunionfaitlafriandise.fr/reglementation/)).
  - **Point non tranché** : une marque qui revend des nerfs déjà transformés et emballés doit-elle s'enregistrer au titre des SPAn ? **À faire confirmer par écrit par la DDPP.**
- **Droit de l'alimentation animale** (repris de `sourcing_jouet_lechage.md` et de `fr_deep_glandes_anales.md`) :
  - le **commerce de détail d'aliments pour animaux familiers est exclu** du règlement (CE) 183/2005 (art. 2, § 2, e), sous réserve de règles nationales ([EUR-Lex 183/2005](https://eur-lex.europa.eu/eli/reg/2005/183)) ;
  - la marque sous le nom de laquelle l'aliment est vendu est responsable de l'**étiquetage selon le règlement (CE) 767/2009** : français, composition, constituants analytiques, lot, fabricant ou numéro d'agrément ([legislation.gov.uk, 767/2009](https://www.legislation.gov.uk/eur/2009/767/chapter/1/data.pdf)) ;
  - formulaire de notification DD(ETS)PP ([agriculture.gouv.fr](https://agriculture.gouv.fr/telecharger/143976)) ;
  - **DGAL compétente pour l'enregistrement depuis le 01/09/2023** ([agriculture.gouv.fr](https://agriculture.gouv.fr/etablissements-agrees)).
- **TVA** : 20 % sur les aliments pour animaux de compagnie (BOFiP, repris de `fr_costs_regulation.md`).
- **Fournisseurs de nerfs : pistes trouvées** (aucun grossiste en marque blanche identifié dans l'UE) :
  - **en France ou dans l'UE, marques à revendre telles quelles** : Trixie (Allemagne), Bubimex (France), Nutrivet Inne (fabrication française), Vadigran (Belgique), Dailys, MultiFit (marque propre de Maxi Zoo, non revendable) ;
  - **intermédiaire** : Zoomici, qui « négocie directement avec les grossistes » européens, vendeur sur Zooplus ([comdewouf, synthèse](https://comdewouf.fr/?p=11702)) ;
  - **guide** : comdewouf.fr, mis à jour en mai 2026, sur les grossistes et la marque blanche, surtout pour les croquettes ([comdewouf](https://comdewouf.fr/?p=11702)) ;
  - **hors UE** : un exportateur britannique sur Freshdi (MOQ de **5 tonnes**) ([Freshdi](https://freshdi.com/product/Hot-Selling-Braided-Bully-Stick-Pizzle-Natural-Intestine-Carved-EcoFriendly-Dog-)) ; **Bully Bundles** (Chicago), vente en gros et « private label packaging » ([Pets+](https://petsplusmag.com/bully-bundles-release-new-wholesale-website/)) ; marques sur Faire : Chewer's Joy, Jojo Modern Pets, Mighty Paw, avec des origines en Thaïlande, aux USA et au Royaume-Uni (pizzle « grass-fed » britannique) ([Faire](https://www.faire.com/en-gb/product/p_arf8ffafaq)).

#### 3.5 Potentiel publicitaire : preuves US, accroches, engagement, rentabilité (deliverable 6)
- **Bow Wow Labs** :
  - comptes sur 6 réseaux (section 1.4) ;
  - une vidéo Amazon Live « Bow Wow Lab Bully Stick Holder for Dogs », VUES non relevées ([Amazon Live](https://www.amazon.com/live/video/0081418c25ac4ef0aef87c785c8ba8bd?ref_=dp_vse_rvc_0)) ;
  - **histoire fondatrice émotionnelle** : Finn, étouffement, urgences vétérinaires ([À propos](https://bowwowlabs.com/pages/about)) ;
  - arguments chiffrés d'entreprise : 5,5 millions de chiens par an ; « 4 out of 5 vets » ; « more than 1 million dogs seeing a vet each year for bully stick and chew incidents » (marketing des fiches Amazon) ; « number one safety device in the world » (communiqué de 2022).
  - **Abonnés, vues et likes : non trouvés.**
- **Bully Grip** :
  - une démonstration TikTok de @prouddogmomblog a suscité un article Cuteness, « Here's Where To Buy The Bully Stick Holder You've Seen On TikTok ». VUES non chiffrées, date non relevée ([Cuteness](https://cuteness.com/blog/content/dogs-notorious-for-chewing)) ;
  - histoire fondatrice : Tesla aux urgences ([Faire](https://www.faire.com/brand/b_5qrfxvey9d)).
- **Angle « danger »** : une vidéo TikTok de @reecelopez mettant en garde contre les « Trader Joe's Bully Chewers » a fait **plus de 168 900 vues** (VUES, Daily Dot, date non relevée). Elle porte sur la friandise, pas sur un support ([Daily Dot](https://dailydot.com/trader-joes-bully-sticks-for-dogs-warning)).
- **Contenus éditoriaux et d'affiliation US** : SheKnows, « amazon bully stick holder » ([SheKnows](https://www.sheknows.com/living/articles/1234879067/amazon-bully-stick-holder/)) ; Fido Friendly ; une lettre d'éducation canine « How to make sure your dog never swallows… » ([Substack](https://dogtraining.substack.com/p/how-to-make-sure-your-dog-never-swallows-195)).
- **Rentabilité** : **aucune donnée de ROAS ni de CPA trouvée.** Le seul indicateur est la **perte nette de 2023 (−20 % du CA)**, avec le marketing en tête de l'usage des fonds de la levée.

#### 3.6 Formulations d'allégations de sécurité
- **Allégations US à ne pas transposer** : « life-protecting », « vet-recommended », « 4 out of 5 veterinarians » (sondage commandité), statistiques US de 5,5 millions et 1 million, « number one safety device ».
- [CP] En France, toute allégation doit être prouvable ; sinon, risque de pratique commerciale trompeuse au sens du Code de la consommation.
- **Formulations prudentes proposées** (inférences de l'auteur, à valider par un juriste) :
  - « Tient le nerf de bœuf pendant que votre chien mâche : le dernier morceau reste dans le support. »
  - « Conçu pour aider à empêcher votre chien d'avaler le bout de son nerf de bœuf. »
  - « Moins de risque d'avaler un morceau trop gros, toujours sous votre surveillance. »
  - « Vous retirez le bout quand il a fini. »
- **Mentions d'avertissement en français** (GPSR, et miroir de la notice US « not a toy ») :
  - « À utiliser sous surveillance » ;
  - « Ce n'est pas un jouet : retirez le support à la fin de la mastication » ;
  - « Choisissez la taille selon le poids du chien et le diamètre du nerf » ;
  - « Inspectez le support avant chaque usage ; remplacez-le s'il est abîmé ».
- **À éviter** :
  - « anti-étouffement garanti », « 100 % sûr », « zéro risque », « sauve la vie de votre chien » ;
  - « recommandé par les vétérinaires », sans étude propre ;
  - « évite les occlusions » (allégation de santé) ;
  - des images de chien réellement en détresse.
  - Le mot « anti-étouffement » est très employé par les concurrents (PetClan, PetTribes). « Anti-avalement » ou « mastication sécurisée » sont des formulations moins absolues (inférence).

#### 3.7 Stratégie de panier et économie par commande (deliverable 7)
**Repères de prix et de modèle :**
- Bow Wow Labs vend des kits de 44,95 à 53,95 $, un abonnement aux bâtonnets (−30 % sur la première livraison, puis −10 %), des lots multi-chiens et le support seul de 28 à 38 $ (section 1.5).
- En France, Chewise est à environ 35,10 € et Fruugo entre 18 et 28 €.
- Repères de `fr_couts_commerciaux.md` : panier moyen en animalerie de 71 € (P40) ; réachat de 72 % (P42, définition non précisée).

**Contribution par commande** [calc]. Paramètres de `fr_couts_commerciaux.md` (valeurs centrales) et hypothèses [H] :

| Poste (€ HT) | A. Support seul, 29,90 € TTC | B. Kit support + 8 nerfs de 15 cm, 49,90 € | C. Duo 2 supports + 16 nerfs, 69,90 € | D. Recharge 12 nerfs en abonnement, 29,90 € −10 % = 26,91 € |
|---|---|---|---|---|
| Prix HT (TTC ÷ 1,2) | 24,92 | 41,58 | 58,25 | 22,43 |
| Produit : support rendu entrepôt 3,00 [H] ; nerf 0,60 pièce [H] | 3,00 | 7,80 | 15,60 | 7,20 |
| Port en point relais : ≤ 500 g 3,66 (P11) ; 1 kg 4,99 (P12) ; 2 kg 6,66 (P15) | 3,66 | 4,99 | 6,66 | 3,66 |
| 3PL : 1,75 + 0,50 par article en plus + 0,23 de stockage (P18, P19, P23) | 1,98 | 2,48 | 2,48 | 1,98 |
| Emballage (P24 [H]) | 0,35 | 0,45 | 0,60 | 0,30 |
| Encaissement, 2,4 % du TTC (P7) | 0,72 | 1,20 | 1,68 | 0,65 |
| Shopify et applications à 100 commandes par mois (P2 + P3) | 0,76 | 0,76 | 0,76 | 0,76 |
| Provision retours : 12 % × (produit + port + 3PL) (P38, méthode [H]) | 1,04 | 1,83 | 2,97 | 1,54 |
| **Contribution avant publicité** | **13,41 (54 %)** | **22,07 (53 %)** | **27,50 (47 %)** | **6,34 (28 %)** |
| **Après un CPA de 39,9 € (P35 central)** | **−26,49** | **−17,83** | **−12,40** | sans CPA si récurrent |
| CPA d'équilibre au premier achat | 13,4 € | 22,1 € | 27,5 € | — |

- **Panier nécessaire pour absorber 39,9 € de CPA** [calc] : avec une contribution de 50 % du HT, il faut un panier d'au moins 79,8 € HT, soit **environ 96 € TTC** (de 87 à 106 € TTC pour une contribution de 55 % à 45 %).
- **Retour sur investissement par l'abonnement** [calc] : avec une recharge à 6,34 €, il faut environ **2,8 recharges** pour combler la perte du kit B, et environ 2 pour le kit C. Le taux de rétention réel est inconnu.
- **Fourchettes des hypothèses** :
  - support rendu entrepôt de 1,8 à 4,5 € [H], à partir de 0,95–3,19 $ FOB, du fret P27, de 6,5 % de droits, de l'agent P25 et du transitaire P28 ;
  - nerf de 15 cm à l'achat de 0,40 à 1,00 € [H]. **Aucun prix de gros de nerfs n'a été trouvé** ; le repère de détail est d'environ 1,37 € la pièce (Trixie 12 cm par 8) et de 54 €/kg (MultiFit) ;
  - poids du support non relevé : Amazon US le dit « heavy enough that a smaller dog may not drag it around ».
- **Micro-entreprise en franchise de TVA** (repris de `fr_couts_commerciaux.md`) : la publicité Meta porte une TVA non déductible. Le CPA effectif monte alors à environ **47,9 €** [calc : 39,9 × 1,2].
- **Expédition simple** : support petit et léger ; nerfs séchés, stables à température ambiante, sans chaîne du froid (inférence). L'odeur impose des sachets fermés (inférence d'après les avis sur l'« odeur forte »).

### Inferences
- **Faisabilité opérationnelle : bonne.** Sourcing bon marché, échantillons faciles, logo standard, colis léger. Le support seul échappe au droit de l'alimentation animale.
- **Faisabilité réglementaire selon les paliers**, en reprenant l'échelle de `sourcing_jouet_lechage.md` :
  - **palier 0**, support seul : GPSR et avertissements, charge **faible** ;
  - **palier 1**, support plus revente de nerfs déjà étiquetés d'une marque de l'UE (Trixie, Bubimex, Nutrivet Inne, sous réserve de leur accord) : charge **faible à moyenne**, à confirmer avec la DDPP ;
  - **palier 2**, nerfs en marque propre fabriqués par un transformateur de l'UE agréé : étiquetage 767/2009, notification éventuelle, traçabilité, charge **moyenne** ;
  - **palier 3**, import direct de pizzles hors UE : établissement agréé, certificat sanitaire, contrôle frontalier, charge **forte, à éviter**.
- **Différenciation crédible et défendable par l'exécution, pas par la loi** :
  1. compatibilité **testée** avec les nerfs vendus en France (Trixie 12 et 30 cm, MultiFit, Nutrivet Inne), via un guide de diamètres et un kit de « nerfs calibrés », réponse directe à la 1re plainte US et aux avis français « trop fins » ;
  2. préhension renforcée : dents en métal, comme Chewise ;
  3. **base antidérapante**, réponse à la plainte de Dogster ;
  4. vis et bague de rechange, garantie de 2 ans ;
  5. tailles L et XL pour les grands chiens, cohérentes avec la clientèle de Pilou ;
  6. contenu et notice en français.
- **Économie** : **le premier achat ne paie pas un CPA de 40 €**, quelle que soit la composition plausible du panier. Le modèle ne tient que dans l'un des cas suivants :
  - un CPA réel nettement sous la valeur centrale. Il reste dans la fourchette P35 (14 € en bas), mais reste à prouver ;
  - un **kit à 50–70 €** combiné à un **abonnement de recharges** et à une rétention d'au moins 2 à 3 recharges ;
  - un lancement d'abord auprès de la **base clients Pilou** (e-mail, reciblage, encart dans les colis), dont le coût d'acquisition est bien inférieur à 40 € (inférence).
  - Même aux US, Bow Wow Labs, avec une marge brute de 51 % et un abonnement, perdait 20 % de son CA en 2023 : le modèle exige de la discipline sur le CPA.
- **Potentiel publicitaire : fort sur le fond, non prouvé en chiffres.**
  - Atouts : le problème se montre en un plan (le petit bout de nerf qui disparaît dans la gueule) ; la démonstration tient en 3 gestes (dévisser, insérer, visser) ; le format avant/après se prête à l'UGC ; l'émotion vient de vraies histoires de passage aux urgences.
  - Accroches à tester : « Le dernier morceau, c'est celui qui coince. » (tour précédent) ; « Votre chien gobe le bout de son nerf de bœuf ? » ; un guide des tailles par race ; le « défi du chien glouton ».
  - Limites : l'éducation au problème allonge le message au-delà de 3 secondes ; les visuels de détresse sont à proscrire [CP, règles publicitaires Meta].
- **Durabilité de la marque : moyenne.** Le support se copie facilement, mais la **marque « mastication sécurisée »** peut s'étendre : nerfs calibrés, autres friandises à mâcher compatibles, pièces de rechange, tailles. Le consommable récurrent est l'élément qui fait vivre le modèle US (section 1).

### Gaps
- **Prix des échantillons, frais de moule pour un design propre, devis avec logo, poids et dimensions du support : non relevés.** Les prix Alibaba viennent de la synthèse du moteur, sans URL par fournisseur sauf pour Hongzhou.
- **Prix de gros des nerfs dans l'UE et conditions des marques (Trixie, Bubimex, Nutrivet Inne) pour la revente en kit : non trouvés.**
- **Enregistrement SPAn ou alimentation animale d'une marque qui revend des nerfs emballés, ou les fait fabriquer sous son nom : non tranché, à demander à la DDPP.** La version consolidée EUR-Lex du règlement 142/2011 (art. 35, annexes XIII et XIV) n'a pas été relue ; seules des versions britanniques l'ont été.
- **Espacenet et EUIPO** (famille WO 2020/102719, dessins) : **non vérifié (accès impossible)**.
- **Engagement chiffré** (vues, likes, abonnés) de Bow Wow Labs, Bully Grip et Chewise ; publicités Meta et TikTok US et FR : **non vérifié (accès impossible)**.
- Coût d'une assurance responsabilité civile produit et de tests de sécurité (arrachement, usure) : non recherché.
- Taux de rétention d'un abonnement de friandises à mâcher : non sourcé.

#### Requêtes envisagées mais non lancées (quota de 45 atteint)
- `"Bow Wow Labs" Form C-AR 2025 EDGAR` (plein texte)
- `"pet treat holder and safety device" EP Espacenet Bow Wow Labs`
- `EUIPO design bully stick holder`
- `bully stick holder amazon.fr prix €` (prix des copies)
- `nerf de boeuf Google Trends France`
- `bully sticks import UE Brésil Colombie établissement agréé TRACES`
- `assurance responsabilité civile produit accessoire animal coût`
- `bully stick holder pull test safety standard`
- `Wamiz nerf de bœuf étouffement`
- `support os à mâcher chien` et `bâton de taureau support`

#### Journal des 45 requêtes (2026-10-28 ; mode « standard » sauf mention contraire)

| # | Requête (verbatim) | Domaines filtrés | Résultat principal |
|---|---|---|---|
| 1 | `"Bow Wow Labs" Form C-AR annual report SEC` | — | Aucun Form C-AR ; Form C/A du 26/04/2023 (CIK 1954010, Novato), émetteur non confirmé |
| 2 | `Bow Wow Labs 2025 news bully stick company` | — | Pet Supplies Plus (07/2025, environ 700 magasins) ; refonte 2024 ; Chewy 4,1/5 sur 198 |
| 3 | `Bow Wow Buddy bully stick holder patent` | — | US 10,015,951 et US 10,856,528 |
| 4 | `Bow Wow Buddy bully stick holder amazon.com ratings bought in past month` | — | Pas d'avis Amazon US ; Walmart 4,5/5 sur 13 ; shop.app 4,8/5 sur 29 ; Dogster (07/2026) |
| 5 | `Bow Wow Labs Wefunder net loss net income 2023 cost of goods sold` | — | RN 2023 −1 223 084 $ ; 2022 coût des ventes 2 641 833 $, RN −340 260 $ ; trésorerie 450 k$ |
| 6 | `Woolwine Hackett "pet treat holder" patent EP OR WO` | — | Aucun EP ni WO ; PDF USPTO 12317862 et 11997986 |
| 7 | `Bow Wow Labs Buddy Safety Device bully stick holder` | amazon.com | ASIN 2024 ; tailles ; « not a toy » ; compatibilité SafeFit |
| 8 | `bully stick holder reddit dog chewed through plastic worth it` | — | Pas de Reddit ; avis desertcart (extraction, usure) |
| 9 | `Bow Wow Labs Inc pet treat holder patents assignee list` | patents.justia.com, patents.google.com | US 12,317,863 B1 (2025) ; WO 2020/102719 (à vérifier) ; attributions douteuses |
| 10 | `"Bow Wow Labs" lawsuit OR infringement OR counterfeit bully stick holder copies` | — | Aucune action ; opposition TTAB BUSY BUDDY / BULLY BUDDY |
| 11 | `nerf de boeuf chien` | zooplus.fr | Au moins 5 références Zooplus |
| 12 | `nerf de boeuf chien prix avis` | maxizoo.fr, zoomalia.com, wanimo.com, animalis.com | Prix MultiFit, Trixie, nerf entier ; rien chez Wanimo |
| 13 | `chien a avalé morceau nerf de boeuf vétérinaire occlusion étouffement` | — | conseils-animaux.fr ; SantéVet |
| 14 | `wamiz OR "30 millions d'amis" friandise à mâcher chien étouffement surveiller dernier morceau` | — | PetsCare FR (« porte-bâton ») ; avis Zooplus |
| 15 | `Bully Stick Holder chien support anti-étouffement` | amazon.fr | Chewise à environ 35,10 € ; Bow Wow (4 ASIN) ; Bully Grip ; génériques |
| 16 | `bully stick holder chien support` | cdiscount.com, manomano.fr, fr.shopping.rakuten.com, fnac.com, temu.com, aliexpress.com | Temu et AliExpress seulement |
| 17 | `porte-friandise à mâcher chien empêche d'avaler le dernier morceau` | — | Aucun support |
| 18 | `bully stick holder alibaba nylon price MOQ custom logo` | — | Pas de fiche Alibaba ; repères de détail (19,99 $, 5,10 $, Bully Lok) |
| 19 | `Regulation 142/2011 Annex XIII dog chews requirements import pizzle` | — | Annexe XIV, ligne 12 ; annexe XIII, ch. II ; art. 35 |
| 20 | `Bow Wow Labs TikTok bully stick holder video views` | — | Pas de vues ; changement de nom en Bow Wow Buddy (2022) ; Cuteness et Bully Grip |
| 21 | `Bully Grip bully stick holder TikTok viral sales founder` | — | Vaso Karras ; Tesla aux urgences ; Amazon 4,2/5 sur 1 714 |
| 22 | `PetClan Chewise bully stick holder brand` | — | Origine Chine, 10/08/2024 ; environ 1 400 avis ; kit |
| 23 | `bully sticks pizzle wholesale supplier Europe private label dog chews` | — | Freshdi (Royaume-Uni, MOQ 5 t) ; Faire ; Bully Bundles (US) |
| 24 | `Regulation 142/2011 Article 3 end point petfood dog chews registration Article 23 distributor` | — | Définition des dog chews ; certificat 8325NFG ; art. 3 non renvoyé |
| 25 | `enregistrement SPAn opérateur distributeur friandises à mâcher chien sous-produits animaux article 23 règlement 1069/2009 commerce de détail exemption DDPP` (**extended**) | — | Enregistrement de tous les opérateurs SPAn ; agrément pour la fabrication de petfood ; DDPP |
| 26 | `"Bow Wow Labs" Inc. 5000 2025 OR 2026` | — | Rien pour 2025 ni 2026 ; communiqué 2024 « second year » |
| 27 | `Bow Wow Buddy review cons bully stick slipped out doesn't fit large dog` | — | WDJ « thick sticks » ; Dogster « slips on hardwood » ; L 3,7/5 sur 217 |
| 28 | `nerf de boeuf origine France friandise naturelle chien marque française` | — | Nutrivet Inne ; Truffaut « Origine France Garantie : Non » |
| 29 | `bully stick holder dog chew holder anti-choking factory` | alibaba.com, made-in-china.com, 1688.com, globalsources.com | 6 usines, 0,95–3,19 $, MOQ de 20 à 1 000 |
| 30 | `#bullystickholder TikTok views bully stick holder video` | — | Hors sujet |
| 31 | `Bow Wow Labs SafeFit bully sticks subscription subscribe save starter kit price` | — | Abonnement −30 % puis −10 % ; kits de 44,95 à 53,95 $ |
| 32 | `Bow Wow Labs revenue 2024 2025 employees estimate` | — | LeadIQ 10–25 M$ ; Prospeo 1,1 M$ ; Caplight 15 salariés |
| 33 | `Bow Wow Labs Buddy Safety Device Redesigned bully stick holder out of 5 stars ratings` | amazon.com | SafeFit 4,2/5 sur 1 311 ; avis sur la tenue ; questions-réponses sur la compatibilité |
| 34 | `"Bow Wow Labs" Instagram OR Facebook followers bully stick holder reel likes` | — | Comptes sociaux ; histoire de Finn ; pas d'abonnés |
| 35 | `bully stick holder European patent application EP chew holder safety device Espacenet` | — | Aucun EP ; Tall Tails, EverChew, ChewEasy |
| 36 | `"Woof" BullySafe bully stick holder brand Pupsicle` | — | Woof confirmé ; 19,99 $ ; boutique britannique wooof.co.uk |
| 37 | `porte-bâton à mâcher chien nerf de bœuf support sécurité acheter` | — | **PetTribes sur Zooplus.fr** ; echoduconsommateur (Chewise) |
| 38 | `bully stick c'est quoi chien nerf de boeuf pizzle` | — | Définitions ; Core77 ; retirer à 2,5–3 pouces |
| 39 | `Bow Wow Labs 2026 Bow Wow Buddy` | — | Aucune actualité 2026 |
| 40 | `Bow Wow Labs Wefunder 2024 campaign raise investors update` | — | Conditions de la campagne 2023 ; conflit de date de clôture (2023 ou 04/2024) |
| 41 | `"support bâton mordant" chien` | — | PetTribes sur Zooplus.fr |
| 42 | `PetTribes support bâton mordant chien prix avis` | zooplus.fr | Cordes PetTribes ; fiche du support non renvoyée |
| 43 | `nerf de boeuf grossiste fournisseur professionnel friandises chien marque blanche` | — | Aucun grossiste ; Zoomici ; Bubimex ; guide comdewouf |
| 44 | `bully stick holder TikTok viral "million views" dog choking video` | — | @reecelopez, plus de 168 900 vues (Trader Joe's) ; Bully Grip |
| 45 | `nerfs de bœuf chien à mâcher naturel évaluations note sur 5` | amazon.fr, zooplus.fr, zoomalia.com | 636, 106 et 90 avis selon les fiches |
