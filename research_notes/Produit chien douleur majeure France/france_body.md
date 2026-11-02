# Body de convalescence post-opératoire pour chien (alternative à la collerette) : marché français, sourcing et rentabilité pour Pilou

> **Note de méthode (relevé du 02/11/2026).**
> - **Budget et outils.**
>   - J'ai envoyé **18 requêtes WebSearch** en mode « standard », soit tout le budget. L'une d'elles (n° 4) a été **rejetée par l'outil** : le domaine idealo.fr n'est pas accessible au robot du moteur (« API Error: 400 … not accessible to our user agent »). Je la compte quand même dans le budget.
>   - J'ai fait **2 tentatives WebFetch sur les 2 autorisées**, et **les deux ont été refusées** (`getaddrinfo ENOTFOUND`) :
>     - ledenicheur.fr ;
>     - www.lacompagniedesanimaux.com.
>
>     Ces deux domaines doivent être **autorisés dans les paramètres réseau de la session** pour être lus. Les notes antérieures signalent le même refus pour asinsight.com et kimola.com.
>   - Je n'ai utilisé ni Bash ni curl.
>   - Le journal numéroté des requêtes est à la fin du document (fin de Q6).
> - **Nature des données.**
>   - Tout vient des **extraits et synthèses du moteur**, basé aux États-Unis. Aucune page marchande n'a été ouverte : les fiches Amazon, Zooplus, Maxi Zoo, Zoomalia, Cdiscount, ManoMano, La Compagnie des Animaux, Place des Vétos et ASINsight sont donc **« non vérifiées (accès impossible) »**.
>   - Le moteur rattache parfois un prix ou un avis à la mauvaise fiche ; je le signale quand c'est le cas (« rattachement non isolé »).
> - **Reprises.** Les faits marqués « (notes antérieures, `fichier`) » viennent de sept fichiers :
>   - `mobilite_senior_grands_chiens.md` (02/11/2026) ;
>   - `chien_confort_senior_premium.md` (28/10/2026) ;
>   - `fr_couts_commerciaux.md` et `fr_costs_regulation.md` (27/10/2026) ;
>   - `fr_douleurs_marche.md` ;
>   - `pub_jouet_lechage.md` et `fr_deep_jouet_lechage_congelable.md`.
>
>   Ils gardent leurs libellés et leurs dates d'origine, et leurs requêtes n'ont pas été relancées.
> - **Libellés.**
>   - [CA DÉCLARÉ] : CA annoncé par l'entreprise. [CA ESTIMÉ – outil] : CA estimé par un outil nommé.
>   - [UNITÉS] : badge Amazon « X+ bought in past month ». [UNITÉS ESTIMÉES – outil] : unités estimées par un outil nommé.
>   - [AVIS] : note et nombre d'avis. [VUES] : vues. [PRIX].
>   - [ÉTUDE] : enquête, étude, registre ou source vétérinaire.
>   - [ARTICLE] : contenu éditorial ; « commercial » s'il vient d'une marque, d'un revendeur, d'un assureur ou d'une clinique qui vend.
>   - [VERBATIM] : citation d'un propriétaire, dans sa langue d'origine.
>   - [H] : hypothèse ; [calc] : calcul.
>
>   Aucun type n'est converti en un autre. **Aucun CA déclaré ni estimé n'a été trouvé : CA non confirmé** pour toutes les marques.
> - **Dates.** Je donne la date de la source quand elle existe, sinon « n.d. ». Pour les pages marchandes, j'écris « capture n.d. ». **Historique** signale une donnée antérieure à 2024. Date d'observation : 02/11/2026.
> - **Âge des fiches et des vidéos.**
>   - L'âge d'une fiche Amazon est parfois déduit du préfixe de l'ASIN (B07… plus ancien que B0D…, B0F… ou B0G…). C'est une **hypothèse de faible confiance** [H].
>   - La date d'une vidéo TikTok est déduite de son identifiant (les 32 premiers bits codent l'heure de publication) [H].
> - **Taux de change.** 1 $ = 0,86 € [H], repris des notes antérieures sans nouvelle source.
> - **Meta Ads Library : non vérifié (accès impossible), à compléter par les captures du propriétaire.**

## Q1 — Le produit, le problème qu'il résout, l'acheteur et la taille du besoin en France (points 1 à 4 ; question ouverte 2)

### Takeaway
Le body de convalescence est un vêtement extensible qui couvre le thorax et l'abdomen pendant **7 à 14 jours** après une stérilisation, une castration ou une autre opération. Il empêche le chien de lécher sa plaie, **à la place de la collerette ou en complément**.

La douleur est **forte et très répandue** :
- 77,4 % des 434 propriétaires d'une étude voient la qualité de vie de l'animal baisser sous collerette (2020, historique) ;
- **57 % des chiens français sont stérilisés** (FACCO/Odoxa 2025, relayé par Virbac) ;
- cela représente de l'ordre de **400 000 à 500 000 stérilisations de chiens par an** [calc sur H].

Mais la douleur est **brève, liée à une date et à achat unique** : le produit ne remplit pas le critère du problème récurrent.

### Cited Findings

#### 1.1 Nom et description du produit
- **Noms observés en France** [PRIX, fiches, captures n.d.] : « body post-opératoire », « body de récupération », « combinaison de convalescence », « combinaison de récupération », « body postopératoire » (Kooa), « Recovery Suit » (Trovet), « Safety Body » (Flamingo), « Medical Pet Shirt », « Buster Body Suit Post-Chirurgie ». Sources : [Zooplus.fr, Kooa](https://www.zooplus.fr/shop/chiens/soins_tondeuses_chien/kooa/2099720) ; [Maxi Zoo FR, Trovet](https://www.maxizoo.fr/p/trovet-body-pour-chien-recovery-suit-noir-m-1272575/) ; [Zoomalia, Safety Body](https://www.zoomalia.com/animalerie/body-post-operatoire-safety-body-pour-chien-p-123012.html) ; [La Compagnie des Animaux, Buster](https://www.lacompagniedesanimaux.com/buster-body-suit-chien-m.html).
- **Matières** (fiches, captures n.d.) :
  - Trovet : 96 % coton et 4 % lycra, lavable en machine à 30 °C — [Maxi Zoo FR](https://www.maxizoo.fr/p/trovet-body-pour-chien-recovery-suit-noir-s-1272573/) ;
  - Buster : coton et élasthanne — [La Compagnie des Animaux](https://www.lacompagniedesanimaux.com/buster-body-suit-chien-l.html) ;
  - Medical Pet Shirt : lavable à 30 °C selon un distributeur français — [La Compagnie des Animaux](https://www.lacompagniedesanimaux.com/medical-pet-shirt-top-4in1-chien-s.html) ;
  - génériques Amazon.fr : du coton au polyester, extensibles et « respirants ». Un avis signale une forte odeur du tissu neuf, à laver avant le premier usage (paraphrase du moteur) — [Amazon.fr, Kuoser](https://www.amazon.fr/Kuoser-Body-chien-apr%C3%A8s-chirurgie/dp/B0C9QLGRRP).
- **Fermetures et coupes** :
  - pressions, zip dans le dos (Kooa) ou scratch ;
  - versions avec pattes arrière ou à manches longues ;
  - **découpe hygiène à tailler** soi-même. Une fiche Amazon.fr écrit [ARTICLE commercial] : « can be trimmed for male dogs to facilitate urination, while the oval near the tail can be trimmed for female dogs to facilitate excretion » — [Amazon.fr](https://www.amazon.fr/TYXHXTF-Combinaison-Recuperation-Operatoire-St%C3%A9Rilisation/dp/B0D415L74R) ;
  - sources : [Cdiscount](https://www.cdiscount.com/animalerie/combinaison-de-rcupration/f-162-aadvj56532.html) ; [ManoMano](https://www.manomano.fr/p/combinaison-de-convalescence-pour-chiens-body-chien-post-operatoire-femelle-male-body-pour-chien-avec-pattes-arriere-body-chien-anti-lechage-alternative-a-la-collerette-chien-90360042) ; [Zooplus.fr, Kooa mâle](https://www.zooplus.fr/shop/chiens/soins_tondeuses_chien/kooa/2100050).
- **Usages annoncés** : stérilisation ou castration, opération, blessure, problèmes de peau — [ManoMano](https://www.manomano.fr/p/combinaison-de-convalescence-pour-chiens-body-chien-post-operatoire-femelle-male-body-pour-chien-avec-pattes-arriere-body-chien-anti-lechage-alternative-a-la-collerette-chien-90360042) ; [La Compagnie des Animaux, Medical Pet Shirt](https://www.lacompagniedesanimaux.com/medical-pet-shirt-top-4in1-chien-l.html).
- **Durée de port** [ARTICLE] : collerette ou protection gardée « entre 10 et 14 jours après une chirurgie », et **7 à 10 jours** pour une stérilisation classique. Rattachement non isolé entre ces pages (dates n.d. sauf Comdewouf, mis à jour en 05/2026) : [synonyme-du-mot](https://www.synonyme-du-mot.com/les-articles/quand-enlever-la-collerette) ; [Comdewouf](https://comdewouf.fr/?p=21461) ; [SantéVet](https://www.santevet.com/?p=32814).

#### 1.2 Le problème : la collerette, et pourquoi il pousse à acheter
- **[ÉTUDE, 2020, HISTORIQUE] Shenoda, Ward, McKeegan et Fawcett, « The Cone of Shame » (*Animals*)** (notes antérieures, `mobilite_senior_grands_chiens.md`) :
  - **77,4 %** des 434 répondants rapportent une qualité de vie plus faible pendant le port de la collerette ;
  - **60,2 %** citent une difficulté à boire, **67,5 %** une incapacité à jouer ;
  - beaucoup de propriétaires hésitent à laisser la collerette ;
  - limites : enquête déclarative, chiens et chats, surtout en Australie.
  - Sources : [PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7070745/) ; [Université de Sydney, 13/03/2020](https://www.sydney.edu.au/news-opinion/news/2020/03/13/the-cone-of-shame-makes-pets-miserable.html).
- **[ARTICLE commercial] Prix d'une stérilisation en France (2026)**, repris des notes antérieures (`mobilite_senior_grands_chiens.md`) : de **130 à 500 €** selon le sexe et le poids — [Truffaut](https://www.truffaut.com/sterilisation-chienne-castration-chien.html) ; [Reassurez-moi](https://reassurez-moi.fr/guide/assurance-chien-chat/assurance-chien/castration-chien) ; [Lecomparateurassurance](https://www.lecomparateurassurance.com/assurance-animaux/guides-chien/frais-veterinaires/prix-operation-chien).
- **[ARTICLE] Contenus français (n.d. ; paraphrases du moteur)** :
  - un chien équipé ne doit pas sortir sans surveillance, car il pourrait s'accrocher ou se blesser ;
  - le choix de la protection relève du vétérinaire ;
  - une chienne a trouvé une technique pour enlever sa collerette, et un body peut alors servir (avis paraphrasé par le moteur).
  - Rattachement non isolé : [SantéVet](https://www.santevet.com/articles/collerette-pour-chien-et-chat-un-accessoire-encombrant) ; [La Compagnie des Animaux, conseil vétérinaire](https://www.lacompagniedesanimaux.com/conseil-veterinaire/quelle-collerette-choisir-pour-son-animal.html) ; [chien.com](https://www.chien.com/accessoires/collerette-pour-chien-choisir-utiliser-entretenir-19048.php).
- **Voix de propriétaires** :
  - [VERBATIM – contenu commercial] « Le cône de la honte ? C'est NON. Buddy a testé la collerette classique… et franchement, c'était un enfer 😩 ». Compte TikTok @labulleveto, vers le 25/06/2025 [H, date déduite de l'identifiant]. La vidéo **promeut un collier BiteNot** : « À choper direct sur le site de Mikan ou chez ton véto ! » — [TikTok](https://www.tiktok.com/@labulleveto/video/7519814217227062550) ;
  - [paraphrase du moteur, rattachement non isolé] une cliente a utilisé un body pour la stérilisation de sa chienne et le juge **beaucoup plus agréable que la « collerette vétérinaire »** — résultats de la requête 8 ;
  - [VERBATIM – fragments, Chewy, captures n.d.] (notes antérieures, `mobilite_senior_grands_chiens.md`) : « wished there was a potty hole in this thing » ; « didn't quite fit my boxer » ; « easy to get my dog in and out of and stayed in place » — [Chewy](https://www.chewy.com/suitical-recovery-suit-dogs/product-reviews/140861).
- **Inconvénients du body** cités par un contenu français [ARTICLE, n.d., rattachement non isolé entre ces deux pages] :
  - une odeur après plusieurs jours de port ;
  - le body doit être détaché pour que l'animal fasse ses besoins ;
  - il est plus cher qu'une collerette classique.
  - Sources : [Zoomalia, blog](https://www.zoomalia.com/blog/article/sterilisation-chien-chat-conseils-zoomalia.html) ; [SantéVet](https://www.santevet.com/?p=32814).

#### 1.3 Taille du besoin en France : stérilisations et autres opérations
- **[ÉTUDE, sondage déclaratif] FACCO/Odoxa 2025, relayé par Virbac** (document Virbac Info n° 175, n.d. ; « Facco-Odexa » dans l'extrait) :
  - la stérilisation touche **57 % des chiens** en France, contre 85 % des chats ;
  - le même document indique que la **WSAVA recommande depuis 2024 de ne plus stériliser systématiquement** ;
  - source : [Virbac, VBI 175](https://pro-fr.virbac.com/files/live/sites/virbac-b2b-fr/files/ressources/Virbac%20Info/vbi-175-sterilisation-chien.pdf).
- [ARTICLE commercial] Petscare : « près de 60 % » des chiens stérilisés en France en 2024. **Rattachement incertain** : l'URL remontée porte sur les chiens au Royaume-Uni — [Petscare](https://www.petscare.com/fr/news/post/how-many-pet-dogs-uk).
- **[ÉTUDE, HISTORIQUE]** Enquêtes plus anciennes : **40 %** de chiens stérilisés (FACCO/Sofres, année non précisée), ou **42,4 % des chiennes** et 21,6 % des mâles (publication non précisée). Rattachement non isolé entre des propositions de loi des 11e et 12e législatures (1997–2007) et une thèse vétérinaire de Toulouse — [Assemblée nationale](https://www.assemblee-nationale.fr/11/pdf/propositions/pion2770.pdf) ; [Assemblée nationale](https://www.assemblee-nationale.fr/12/pdf/propositions/pion0287.pdf) ; [ENVT](https://archivet.envt.fr/oatao.univ-toulouse.fr/2029/1/picco_2029.pdf).
- [ÉTUDE, 2020, HISTORIQUE] Ipsos pour Royal Canin : les chats sont « bien plus stérilisés que les chiens ». Le pourcentage canin n'est pas lisible dans l'extrait — [Ipsos](https://www.ipsos.com/sites/default/files/ct/news/documents/2020-06/enquete_royal-canin-030620_v26.pdf).
- **Population canine** (notes antérieures, `fr_douleurs_marche.md`) :
  - [ÉTUDE, registre] **713 812 nouvelles identifications de chiens en 2024** (I-CAD, communiqué de juin 2025) — [I-CAD, copie Fondation Brigitte Bardot](https://www.fondationbrigittebardot.fr/wp-content/uploads/2025/06/CP_Le-Fichier-National-I-CAD-presente-ledition-2025-du-barometre-de-lidentification-des-chiens-et-des-chats-en-France.pdf) ;
  - [ARTICLE] environ **9,7 à 9,9 M de chiens** (sources secondaires citant FACCO et I-CAD, 2024–2025) — [statistiques.com](https://www.statistiques.com/divers/chiens) ; [Planète Grandes Écoles](https://www.planetegrandesecoles.com/?p=127526) ;
  - [ÉTUDE, sondage] selon leurs maîtres, **12 % des chiens ne sont pas identifiés** (FACCO/Odoxa 2025) — [FACCO 2025](https://www.facco.fr/wp-content/uploads/2025/06/2025-06-facco-chiffres-odoxa.pdf) ;
  - [ÉTUDE, registre] le berger australien est la 1re race identifiée en 2025 (31 633), le golden retriever la 4e (I-CAD, 01/2026) — [I-CAD](https://www.i-cad.fr/uploads/CP_Chiens_Chats_preferes_2025.pdf).
- **Nombre annuel d'autres opérations sur des chiens en France** (tumeurs, orthopédie, peau, abdomen) : **non trouvé**.

#### 1.4 Indices sur l'acheteur
- Selon des avis Maxi Zoo sur Trovet (paraphrase du moteur, nombre et note des avis non relevés, captures n.d.) :
  - le body **doit être enfilé avant l'opération**, ce qui peut être difficile ;
  - la taille doit être choisie avec soin, car certains chiens l'ont trouvé trop petit.
  - Source : [Maxi Zoo FR](https://www.maxizoo.fr/p/trovet-body-pour-chien-recovery-suit-noir-xxl-1272579/).
- Kooa est vendu en **deux versions, chienne et mâle** — [Zooplus.fr, chiennes](https://www.zooplus.fr/shop/chiens/soins_tondeuses_chien/kooa/2099720) ; [Zooplus.fr, mâle](https://www.zooplus.fr/shop/chiens/soins_tondeuses_chien/kooa/2100050).
- **Âge moyen à la stérilisation et profil sociodémographique des acheteurs : non trouvés.**

### Inferences
- **Volume annuel de stérilisations de chiens en France** [calc sur H] :
  - **méthode 1 (cohorte)** : 713 812 identifications × 57 % ≈ **406 900 stérilisations par an**. Hypothèses [H] : chaque cohorte est stérilisée au même taux que le parc, une seule fois dans la vie. Les 12 % de chiens non identifiés rendent ce chiffre plutôt prudent ;
  - **méthode 2 (stock)** : 9,7–9,9 M × 57 % = 5,53–5,64 M de chiens stérilisés. Divisés par une durée de vie de 11 à 13 ans [H], cela donne environ **425 000 à 513 000 par an** ;
  - **ordre de grandeur retenu : 0,4 à 0,5 M de stérilisations par an**, hors autres opérations (non trouvées). La répartition par sexe n'est connue que par une donnée historique : 42,4 % des chiennes contre 21,6 % des mâles stérilisés. Or ce sont les femelles qui subissent une chirurgie abdominale, le cas d'usage principal du body.
- **Marché adressable des bodies** [calc sur H] : si 5 %, 10 % ou 20 % des stérilisations s'accompagnent d'un body [H, aucun taux trouvé], cela fait environ **20 300, 40 700 ou 81 400 bodies par an** (base 406 873), tous vendeurs confondus. À 20 € TTC en moyenne [H], cela représente **0,4 à 1,6 M€ TTC par an** pour tout le marché français. **C'est un petit marché.**
- **Pourquoi la douleur déclenche un achat** [H] :
  - elle est visible et émotionnelle : le chien se cogne, boit mal, ne joue plus (60,2 % et 67,5 %) ;
  - elle est **datée** : l'opération est programmée, et l'achat a lieu avant le jour J ;
  - le budget est déjà engagé : 130 à 500 € d'opération. Un body à 20–30 € représente de 4 % (20 € sur 500 €) à 23 % (30 € sur 130 €) du prix de l'opération [calc] ;
  - le body se compare à un produit gratuit ou peu cher (la collerette remise par la clinique [H]), et il est jugé « plus cher » qu'elle.
- **Profil acheteur probable** [H] :
  - propriétaire d'une **chienne** dont la stérilisation est programmée dans 1 à 4 semaines, souvent un premier chien, qui redoute la collerette ;
  - ou propriétaire d'un chien qui vient d'être opéré et qui supporte mal la collerette, ou qui l'enlève ;
  - il achète en ligne, sur conseil ou avec l'accord du vétérinaire.
  - **Pour Pilou**, le sous-segment pertinent est celui des **grands chiens jeunes à sous-poil** (berger australien, golden) en tailles L à XXL, chez qui la collerette est la plus encombrante [H].
- **Récurrence** : l'achat est **unique** par opération. L'animal ne se fait stériliser qu'une fois, et le port dure 7 à 14 jours. Les autres usages (peau, plaie) prolongent un peu la vie du produit, sans données [H].

### Gaps
- **Nombre annuel d'opérations autres que la stérilisation** chez le chien en France : non trouvé.
- **Taux d'équipement** (part des opérations suivies d'un achat de body) : non trouvé ; d'où les scénarios [H].
- **Répartition récente des stérilisations par sexe**, **âge à l'opération** et méthodologie FACCO/Odoxa 2025 : non vérifiées. Le communiqué FACCO primaire n'a pas été lu ; facco.fr est inaccessible selon les notes antérieures.
- **Effet de la recommandation WSAVA de 2024** sur le nombre de stérilisations en France : non mesuré.
- **Volumes de recherche** français (« body chien stérilisation », « alternative collerette ») : non mesurés, Google Trends n'étant pas accessible.

## Q2 — Preuves de demande aux États-Unis, marques, boutiques et signaux publicitaires (points 5 à 7)

### Takeaway
La demande américaine porte sur des **ventes réelles et régulières**, pas sur de la viralité :
- [UNITÉS ESTIMÉES – ASINsight, 04/2026] l'ASIN en tête du mot-clé « surgery suit for dogs » dépasse **4 000 commandes en avril 2026** ;
- [UNITÉS] le body Kuoser affiche le badge **900+** sur Amazon.com, et une étiquette « 1,000+ » avec **16 643 notes** relayée par ASINsight ;
- [AVIS] Suitical cumule **18 068 notes Amazon** (via un miroir) et 2 910 chez Chewy ;
- le produit est distribué chez Target, Walmart et Chewy.

**L'attribution de la fiche à plus de 4 000 commandes reste contradictoire** : Supet selon le titre du rapport, Kuoser en tête du tableau selon la capture antérieure. Le ticket est bas : 27–37 $ pour Suitical, la marque de référence ; la plupart des fiches sont entre 20 et 50 $.

### Cited Findings

#### 2.1 Vérification du chiffre « plus de 4 000 commandes » : quel outil, quelle fiche
- **Outil : ASINsight**, rapport « **Best Selling Surgery Suit For Dogs 2026 (#1: Supet)** », marché Amazon.com (États-Unis) — [ASINsight](https://www.asinsight.com/report/US/surgery-suit-for-dogs).
- **Méthode, citée par le moteur** : « This list compiles the monthly sales and rankings of all ASINs that appeared within the first three pages of search results for the keyword "surgery suit for dogs" on Amazon.com in the United States, totaling 128 products. Under this keyword, the top-ranked ASIN recorded more than 4,000 orders in April. » [UNITÉS ESTIMÉES – ASINsight, données d'avril 2026].
- **Même page** : un body Kuoser pour chien porte une étiquette de volume « **1,000+** », vraisemblablement le badge Amazon reproduit par l'outil, et **16 643 notes** [UNITÉS – badge relayé par ASINsight ; AVIS : nombre de notes, note moyenne non relevée].
- **Capture antérieure** (notes antérieures, `mobilite_senior_grands_chiens.md`, même rapport) :
  - le tableau plaçait **un body Kuoser en tête**, alors que le titre annonce Supet ;
  - **BellyGuard 800+ par mois**, **Lukovee environ 400** [UNITÉS ESTIMÉES – ASINsight, 04/2026] ;
  - « la plupart entre 20 et 50 $ » ;
  - une mention « 309 ASIN, 59,31 % » incohérente avec 128 produits.
- **Dates** : les captures du moteur portent tantôt sur avril, tantôt sur juin ou juillet 2026.
- **Conclusion de la vérification** : le chiffre de plus de 4 000 commandes est une **estimation ASINsight pour avril 2026**, attachée au 1er ASIN du mot-clé. **La marque de cet ASIN n'est pas isolée** (Supet ou Kuoser) et la page n'a pas pu être ouverte.

#### 2.2 Badges Amazon.com [UNITÉS, captures n.d.]
- **Kuoser** Recovery Suit for Dogs and Cats (spay et neuter, « cone alternative ») : **900+ bought in past month**, le plus haut badge relevé.
- **SlowTon** Dog Surgery Recovery Suit (zip, ceinture réglable, gris) : **100+**.
- Kuoser Dog Surgery Recovery Suit XL : 100+. **Rattachement du badge incertain.**
- Kuoser Dog Recovery Suit with Rear Leg Sleeve : 50+.
- Autres fiches présentes, sans badge lisible dans l'extrait :
  - Suitical ;
  - **Surgi Snuggly**, B07FF7XWTJ, vers 2018 [H] ;
  - BellyGuard ;
  - **Pupcovery**, B0GSJH3KG4, vers 2026 [H], donc un **nouvel entrant** ;
  - « Dog Recovery Suit After Surgery », B0CSCQLTX9.
- Sources : [Amazon, recherche Suitical](https://www.amazon.com/suitical-recovery-suit-dogs/s?k=suitical+recovery+suit+for+dogs) ; [Amazon, « dog surgical suit »](https://www.amazon.com/dog-surgical-suit/s?k=dog+surgical+suit) ; [Amazon, « dog surgical recovery suit »](https://us.amazon.com/dog-surgical-recovery-suit/s?k=dog+surgical+recovery+suit) ; [Amazon, « post-surgery recovery suits »](https://www.amazon.com/post-surgery-recovery-suits-dogs/s?k=post-surgery+recovery+suits+for+dogs) ; [Amazon, « with legs »](https://www.amazon.com/dog-recovery-suit-legs/s?k=dog+recovery+suit+with+legs) ; [Amazon, « back legs »](https://www.amazon.com/dog-recovery-suit-back-legs/s?k=dog+recovery+suit+back+legs) ; [Surgi Snuggly](https://www.amazon.com/SurgiSnuggly-Dog-Surgical-Recovery-Suit-for-Female-Spay-or-Male-Dogs-Neuters/dp/B07FF7XWTJ) ; [Pupcovery](https://www.amazon.com/Pupcovery-Recovery-Suit-After-Surgery/dp/B0GSJH3KG4) ; [B0CSCQLTX9](https://www.amazon.com/Dog-Recovery-Suit-After-Surgery/dp/B0CSCQLTX9).
- **Substitut** [UNITÉS ESTIMÉES – ASINsight, captures de 06–07/2026] : les **collerettes gonflables Supet** sont estimées à environ **5 000 unités par mois** dans un classement et à 6 000–8 000 dans d'autres. Ce sont des collerettes, pas des bodies — [ASINsight](https://www.asinsight.com/report/US/inflatable-dog-cone-collar) ; [ASINsight](https://www.asinsight.com/report/US/inflatable-cone-collar-for-dogs) ; [ASINsight](https://www.asinsight.com/report/US/inflatable-e-collar-for-dogs).

#### 2.3 Avis, prix et classements
- **[AVIS] Suitical** (notes antérieures, `mobilite_senior_grands_chiens.md`, captures n.d.) :
  - **4,5/5 sur 2 910 notes** chez Chewy ;
  - **4,4/5 sur 18 068** pour Amazon, via un miroir desertcart ;
  - Recovery Sleeve : 4,2/5 sur 773 notes chez Chewy.
  - Sources : [Chewy](https://www.chewy.com/suitical-recovery-suit-dogs/product-reviews/140861) ; [desertcart](https://www.desertcart.ni/products/17220713).
  - Analyses Fakespot de 2021 et 2022 (HISTORIQUE) : la fiche existe au moins depuis 2021 — [Fakespot](https://www.fakespot.com/product/suitical-recovery-dog-suit-small-black).
- **[PRIX] Suitical aux États-Unis** (captures n.d.) :
  - Chewy : XX-Small Blue Camo à **34,64 $** (−1 %), Black Medium à **29,59 $** (−15 %) — [Chewy XXS](https://www.chewy.com/suitical-recovery-suit-dogs/dp/140869) ; [Chewy M](https://www.chewy.com/suitical-recovery-suit-dogs/dp/140879) ;
  - Petfood Express : **27,00–31,00 $**, avec une offre « Buy 3, Get the 4th Free » — [Petfood Express](https://www.petfood.express/products/suitical-recovery-suit-for-dogs.html) ;
  - Walmart : environ 31–35 $ selon la taille — [Walmart](https://www.walmart.com/ip/391189000) ;
  - boutique Canine Styles : **65,00 $** en « regular price » — [Canine Styles](https://www.caninestyles.com/products/suitical-recovery-suit-for-dogs) ;
  - autres revendeurs (Bluebarn, Bunnings) dans une fourchette d'environ 30 à 65 $ — [Bluebarn](https://www.bluebarn.shop/product/suitical-recovery-suit-for-dogs-black/) ; [Bunnings, manchon](https://www.bunnings.com.au/suitical-recovery-sleeve-dog_p0675745) ;
  - une fiche desertcart.us à 1 107,08 $ est une erreur manifeste, écartée.
- **Repère britannique** (notes antérieures) : Suitical Recovery Shirt à **21,00 £** chez Chelsea Dogs — [Chelsea Dogs](https://www.chelseadogs.com/suitical-recovery-shirt-for-dogs).
- **[ARTICLE, 2026, possiblement affilié]** :
  - iHeartDogs, « Dog Surgical Recovery Suits: Veterinary Clinic Testing Results (2026) » : Suitical arrive 3e — [iHeartDogs](https://iheartdogs.com/?p=3858695) ;
  - une autre liste de 2026 classe Suitical « Best Alternative » (« Review count: 18,000 ») et BellyGuard en « premium pick ». Rattachement probable à un site de comparatifs de faible fiabilité — [product-review-usa](https://product-review-usa.pages.dev/surgical-recovery-suit-for-dogs.html).

#### 2.4 Marques américaines ou vendues aux États-Unis, boutiques et signaux publicitaires
| Marque | Origine | Prix US [PRIX] | Meilleure preuve typée | Boutiques et liens vus | Signaux publicitaires |
|---|---|---|---|---|---|
| **Suitical** | Suitical International BV, Pays-Bas — [Global Pet Industry](https://globalpetindustry.com/company/suitical-international-bv/) | 27–37 $ ; 65 $ en boutique | [AVIS] 18 068 (miroir Amazon), 2 910 (Chewy) | [Chewy](https://www.chewy.com/suitical-recovery-suit-dogs/dp/140885), [Walmart](https://www.walmart.com/ip/401201735), [Petfood Express](https://www.petfood.express/products/suitical-recovery-suit-for-dogs.html), manchons et double manchons ([Chewy](https://www.chewy.com/suitical-recovery-double-sleeves-dog/dp/855342)). Site de marque : non remonté | Promotion revendeur « 3 + 1 offert ». Meta non vérifié |
| **Kuoser** | Vendeur Amazon, origine non trouvée | Non relevé | [UNITÉS] 900+ ; « 1,000+ » et 16 643 notes (ASINsight) | Amazon.com ; aussi [Amazon.fr](https://www.amazon.fr/Kuoser-Body-chien-apr%C3%A8s-chirurgie/dp/B0C9QLGRRP) | Non vérifié |
| **Supet** | Non trouvée | Non relevé | Titre « #1 : Supet » du rapport ASINsight ; ses collerettes gonflables sont estimées à 5 000–8 000 par mois | Amazon.com | Non vérifié |
| **BellyGuard** | Non trouvée | Non relevé | [UNITÉS ESTIMÉES – ASINsight, 04/2026] 800+ par mois (notes antérieures) ; « premium pick » d'une liste de 2026 | Amazon.com | Non vérifié |
| **Lukovee** | Non trouvée | Non relevé | [UNITÉS ESTIMÉES – ASINsight, 04/2026] environ 400 par mois (notes antérieures) | Amazon.com | Non vérifié |
| **SlowTon** | Non trouvée | Non relevé | [UNITÉS] 100+ | Amazon.com | Non vérifié |
| **Surgi Snuggly** | Non trouvée | Non relevé | Fiche B07FF7XWTJ (vers 2018 [H]) | [Amazon](https://www.amazon.com/SurgiSnuggly-Dog-Surgical-Recovery-Suit-for-Female-Spay-or-Male-Dogs-Neuters/dp/B07FF7XWTJ) | Non vérifié |
| **Pupcovery** | Non trouvée | Non relevé | Fiche B0GSJH3KG4 (vers 2026 [H]) | [Amazon](https://www.amazon.com/Pupcovery-Recovery-Suit-After-Surgery/dp/B0GSJH3KG4) | Non vérifié |
| **Medical Pet Shirt** (MPS) | Medical Pet Shirts International et Europe, Pays-Bas ; le fabricant dit concevoir et fabriquer ses vêtements avec des vétérinaires | Non relevé | Distribution vétérinaire : catalogue Penn Vet, réf. MPS110 « Protective Pet Shirt Dog Small length 43cm » — [Penn Vet](https://www.pennvet.com/customer/portal/catalog/home/productdetail/mps110/protective+pet+shirt+dog+small+length-43cm) | Manuel de sécurité et de garantie, 06/2025 — [MPS](https://a.storyblok.com/f/317820/x/71962a74b2/safety-and-warranty-manual-pet-owner-mps-protective-top-shirt-june-2025-v02.pdf) ; page Fear Free — [Fear Free](https://www.fearfree.com/?p=5431) | **Marketing B2B vétérinaire** : exposant à BVA Live (Royaume-Uni) et à la Wild West Veterinary Conference (États-Unis), et probablement au Tierärztekongress (Allemagne ; rattachement de la page non isolé) — [BVA Live](https://bvalive.vetshow.com/exhibitors/medical-pet-shirts-europe), [Wild West](https://wildwest.vetshow.com/exhibitors/medical-pet-shirts-international), [Tierärztekongress](https://www.tieraerztekongress.de/exhibitors-products/product/tieraerztekongress/1216/615). Meta non vérifié |
| **Wowwoo** | Non trouvée | **Non trouvé** | **Non trouvé** (requête 14) | Non trouvé | Non vérifié |
| « Recovery Suit Black » (Target) | Non trouvée | Non relevé | Présence en grande surface (notes antérieures) | [Target](https://www.target.com/p/recovery-suit-black/-/A-93181349) | Non vérifié |

- **Meta Ads Library : non vérifié (accès impossible), à compléter par les captures du propriétaire.**
- **TikTok** : aucune requête ne visait les publicités américaines (budget). Aucune publicité TikTok d'une marque américaine de body n'a donc été observée (non vérifié).

### Inferences
- **Ventes et non viralité.** Les signaux sont des **volumes mensuels** (estimation ASINsight, badges Amazon) sur des fiches présentes depuis des années :
  - Suitical depuis au moins 2021 ;
  - Surgi Snuggly vers 2018 [H] ;
  - plusieurs marques indépendantes ;
  - une distribution en grande surface.
  
  Cela correspond à une **catégorie installée**.
- **Le volume est capté par des génériques Amazon à petit prix** (Kuoser, Supet), avec Suitical comme marque de référence à 27–37 $. **Aucune marque US ne vend un body haut de gamme en volume**, sauf la boutique Canine Styles à 65 $, sans preuve de volume.
- **Le substitut le plus vendu est la collerette gonflable** (Supet, 5 000–8 000 par mois estimées), au-dessus du meilleur body (plus de 4 000). La concurrence ne vient donc pas que des bodies [H].
- **De nouveaux entrants arrivent encore** (Pupcovery en B0G… [H]) : la catégorie reste attractive pour les vendeurs, donc probablement concurrentielle en prix [H].
- **Medical Pet Shirt prouve qu'on peut construire une marque par le canal vétérinaire** : salons professionnels et distributeurs. C'est un modèle B2B différent du DTC de Pilou [H].

### Gaps
- **Tableau ASINsight complet** (marque et ASIN du 1er, prix, avis) : non lu, car la page est inaccessible. **L'attribution Supet ou Kuoser reste contradictoire.**
- **Prix** de Kuoser, Supet, BellyGuard, Lukovee, SlowTon et Medical Pet Shirt aux États-Unis : non relevés.
- **Wowwoo** : aucun résultat (prix, avis, boutique).
- **Sites de marque** (Suitical, Kuoser, BellyGuard) et **date de fondation** : non trouvés. CA déclaré ou estimé : **non trouvé**.
- **Publicités de longue durée** (Meta, TikTok) : non vérifiées.

## Q3 — Concurrence en France et rôle du canal vétérinaire (point 8 ; questions ouvertes 1 et 3)

### Takeaway
**L'offre française est déjà dense.** Dix-huit requêtes ont permis de relever **au moins 26 offres** dans **au moins 10 canaux** :
- marketplaces : Amazon.fr, Cdiscount, ManoMano, Rue du Commerce ;
- enseignes spécialisées : Zooplus, Maxi Zoo, Zoomalia, La Compagnie des Animaux ;
- canal vétérinaire : Place des Vétos ;
- comparateur : leDénicheur.

L'**ancrage de prix est bas** :
- génériques à 11–26 € ;
- **marque propre Zooplus Kooa dès 12,99 €** ;
- Medical Pet Shirt à 21–27,60 € ;
- Trovet à 29–31 € ;
- Flamingo de 17,99 à 54,99 € selon la taille.

**Aucune marque française** ne porte ce produit, et aucune boutique DTC française dédiée n'a été trouvée. Les vendeurs sont des marques européennes à positionnement vétérinaire (Medical Pet Shirt, Buster/Kruuse, Trovet), Flamingo, une marque d'enseigne (Kooa) et des génériques de marketplace.

**Niveau : forte en présence et en prix, faible en marketing de marque.** Le canal vétérinaire **ne bloque pas** la vente directe, puisque le produit se vend sans ordonnance partout. Mais le **vétérinaire prescrit** la protection et remet en général la collerette.

### Cited Findings

#### 3.1 Tableau des concurrents français (captures n.d. ; prix TTC lus dans les extraits du moteur)
| # | Canal | Offre (marque) | Prix [PRIX] | Qualité de l'offre et remarques | Source |
|---|---|---|---|---|---|
| 1 | Zooplus.fr (enseigne) | **Kooa**, « Body postopératoire kooa pour chiennes » ; marque propre de zooplus SE (Munich) | **Dès 12,99 €** | Version femelle ; page d'avis avec filtre par étoiles, nombre d'avis non relevé | [Zooplus.fr](https://www.zooplus.fr/shop/chiens/soins_tondeuses_chien/kooa/2099720) ; [avis](https://www.zooplus.fr/feedback/shop/chiens/soins_tondeuses_chien/kooa/2099720?stars=3) |
| 2 | Zooplus.fr | **Kooa**, « Body postopératoire kooa pour chien mâle » | **Dès 13,79 €** ; 10,34 € pour le S dans les données structurées (incohérent) | Zip dans le dos, matière respirante ; **au moins 5 pages d'avis** (URL ?page=5), nombre non relevé | [Zooplus.fr](https://www.zooplus.fr/shop/chiens/soins_tondeuses_chien/kooa/2100050) ; [avis p. 5](https://www.zooplus.fr/feedback/shop/chiens/soins_tondeuses_chien/kooa/2100050?page=5) |
| 3 | Maxi Zoo France (enseigne) | **Trovet** Recovery Suit noir | **Environ 29–31 €** selon la taille ; certaines tailles en rupture | **10 tailles** (XXXS, XXS, XS, S, S-M, M, M-L, L, XL, XXL). « Alternative professionnelle à la collerette », 96 % coton. Avis : taille délicate, enfilage avant l'opération | [Maxi Zoo M](https://www.maxizoo.fr/p/trovet-body-pour-chien-recovery-suit-noir-m-1272575/) ; [XL](https://www.maxizoo.fr/p/trovet-body-pour-chien-recovery-suit-noir-xl-1272578/) ; [XXXS](https://www.maxizoo.fr/p/trovet-body-pour-chien-recovery-suit-noir-xxxs-1272570/) |
| 4 | Zoomalia (enseigne) | **Flamingo** « Body post opératoire Safety Body pour chien » | **17,99 €** (26 cm) à **54,99 €** (68×76 cm) | Tailles en longueur de dos ; seule offre au-dessus de 50 €, en très grande taille | [Zoomalia](https://www.zoomalia.com/animalerie/body-post-operatoire-safety-body-pour-chien-p-123012.html) |
| 5–6 | La Compagnie des Animaux (e-commerçant spécialisé) | **Medical Pet Shirt** (Pays-Bas), classé en « collerette chien » : modèle classique et Top 4in1 (2 offres) | **21,11 € (S), 23,48 € (M), 24,23 € (XL), 22,98 € (XXL), 21,20 € (XXXS, XXS)** (notes antérieures) ; **Top 4in1 S à 27,60 €** (nouveau relevé) | Top 4in1 en XXS à XL, S pour un poitrail de 48–68 cm ; article maison « On a testé » | [catégorie](https://www.lacompagniedesanimaux.com/chien/accessoires-chien/collerette-chien.html?page=3) ; [Top 4in1 S](https://www.lacompagniedesanimaux.com/medical-pet-shirt-top-4in1-chien-s.html) ; [test](https://www.lacompagniedesanimaux.com/conseil-veterinaire/on-a-teste-le-gilet-medical-pet-shirt.html) |
| 7 | La Compagnie des Animaux | **Buster Body Suit Post-Chirurgie** (Buster est une marque Kruuse, fournisseur vétérinaire danois [H]) | **Non trouvé** | Tailles S, M, L ; coton et élasthanne | [S](https://www.lacompagniedesanimaux.com/buster-body-suit-chien-s.html) ; [M](https://www.lacompagniedesanimaux.com/buster-body-suit-chien-m.html) ; [L](https://www.lacompagniedesanimaux.com/buster-body-suit-chien-l.html) |
| 8 | **Place des Vétos** (plateforme des boutiques en ligne de cliniques vétérinaires [H]) | « Gilet Pet Shirt pour chien », probablement Medical Pet Shirt [H] | **Non trouvé** | Preuve de présence dans le canal vétérinaire en ligne | [Place des Vétos](https://www.placedesvetos.fr/p/2928-2920-gilet-pet-shirt-pour-chien) |
| 9–18 | **Amazon.fr** | **Au moins 10 fiches** : TYXHXTF, Cyponpy, HEYWEAN, **Kuoser**, Hjumarayan, KONVINIT, et 4 fiches sans marque lisible (body femelle 4–9 kg, manchon de pattes arrière, body à manches longues, « Post-operative Dog Bodysuit ») | **Environ 11 à 26 €** selon la marque (rattachement prix-fiche non isolé) | Titres traduits de l'anglais ou en anglais ; découpes hygiène à tailler ; badges et nombres d'avis non visibles. ASIN de B09G… à B0FS…, soit de 2021 à 2025 [H] | [TYXHXTF](https://www.amazon.fr/TYXHXTF-Combinaison-Recuperation-Operatoire-St%C3%A9Rilisation/dp/B0D415L74R) ; [femelle 4–9 kg](https://www.amazon.fr/Combinaison-convalescence-chirurgicale-protection-anti-l%C3%A9chage/dp/B0FCY7QKWF) ; [manchon](https://www.amazon.fr/Operatoire-St%C3%A9rilisation-V%C3%AAtement-Chirurgie-R%C3%A9cup%C3%A9ration/dp/B0FDQTTVW8) ; [Cyponpy](https://www.amazon.fr/Cyponpy-Operatoire-Combinaison-Sterilisation-Recuperation/dp/B0F892W7Z1) ; [manches longues](https://www.amazon.fr/chirurgie-protection-op%C3%A9ration-r%C3%A9cup%C3%A9ration-combinaison/dp/B0FSD5XS6J) ; [Bodysuit](https://www.amazon.fr/Body-Chien-Post-Op%C3%A9ratoire-St%C3%A9rilisation-D%C3%A9guisement/dp/B0CH77CBZF) ; [HEYWEAN](https://www.amazon.fr/HEYWEAN-St%C3%A9rilisation-Combinaison-Recuperation-Alternatives/dp/B0DHW4CBT3) ; [Kuoser](https://www.amazon.fr/Kuoser-Body-chien-apr%C3%A8s-chirurgie/dp/B0C9QLGRRP) ; [Hjumarayan](https://www.amazon.fr/Hjumarayan-Body-Chien-R%C3%A9cup%C3%A9ration-Chirurgicale/dp/B09GK73YSL) ; [KONVINIT](https://www.amazon.fr/KONVINIT-St%C3%A9rilisation-Convalescence-%C3%89lectronique-Anti-l%C3%A9chage/dp/B0CJBX7HYP) |
| 19–21 | **Cdiscount** | Au moins 3 fiches : combinaison à manches longues et zip ; **lot de 2** Aucunely (bleu M) ; VGEBY. Plus des pages de recherche dédiées | **Environ 11 € à plus de 25 €** (Cdiscount et ManoMano confondus), avec « de nombreuses offres en promotion » | Le lot de 2 existe déjà | [zip](https://www.cdiscount.com/animalerie/combinaison-de-rcupration/f-162-aadvj56532.html) ; [lot de 2](https://www.cdiscount.com/animalerie/combinaison-rcupration-chien/f-162-aacya44185.html) ; [VGEBY](https://www.cdiscount.com/animalerie/vgeby-combinaison-de-recuperation-pour-chien-chien/f-162-vge1693354949933.html) ; [recherche](https://www.cdiscount.com/animalerie/r-combinaison+recuperation+chiens.html) ; [anti-léchage](https://www.cdiscount.com/animalerie/r-combinaison+anti+lechage+chien.html) |
| 22–24 | **ManoMano** | Au moins 3 fiches : combinaison avec pattes arrière ; body coton « Dos 30 cm » pour petits chiens jusqu'à environ 13 kg ; « costume de récupération » bleu | Même fourchette (voir ligne précédente) | Une annonce mélange l'anglais et le français | [pattes](https://www.manomano.fr/p/combinaison-de-convalescence-pour-chiens-body-chien-post-operatoire-femelle-male-body-pour-chien-avec-pattes-arriere-body-chien-anti-lechage-alternative-a-la-collerette-chien-90360042) ; [Dos 30 cm](https://www.manomano.fr/p/body-chien-post-operatoire-dos-30-cm-combinaison-de-recuperation-anti-lechage-vetement-chien-coton-confortable-alternative-collerette-pour-petits-chiens-jaune-miel-l-223986948) ; [bleu](https://www.manomano.fr/p/combinaison-de-recuperation-pour-chien-apres-la-chirurgie-chiot-plaies-abdominales-vetements-postoperatoires-cone-e-collar-substitut-gilet-de-protection-pour-animaux-de-compagnie-modele-bleu-xx-large-38709970) |
| 25–26 | **Rue du Commerce** | Body « INF » ; personne responsable : DRAGON ECOM INTERNATIONAL LIMITED | Non relevé | Vendeur étranger, aucune origine française | [fiche 1](https://www.rueducommerce.fr/p/m26079730346.html) ; [fiche 2](https://www.rueducommerce.fr/p/m26079730455.html) |
| — | **leDénicheur** (comparateur, non compté comme offre) | Pages « body chien » et « body pour chien » | **Environ 10 € à plus de 40 €** selon le modèle et la taille | Modèles mâle et femelle, zip ou scratch, avec pattes ou manches longues | [body pour chien](https://ledenicheur.fr/s/body-pour-chien/) ; [body chien](https://ledenicheur.fr/s/body-chien/) |

#### 3.2 Canaux vérifiés sans résultat, ou inaccessibles
- **Wanimo, Animalis, Truffaut, Jardiland, Botanic** : présents dans le filtre de la requête 2, mais **aucun résultat remonté**. Ce n'est pas un constat d'absence.
- **Fnac, Rakuten, Kaufland** : présents dans le filtre de la requête 3, **aucun résultat remonté**.
- **idealo.fr** : refusé par le moteur (requête 4). **Google Shopping** : non accessible.
- **Pharmacies en ligne** :
  - Pharma-GDD vend des **collerettes**, dont les codes EAN commencent par 5703188 (préfixe danois, compatible avec Kruuse [H]). **Aucun body n'y est remonté** — [Pharma-GDD](https://www.pharma-gdd.com/fr/collerette-chien-chat?code=5703188232984) ;
  - **Suitical en pharmacie vétérinaire française : non trouvé** (requête 6). La requête n'a remonté que des revendeurs étrangers (Chewy, desertcart, Bunnings, Bluebarn, Canine Styles). Les notes antérieures situaient Suitical chez un grossiste vétérinaire **britannique** (VetUK).

#### 3.3 Canal vétérinaire et pharmacie : prescripteur ou barrière ?
- **La collerette reste la protection standard en France**, et le choix revient au vétérinaire. Selon des sources françaises [ARTICLE, n.d.], les alternatives (body médical, collerette gonflable) se font « uniquement sur avis du vétérinaire », car elles ont aussi leurs limites. Un vétérinaire peut recommander une collerette si le chien atteint les sutures au-dessus de la combinaison. Rattachement non isolé : [SantéVet](https://www.santevet.com/articles/collerette-pour-chien-et-chat-un-accessoire-encombrant) ; [La Compagnie des Animaux](https://www.lacompagniedesanimaux.com/conseil-veterinaire/quelle-collerette-choisir-pour-son-animal.html) ; [Zoomalia, blog](https://www.zoomalia.com/blog/article/sterilisation-chien-chat-conseils-zoomalia.html).
- **[ARTICLE commercial] Cliniques sur TikTok** :
  - Clinique vétérinaire d'Isneauville (76) : « Après une opération, le body aide à protéger la plaie, mais une collerette peut être nécessaire pour éviter que votre animal ne se lèche. » Vidéo vers le 06/01/2025 [H, date déduite de l'identifiant] — [TikTok](https://www.tiktok.com/@clinicvet_veterinaire/video/7456828359805242646) ;
  - Sevetys (groupe de cliniques vétérinaires [H]) : « Body ou Collerette pour Chien : Quel est le Meilleur Choix ». Vidéo vers le 15/02/2023 [H, date déduite de l'identifiant], donc HISTORIQUE — [TikTok](https://www.tiktok.com/@sevetys/video/7200392132388048133).
- **Marques à positionnement vétérinaire déjà présentes en France** :
  - Medical Pet Shirt, que le fabricant dit concevoir et fabriquer avec des vétérinaires, vendu chez La Compagnie des Animaux et sur Place des Vétos ;
  - Buster (Kruuse) ;
  - Trovet, « alternative professionnelle ».
  - Notes antérieures : Kruuse Rehab chez le grossiste vétérinaire Alcyon — [Alcyon](https://www.test.alcyon.acsone.eu/p/rehab-protege-coude-l-gauche-10006829).
- **Pas d'ordonnance requise** : le produit est en libre-service aux États-Unis (Target, Walmart, Chewy ; notes antérieures) comme en France (Zooplus, Maxi Zoo, Zoomalia, Amazon.fr).
- **[ARTICLE commercial] La Compagnie des Animaux, « On a testé : Le gilet Medical Pet Shirt »** (n.d.) : le chien n'a pas pu retirer le gilet grâce à sa fermeture arrière, et le test le recommande après une opération — [La Compagnie des Animaux](https://www.lacompagniedesanimaux.com/conseil-veterinaire/on-a-teste-le-gilet-medical-pet-shirt.html).
- **Non trouvés** :
  - la collerette est-elle incluse dans le prix de la stérilisation ?
  - prix d'un body vendu en clinique ;
  - part des cliniques qui vendent des bodies.

#### 3.4 Marques françaises et boutiques Shopify
- **Aucune marque française trouvée** (requête 7, « marque française », et requête 8, phrase de problème). Origine des marques remontées :
  - Kooa : fabricant indiqué zooplus SE, Munich ;
  - Buster : Kruuse ;
  - INF : DRAGON ECOM INTERNATIONAL LIMITED ;
  - Safety Body : Flamingo ;
  - Medical Pet Shirt : Pays-Bas.
  - Sources : [Zooplus.fr](https://www.zooplus.fr/shop/chiens/soins_tondeuses_chien/kooa/2099720) ; [Rue du Commerce](https://www.rueducommerce.fr/p/m26079730346.html) ; [Zoomalia](https://www.zoomalia.com/animalerie/body-post-operatoire-safety-body-pour-chien-p-123012.html).
- **Aucune boutique Shopify française dédiée** n'est remontée dans les requêtes 7 et 8 (ce n'est pas une preuve d'absence).
- **Marque propre d'enseigne** : Kooa chez Zooplus. Zolia (Zoomalia) n'est **pas** remontée sur ce produit.

#### 3.5 TikTok France
- Les contenus remontés sont **vétérinaires ou commerciaux** : Sevetys, la clinique d'Isneauville, et @labulleveto pour le collier BiteNot vendu par Mikan.
  - On trouve aussi une page « Chien Collerette Occupation » — [TikTok](https://www.tiktok.com/discover/chien-collerette-occupation).
  - Les autres résultats concernent les chats ou sont hispanophones, et sont écartés.
- **[VUES] : non relevées** (non visibles dans les extraits).
- **Aucune marque de body** ne fait de publicité sur TikTok en France dans les résultats (non vérifié dans le Creative Center).

#### 3.6 Meta
- **Meta Ads Library : non vérifié (accès impossible), à compléter par les captures du propriétaire.**

### Inferences
- **Nombre de concurrents** [calc] : 26 offres repérées (8 en enseignes ou canal vétérinaire, 18 sur des marketplaces), pour au moins 6 marques européennes ou d'enseigne et au moins 8 marques génériques. C'est un **minimum** : Amazon.fr n'a été vu qu'à travers une requête, et les autres enseignes ne sont pas remontées.
- **Niveau de concurrence : forte** (présence et prix), avec un **marketing de marque faible** :
  - le produit est rangé dans les rayons « collerette » ou « soins » ;
  - les fiches génériques sont traduites ;
  - aucune page de marque française, aucun récit de marque, aucun site DTC n'a été trouvé.
  
  L'**espace « marque »** est libre. L'**espace « prix »** ne l'est pas : Kooa à 12,99 €.
- **Ancrage de prix** [calc] :
  - médiane approximative des prix unitaires relevés : 20–25 € ;
  - plancher : 10–13 € ;
  - au-dessus de 30 €, on ne trouve que Flamingo en très grande taille (54,99 € en 68×76 cm) et le haut de la fourchette leDénicheur (« plus de 40 € »).
- **Le canal vétérinaire ne bloque pas la vente directe, il la conditionne** [H] :
  1. le vétérinaire décide de la protection et remet probablement la collerette le jour de l'opération (l'avis client parle de « collerette vétérinaire ») ;
  2. l'acheteur doit avoir le body **avant le jour J**, et le vétérinaire ou le propriétaire l'enfile (avis Trovet) ;
  3. des marques à positionnement vétérinaire (Medical Pet Shirt, Kruuse) sont déjà vendues par les cliniques ou leurs boutiques en ligne (Place des Vétos), et captent une partie de la demande au comptoir.
  
  Une marque DTC doit donc parler le langage du vétérinaire (« à utiliser sur avis de votre vétérinaire ») et toucher l'acheteur 1 à 4 semaines avant l'opération [H].
- **Les cliniques produisent déjà du contenu TikTok** sur « body ou collerette ». Le sujet intéresse, mais la parole d'autorité appartient aux vétérinaires [H].

### Gaps
- **Amazon.fr** : badges « achetés au cours du mois », nombre d'avis et vendeurs réels : non vus (pages non ouvertes).
- **Prix et avis non relevés** : nombre d'avis Kooa, prix Buster, prix Place des Vétos, prix ManoMano par fiche.
- **Enseignes non remontées** (Wanimo, Animalis, Truffaut, Jardiland, Botanic), et Fnac, Rakuten, Kaufland : présence non confirmée.
- **Pratique des cliniques** : collerette incluse ou non dans le prix de l'opération ; prix et part des bodies vendus en clinique : **non trouvés**.
- **Publicités** Meta et TikTok en France : non vérifiées.

## Q4 — Sourcing, dropshipping, tailles, qualité et risque de retour (points 10 et 11 ; question ouverte 4)

### Takeaway
Le produit est **léger, plat et très bon marché à la source** :
- **2,70–2,90 $ dès 2 pièces** sur Alibaba (Shenzhen Zhongce) ;
- **4,56–4,87 $ à partir de 500 pièces** pour un modèle en coton (Guangzhou Voyager).

En dropshipping, le **coût rendu est d'environ 15 € par body** (de 12 à 19 €) et d'environ **19,50 € pour un lot de 2** [calc]. Ces montants incluent les 3 € de droit UE et les 2 € de frais de traitement ; la ligne de transport reste une hypothèse.

Les freins sont les suivants :
- **aucun body n'a été trouvé chez CJ Dropshipping** (trois requêtes au total) ;
- aucun entrepôt UE n'a été trouvé ;
- le délai Chine–France de 6 à 14 jours convient mal à un besoin **daté** ;
- il faut **6 à 10 tailles** et des versions mâle et femelle ;
- un body porté sur une plaie n'est pas revendable.

### Cited Findings
- **Alibaba** [PRIX, captures n.d. ; rattachement exact de chaque prix à sa page non isolé] :
  - Shenzhen Zhongce, « Clothes Anti Licking Post Surgical Pet Dog Surgery Recovery Suit » : **MOQ de 2 pièces**, **2,70–2,90 $** ;
  - USMILEPET, combinaison : MOQ de 50 pièces, prix non relevé ;
  - Guangzhou Voyager, body en coton : **MOQ de 500 pièces**, **4,56–4,87 $** ;
  - Kunshan Zhongru : 0,29–0,79 $ pour un MOQ de 1 000 pièces, **produit non confirmé** ;
  - gammes proposées : bodies anti-léchage, manchons de pattes avant ou arrière, coton ou polyester ;
  - sources : [Alibaba, recovery suit dogs surgery](https://www.alibaba.com/wholesale/recovery-suit-dogs-surgery.html) ; [Alibaba, dog surgical suit](https://www.alibaba.com/wholesale/dog-surgical-suit.html) ; [Alibaba, recovery suit legs](https://www.alibaba.com/wholesale/dog-recovery-suit-legs.html) ; [Alibaba, neuter surgical suit](https://www.alibaba.com/wholesale/dog-neuter-surgical-suit.html) ; [Alibaba, showroom](https://www.alibaba.com/showroom/dog-recovery-suit.html) ; [Kunshan Zhongru](https://zhongrugifts.en.alibaba.com/).
- **AliExpress** (notes antérieures, `mobilite_senior_grands_chiens.md`) :
  - plusieurs fiches, dont un body 100 % coton pour plaies abdominales et des versions mâle et femelle ;
  - **prix non fiables** (texte généré par IA) ;
  - port de **7 à 10 jours** ;
  - taille mesurée à la poitrine et au cou, avec deux doigts de jeu.
  - Sources : [AliExpress](https://www.aliexpress.us/item/3256804934720518.html) ; [AliExpress](https://www.aliexpress.com/w/wholesale-dog-recovery-suit-after-neutering.html).
- **CJ Dropshipping** : **aucun body** dans la requête 16 de ce relevé ni dans les requêtes 21 et 22 des notes antérieures. Seuls des articles de blog sur le dropshipping animalier sont remontés — [CJ, blog](https://blog.cjdropshipping.com/detail/Top-10-Profitable-Pet-Dropshipping-Products). **Non trouvé.**
- **1688 et entrepôts UE** : **non cherchés et non trouvés** (budget).
- **Lignes et délais** (notes antérieures, `fr_couts_commerciaux.md`) :
  - CJPacket « Euro Ordinary » vers la France : **6 à 14 jours** [S2] ;
  - **aucun prix de ligne 2026 trouvé** ; repères [H] de 4,50 / 6,50 / 8,00 € par colis de 0,2 à 0,5 kg.
- **Droits** (notes antérieures, `fr_costs_regulation.md` et `fr_couts_commerciaux.md`) :
  - droit forfaitaire UE de **3 € par article distinct** (sous-position tarifaire) sur les envois de 150 € ou moins, du 01/07/2026 au 01/07/2028. **Cinq t-shirts identiques ne paient qu'un droit** (exemple de la Commission) ;
  - **frais de traitement UE de 2 € par article** à partir du **01/11/2026**, annoncés par l'administration irlandaise le 29/09/2026. La publication au Journal officiel n'est pas vérifiée, et le sens de l'« article » (unité ou ligne tarifaire) reste ouvert.
- **Agent de sourcing** (notes antérieures) : commission de **3 / 7,5 / 15 %** du coût produit [S2].
- **Tailles et variantes** [PRIX, fiches, captures n.d.] :
  - Trovet : **10 tailles** — [Maxi Zoo FR](https://www.maxizoo.fr/p/trovet-body-pour-chien-recovery-suit-noir-s-m-1272574/) ;
  - Medical Pet Shirt : au moins 6 tailles de XXXS à XXL (notes antérieures), et Top 4in1 en XXS à XL (S pour un poitrail de 48–68 cm). Une fiche indique « Labrador L : 67–76 cm » (notes antérieures) ;
  - Flamingo : de 26 cm à 68×76 cm ;
  - Kooa : versions mâle et femelle ;
  - génériques : choix au tour de poitrine et au poids, de XS à XXL ; certains modèles sont réservés aux petits chiens, jusqu'à environ 13 kg ;
  - les revendeurs conseillent **d'en avoir deux pour en laver un** (notes antérieures) — [desertcart](https://www.desertcart.nz/products/11558948-suitical-recovery-suit-for-dogs-spay-and-neutering-dog-surgery).
- **Signaux qualité** :
  - odeur forte du tissu neuf (avis Amazon.fr, paraphrase) ;
  - odeur après plusieurs jours de port (article français) ;
  - pressions difficiles à manipuler, guide des tailles décalé (avis Chewy sur Suitical, notes antérieures) ;
  - modèles trop petits (avis Maxi Zoo sur Trovet).
- **Poids et dimensions emballés** : **non trouvés.**

### Inferences
- **Coût rendu par commande en dropshipping** (le fournisseur expédie au client, port et droits inclus). Tous les montants sont en € [calc], les entrées sont marquées.

| Poste | Body seul : bas | Body seul : central | Body seul : haut | Lot de 2 : bas | Lot de 2 : central | Lot de 2 : haut |
|---|---|---|---|---|---|---|
| Produit [H, d'après les prix Alibaba de 2,70–4,87 $] | 2,50 | 3,50 | 5,50 (tissu premium, zip ou ouverture hygiène [H]) | 5,00 | 7,00 | 11,00 |
| Commission d'agent (3 / 7,5 / 15 %) [S2 ; calc] | 0,08 | 0,26 | 0,83 | 0,15 | 0,53 | 1,65 |
| Ligne Chine–France [H] | 4,50 | 6,50 | 8,00 | 5,00 | 7,00 | 8,50 |
| Droit UE de 3 € (un seul pour des articles identiques) [S] | 3,00 | 3,00 | 3,00 | 3,00 | 3,00 | 3,00 |
| Frais de traitement UE de 2 € [S, sous réserve] | 2,00 | 2,00 | 2,00 | 2,00 | 2,00 | 4,00 (si dû par unité) |
| **Coût rendu par commande** [calc] | **12,08** | **15,26** | **19,33** | **15,15** | **19,53** | **28,15** |

  - Taux de change de 1 $ = 0,86 € [H]. En lot de 2, la ligne est majorée de 0,50 € [H] pour le poids.
  - Emballage inclus dans le prix fournisseur [H]. Poids [H] : 80–200 g par body, colis plat de moins de 300 g, donc dans la tranche postale la moins chère.
- **Faisabilité du dropshipping** :
  - **oui techniquement** : MOQ dès 2 pièces, produit léger, agent qui expédie au client ;
  - **mais le calendrier est risqué** : un client qui commande 5 jours avant l'opération ne sera pas livré à temps avec 6 à 14 jours de transit [H].
  
  Il faut au minimum afficher le délai et pousser l'achat tôt (« commandez 2 semaines avant »). L'idéal serait un **stock UE chez l'agent** ou une ligne express, ce qui n'a pas été trouvé.
- **Complexité des références** [calc] : 10 tailles × 2 versions (mâle, femelle) = 20 références par coloris. Avec 2 coloris, on atteint 40 références. Le dropshipping évite le stock, mais pas les erreurs de taille.
- **Risque de retour et de remboursement** (décrit, non chiffré dans la marge) :
  1. **La taille est le premier motif** dans toutes les sources (Suitical, Trovet, génériques).
  2. **Un body porté sur une plaie n'est pas revendable** [H], et le retour vers la Chine n'est pas rentable (notes antérieures). Chaque retour coûte donc environ le coût rendu complet.
  3. **Un retard de livraison** après l'opération rend le produit inutile : demande de remboursement ou litige « non reçu à temps » [H].
  4. **Le vétérinaire peut imposer la collerette** malgré le body (clinique d'Isneauville).
  5. Repère : le taux de retour central de l'animalerie est de **12 %** (Wisepim, 07/05/2026 ; notes antérieures). Il est probablement plus élevé pour un textile à tailles [H].
  
  La parade est l'**échange de taille avant usage**, au client de prouver que le body n'a pas été porté [H], plus un guide en 3 mesures (cou, poitrail, dos).
- **Qualité** : il faut des **échantillons** de 3 fournisseurs au moins [H], pour tester l'odeur, les coutures, le zip ou les pressions et l'ouverture hygiène. Il faut aussi des rapports REACH (colorants azoïques, NPE) pour un textile en contact prolongé avec la peau (notes antérieures, `fr_costs_regulation.md`).

### Gaps
- **Prix de lignes Chine–France** pour 0,2–0,5 kg, et inclusion réelle des 3 € et 2 € dans le prix de l'agent : non trouvés. C'est à demander au **sourcing agent de Pilou**.
- **Entrepôts UE** (CJ, agents) proposant ce produit : non trouvés. **1688** : non cherché.
- **Poids et dimensions** réels : non trouvés.
- **Classement tarifaire** : la position 4201 00 00 (« manteaux pour chiens », 2,7 % en import de stock, notes antérieures) est probable [H], à confirmer par un RTC.

## Q5 — Prix de vente recommandé, marge et moyens de vendre au-dessus de 30 € (points 9 et 12 ; question ouverte 5)

### Takeaway
**Prix recommandé** [H] :
- **un lot de 2 bodies à 39,99 € TTC**, soit environ 20 € l'unité, au niveau de Medical Pet Shirt ;
- un **body seul à 24,99–29,99 € TTC** selon la taille.

**Marges** [calc] :
- body seul à 29,99 € : marge brute d'environ **9,73 € HT** et **contribution avant publicité d'environ 9,03 €** ;
- lot de 2 à 39,99 € : **13,80 € HT** de marge brute et **12,95 €** de contribution.

Ce sont aussi les **coûts par achat de point mort** : environ **9 à 13 €**, contre **80 à 97 €** de coût par achat récent chez Pilou et environ 40 € de CPA central de référence (notes antérieures). **Aucune formule ne rend le produit rentable en acquisition Meta froide.** Le lot de 2 est la seule manière crédible de passer 30 € ; le kit de convalescence relève le panier mais ajoute des droits en dropshipping.

### Cited Findings
- **Ancrages français** (voir Q3) :
  - Kooa dès 12,99 € ;
  - génériques Amazon.fr à 11–26 € ;
  - Cdiscount et ManoMano de 11 € à plus de 25 € ;
  - Flamingo de 17,99 à 54,99 € ;
  - Medical Pet Shirt de 21,11 à 27,60 € ;
  - Trovet de 29 à 31 € ;
  - leDénicheur de 10 € à plus de 40 €.
- **Ancrages américains** : Suitical de 27 à 37 $, et 65 $ chez Canine Styles. Catégorie « la plupart entre 20 et 50 $ » (ASINsight, notes antérieures).
- **Lots** :
  - un **lot de 2** existe déjà sur Cdiscount (Aucunely) — [Cdiscount](https://www.cdiscount.com/animalerie/combinaison-rcupration-chien/f-162-aacya44185.html) ;
  - Petfood Express propose « Buy 3, Get the 4th Free » sur Suitical — [Petfood Express](https://www.petfood.express/products/suitical-recovery-suit-for-dogs.html).
- **Produits complémentaires d'un kit** :
  - manchons Suitical (Recovery Sleeve, 4,2/5 sur 773 notes ; double manchons) — [Chewy](https://www.chewy.com/suitical-recovery-double-sleeves-dog/dp/855342) ;
  - collerettes gonflables (Supet, 5 000–8 000 par mois estimées) ;
  - jouets à lécher pour le repos postopératoire, avec la collection « Post Surgery » de SodaPup et l'histoire d'origine de la Pupsicle de Woof (notes antérieures, `pub_jouet_lechage.md`) — [SodaPup](https://sodapup.com/collections/post-surgery).
- **Paramètres de calcul** (notes antérieures, `fr_couts_commerciaux.md` et `fr_costs_regulation.md`) :
  - TVA de 20 % (HT = TTC ÷ 1,2) ;
  - frais de paiement de **1,5 % + 0,25 €** (Shopify Payments, carte standard, Basic ; relevé Kanal du 07/10/2026) ;
  - CPA Meta central de référence : environ 39,9 € [calc des notes antérieures].
- **Contexte Pilou** (consigne) : coût par achat Meta récent d'environ 80 à 97 € sur la brosse à 39,99 €.

### Inferences
**Calcul de marge** [calc] : prix HT = TTC ÷ 1,2 ; frais = 1,5 % du TTC + 0,25 € ; marge brute HT = prix HT − coût rendu ; contribution = marge brute − frais ; CPA de point mort = contribution.

| Poste | Body seul à 29,99 € : bas | Body seul : central | Body seul : haut | Lot de 2 à 39,99 € : bas | Lot de 2 : central | Lot de 2 : haut |
|---|---|---|---|---|---|---|
| Prix HT [calc] | 24,99 | 24,99 | 24,99 | 33,33 | 33,33 | 33,33 |
| Coût rendu (Q4) [calc] | 12,08 | 15,26 | 19,33 | 15,15 | 19,53 | 28,15 |
| **Marge brute HT** [calc] | **12,91** | **9,73** | **5,66** | **18,18** | **13,80** | **5,18** |
| Frais de paiement [calc] | 0,70 | 0,70 | 0,70 | 0,85 | 0,85 | 0,85 |
| **Contribution avant publicité = CPA de point mort** [calc] | **12,21** | **9,03** | **4,96** | **17,33** | **12,95** | **4,33** |
| ROAS de point mort (TTC ÷ contribution) [calc] | 2,46 | 3,32 | 6,05 | 2,31 | 3,09 | 9,24 |

- **Sensibilité** [calc] : si les frais de 2 € sont dus **par unité**, le lot de 2 central passe à 21,53 € de coût rendu, 11,80 € de marge brute et 10,95 € de contribution.
- **Kit de convalescence à 49,99 € TTC** (2 bodies et 1 accessoire, manchon ou collerette gonflable), à titre d'illustration [calc sur H] :
  - prix HT de 41,66 € et frais de 1,00 € ;
  - coût rendu : bodies 7,00 €, accessoire 3,00 € [H], agent 0,75 €, ligne 7,50 € [H], droits et frais de 7,00 à 10,00 € selon que l'accessoire tombe dans la même sous-position que les bodies ou non [H]. Total de **25,25 à 28,25 €** ;
  - marge brute de **13,41 à 16,41 €** et contribution de **12,41 à 15,41 €**.
  
  En dropshipping, **chaque article distinct ajoute 3 € et 2 € de droits et frais**. Le kit ne rapporte donc guère plus que le lot de 2. Il faut garder les composants dans la même position tarifaire si possible (à vérifier).
- **Vendre au-dessus de 30 € : les trois pistes**
  1. **Lot de 2 à 39,99 €** : justifié par l'usage (laver un body pendant qu'on porte l'autre, odeur après quelques jours). L'unité revient à environ 20 €, au niveau de Medical Pet Shirt. C'est la **meilleure piste**, mais elle existe déjà sur Cdiscount, à un prix non relevé.
  2. **Tissu premium** (coton bio, bambou, antibactérien) [H] : **aucune preuve** de disposition à payer en France. Seuls Trovet (29–31 €, coton et lycra), Flamingo en très grande taille (54,99 €) et Canine Styles (65 $) dépassent 30 €. C'est à réserver aux **grandes tailles** (L à XXL), cohérentes avec l'audience grands chiens de Pilou [H].
  3. **Kit de convalescence** : il relève le panier (49,99 €), mais pas la marge unitaire, à cause des droits par article. Il s'enrichit surtout de contenu sans coût (guide « J−7 avant la stérilisation », vidéo d'enfilage) [H].
- **Rentabilité** [calc] : même le scénario bas du lot (17,33 €) reste **à environ un cinquième** du coût par achat Pilou de 80–97 €, et sous le CPA central de référence de 39,9 €. Après une publicité à 40 €, la contribution du lot central est de **−27,05 €**. **Le produit n'est pas un produit d'acquisition payante.** Il peut servir de vente croisée ou de complément de panier pour des clients déjà acquis, ou être testé en organique (TikTok, partenariats vétérinaires) [H].

### Gaps
- **Prix du lot de 2 sur Cdiscount** et prix des lots chez les autres vendeurs : non relevés.
- **Prix fournisseur d'un manchon ou d'une collerette gonflable** (pour le kit) : non cherché [H].
- **Coûts fixes** (Shopify, applications, REP, retours) : exclus du calcul, comme demandé. **Les remboursements ne sont pas inclus** (voir le risque en Q4).
- **Taux de conversion d'un produit à 30–40 €** sur l'audience de Pilou : inconnu.

## Q6 — Différenciation, potentiel créatif, risques et notes provisoires (points 13 à 15)

### Takeaway
La **différenciation possible** n'est pas technique, car tout existe déjà : versions mâle et femelle, zip, 10 tailles, lot de 2. Elle passe par :
- **le service** : guide de taille, échange gratuit avant usage, délai affiché ;
- **le contenu** : guide vétérinaire, « J−7 » ;
- **le focus grands chiens**.

Le **potentiel créatif est fort** : un avant/après collerette contre body, une démo d'enfilage, l'accroche « cône de la honte ». Mais les cliniques occupent déjà le sujet, et les images chirurgicales sont sensibles. Les **risques** dominants sont économiques (ancrage bas, CPA de point mort de 9 à 13 €) et logistiques (besoin daté, tailles, retours non revendables).

**Note pondérée provisoire : 4,9/10** [calc].

### Cited Findings
- **Ce qui existe déjà** (Q3 et Q4) :
  - versions mâle et femelle (Kooa) ;
  - zip dorsal (Kooa, Medical Pet Shirt avec fermeture arrière) ;
  - 10 tailles (Trovet) ;
  - lot de 2 (Cdiscount) ;
  - versions à pattes et manchons (Amazon.fr, ManoMano, Suitical).
- **Plaintes à résoudre** :
  - taille ;
  - pressions ;
  - absence d'ouverture hygiène (« wished there was a potty hole ») ;
  - odeur ;
  - enfilage avant l'opération ;
  - contournement de la protection (collerette retirée, sutures atteintes).
- **Contenus et accroches existants** :
  - « Le cône de la honte ? C'est NON » (@labulleveto, vers 06/2025 [H]) — [TikTok](https://www.tiktok.com/@labulleveto/video/7519814217227062550) ;
  - « Body ou Collerette pour Chien : Quel est le Meilleur Choix » (Sevetys, vers 02/2023 [H], historique) — [TikTok](https://www.tiktok.com/@sevetys/video/7200392132388048133) ;
  - [ÉTUDE] 60,2 % des propriétaires citent une difficulté à boire et 67,5 % une incapacité à jouer (Shenoda 2020, historique).
- **Conformité** (notes antérieures, `fr_costs_regulation.md` et `mobilite_senior_grands_chiens.md`) :
  - GPSR, art. 19 : identité et adresses du responsable, identification du produit et avertissements en français sur la fiche ;
  - REACH textile (colorants azoïques, NPE) ;
  - allégations prudentes : body « à discours encadré », du type « protège la plaie, sur conseil de votre vétérinaire » ;
  - le statut des dispositifs médicaux vétérinaires dans l'UE n'est **pas vérifié** ;
  - prix barré soumis à la règle du prix le plus bas des 30 jours précédents.

### Inferences

#### Différenciation (pistes [H])
1. **Spécialiste « grands chiens »** : tailles L à XXL pour 25 à 45 kg, avec une gamme dédiée aux races de l'audience Pilou (berger australien, golden). C'est le seul segment où des prix de plus de 30 € l'unité existent déjà (Flamingo, Trovet).
2. **Service de taille** : guide en 3 mesures avec vidéo, conseiller par message, **échange gratuit de la première taille avant usage**. Cela répond à l'échec n° 1 de la catégorie.
3. **Ouverture hygiène zippée**, adaptée au sexe, sans pressions, et **tissu à séchage rapide et anti-odeur**. Ces deux points répondent à deux plaintes documentées.
4. **Lot de 2 par défaut** (rotation et lavage) et **kit « J−7 »** : guide de préparation à la stérilisation relu par un vétérinaire, checklist, vidéo d'enfilage avant l'opération, jouet à lécher en option.
5. **Discours vétérinaire** : « à utiliser sur avis de votre vétérinaire », une fiche à montrer à la clinique, et peut-être des partenariats avec des créateurs vétérinaires ou des auxiliaires spécialisées vétérinaires sur TikTok, puisque ces créateurs existent.
6. **Livraison datée** : promesse « reçu avant votre opération » seulement si un stock UE ou une ligne express est obtenu. Sinon, il faut afficher clairement le délai et pousser à commander tôt.

#### Potentiel créatif pour TikTok, Meta et UGC
- **Accroches** [H] :
  - « Stérilisation prévue ? Votre chien n'est pas obligé de porter le cône de la honte. » ;
  - « Il ne pouvait plus boire avec sa collerette… » (appuyé sur les 60,2 %) ;
  - « 10 jours de collerette, ou 10 jours de vie normale ? » ;
  - « Ce que j'aurais aimé savoir avant la stérilisation de ma chienne ».
- **Avant/après** : le même chien avec collerette (se cogne aux portes, boit difficilement, prostré) puis en body (dort en boule, joue, boit). C'est très lisible en 3 secondes [H].
- **Démos** : enfilage en 20 secondes, ouverture hygiène, mesure du chien au mètre ruban, rotation de 2 bodies au lavage [H].
- **UGC** : vidéos de propriétaires à J+1 et J+7, et témoignages d'auxiliaires vétérinaires. Les cliniques françaises publient déjà ce type de contenu (Sevetys, Isneauville), ce qui confirme l'intérêt du sujet.
- **Limites** [H] :
  - ne pas montrer de plaie ni de sutures (politiques publicitaires sur le contenu médical ou choquant, non vérifiées) ;
  - ne pas promettre de guérison ;
  - ne pas dénigrer la collerette prescrite.
  
  La saison n'a pas été mesurée.
- **Viralité et ventes** : les [VUES] n'ont pas été relevées. Le potentiel créatif ne compense pas l'écart entre la contribution (9–13 €) et le coût par achat actuel (80–97 €) [calc].

#### Risques commerciaux et logistiques
1. **Prix** : ancrage bas (Kooa à 12,99 €, Amazon.fr à 11–26 €).
2. **Rentabilité** : CPA de point mort de 9 à 13 € [calc], contre 80 à 97 € chez Pilou.
3. **Achat unique et fenêtre courte** : pas de réachat.
4. **Besoin daté** face à 6 à 14 jours de transit depuis la Chine : retards, remboursements, litiges.
5. **Tailles** : 10 tailles et 2 versions, erreurs fréquentes.
6. **Retours non revendables** : hygiène, et retour vers la Chine non rentable.
7. **Prescripteur vétérinaire** : la collerette peut rester imposée, et des marques vétérinaires sont vendues en clinique.
8. **Recommandation WSAVA de 2024** contre la stérilisation systématique : le volume pourrait reculer [H].
9. **Produit générique facile à copier**, et substituts (collerettes gonflables ou souples, BiteNot).
10. **Droits** de 3 € et 2 € par article distinct, qui pénalisent les kits.
11. **Conformité** : GPSR, REACH, allégations médicales.
12. **Qualité** : odeur, coutures, pressions. Des échantillons sont nécessaires.

#### Notes provisoires sur 10
| Critère (poids) | Note | Justification |
|---|---|---|
| Intensité du problème (30 %) | **6** | Douleur forte et quasi universelle (77,4 % de qualité de vie dégradée ; 57 % des chiens stérilisés), mais brève (7–14 jours), unique par opération et non récurrente |
| Potentiel commercial en France (25 %) | **3** | Environ 400 000 stérilisations par an [calc], mais un marché du body estimé à 0,4–1,6 M€ par an [calc sur H], un ancrage de 11–31 € et un CPA de point mort de 9–13 € contre 80–97 € |
| Preuve de demande US (20 %) | **7** | Plus de 4 000 commandes estimées en avril 2026 pour le 1er ASIN (ASINsight), badge Kuoser 900+, 16 643 et 18 068 notes, distribution Target, Walmart et Chewy ; mais petit ticket et attribution contradictoire |
| Faiblesse de la concurrence française (15 %) | **3** | Au moins 26 offres dans au moins 10 canaux, marque propre Zooplus dès 12,99 €, marques vétérinaires en clinique ; seul le marketing de marque française est absent |
| Facilité de sourcing et de vente (10 %) | **5** | Produit léger, MOQ dès 2 pièces et 2,70–4,87 $ à la source ; mais 10 tailles et 2 versions, besoin daté contre 6–14 jours de transit, aucun body chez CJ, retours non revendables |
| **Note pondérée** [calc] | **4,9** | 6 × 0,30 + 3 × 0,25 + 7 × 0,20 + 3 × 0,15 + 5 × 0,10 = 1,80 + 0,75 + 1,40 + 0,45 + 0,50 = 4,90 |

- **Verdict provisoire** [H] : **à écarter comme produit phare d'acquisition payante.** On peut le garder comme produit d'appoint (vente croisée ou panier) dans une future gamme « convalescence et grands chiens », ou pour un test organique. La prochaine vérification serait un devis de l'agent avec un stock UE et un délai garanti.

### Gaps
- **Captures publicitaires** (Meta Ads Library, TikTok Creative Center) : non vérifiées. Elles sont à fournir par le propriétaire.
- **Saisonnalité** des stérilisations et des recherches : non trouvée.
- **Règles publicitaires Meta et TikTok** sur les images post-opératoires : non vérifiées [H].
- **Statut juridique** d'un textile « post-opératoire » au regard des dispositifs médicaux vétérinaires : non vérifié.

#### Journal numéroté des requêtes (02/11/2026 ; WebSearch en mode « standard » ; filtres de domaine entre crochets)
| N° | Requête (verbatim) | Volet | Résultat principal |
|---|---|---|---|
| 1 | `body chien après opération stérilisation` [amazon.fr] | France, Amazon.fr | Au moins 10 fiches génériques (TYXHXTF, Cyponpy, HEYWEAN, Kuoser, Hjumarayan, KONVINIT…), environ 11–26 € |
| 2 | `body post opératoire chien` [zooplus.fr, zoomalia.com, wanimo.com, maxizoo.fr, animalis.com, truffaut.com, jardiland.com, botanic.com] | France, enseignes | Trovet chez Maxi Zoo France (9 tailles vues), 96 % coton ; aucune autre enseigne remontée |
| 3 | `body de récupération chien` [cdiscount.com, manomano.fr, fnac.com, rakuten.fr, kaufland.fr] | France, marketplaces | Cdiscount (dont un lot de 2) et ManoMano, environ 11 € à plus de 25 € ; ni Fnac, ni Rakuten, ni Kaufland |
| 4 | `body chien post opératoire prix` [idealo.fr, ledenicheur.fr] | France, comparateurs | **Rejetée par l'outil** : idealo.fr inaccessible au robot du moteur (erreur 400) |
| 5 | `body chien post opératoire` [ledenicheur.fr] | France, comparateur | Pages « body chien » et « body pour chien », environ 10 € à plus de 40 € |
| 6 | `Suitical Recovery Suit chien pharmacie vétérinaire` | France, pharmacies et vétérinaires | Aucune pharmacie française ; Suitical à 30–65 $ ; Suitical International BV (Pays-Bas) |
| 7 | `body post opératoire chien marque française` | France, marques | Aucune marque française ; Kooa (zooplus SE), Buster, INF, Safety Body |
| 8 | `alternative collerette chien combinaison après stérilisation` | France, phrase de problème | Contenus SantéVet et La Compagnie des Animaux ; collerettes chez Pharma-GDD ; avis client paraphrasé ; durée de 10–14 jours |
| 9 | `body chien stérilisation collerette` [tiktok.com] | France, TikTok | Sevetys, clinique d'Isneauville, @labulleveto (BiteNot) ; vues non visibles |
| 10 | `pourcentage chiens stérilisés France` | Taille du besoin | 57 % (FACCO/Odoxa 2025 via Virbac) ; près de 60 % (Petscare) ; 40 % et 42,4 % / 21,6 % (historique) |
| 11 | `vétérinaire body ou collerette après stérilisation chienne` | Canal vétérinaire | Collerette standard ; alternatives sur avis vétérinaire ; inconvénients du body ; 7–14 jours |
| 12 | `dog recovery suit after surgery bought in past month` [amazon.com] | US, badges | Kuoser 900+ ; SlowTon 100+ ; Kuoser XL 100+ (incertain) ; manchon Kuoser 50+ |
| 13 | `surgery suit for dogs Kuoser Supet monthly orders` [asinsight.com] | US, vérification ASINsight | Plus de 4 000 commandes en avril pour le 1er ASIN (128 produits) ; Kuoser « 1,000+ » et 16 643 notes ; collerettes Supet à 5 000–8 000 par mois |
| 14 | `best dog recovery suit 2026 Suitical Wowwoo Medical Pet Shirt price` | US, marques et prix | Suitical à 27–37 $ (Chewy, Petfood Express, Walmart), 65 $ chez Canine Styles ; iHeartDogs 2026 ; Wowwoo non trouvé |
| 15 | `dog recovery suit after surgery wholesale` [alibaba.com] | Sourcing | MOQ de 2 à 2,70–2,90 $ ; MOQ de 500 à 4,56–4,87 $ ; MOQ de 1 000 à 0,29–0,79 $ (non confirmé) |
| 16 | `dog recovery suit` [cjdropshipping.com] | Sourcing, CJ | Aucun body ; seulement des articles de blog |
| 17 | `body postopératoire Kooa Trovet Buster Safety Body chien prix` [zooplus.fr, maxizoo.fr, lacompagniedesanimaux.com, zoomalia.com] | France, prix des enseignes | Kooa dès 12,99 € et 13,79 € ; Trovet à 29–31 € ; Flamingo Safety Body à 17,99–54,99 € |
| 18 | `Medical Pet Shirt vétérinaire France body chien` | France, canal vétérinaire et marque | La Compagnie des Animaux (Top 4in1 S à 27,60 €), Place des Vétos, salons vétérinaires, Penn Vet |
| W1 | WebFetch `https://ledenicheur.fr/s/body-pour-chien/` | France, comparateur | **Refusé : ENOTFOUND** (domaine à autoriser dans les paramètres réseau) |
| W2 | WebFetch `https://www.lacompagniedesanimaux.com/chien/accessoires-chien/collerette-chien.html?page=3` | France, prix spécialistes | **Refusé : ENOTFOUND** (domaine à autoriser dans les paramètres réseau) |
