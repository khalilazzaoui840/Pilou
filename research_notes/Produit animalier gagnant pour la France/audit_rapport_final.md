# Audit du rapport final « Produit animalier gagnant pour la France »

*Audit du 28/10/2026 sur `reports/Produit animalier gagnant pour la France.md` (329 lignes, commit 8068f6a « version avant relecture »). Les numéros de ligne renvoient à ce fichier. Le rapport n'a pas été modifié.*

**Méthode.**
- Lecture intégrale du rapport.
- Lecture intégrale de `analyse_financiere_finalistes.md`, `verification_jouet_lechage.md`, `us_verif_woof_pupsicle.md`, `fr_deep_jouet_lechage_congelable.md` et `fr_demande_jouet_lechage.md`.
- Lecture ciblée de `sourcing_jouet_lechage.md`, `pub_jouet_lechage.md`, `deep_support_nerf_de_boeuf.md`, `fr_deep_glandes_anales.md`, `fr_deep_litiere_indicatrice_sante.md`, `faisabilite_litiere_et_bouchees.md`, `pub_litiere_et_bouchees.md`, `deep_boite_puzzle_chat.md`, `fr_screening_alternatives.md`, `us_decouverte_marques_meconnues.md`, `fr_couts_commerciaux.md`, `fr_costs_regulation.md` et des autres notes `us_*` (tableau des éliminations).
- Recalculs de contrôle avec le modèle Python de l'étude (`scratchpad/finance/model.py`). Les chiffres marqués **[calcul de l'audit]** en sortent.
- Trois recherches web sur les dix autorisées, pour des faits douteux (§8). Aucun WebFetch ni curl.

## Verdict

**Ne pas livrer en l'état.** Ce qui tient :
- les montants financiers sont recopiés fidèlement : les tableaux de rentabilité, de sensibilité, de comparaison et de budget concordent au centime avec la note financière ;
- les faits clés sur Woof sont exacts et bien sourcés (Inc. 5000, rachat, dates corrigées, prix, livraison aux États-Unis seulement) ;
- les relevés de concurrence française sont fidèles aux notes.

Cinq problèmes bloquants touchent la décision elle-même :
1. le seuil « poursuivre sous 18 à 20 € » fait perdre de l'argent avec l'hypothèse de 30 % de duos du rapport ;
2. le palier à 4 700 € ne mesure pas un « vrai coût par achat » tel que le plan de 30 jours l'organise ;
3. le produit chiffré et testé (balle de catalogue, 8 cm au plus) n'est pas le produit recommandé (balle d'au moins 9 cm pour grands chiens, fermeture sans filetage) ;
4. le calendrier de 30 jours est irréalisable pour les échantillons et déborde le jour 30 ;
5. les résultats de recherche Google, exigés en partie C, ne sont ni fournis ni déclarés « non vérifiés ».

**Bilan :** 5 corrections bloquantes, 23 importantes, 23 mineures. Sur 82 lignes de vérification couvrant plus de 100 chiffres (§5), 61 sont conformes et 21 posent un problème : 3 faux ou contredits, 4 incomplets, 5 mal étiquetés, 3 incohérences chiffrées, 5 sources ou dates manquantes, 1 invérifiable.

---

## 1. Corrections bloquantes

### B1. Le seuil de décision « poursuivre sous 18 à 20 € » fait perdre de l'argent
- **Où :** l. 283 (règle de décision) ; l. 279 (indicateurs) ; l. 3 (ouverture) ; l. 287 (offre « Duo ») ; l. 322 (Q6) ; l. 241 (« facteur 5 »).
- **Passages :**
  - l. 283 : « **Décision finale**, après environ 50 achats avec stock : **poursuivre** si le CPA observé reste sous 18 à 20 € ; **modifier** entre 20 et 30 € […] ; **arrêter** au-delà de 30 € » ;
  - l. 279 : « Coût par achat | 18 à 20 € au plus (duo) » ;
  - l. 3 : « Le jouet ne devient rentable que si le coût par achat observé reste sous 18 à 20 € avec le duo ».
- **Problème :**
  - 18,41 € est l'équilibre d'une première commande **quand 100 % des clients prennent le duo** (19,80 € sur 12 mois).
  - Le rapport suppose lui-même 30 % de duos (l. 280). La marge moyenne d'une première commande vaut alors 12,70 € (`analyse_financiere_finalistes.md` §6.2), soit 14,09 € sur 12 mois [calcul de l'audit].
  - Poursuivre à 18–20 € ferait donc perdre environ 5,30 à 7,30 € par première commande, et 3,90 à 5,90 € par client sur 12 mois.
  - La borne de 20 € dépasse même l'équilibre d'un duo pris par tous les clients (19,80 € sur 12 mois).
  - La note financière précise aussi (§1.2) que l'avantage du lot est un maximum, puisque le même CPA est appliqué à une offre plus chère.
- **Correction :**
  - Remplacer le seuil fixe par un seuil lié au mix observé : « poursuivre si le CPA observé est inférieur à la marge moyenne par commande réellement observée, soit environ 10,26 € + 8,15 € × la part des duos. Cela fait 12,70 € avec 30 % de duos, et 18,41 € seulement si tous les clients prennent le duo. Modifier l'offre entre ce seuil et 30 € ; arrêter au-delà de 30 €. »
  - Reporter la formule :
    - en l. 3 et l. 322 ;
    - en l. 279 : « environ 13 € avec 30 % de duos ; 18,41 € si 100 % » ;
    - en l. 287 : « seule structure à l'équilibre vers 18 € si tous les clients la choisissent ».
  - En l. 241, remplacer « facteur 5 » par « facteur 7 à 8 (96,61 € contre environ 12,70 €) ; facteur 5 seulement si tous les clients prenaient le duo ».

### B2. Le palier à 4 700 € ne mesure pas un « vrai coût par achat »
- **Où :** l. 3 ; l. 249 ; l. 257 ; l. 258 ; l. 321 (Q5).
- **Passages :**
  - l. 3 : « environ 4 700 € HT pour mesurer un vrai coût par achat » ;
  - l. 321 : « Environ 4 700 € HT pour un premier test qui mesure un vrai coût par achat (…, 630 € de publicité) » ;
  - l. 257 : « lancement Meta : deux ensembles à 15 €/jour optimisés sur l'ajout au panier, page en précommande […] publicité 630 € sur 21 jours » ;
  - l. 258 : « commander le premier lot (200 kits en aérien, environ 1 784 €) pour mesurer le vrai coût par achat ».
- **Problème :**
  - Dans le plan, les 630 € de publicité sont dépensés **avant que le stock existe**, sur une page en précommande, avec une optimisation sur l'ajout au panier.
  - Le lot de 200 kits n'est commandé qu'en J22–J30. Il arrive environ 5,5 à 10,5 semaines plus tard (production, contrôle, aérien et réception, `sourcing_jouet_lechage.md` §3). Il ne reste alors **aucun budget publicitaire** pour mesurer le coût par achat.
  - La note financière (§5.1) et la dernière phrase de Q5 disent elles-mêmes qu'un test sans stock « ne mesure que le coût par ajout au panier ».
  - 630 € ne donnent qu'environ 16 achats au CPA central, soit environ 8 par angle. C'est sous les seuils du rapport (15 à 20 achats par angle, environ 50 pour décider). Ces achats suffisent à détecter un échec, pas à valider une réussite.
  - Chaque vente du lot test ne dégage qu'environ 6,38 € (kit) ou 10,65 € (duo), à cause d'un coût rendu de 8,17 € le kit [calcul de l'audit].
- **Correction :** choisir et écrire l'une de ces deux options.
  - **Option (a) :** garder le pré-test sans stock en J15–J30, présenté comme une mesure du coût par ajout au panier et des précommandes. Ajouter 630 € de publicité à la réception du lot. Le palier bas passe alors à environ 5 330 € HT (4 699 + 630), ou environ 5 390 € avec 10 % d'imprévus.
  - **Option (b) :** supprimer la publicité du premier mois et lancer les 630 € à la réception du lot. Le palier bas reste à environ 4 700 € HT, mais le premier coût par achat réel arrive en janvier ou février 2027.
  - Dans les deux cas, réécrire l. 3 et Q5 : « environ 4 700 € (ou 5 330 €) HT pour un pré-test capable de révéler un échec, avec environ 16 achats au CPA central. Confirmer une réussite demande environ 50 achats, soit environ 2 000 € de publicité au CPA central. »

### B3. Le produit chiffré et testé n'est pas le produit recommandé
- **Où :** l. 142, 148, 149, 155, 254, 321 ; partie D (« Kit L » à 10,26 €).
- **Passages :**
  - l. 142 : « tailles L puis XL » ;
  - l. 155 : « aucune balle de catalogue relevée chez les fabricants chinois ne dépasse 8 cm ; la règle « le jouet ne doit jamais entrer entièrement dans la gueule » impose de trouver un fabricant ayant déjà un moule plus grand ou de financer un moule » ;
  - l. 254 : « Exiger une balle d'au moins 9 cm, deux ouvertures, une fermeture sans filetage » ;
  - l. 321 : « 200 kits de catalogue améliorés » et « 1 000 kits L ».
- **Problème :**
  - Le « kit L » du modèle (balle à 1,91 $ FOB, coût rendu de 4,04 €) et le lot test (balle Newtop à 3,80 $) sont des **balles de catalogue**.
  - Les notes plafonnent ces balles à 8 cm (`sourcing_jouet_lechage.md` §1 ; `analyse_financiere_finalistes.md` §1.3 : « Taille maximale en catalogue : 8 cm (Woof L : 9,1 cm) »).
  - La fermeture sans filetage (insert à baïonnette) n'est chiffrée nulle part (§4.4).
  - Les paliers à 4 700 € et à 14 923 € testeraient donc une balle plus petite que la Pupsicle L, sans la fermeture promise, auprès de propriétaires de grands chiens. Le rapport juge pourtant lui-même ce format inadapté.
  - Seul le palier haut (35 885 €, absent du rapport) inclut un moule propriétaire, et seulement pour la XL.
  - Si une balle d'au moins 9 cm exige un moule propre, la marge chute [calcul de l'audit, 4 000 $ d'outillage amortis sur 1 000 kits] :

    | Prix d'achat de la balle | Marge du kit (10,26 € aujourd'hui) | Marge du duo (18,41 € aujourd'hui) |
    |---|---:|---:|
    | 1,91 $ | 7,03 € | 11,94 € |
    | 5 $ (sur mesure) | 4,28 € | 6,45 € |

  - Le délai passe alors à 14,5 à 35,5 semaines.
- **Correction :**
  1. Écrire en partie A et en Q5 que les deux premiers paliers testent une balle de catalogue (8 cm au plus dans les relevés), donc plutôt pour des chiens moyens. La version « grands chiens, fermeture sans filetage » demande un moule propriétaire.
  2. Ajouter à l'étape J1–J7 la conduite à tenir si aucun fabricant n'a de balle d'au moins 9 cm : tester sur des chiens moyens, ou financer un moule L avant le test sérieux.
  3. Chiffrer la variante « moule L propriétaire » en partie D et dans le budget du test sérieux.
  4. Réserver l'angle « Il s'ouvre toujours » et la promesse « tient tête aux grands mâcheurs » à cette version, une fois les essais faits.

### B4. Le calendrier de 30 jours est irréalisable
- **Où :** l. 254, 256, 257, 258.
- **Passages :**
  - l. 254 : « J1 à J7 | Appel d'offres auprès de 8 à 11 fabricants » ;
  - l. 256 : « J8 à J14 | Essais des échantillons » ;
  - l. 257 : « J15 à J21 | Tournage […] avec les échantillons ; […] publicité 630 € sur 21 jours » et « Coupure de tout ensemble qui dépense 45 € sans résultat » ;
  - l. 258 : « J22 à J30 | Lecture des indicateurs ; tri des angles ; décision ».
- **Problème :**
  - Selon la note de sourcing (§3, scénario A), l'appel d'offres prend 1 à 2 semaines, la préparation des échantillons 1 à 3 semaines et l'envoi express environ une semaine.
  - Les premiers échantillons arrivent donc au mieux vers J15–J20, au pire vers J42. Les essais ne peuvent pas avoir lieu en J8–J14, ni le tournage avec les échantillons commencer en J15.
  - « 630 € sur 21 jours » lancés en J15 courent jusqu'à J35, au-delà du plan. La décision de J22–J30 tomberait après une à deux semaines de diffusion au plus.
  - La règle de coupure (45 €, soit trois fois un coût par **achat** de 15 €) ne correspond pas à l'événement optimisé (l'ajout au panier).
- **Correction :**
  - Recaler le plan :
    - J1–J14 : appel d'offres et commande d'échantillons, si possible pris en stock ;
    - J15–J35 : réception, essais, puis tournage des vidéos UGC avec les échantillons reçus ;
    - publicité seulement si elle tient dans la fenêtre, sinon plan étendu à 45 jours avec un budget recalculé ;
    - décision sur le lot vers J35–J45.
  - Définir la règle de coupure sur l'événement optimisé : trois fois le coût visé par ajout au panier.

### B5. Les résultats de recherche Google manquent en partie C
- **Où :** tableau des recherches, l. 194–207.
- **Problème :**
  - Le client demande les résultats de recherche Google et des places de marché. Le tableau couvre Amazon.fr, Cdiscount, les enseignes, Fnac, Darty, Rakuten et TikTok, et déclare non vérifiés Google Shopping et les comparateurs (l. 207).
  - Aucun résultat naturel de Google.fr n'est rapporté, et la partie C ne dit pas qu'ils n'ont pas pu être relevés : le moteur utilisé est américain (l. 9).
  - Un lecteur croira que Google a été consulté.
- **Correction :**
  - Ajouter au tableau une ligne : « Google.fr, résultats naturels (« balle à lécher chien », « jouet à lécher congelable », « pupsicle ») | Non vérifié (accès impossible) : toutes les recherches de l'étude passent par un moteur américain filtré par domaines ; aucun classement Google.fr n'a été observé. »
  - Ajouter cette vérification au tableau « Vérification à faire soi-même » : en navigation privée, relever les 10 premiers résultats et les encarts Shopping.

---

## 2. Corrections importantes

Elles sont classées de la plus grave à la moins grave.

### I1. Chiffres Meta de Pilou : source, lecture et formulation (l. 241 ; repris l. 3 et 322)
- **Passage :** « trois ensembles ont obtenu un coût par achat de 65,69 € (2 achats), 112,08 € (1 achat) et 22,22 € (1 achat), et un quatrième a dépensé 120,76 € sans achat. Au total, 386,44 € pour 4 achats, soit **96,61 € par achat en moyenne** [calcul] » ; « la règle de coupure n'a pas été appliquée — l'ensemble sans achat a dépensé environ huit fois une cible de 15 € ».
- **Problème :**
  - Ces chiffres ne figurent dans aucune note : la seule source est une série de captures du client, sans date ni période dans le rapport.
  - Le calcul est exact si 65,69 € est un **coût par achat** (131,38 € dépensés). Si c'est le **montant dépensé** pour 2 achats, le total tombe à 320,75 € et la moyenne à 80,19 € [calcul de l'audit]. Pour les ensembles à un achat, les deux lectures donnent le même chiffre.
  - La « cible de 15 € » confond le budget quotidien (15 €/jour) avec un coût par achat visé.
  - La règle des « trois CPA cibles » est une proposition de l'étude, que le client ne pouvait pas appliquer. La cible de Pilou (autre produit, autre marge) n'est pas connue.
- **Correction :**
  - Vérifier sur les captures la colonne lue (« Coût par résultat » ou « Montant dépensé ») et indiquer la période des campagnes et la date des captures.
  - Écrire « 96,61 € si 65,69 € est un coût par achat, 80,19 € s'il s'agit de la dépense ».
  - Remplacer la phrase sur la règle par : « À titre d'illustration, la règle proposée ici (couper après trois fois le coût par achat visé, soit 45 € pour une cible de 15 €) aurait arrêté l'ensemble sans achat bien avant 120,76 €. »
  - Ajuster le facteur d'écart (voir B1).

### I2. Prix du rachat de PrettyLitter incomplet (l. 52, 61)
- **Passage :** « rachat par Mars en 2021 pour un prix rapporté de 500 M$ à 1 Md$, jamais confirmé ([Bloomberg]) », suivi d'un lien Inc. intitulé « …turned-1-million-in-capital-into-a-1-4-billion-exit ».
- **Problème :**
  - Selon `pub_litiere_et_bouchees.md` (§1), l'article d'Inc. cité dans la même phrase parle d'une sortie à 1,4 Md$, avec un rachat des parts du fondateur finalisé en 2024. La note juge la divergence « non résolue ».
  - Le lecteur qui ouvre le lien verra un autre chiffre.
  - La recherche web (§8) ne retrouve que la fourchette de Bloomberg (article du 07/09/2021) et « 1 Md$ » sur Wikipedia.
- **Correction :** « rachat par Mars annoncé en 2021, pour un prix rapporté de 500 M$ à 1 Md$ (Bloomberg, 2021), voire 1,4 Md$ selon Inc., qui situe la finalisation en 2024 ; aucun montant confirmé par les parties ». Appliquer la même nuance en l. 52.

### I3. « La seule donnée financière déposée de l'étude » (l. 57)
- **Problème :** c'est faux. Le rapport cite lui-même deux autres dépôts à la SEC : le 10-Q de PetIQ sur le rachat de Rocco & Roxie (l. 17) et le 8-K de BARK (l. 27).
- **Correction :** « la seule donnée financière déposée parmi les cinq finalistes (déclarée, non auditée, exercice 2023) ».

### I4. Mauvais statut pour le classement Inc. 5000 (l. 146, 157, 176, 313, 327)
- **Passages :**
  - l. 146 : « Succès américain certifié » ;
  - l. 157 (titre) : « une croissance certifiée » ;
  - l. 313 : « croissance certifiée deux années de suite » ;
  - l. 176 : « il a atteint la troisième croissance privée des États-Unis » ;
  - l. 327 : « Woof est devenue la troisième croissance privée des États-Unis ».
- **Problème :**
  - La l. 165 dit à juste titre que la croissance Inc. est « déclarative, pas un CA ».
  - « Certifiée » et « troisième croissance privée des États-Unis » surestiment la preuve. L'Inc. 5000 classe des entreprises privées **candidates**, sur des états financiers signés par le dirigeant et un tiers, non publiés.
- **Correction :**
  - Écrire « n°3 du classement Inc. 5000 2025 des entreprises privées candidates ».
  - Remplacer « certifiée » par « déclarée au classement Inc. 5000 (états financiers signés, non publiés) ».

### I5. Comment Woof a grandi : affirmation contredite par les notes (l. 81, 174, 176, 327)
- **Passages :**
  - l. 81 : « Woof a grandi avec des vidéos de créateurs plafonnant à environ 3 700 « j'aime » » ;
  - l. 176 : « il a grandi par Amazon, la grande distribution et l'affiliation, pas par une vidéo virale » ;
  - l. 327 : « en s'appuyant sur Amazon et 5 000 points de vente plutôt que sur une vidéo virale ».
- **Problème :**
  - Le communiqué BusinessWire du 19/11/2024 présente Woof comme « primarily direct-to-consumer » jusqu'à son entrée chez PetSmart (`us_verif_woof_pupsicle.md` §2). La croissance mesurée par Inc. (2021–2024) précède donc l'essentiel de la grande distribution.
  - Les 3 700 « j'aime » sont le maximum vu dans les extraits de pages TikTok mises à jour en juillet–août 2026. Ce n'est ni un plafond ni un moteur prouvé de la croissance.
  - Présenter des vues comme cause de croissance est la confusion que le client a exclue.
- **Correction :**
  - Remplacer par : « Woof se décrivait comme vendant surtout en direct jusqu'à son entrée chez PetSmart en novembre 2024 ; la grande distribution (plus de 5 000 points de vente annoncés) est venue ensuite. Aucune vidéo virale massive n'a été trouvée : les vidéos de créateurs relevées en juillet–août 2026 atteignent au plus environ 3 700 « j'aime » dans les extraits consultés. »
  - Supprimer « Woof a grandi avec ».

### I6. Absences affirmées sans vérification suffisante (l. 3, 57, 147)
- **Passages :**
  - l. 3 : « aucune marque française n'occupe la catégorie » ;
  - l. 147 : « Aucune marque française » ;
  - l. 57 : « le support n'existe qu'en offres transfrontalières ».
- **Problème :**
  - Ce sont des résultats d'un moteur américain, et la l. 9 rappelle elle-même qu'un résultat vide ne prouve pas une absence.
  - Pour le support, la note cite aussi Bow Wow Labs (souvent en rupture) et d'autres fiches sur Amazon.fr. L'origine du vendeur PetTribes sur Zooplus.fr n'est pas établie.
- **Correction :**
  - l. 3 et l. 147 : « aucune marque française n'a été trouvée ».
  - l. 57 : « le support ne s'y trouve que chez des vendeurs de places de marché, souvent transfrontaliers (Bow Wow Labs, souvent en rupture, et PetClan Chewise sur Amazon.fr ; PetTribes sur Zooplus.fr ; annonces Fruugo) ; aucune marque française trouvée ».

### I7. Affirmations douanières trop affirmatives ou inexactes (l. 209, 329)
- **Passages :**
  - l. 209 : « à partir du 01/11/2026 2 € de frais de traitement par article » et « contre 0,10 à 0,20 € de droits » ;
  - l. 329 : « fait payer 8 à 10 € par kit aux clones ».
- **Problème :**
  - Les frais de 2 € et leur date sont confirmés. Mais les sources divergent sur l'unité (par article ou par envoi), et la publication au Journal officiel n'apparaît que dans une source (`verification_jouet_lechage.md`, n°30).
  - La recherche web (§8) le confirme : une source cite l'acte C(2026) 6694 du 21/09, sans le numéro 2026/2152, et les sources se partagent sur l'unité.
  - Un clone typique (balle seule) paie 3 € + 2 € = 5 €, pas 8 à 10 €.
  - Le modèle retient 0,10 à 0,31 € de droits par kit importé en stock.
- **Correction :**
  - l. 209 : « et, à partir du 01/11/2026, des frais de traitement de 2 € (par article selon la Commission, par envoi selon d'autres sources ; publication au Journal officiel non vérifiée) » ; « 0,10 à 0,30 € ».
  - l. 329 : « 5 € (balle seule) à 10 € (kit balle + moule) par envoi ».

### I8. Points réglementaires présentés comme acquis (l. 57, 297)
- **Passages :**
  - l. 297 : « « apaise » ou « anti-stress » sont à proscrire en titre, la publicité ne devant jamais faire apparaître la consultation vétérinaire comme superflue ([décret de 2015]) » ;
  - l. 57 : « vendre des nerfs en kit fait entrer la marque dans le régime des sous-produits animaux, ce que la DDPP doit confirmer par écrit ».
- **Problème :**
  - Le décret de 2015 encadre la publicité des **médicaments vétérinaires**. La note `pub_jouet_lechage.md` (§3) l'applique « par principe » et signale que son articulation avec le règlement (UE) 2019/6 n'est pas vérifiée.
  - Pour les nerfs, `deep_support_nerf_de_boeuf.md` dit « point non tranché ».
- **Correction :**
  - l. 297 : « Éviter « apaise » ou « anti-stress » en titre : une promesse de traitement pourrait faire requalifier le produit. Par prudence, appliquer aussi le principe du décret de 2015 sur la publicité des médicaments vétérinaires (ne jamais laisser entendre qu'une consultation est inutile), même si son application à un jouet n'est pas vérifiée. »
  - l. 57 : « pourrait faire entrer la marque dans le régime des sous-produits animaux (point non tranché, à faire confirmer par écrit par la DDPP) ».

### I9. Argument de vente non prouvé (l. 148, 320)
- **Passage :** « … une balle à remplir, congeler et lécher, qui s'ouvre toujours et tient tête aux grands mâcheurs. »
- **Problème :**
  - Ce sont deux promesses de résultat sans preuve : aucun échantillon n'a été testé, et même la version renforcée de Woof s'écaille.
  - Elles contredisent l'avertissement « aucun jouet n'est indestructible » recommandé par `sourcing_jouet_lechage.md` (§3.4).
  - Risque de pratique commerciale trompeuse (même note, check-list, ligne 15).
- **Correction :**
  - Écrire « Le grand chien occupé, le maître tranquille : une balle à remplir, congeler et lécher. »
  - N'ajouter « qui s'ouvre facilement, même après 100 lavages » et « pensée pour les grands mâcheurs » qu'après des essais documentés.
  - Garder « aucun jouet n'est indestructible » sur la fiche produit.

### I10. Public cible : chiffre déclaratif non étiqueté et cible non démontrée (l. 145)
- **Passage :** « clients Pilou, moins de 35 ans, qui dépensent environ 150 € par mois pour leurs animaux ([Bonial]) ».
- **Problème :**
  - Ce chiffre vient d'un sondage déclaratif (OpinionWay pour Bonial, communiqué du 26/09/2024), tous animaux confondus. Le rapport ne le date ni ne l'étiquette.
  - Rien n'indique que les clients Pilou ont moins de 35 ans : `fr_market_landscape.md` en fait une hypothèse de ciblage publicitaire.
- **Correction :** « Propriétaires de grands chiens, à commencer par les clients Pilou (taille de la base inconnue). Cible publicitaire à tester : les moins de 35 ans, qui déclarent dépenser environ 150 € par mois pour l'ensemble de leurs animaux (sondage OpinionWay pour Bonial, septembre 2024). »

### I11. Notes de la grille en décalage avec les preuves (l. 43, 51, 303–313)
- **Problème :**
  - **(a) Concurrence.** Les l. 43 et 47–53 classent les cinq finalistes en « concurrence moyenne ». Pourtant, la grille donne 5/20 aux bouchées, 8 à la boîte, 9 à la litière, 10 au jouet et 12 au support, sans dire ce que valent ces niveaux.
  - **(b) Marge.** La boîte a 9, comme le jouet, alors que son offre principale dégage 14,14 € contre 10,26 € et que son cumul à 12 mois est meilleur (−25,34 € contre −28,23 €).
  - **(c) Faisabilité.** Le jouet a 8/10 alors que sa version recommandée dépend d'un moule propriétaire non chiffré (B3).
  - **(d) Justification.** Aucune note n'est justifiée critère par critère.
- **Correction :**
  - Ajouter sous le tableau une justification d'une ligne par critère et par finaliste.
  - Qualifier la concurrence des bouchées de « forte (leader américain déjà présent) » en l. 43 et 51.
  - Soit justifier le 9 de la boîte (guerre des prix à 2,99 €, retours), soit le porter à 10–11.
  - Ramener la faisabilité du jouet à 6–7 si B3 se confirme.
  - Le classement ne change pas : jouet à 66 au moins, bouchées à 59.

### I12. La recommandation face aux résultats financiers (l. 313, 317)
- **Problème :** le rapport ne dit pas clairement que le jouet est, avec le support, le finaliste qui exige le coût d'acquisition le plus bas (`analyse_financiere_finalistes.md` §6.2 et §3.2).
  - Avec 30 % de lots, l'équilibre vaut 12,70 € pour le jouet et 12,79 € pour le support, contre 15,21 € pour la boîte, 17,30 € pour les bouchées et 18,12 € pour l'additif.
  - Sur 12 mois, l'offre principale du jouet récupère au plus 11,65 € de coût d'acquisition, contre 24,44 à 27,42 € pour les deux consommables.
- **Correction :** ajouter en l. 313 ou en Q1 : « Le jouet est aussi le finaliste qui exige le coût d'acquisition le plus bas pour être rentable : le choisir est un pari sur la publicité, pas sur la marge. »

### I13. Hypothèses des scénarios prudent et optimiste non expliquées (partie D, l. 230)
- **Problème :** seules les hypothèses centrales et le CPA sont détaillés. Les valeurs prudentes et optimistes n'apparaissent pas :
  - prix d'achat de la balle : 2,29 $ et 1,53 $ ;
  - commission d'agent : 15 % et 3 % ;
  - fret : ferroviaire à 450 $/m³ et maritime à 30 $/m³ ;
  - préparation : 5,25 € et 1,00 € ;
  - retours : 24 % et 5 %, cette dernière valeur étant une hypothèse non sourcée ;
  - part invendable : 75 % et 30 % ;
  - volume : 50 et 250 commandes par mois ;
  - mix de paiement.
- **Correction :** insérer après le tableau un tableau d'hypothèses en trois colonnes, repris de `analyse_financiere_finalistes.md` §1.1 (H3 à H34) et §1.3, avec le statut de chaque valeur.

### I14. Dates et sources manquantes (tableau l. 15–41 ; l. 81, 174, 192)
- **Problème :**
  - **Dates absentes.** La colonne « (type, date) » n'a pas de date pour Snuggle Puppy, K9 Sport Sack, Help 'Em Up, ToeGrips, Panther Armor, DoggieLawn, Joyride, ThunderShirt et MudBuster.
  - **Constats français sans source française.** Panther Armor (« saturé en France, panier d'environ 20 € »), Ruff Liners, Paw.com et Help 'Em Up (« génériques à 15 € »).
  - **« LickiMat à 26–28 € » sans lien.** Ce sont deux modèles de zooplus.fr en rupture, et le prix du Soother n'a pas été relevé.
  - **Autres dates absentes.** La vidéo du golden retriever, probablement de 2023, et l'estimation BrandSearch (n.d.).
  - **Miroirs.** Plusieurs compteurs d'avis américains viennent de miroirs (desertcart).
- **Correction :**
  - Écrire « capture n.d., relevé le 27/10/2026 » quand la date est inconnue.
  - Reprendre les liens français des notes : criblage FR-D1 de `us_decouverte_marques_meconnues.md` pour Ruff Liners ; Zooplus.fr, vendeur Mikan, dans `us_anxiety_sleep_senior.md` pour Help 'Em Up. Sinon, écrire « saturation en France non vérifiée » (Panther Armor).
  - Écrire « LickiMat (Soother Tuff Pro 26 €, Yoggie Pot 28 €, zooplus.fr, en rupture) » avec les liens.
  - Ajouter « vidéo probablement de 2023 » et « (miroir non officiel) » après desertcart.

### I15. « Chaque chiffre porte son statut » n'est pas tenu (l. 9)
- **Problème :** dans le texte courant, beaucoup de chiffres n'ont pas de statut :
  - 150 €/mois (déclaratif) ;
  - 13 € de CPM (milieu d'une fourchette) ;
  - 2 % de conversion (repère) ;
  - 52–53 jours de vague de chaleur (fait sourcé) ;
  - 33 000 vendeurs TikTok (déclaré par TikTok) ;
  - « au moins 18 marques » (calcul) ;
  - 30 % de duos (hypothèse, signalée seulement dans les indicateurs).
- **Correction :** l'une ou l'autre des deux options suivantes.
  - Ajouter les étiquettes [fait sourcé], [déclaré], [estimation d'outil], [calcul], [hypothèse] et [non vérifié] aux chiffres du texte.
  - Ou écrire : « Les tableaux indiquent le statut de chaque chiffre ; dans le texte, les déclarations, estimations, calculs et hypothèses sont signalés comme tels », puis appliquer cette règle.

### I16. Finalistes 2 à 5 : analyse américaine trop mince (l. 47–53, 57–63)
- **Problème :** le client demande les cinq finalistes analysés en profondeur, aux États-Unis comme en France. Pour Bow Wow Labs, Glandex, PrettyLitter et Cat Amazing, le rapport ne donne ni lien vers la boutique officielle, ni prix américain.
- **Correction :** ajouter une ligne par finaliste, datée :

  | Finaliste | Boutique officielle | Prix américain relevé |
  |---|---|---|
  | Bow Wow Labs | bowwowlabs.com | 28 à 38 $ pour le support |
  | Glandex | vetnique.com | 33,99 $ sur Amazon (août 2025) |
  | Cat Amazing | catamazing.com | MEGA à 34,95 $ |
  | PrettyLitter | site officiel à relever | prix à relever |

### I17. Revue de faisabilité dispersée et incomplète (l. 155, 230, 245, 249–258)
- **Problème :** aucune section ne reprend les douze points demandés. Il manque :
  - les phtalates et les substances SVHC (REACH, entrée 51 et article 33 ; `sourcing_jouet_lechage.md` §3) ;
  - la précaution de viser 0,5 mg/kg pour les HAP ;
  - le contrôle qualité avant expédition ;
  - le stockage (devis de logisticiens) ;
  - l'absence d'électronique, à écrire explicitement ;
  - pour les quatre autres finalistes, les fournisseurs, les échantillons et les délais.
- **Correction :**
  - Ajouter un tableau « Faisabilité » pour le jouet, avec une ligne par point : fournisseurs, échantillons, qualité, délais, personnalisation, emballage de marque, stockage et transport, règles de l'UE, santé de l'animal, substances, électronique, allégations.
  - Ajouter une ligne de synthèse par autre finaliste.

### I18. Signaux d'expansion de Woof omis (l. 176, 211)
- **Problème :** deux éléments des notes pourraient invalider la conclusion et n'apparaissent pas.
  - Woof Pet a déposé le 02/06/2026 des enregistrements internationaux de Madrid désignant le Royaume-Uni, dont une marque non identifiée pour « dog toys » et « edible dog treats ».
  - Ses produits sont déjà distribués au Royaume-Uni par des tiers (Pets Corner, PAWS Wholesale, wooof.co.uk).
- **Correction :** ajouter en l. 211 : « Woof a déposé en juin 2026 des marques internationales désignant au moins le Royaume-Uni, où ses produits sont déjà distribués par des tiers ; les éventuelles désignations dans l'UE ne sont pas connues (à vérifier dans WIPO Madrid Monitor). »

### I19. Réponse à la question 5 imprécise (l. 321)
- **Problème :** la question demande un budget minimal pour un test sérieux. La réponse donne trois montants (4 700 €, 14 923 €, 1 756 €) et qualifie de « vrai » un test qui ne l'est pas (B2).
- **Correction :** « Budget minimal d'un test sérieux : 14 923 € HT (1 000 kits L en maritime, huit vidéos, 2 520 € de publicité), à majorer d'un moule propriétaire si B3 l'impose. Avant de l'engager, un pré-test d'environ 4 700 à 5 330 € HT peut révéler un échec. »

### I20. Mauvais libellé de la ligne Vet's Best (l. 39)
- **Problème :** l'estimation de 20 000 unités par mois porte sur un **kit brosse-doigt et dentifrice** (ASIN B06XKJNFXX). « Sans brosse » est donc faux. La note signale aussi des confusions d'ASIN dans les rapports AsinSight (`us_grooming_hygiene.md`).
- **Correction :** « Kit brosse-doigt et dentifrice (Vet's Best) | environ 20 000 unités par mois estimées (AsinSight, 07/2026 ; fiabilité faible) ».

### I21. Oh Pacha : mauvaise date et décompte des marques (l. 52, 61)
- **Problème :** 08/2024 est la date de la plus ancienne vidéo sponsorisée trouvée, pas une date de lancement, qui reste inconnue (`pub_litiere_et_bouchees.md` §3). Oh Pacha ne fait pas partie des 13 marques comptées.
- **Correction :** « au moins depuis 08/2024 » ; « au moins 14 marques, dont une en vente directe (Oh Pacha) ».

### I22. « Quatre raisons démontrées » (l. 209)
- **Problème :** les preuves sont indirectes (extraits de moteur, absences de résultats). Seule la raison douanière repose sur un fait réglementaire.
- **Correction :** « pour quatre raisons, fondées sur des indices indirects ».

### I23. Chiffres incohérents d'une section à l'autre
- **Nombre d'avis.** « 8 à 64 avis » (l. 3 et l. 49) contre « 0 à 12 » (l. 190). Écrire : « de 0 avis pour les clones à 64 pour la meilleure balle de marque ».
- **Franchise de TVA.** « 2,16 à 5,75 € » (l. 230) couvre les cinq finalistes. Pour le jouet, écrire : « 4,03 € (duo) à 5,75 € (kit) ».
- **Réachat à 12 mois.** « seul le lot de deux pots de bouchées approche l'équilibre en douze mois (−0,14 €) […] soit le milieu ou le haut des repères publiés » (l. 77).
  - Le coffret de 6 mois d'additif s'en approche aussi (−5,24 €).
  - La condition d'attrition (7,1 % par mois) manque.
  - La note financière (§3.4) parle du « haut des repères ».
  - Corriger ces trois points.

---

## 3. Corrections mineures (clarté et précision)

- **M1, l. 7.** « compléments ingérables » se lit « impossibles à gérer ». Écrire « compléments à avaler » ou « compléments alimentaires ».
- **M2.** Abréviations non définies : « n.o. » (l. 189–190), « n.a. » (l. 226), « n.d. » (l. 168), « P / I / O » (l. 69), « [calcul] ». Ajouter une légende sous le premier tableau qui les emploie.
- **M3.** Jargon à expliquer dans un glossaire d'une page, en mots simples :
  - **publicité :** CPM (coût pour 1 000 affichages), taux de clic, CPA, ROAS, CPA et ROAS d'équilibre, UGC (vidéo tournée par un créateur rémunéré), phase d'apprentissage, Meta Ad Library ;
  - **finance :** marge contributive (ce qui reste d'une vente après produit, transport, frais et retours, avant publicité et frais fixes) ;
  - **achat et transport :** FOB (prix départ usine), minimum de commande, groupage, aérien DDP, point relais ;
  - **réglementation :** HAP, REACH, CLP, GPSR, TARIC, RTC, DDPP, Safety Gate, RappelConso ;
  - **classements et bases :** LOF, Inc. 5000, Wefunder, dépôt SEC, EUIPO, TMview, WIPO Madrid Monitor, Espacenet, DesignView.
- **M4, structure.** Les six parties demandées commencent à la ligne 138. Ajouter après le titre un sommaire et un encadré « Ce qu'il faut retenir » de 5 à 7 puces, et annoncer que l'entonnoir, les finalistes et les concepts publicitaires précèdent les parties A à F.
- **M5, l. 3.** Le paragraphe d'ouverture enchaîne plus de vingt chiffres d'un bloc. Le découper en puces : produit, preuve américaine, concurrence, rentabilité, recommandation, confiance.
- **M6, l. 230.**
  - « 13 € de CPM ([La Fabrique du Net]) » → « 13 € (milieu de la fourchette de 8 à 18 € relevée par La Fabrique du Net) ».
  - « 12 % de retours dans l'animalerie ([Wisepim]) » → ajouter « périmètre géographique non précisé ».
  - « Shopify Basic à 36 € par mois plus 40 € d'applications […] réparti sur 100 commandes ([Kanal]) » → préciser que les 40 € et les 100 commandes sont des hypothèses.
- **M7, l. 190.** « probablement Chine » → « origine non vérifiée (probablement Chine) ». Sortir Trixie, marque allemande, de la ligne des génériques.
- **M8, l. 207.** « trois requêtes sur des outils d'espionnage publicitaire (Minea, PPSPY, Dropispy) » → « une requête limitée à Minea, PPSPY et Dropispy, et deux requêtes générales ».
- **M9, l. 33.** Paw.com « CA estimé à 519 719 $ (Grips, 03/2024) » → « pour le seul mois de mars 2024 ».
- **M10, l. 171.** La mention « (PitchBook, relayé) » renvoie à CB Insights. Ajouter le lien Inc. (K. Haynes) qui relaie PitchBook.
- **M11, l. 254.** « Xiamen Newtop (balle et bac en silicone, dès 100 pièces) » mélange deux annonces. Écrire : « ensemble balle et bac en silicone dès 1 000 pièces ; balle seule dès 100 pièces à 3,80 $ ».
- **M12, l. 254.** « 8 à 11 fabricants » ne correspond pas au budget d'échantillons, prévu pour 4 à 8 fournisseurs. Aligner : 1 228 € pour 11 fournisseurs selon la note.
- **M13, l. 253.** « environ 84 € de produits » figure dans une colonne « budget HT » alors que ce sont des prix TTC. Écrire « environ 84 € TTC (environ 70 € HT) ».
- **M14, l. 288.** « livret de recettes validées par un vétérinaire » : budgéter la relecture ou écrire « relues par un vétérinaire (à prévoir) ».
- **M15, l. 329.** « elle transforme un stock européen en barrière à l'entrée » → « en avantage de coût ». Des concurrents stockent déjà dans l'UE (SmoothieDog ; Freezbone chez A Pet Store).
- **M16, l. 100.** « nerfs des enseignes françaises (Trixie, MultiFit, Nutrivet Inne) » → « nerfs vendus par des enseignes françaises ». Trixie est allemande et MultiFit est la marque propre de Maxi Zoo.
- **M17, l. 13.** « plus d'une centaine de pistes […], dont plus de soixante » : ces décomptes n'apparaissent dans aucune note. Ajouter une annexe listant les pistes, ou écrire « plusieurs dizaines de pistes ».
- **M18, l. 176.** Après « only within the USA », ajouter « (Canada et Royaume-Uni via des transporteurs tiers) ».
- **M19, l. 155.**
  - « limite REACH des HAP à 1 mg/kg » → « 1 mg/kg (limite générale ; 0,5 mg/kg pour les jouets d'enfants, à viser par prudence) ; phtalates sous 0,1 % (entrée 51) ».
  - Pour le règlement 183/2005, ajouter « sous réserve de règles nationales ».
- **M20, l. 206.** « plus de 33 000 vendeurs » → « selon TikTok ».
- **M21, l. 241.** « avec cinq achats, le vrai coût par achat se situe déjà entre 0,43 et 3,08 fois » → « même avec cinq achats, le vrai coût par achat peut aller de 0,43 à 3,08 fois la valeur observée ». « Déjà » laisse croire à une précision qui n'existe pas.
- **M22, l. 1.** Ajouter la date du rapport (28/10/2026) et la mention « version client ».
- **M23, l. 198.** Cdiscount « Aucune balle rechargeable » → « aucune balle rechargeable identifiée ». La note mentionne une « dog lick ball with suction cups » non précisée.

---

## 4. Contrôle de complétude, exigence par exigence

| Exigence du client | Statut | Où | Remarque |
|---|---|---|---|
| A — les dix rubriques (nom, fonctionnement, problème, cible, pourquoi ça se vend, pourquoi la France, argument, prix, confiance, page de référence) | Complet | l. 140–151 | Cible mal étiquetée (I10) ; argument non prouvé (I9) |
| B — marque, boutique officielle, lien produit, prix | Complet | l. 159 | — |
| B — preuve de CA, en disant si aucune n'est fiable | Complet | l. 161–172 | Bien traité : « aucune preuve fiable du CA » |
| B — preuve de demande | Complet | l. 174 | — |
| B — publicités si accessibles | Complet | l. 174 | Dater l'estimation BrandSearch (I14) |
| B — avis pertinents | Complet | l. 176 | — |
| B — pourquoi c'est un bon modèle | Complet, à corriger | l. 176 | I4, I5 |
| C — concurrents directs et indirects, prix | Complet | l. 182–192 | — |
| C — sites français qui le vendent déjà | Complet | l. 182–190, 203 | — |
| C — publicités françaises identifiées | Complet (non vérifié, déclaré comme tel) | l. 207, 211 | — |
| C — résultats Google et places de marché | **Incomplet** | l. 194–207 | Places de marché : oui. Google.fr : ni fourni ni déclaré non vérifié (B5) |
| C — pourquoi le marché paraît sous-exploité ; ce qui invaliderait la conclusion | Complet | l. 209–211 | « démontrées » (I22) ; signaux Madrid et Royaume-Uni absents (I18) |
| D — les huit lignes demandées | Complet | l. 215–226 | Exactes au centime |
| D — trois scénarios aux hypothèses expliquées | **Partiel** | l. 230 | Prudent et optimiste non détaillés (I13) |
| E — plan de 30 jours (fournisseurs et échantillons, analyse client, marque, Shopify, vidéos, campagnes, indicateurs, critères) | Présent mais irréaliste | l. 249–283 | B1, B2, B4 |
| E — trois offres commerciales | Complet | l. 285–289 | Ligne « Duo » à corriger (B1) |
| E — cinq angles publicitaires pour la France | Complet | l. 291–297 | Décret de 2015 (I8) |
| F — note sur 100 des cinq finalistes selon la grille | Complet | l. 301–309 | Pas de justification par critère ; incohérences (I11) |
| F — classement | Complet | l. 313 | — |
| F — réponses précises aux sept questions | Complet, Q5 imprécise | l. 315–323 | I19 ; Q6 à corriger (B1) |
| Trois concepts publicitaires par finaliste, six champs chacun | Complet | l. 83–136 | Quinze concepts, tous les champs remplis |
| Revue de faisabilité (douze points) | **Partielle, dispersée** | l. 155, 230, 245, 249–258 | I17 |
| Entonnoir d'au moins 20 produits avec motifs d'élimination | Complet | l. 13–41 | 25 éliminations et 5 finalistes ; « plus d'une centaine » non traçable (M17) |
| Top 5 analysé en profondeur aux États-Unis et en France | **Partiel** | l. 47–63 | Ni lien officiel ni prix US pour 4 finalistes (I16) |
| Lien source et date pour chaque affirmation commerciale importante | **Partiel** | tableau l. 15–41 ; l. 192, 241 | I14 |
| Distinction systématique entre faits, estimations, hypothèses et non vérifié | **Partiel** | l. 9 | I15 |
| Pas de confusion entre CA estimé, CA déclaré, trafic, vues et ventes | Respecté, avec une entorse | l. 81, 176 | Vues présentées comme moteur de croissance (I5) |
| Pas d'absence affirmée sans vérification | **Deux entorses** | l. 3, 57, 147 | I6 |
| Pas de marge théorique présentée comme bénéfice net | Respecté | l. 77, 228 | — |
| Déclaration honnête si aucun candidat ne remplit tous les critères | Respecté | l. 313 | — |

---

## 5. Vérification factuelle (82 lignes, plus de 100 chiffres)

Verdicts possibles : **Conforme** ; **Faux** ou **Contredit** ; **Incomplet** ; **Mal étiqueté** (mauvais statut) ; **Incohérent** ; **Source ou date manquante** ; **Invérifiable**.

| # | Affirmation du rapport (ligne) | Note de référence | Verdict | Commentaire |
|---|---|---|---|---|
| 1 | Woof n°3 de l'Inc. 5000 2025, +25 621 % sur 2021–2024 (l. 3, 165) | verification §1.1 n°1 | Conforme | Confirmé par Inc.com ; voir I4 pour le vocabulaire |
| 2 | n°1 « Consumer Products » (l. 165) | verification n°2 | Conforme | Déclaration de Woof (communiqué) |
| 3 | n°31 de l'Inc. 5000 2026, +7 939 % sur 2022–2025 (l. 3, 166) | verification n°3 | Conforme | — |
| 4 | Rachat annoncé le 06/08/2026, clos le 18/09/2026, montant non communiqué, première acquisition (l. 3, 172) | verification n°4–6 | Conforme | La date du 13/08 du premier tour est bien corrigée |
| 5 | Fondation en 2019 à Denver par Daniel Haarburger ; chien Milo opéré (l. 159) | verification n°8 ; us_verif §2 | Conforme | Deux versions de la blessure (rotule cassée ou luxation) : « genou » reste acceptable |
| 6 | Un seul tour d'amorçage de 1,69 M$ (Kokopelli), 02/2023 (l. 171) | verification n°9 | Source à compléter | Le relais de PitchBook est Inc. ou The Underbite, pas CB Insights (M10) |
| 7 | Essai « $40-Million-a-Year Business », année inconnue (l. 168) | us_verif §1 n°3 ; recherche web 3 | Conforme | Essai bien attribué à Haarburger ; CA non confirmé, bien étiqueté |
| 8 | Plancher de CA 2024 d'environ 25,7 M$ (l. 167) | us_verif §1 | Conforme | Calcul exact (100 000 $ × 257,21), bien étiqueté |
| 9 | Pupsicle à 19,99 $ quelle que soit la taille ; Pops 14,99 $ (13,49 $) ; Starter Pack 44,99, 55 ou 67 $ (l. 159) | verification §2.1 | Conforme | — |
| 10 | Environ 6 000 unités par mois sur Amazon US (AS Insight, 06/2026) (l. 169) | us_verif §4 | Conforme | Bien étiqueté « estimation d'outil » |
| 11 | Plus de 5 000 points de vente, dont plus de 1 600 PetSmart (11/2024) ; 2 270 Tractor Supply (l. 170) | us_verif §1 n°5–6 | Conforme | Déclaratif ; date Tractor Supply déduite |
| 12 | Walmart : 4,6/5 sur 1 718 avis, taille S (l. 174) | us_verif §4 | Conforme | Capture n.d. |
| 13 | Badge « 1730+ bought in past month » vu sur un miroir (l. 174) | us_verif §4 | Conforme | — |
| 14 | Glimpse : environ 51 000 recherches par mois (+166 %) ; Exploding Topics : 18 100 (l. 174) | us_verif §4 | Conforme | Estimations contradictoires, bien signalées |
| 15 | Instagram @mywoof : 136 000 abonnés (l. 174) | pub_jouet W4 | Conforme | Relevé du 28/10/2026 |
| 16 | 125 publicités Meta actives selon BrandSearch, pour le Bite n' Brush (l. 174) | us_verif §5 | Date manquante | Estimation tierce n.d. (I14) |
| 17 | Vidéos de créateurs « plafonnant à environ 3 700 j'aime » ; « Woof a grandi avec » (l. 81, 174, 327) | us_verif §4 ; pub_jouet | Mal étiqueté | Maximum vu en 07–08/2026, pas un plafond ; lien avec la croissance non démontré (I5) |
| 18 | Woof a grandi « par Amazon, la grande distribution et l'affiliation » (l. 176, 327) | us_verif §2 (« Canaux ») | Contredit | « Primarily direct-to-consumer » jusqu'en 11/2024 (I5) |
| 19 | « troisième croissance privée des États-Unis » (l. 176, 327) | us_verif §1 | Mal étiqueté | Rang dans un classement sur candidature, à données déclaratives (I4) |
| 20 | Brevets US 12 402 601 et 12 582 096 ; marque PUPSICLE enregistrée aux États-Unis ; rien en Europe (l. 176) | us_verif §3 ; verification n°17 | Incomplet | Dépôts de Madrid de 06/2026 et distribution britannique omis (I18) |
| 21 | Woof ne livre « only within the USA » (l. 176) | verification n°15 | Conforme | Ajouter Canada et Royaume-Uni via des tiers (M18) |
| 22 | Original chez Manavibe à 19,90, 23,90 et 26,90 €, épuisé ; Amazon.fr de 33,83 à 60,84 € (l. 184) | verification n°18, n°20 | Conforme | — |
| 23 | Freezball à 23,90, 26,90 et 29,90 € ; XL jusqu'à environ 50 kg (l. 185) | verification n°21 | Conforme | Le fabricant annonce environ 63 kg |
| 24 | SmoothieDog de 19,90 à 35 € ; 64 évaluations à 4,6/5 (l. 186) | verification n°22 ; fr_demande B11 | Conforme | — |
| 25 | Darryy à 45,99 € chez Leroy Merlin (l. 187) | verification §4.1 | Conforme | — |
| 26 | PetSafe à 7,99 €, environ 1 300 avis par variante (l. 188) | fr_deep §1.2 | Conforme | Compteurs peut-être mutualisés entre variantes |
| 27 | « Au moins 18 marques ou vendeurs » (l. 49, 192) | fr_deep §1.2 ; verification §4 | Source manquante (calcul non expliqué) | Défendable (16 relevés, plus Freezbone et Darryy), mais ce calcul n'apparaît dans aucune note : l'expliciter |
| 28 | « 8 à 64 avis par offre » (l. 3, 49) contre « 0 à 12 » (l. 190) | fr_demande B11–B14 ; fr_deep §1.2 | Incohérent | Les clones n'ont aucun avis visible (I23) |
| 29 | KONG Classic M en lot de 2 : plus de 6 700 ; LickiMat Soother : plus de 8 000 ; Toppl XL : environ 1 600, à environ 31,70 € (l. 153) | fr_demande B1, B5, B10 | Conforme | Compteurs multi-pays, signalé en l. 9 |
| 30 | LickiMat à 26–28 € (l. 192) | fr_demande §1.2 | Source manquante | Modèles Tuff Pro et Yoggie Pot, en rupture sur zooplus.fr (I14) |
| 31 | TikTok Shop France actif depuis le 31/03/2025 ; plus de 33 000 vendeurs en 03/2026 (l. 206) | verification n°31 | Conforme | Déclaré par TikTok (M20) |
| 32 | Droit forfaitaire de 3 € par ligne tarifaire depuis le 01/07/2026 (l. 209) | verification n°29 | Conforme | Divergences sur le champ (IOSS) signalées dans la note |
| 33 | 2 € de frais de traitement par article à partir du 01/11/2026 (l. 209) | verification n°30 ; recherche web 1 | Incomplet | Frais et date confirmés ; unité et publication au Journal officiel non tranchées (I7) |
| 34 | Environ 8 à 10 € par kit pour un vendeur transfrontalier (l. 209) | verification §5 | Conforme | Valable pour un kit balle + moule (deux lignes) |
| 35 | « 8 à 10 € par kit aux clones » (l. 329) | verification §5 | Faux | Une balle seule paie 3 € + 2 € = 5 € (I7) |
| 36 | Droits d'un stock importé : 0,10 à 0,20 € par kit (l. 209) | verification §5 ; analyse_financiere H19 et §4.3 | Incohérent | Le modèle retient 0,10 à 0,31 € (I7) |
| 37 | Maxi Zoo : 478 magasins (l. 211) | fr_deep §1 (LSA) | Conforme | — |
| 38 | Original en Allemagne à 24,99 €, XL à 29,99 € (l. 211) | verification n°20 | Conforme | — |
| 39 | Bow Wow Labs en 2023 : CA de 6,01 M$ (+17 %), marge brute de 51 %, perte nette de 1,22 M$ (l. 50, 57) | deep_support §1.1 | Conforme | Ajouter « déclaré, non audité, historique » |
| 40 | « La seule donnée financière déposée de l'étude » (l. 57) | us_feeding (10-Q de PetIQ, 8-K de BARK) | Faux | Le rapport cite lui-même deux dépôts SEC (I3) |
| 41 | Plus de 200 000 supports vendus (l. 50, 57) | deep_support §1.1 | Conforme | Déclaré en 2023 : dater |
| 42 | Environ 700 magasins Pet Supplies Plus en 08/2025 (l. 57) | deep_support §1.4 | Conforme | — |
| 43 | 636 évaluations pour un lot de nerfs sur Amazon.fr (l. 57) | deep_support §2 | Conforme | — |
| 44 | Chewise à environ 35,10 € ; PetTribes sur Zooplus ; Fruugo de 18 à 28 € (l. 57) | deep_support §2 | Conforme | Mais « n'existe qu'en offres transfrontalières » n'est pas établi (I6) |
| 45 | BullySafe de Woof à 19,99 $ (l. 317) | deep_support §1 | Conforme | — |
| 46 | Vetnique rachetée par Gryphon (2023), puis rachat de YuMOVE (2024) (l. 51, 59) | us_ingestible ; pub_litiere | Conforme | Avril 2023 ; juillet 2024 |
| 47 | 11 références dans 3 563 magasins Walmart (communiqué de 09/2025) (l. 59) | pub_litiere V7 | Conforme | Allégation de l'entreprise, bien attribuée |
| 48 | CA de Vetnique estimé entre 6,2 et 27,4 M$ (l. 59) | pub_litiere V8 | Conforme | Estimations d'outils, bien étiquetées |
| 49 | Glandex sur Amazon.fr : 4,2/5 sur 18 805, abonnement à −15 % ; aussi chez Cdiscount et Tom&Co (l. 59) | fr_deep_glandes §1 | Conforme | — |
| 50 | 10 marques de bouchées en France (l. 51) | fr_deep_glandes §7 | Conforme | — |
| 51 | Mars, 2021, « prix rapporté de 500 M$ à 1 Md$ » (l. 52, 61) | us_indoor_cats ; pub_litiere §1 | Incomplet | L'article d'Inc. cité dans la même phrase parle de 1,4 Md$, avec une finalisation en 2024 (I2) |
| 52 | Environ 20 % du CA brut en marketing ; CAC inférieur au revenu par client (l. 61) | pub_litiere P1–P2 | Conforme | Période non précisée |
| 53 | Plus de 50 millions de sacs (l. 52) | us_indoor_cats | Conforme | Déclaratif, n.d. |
| 54 | 13 marques de litière ou d'additif indicateur (l. 52, 61) | fr_deep_litiere §7 | Conforme | Oh Pacha s'y ajoute : au moins 14 (I21) |
| 55 | Nullodor (Demavic) à 6,49 € ; Tigerino VET à 16,49 € (l. 61) | fr_deep_litiere §1 | Conforme | — |
| 56 | Oh Pacha « depuis 08/2024 » ou « depuis 2024 » (l. 52, 61) | pub_litiere §3 | Mal étiqueté | « Au moins depuis 08/2024 » (I21) |
| 57 | Litière mensuelle : 1,38 € de marge par mois (l. 61) | analyse_financiere §2.3 | Conforme | — |
| 58 | Cat Amazing : 550 k$ en 2020, 720 k$ visés en 2022, accord non conclu en 03/2023 (l. 53, 63) | deep_boite §1 | Conforme | Déclaré, historique |
| 59 | Badge « 600+ bought in past month » (l. 53, 63) | deep_boite §1 | Conforme | Date inconnue, signalée |
| 60 | Original à 51,40 € ; boîtes en bois de 19,99 à 25 € ; labyrinthe Action à 2,99 € ; 1,58 kg de poids volumétrique (l. 63) | deep_boite §2 | Conforme | Le labyrinthe d'Action est à balles, pas à friandises |
| 61 | Tableau de rentabilité de la partie D, 54 cellules (l. 217–226) | analyse_financiere §2.1 | Conforme | Recalculé : lignes 2 à 8, CPA et ROAS d'équilibre exacts |
| 62 | CPA de 94,61, 39,88 et 14,05 € et formule de calcul (l. 67, 230) | analyse_financiere §1.2 | Conforme | — |
| 63 | Tableau comparatif des cinq finalistes (l. 71–75) | analyse_financiere §6.1 | Conforme | — |
| 64 | Tableau de sensibilité au CPA (l. 236–237) | analyse_financiere §6.3 | Conforme | — |
| 65 | Budgets de 4 700, 14 923 et 1 756 € ; 648 € récupérés (l. 3, 258, 283, 321) | analyse_financiere §5 | Conforme aux notes | Usage incohérent dans le plan (B2) |
| 66 | 10,5 à 19,5 semaines (catalogue, aérien) ; 14,5 à 35,5 semaines (moule propriétaire, aérien) ; Nouvel An chinois le 06/02/2027 (l. 249) | sourcing §3 | Conforme | — |
| 67 | Micro-entreprise en franchise : 2,16 à 5,75 € de perte en plus (l. 230) | analyse_financiere §2.7 | Incohérent | Fourchette des cinq finalistes ; pour le jouet, 4,03 à 5,75 € (I23) |
| 68 | Meta Pilou : 65,69 € (2 achats), 112,08 €, 22,22 €, 120,76 € sans achat, soit 386,44 € et 96,61 € par achat (l. 241) | aucune note | Invérifiable | Exact si 65,69 € est un coût par achat ; 320,75 € et 80,19 € si c'est la dépense (I1) |
| 69 | Intervalle de 0,43 à 3,08 fois avec 5 achats (l. 241) | analyse_financiere §5.2 | Conforme | — |
| 70 | LOF 2025 : Golden Retriever 15 062, Berger Australien 14 609 (l. 145) | fr_demande F1 | Conforme | — |
| 71 | Moins de 35 ans, environ 150 € par mois (l. 145) | fr_demande §1.3 ; fr_market_landscape | Mal étiqueté | Sondage déclaratif, tous animaux ; ce n'est pas une donnée sur les clients Pilou (I10) |
| 72 | 52 à 53 jours de vague de chaleur en 2026 (l. 146, 296) | fr_demande E2 | Conforme | — |
| 73 | Pupsicle L : 9,1 cm (11–34 kg) ; XL : 12,2 cm ; catalogue limité à 8 cm (l. 155) | us_verif §2 ; sourcing §1 | Conforme | Contradictoire avec le chiffrage du « kit L » (B3) |
| 74 | Limite REACH des HAP à 1 mg/kg (l. 155) | sourcing §3.2 | Incomplet | 0,5 mg/kg à viser par prudence ; phtalates absents (M19, I17) |
| 75 | Vente au détail d'aliments pour animaux exclue du règlement 183/2005 (l. 155) | sourcing §4 | Conforme | Sous réserve de règles nationales (M19) |
| 76 | Rappel de Purina Australie en 02/2026 (l. 155) | verification n°34 | Conforme | — |
| 77 | Moules de compression de 500 à 3 500 $ par jeu (l. 155) | sourcing §2 | Conforme | — |
| 78 | Vidéo UGC de 170 à 320 € en France (l. 81) | pub_jouet §2 | Conforme | — |
| 79 | Golden retriever : plus de 1,4 million de vues (l. 81) | pub_jouet C1 | Date manquante | Probablement 2023, historique (I14) |
| 80 | Vet's Best « hygiène dentaire sans brosse », environ 20 000 unités par mois (l. 39) | us_grooming_hygiene §1 | Mal étiqueté | C'est un kit brosse-doigt et dentifrice (I20) |
| 81 | Rocco & Roxie racheté 26,5 M$ (01/2023, SEC) ; Angry Orange à 3,9/5 sur 1 168 (l. 17) | us_feeding ; fr_screening | Conforme | — |
| 82 | Autres chiffres du tableau des éliminations (l. 18–41) : Snuggle Puppy 64 632 notes ; K9 Sport Sack 510 k$/mois ; Help 'Em Up 625 avis et 109–173 € ; ToeGrips 3 449 avis ; Litter-Robot environ 300 M$ ; One Fast Cat 179–195 $ ; Panther Armor 11 784 ; Wuffes n°400 ; Zesty Paws 610 M$ ; BarkBox 86,6 M$ (−25 %) ; DoggieLawn 436 k$/mois ; Halo 75 M$ ; FluentPet 7 M$ ; Joyride 41 674+ ; Ruff Liners 3,1 M$ ; Paw.com 519 719 $ ; Pawnix 105 k$ ; Gerty environ 200 unités ; ThunderShirt environ 55 000 avis ; Best Friends 69 195 notes et rachat en 2021 ; MudBuster 62 000 avis ; Cuddle Clones 3,5 M$ | notes us_* ; fr_screening ; us_decouverte | Conforme | Dates et sources françaises manquantes sur plusieurs lignes (I14) ; Paw.com : mois de mars 2024 seulement (M9) |

---

## 6. Cohérence interne

### 6.1 Notes de la grille et preuves
- Le classement est robuste : même en corrigeant les points de I11, le jouet garde au moins 66 points, et les bouchées restent deuxièmes avec 59.
- Mais trois notes sont mal reliées aux preuves :
  - concurrence « moyenne » partout contre des notes de 5 à 12 sur 20 ;
  - marge de la boîte à 9, comme le jouet, malgré une meilleure marge ;
  - faisabilité du jouet à 8 malgré la dépendance à un moule propriétaire (B3).
- Aucune note n'est justifiée critère par critère.

### 6.2 Recommandation et résultats financiers
- La recommandation reste défendable (preuve américaine, démonstration, audience Pilou). Mais le rapport doit dire que :
  - le jouet est, avec le support, le finaliste dont l'équilibre est le plus exigeant (I12) ;
  - le seuil de poursuite est trop haut (B1) ;
  - les tests proposés ne mesurent pas ce qu'ils annoncent (B2) ;
  - ces tests ne portent pas sur le produit recommandé (B3).
- Les bouchées en lot approchent l'équilibre sur 12 mois (−0,14 €) mais sont écartées pour des raisons stratégiques : leader déjà présent, cible de petites races. Cet arbitrage est cohérent ; il gagnerait à être écrit tel quel en Q1.

### 6.3 Chiffres repris à plusieurs endroits
- **Cohérents :**
  - 96,61 € (l. 3, 241, 322) ;
  - 18 à 20 € (l. 3, 279, 283, 322), cohérent mais faux (B1) ;
  - 4 700 € et 14 923 € (l. 3, 75, 258, 283, 321) ;
  - 10,26 €, 18,41 € et 39,88 € (partout) ;
  - 52 à 53 jours (l. 146, 296) ;
  - 25 mois et 4 040 € (l. 245) ;
  - 1,69 M$ et 5 000 points de vente (l. 171, 176, 327) ;
  - au moins 18 marques (l. 49, 192).
- **Incohérents :**
  - « 8 à 64 » contre « 0 à 12 » avis ;
  - 0,10–0,20 € contre 0,10–0,31 € de droits ;
  - « 2,16 à 5,75 € » appliqué au seul jouet ;
  - « facteur 5 » contre 7,6 avec le mix supposé ;
  - « 8 à 10 € » appliqué aux clones ;
  - « concurrence moyenne » contre 5/20 ;
  - « depuis 2024 » contre « depuis 08/2024 » ;
  - « vrai coût par achat » (l. 3, 321) contre « ne mesure que le coût par ajout au panier » (fin de l. 321) et « le vrai coût par achat se mesurera à l'arrivée du premier lot » (l. 249).

---

## 7. Clarté pour un lecteur non technique

- **Structure.**
  - 137 lignes précèdent la partie A.
  - Le lecteur qui attend les six parties demandées ne trouve ni sommaire ni encadré de synthèse.
  - Le paragraphe d'ouverture et plusieurs paragraphes de la partie D (l. 230, 245) dépassent 150 mots et alignent des dizaines de chiffres.
- **Jargon non expliqué.**
  - Publicité : CPM, ROAS, UGC, Meta Ad Library.
  - Achat : FOB.
  - Réglementation : HAP, REACH, CLP, TARIC, DDPP.
  - Classements et bases : LOF, Inc. 5000, EUIPO, TMview, Espacenet, DesignView.
  - Abréviations : n.o., n.a., P / I / O.
  - « Marge contributive » n'est jamais définie en une phrase.
- **Mot ambigu.** « Ingérables » (l. 7) se lit « impossibles à gérer ».
- **Ce qui est bien fait.** Les tableaux A et F sont lisibles ; les règles de décision sont formulées en verbes d'action ; les limites de l'étude sont annoncées tôt (l. 9).

---

## 8. Recherches web de l'audit (3 sur 10)

1. **Frais de traitement de 2 € (UE).** Frais confirmés à partir de novembre 2026 (accord du 26/03/2026). Unité « par article » ou « par envoi » selon les sources. Une source cite l'acte C(2026) 6694 du 21/09 sans le numéro 2026/2152. Sources : [RSM Belgique](https://www.rsm.global/belgium/en/insights/eu-introduces-new-charges-low-value-imports) ; [Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/18538/eu-handling-fee-2-euro-non-eu-parcels) ; [DHL](https://www.dhl.com/gb-en/ecommerce/uk/international-parcel-delivery/eu-customs-changes-2026.html) ; [Transglobal Express](https://www.transglobalexpress.co.uk/news/1593/) ; [Connexion France](https://www.connexionfrance.com/news/why-your-parcels-may-soon-become-more-expensive-in-france/753459) ; [byrd](https://blog.getbyrd.com/en/de-minimis-eu) ; [PwC Italie](https://blog.pwc.it/?p=23058).
2. **Prix du rachat de PrettyLitter.** Seuls « 500 M$ à 1 Md$ » (Bloomberg, article du 07/09/2021) et « 1 Md$ » (Wikipedia) sont retrouvés. Le 1,4 Md$ d'Inc. n'est ni confirmé ni infirmé. Sources : [Bloomberg](https://www.bloomberg.com/news/articles/2021-09-07/mars-is-said-to-acquire-prettylitter-for-under-1-billion) ; [BloombergQuint](https://www.bloombergquint.com/business/mars-is-said-to-acquire-prettylitter-for-under-1-billion) ; [Wikipedia](https://en.wikipedia.org/wiki/PrettyLitter).
3. **Essai « $40-Million-a-Year Business From My Garage ».** Essai recueilli par Amanda Breen auprès du fondateur de Woof, Daniel Haarburger (croissance de 6 000 % de 2021 à 2023) ; année du CA de 40 M$ non visible. Sources : [Entrepreneur](https://www.entrepreneur.com/starting-a-business/how-i-built-a-40-million-a-year-business-from-my-garage/489463) ; [JingSourcing](https://jingsourcing.com/fb-dog-treat-toy/) ; [mywoof.com, About us](https://mywoof.com/pages/about-us) ; [City Lifestyle](https://citylifestyle.com/articles/inventing-for-mans-best-friend) ; [U.S. Chamber](https://uschamber.com/co/profiles/woof).
