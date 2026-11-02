# Contre-vérification : la douleur que résout une station de repas surélevée anti-dégâts (relevé du 02/11/2026)

Conventions de lecture (ce ne sont pas des constats) :
- **Objet** : essayer de réfuter les affirmations clés des trois notes sœurs, puis trancher une question. La douleur est-elle assez forte pour qu'un maître français de grand chien paie environ 49,90 € une station anti-dégâts (référence américaine : Neater Feeder), alors qu'un tapis ou une gamelle anti-éclaboussures à 10–15 € existe ?
- **Notes contrôlées** : les trois fichiers sont présents et ont été lus en entier.
  - `us_voix_client.md` : requêtes V1 à V22 ;
  - `fr_voix_client.md` : requêtes Q1 à Q22 ;
  - `objections_substituts.md` : requêtes O1 à O14.
- **Méthode** :
  - 12 requêtes WebSearch en mode « standard », toutes le 02/11/2026 (W1 à W12). Le quota est atteint.
  - 1 WebFetch tenté (F1, sur PubMed) : **échec** `getaddrinfo ENOTFOUND pubmed.ncbi.nlm.nih.gov`. Le message d'erreur demande de ne pas essayer d'autres sites. **Aucune page n'a donc été ouverte** : tout vient des extraits et des synthèses du moteur.
  - Pour lire les pages, il faut autoriser ces domaines dans les réglages réseau de la session : pubmed.ncbi.nlm.nih.gov, plus ceux déjà signalés par les notes sœurs (www.chien.com, www.desertcart.lk, veterinaryevidence.org).
  - Ni Bash ni curl.
- **Verdicts** :
  - **confirmé** : j'ai revu le texte ou le chiffre dans mes propres résultats ;
  - **plausible** : cohérent avec ce que j'ai vu, mais pas retrouvé ;
  - **réfuté** : contredit ou mal cité ;
  - **non vérifiable**.
  - Dans le doute, jamais « confirmé ». Un texte « confirmé » reste un extrait moteur, que le moteur a pu retoucher.
- **Étiquettes** : [VERBATIM], [ARTICLE], [ÉTUDE], [AVIS], [H] hypothèse ou jugement, [calc] calcul ; « extrait moteur » ; « reformulation moteur » (ce n'est pas une citation).
- **Renvois** : A1 à A12 désignent les affirmations de la section 1. W1 à W12 et F1 renvoient au journal, en fin de note.

## 1. Verdicts sur les 12 affirmations qui comptent

### Takeaway
- **5 affirmations confirmées** : le parquet abîmé de Hometalk (A5), le texte « sooooo worth it » (A7), l'objection santé (A10), les prix des substituts (A11) et le volume d'avis américain (A12).
- **7 plausibles** : aucune n'est contredite, mais leur mot à mot ou leur comptage n'a pas été retrouvé.
- **Aucune affirmation n'est réfutée sur le texte.** Deux le sont sur le **contexte** :
  - la citation de soulagement américaine la plus forte vient d'un maître de **chat** (A7) ;
  - la parade « hauteur basse » contre l'objection santé ne tient pas pour les grandes races (A10).
- Point de lecture : les deux verbatims de soulagement français viennent d'acheteurs de **substituts** (A9).

### Tableau
| # | Affirmation (note d'origine) | Verdict |
|---|---|---|
| A1 | Classement américain : la traînée d'eau (8 sources de maîtres) et l'eau autour de la gamelle (7) dominent à égalité, devant le sol abîmé (3) et le nettoyage (3) (US §1.1) | plausible |
| A2 | Aux États-Unis, douleur quotidienne d'intensité modérée ; forte quand un parquet ou un stratifié est abîmé (US §2) | plausible |
| A3 | En France, intensité faible à modérée, ton de l'anecdote amusée, voix mince et ancienne (FR §1–2) | plausible |
| A4 | Les plus touchés : grands chiens baveurs ou gros buveurs et chiens barbus, surtout sur parquet ; la station ne règle pas la traînée (US §3 et §5, FR §3) | plausible |
| A5 | Hometalk : parquet abîmé sur 8 × 8 pouces sous la gamelle, serviette jamais changée (US §1.2 C) | confirmé |
| A6 | Verbatims américains du goldendoodle (Houzz), du briard et du braque de Weimar (US §1.2) | plausible |
| A7 | « Expensive but sooooo worth it and a problem solver indeed!!! » (US §2) | confirmé (texte) ; c'est un maître de chat |
| A8 | Fil chien.com t2146 : « boit comme un cochon », « il en fout partout » (FR §1.1) | plausible |
| A9 | Avis Zooplus « … TERMINÉ!!! » et « Plus d'éclaboussures et plus d'eau transportée dans les babines ! » (FR §1.1 et §1.3) | plausible |
| A10 | Objection santé : Glickman et al. (2000) et la synthèse vétérinaire de Buckley (objections §2) | confirmé |
| A11 | Substituts : tapis TIAKI à 8,19 €, gamelle Love Story à 14,49 €, soit 22,68 € ensemble (objections §1) | confirmé |
| A12 | Volume américain : ≈ 33 770 notes Amazon à 4,6/5 (pages miroirs) ; prix courant ≈ 50 $ (US §2) | confirmé (ordre de grandeur) |

### Détail par affirmation

**A1 — Classement américain des thèmes : plausible**
- Revu :
  - les fils Hometalk et Houzz « dog vs hardwood » existent (W3), ainsi que le fil Straight Dope « my dog is a sloppy drinker » (W1, page 2) — [Straight Dope](https://boards.straightdope.com/t/my-dog-is-a-sloppy-drinker/781181?page=2) ;
  - reformulation moteur d'un avis sur le modèle Express : un chien qui boit puis part en courant laisse encore de l'eau au sol, même si le bac récupère le trop-plein (W4).
- Pas revu : les deux verbatims phares du thème « traînée » (W1, W2 ; voir A6).
- Ce qui est surévalué :
  - 8 contre 7 n'est pas un écart ;
  - les comptages viennent de requêtes ciblées, comme la note le dit elle-même ;
  - plusieurs sources comptées comme voix de maîtres sont des reformulations ou des attributions incertaines.
- Lecture défendable : **deux thèmes dominent**, l'eau à la gamelle et la traînée ; les autres sont marginaux. Ce n'est pas un classement.

**A2 — Intensité américaine : plausible**
- Revu (W3), sur le fil Hometalk (synthèse moteur) :
  - une réponse conseille de poncer pour voir si la tache part, et de remplacer les lames si le dégât est plus étendu ;
  - la gamelle a ensuite été déplacée sur du carrelage.
- Cela appuie « forte quand le sol en bois est abîmé ». Aucune de mes 12 requêtes ne fait remonter un vocabulaire de détresse. « Modérée » reste un jugement de la note, non contredit.
- Dans les mêmes résultats, des guides conseillent un tapis étanche à rebord sous les gamelles, ou de les poser sur du carrelage ou du vinyle (W3). La parade bon marché est la première recommandée.
- Nuance : le volume américain (A12) montre une douleur **répandue**, pas une douleur **intense**.

**A3 — Intensité française : plausible**
- Revu (W6) : le fil « Peut-il boire proprement ? » existe — [chien.com t2146](https://www.chien.com/forum/f6/peut-il-boire-proprement-t2146/). Selon la synthèse moteur :
  - le maître décrit un chien qui éclabousse tout en buvant, un « barbare de la boisson » qu'il compare à un cochon ;
  - « Les réponses de ce fil sont courtes et ne donnent pas de solution concrète ».
- Même requête, extrait moteur d'un site non identifié : « plus le chien est gros, plus il s'abreuve en faisant de grosses éclaboussures, voire même du bruit ». L'attribution est incertaine entre deux pages de chien.com ([quantité d'eau](https://www.chien.com/alimentation/quantite-eau-pour-chien-21502.php), [fontaine](https://www.chien.com/accessoires-objets-pour-chien-67/fontaine-a-eau-pour-chien-3160.php)). Le moteur en conclut que le désordre est courant et ne signale pas un problème (interprétation moteur).
- Pas revu : les deux avis Zooplus (W5, W9). Le moteur, réglé sur les États-Unis, indexe mal ces avis : ce silence ne prouve rien.
- Le ton de normalisation et la minceur de la voix française sont appuyés. **L'intensité française peut toutefois être sous-estimée**, à cause de ce biais d'indexation.
- Contradiction mineure : si les réponses de t2146 ne proposent pas de solution, le verbatim « support à hauteur de sa tête », que la note rattachait à t2146 ou à t2027, vient plus probablement de [t2027](https://www.chien.com/forum/f46/il-renverse-son-eau-t2027/).

**A4 — Profils les plus touchés : plausible**
- Cohérent avec W3 (parquet), W4 (chien qui part en buvant) et W6 (gros chien, grosses éclaboussures).
- Pas revu : l'avis du braque de Weimar (W8), celui du terre-neuve de 130 lb.
- Point adverse 1 : le profil le plus « émotionnel » chez les Américains, le chien barbu qui s'éloigne en gouttant, est celui que la station sert le moins (W4).
- Point adverse 2 [H, connaissance préalable, **non vérifiée dans cette session**] : à ma connaissance, la cohorte de Glickman et al. (2000) comprenait le terre-neuve, le braque de Weimar, le dogue allemand et le caniche royal parmi ses 11 races. Si c'est exact, les chiens qui souffrent le plus du désordre appartiennent au groupe étudié pour le risque de torsion (A10).

**A5 — Parquet abîmé, Hometalk : confirmé**
- Revu mot pour mot, comme titre de page (W3) : « Wood floors has water damage from dog water bowl. Area approx 8" x 8" » — [Hometalk](https://www.hometalk.com/diy/floors-ceilings/q-wood-floors-has-water-damage-from-dog-water-bowl-area-approx-8-x-8-32956153).
- La serviette est revue **sur le fond** : le mari avait laissé une serviette sous la gamelle sans la changer quand elle était mouillée (synthèse moteur). La phrase « He had a towel under the bowl but did not switch it out when it got wet. » n'est pas réaffichée.
- En publicité, n'utiliser que le titre.

**A6 — Verbatims du goldendoodle, du briard et du braque de Weimar : plausible**
- Recherches à la phrase exacte : aucune correspondance (W1, W2, W8).
- Seul le fil [Houzz « dog vs hardwood »](https://www.houzz.com/discussions/5306356/dog-vs-hardwood) est revu (W3). Les pages Dog Trick Academy et desertcart AR ne remontent pas.
- Rien ne les contredit, mais le mot à mot n'est pas garanti. Le braque de Weimar était déjà « [VERBATIM ?] » dans la note.

**A7 — « Expensive but sooooo worth it and a problem solver indeed!!! » : confirmé (texte), contexte corrigé**
- Revu (W4) : selon le moteur, la phrase exacte vient d'un avis d'acheteur vérifié sur une fiche revendeur du Neater Feeder Deluxe. Attribution probable : [shopabunda](https://www.shopabunda.com/products/neater-pet-brands-neater-feeder-deluxe-for-dogs-mess-proof-elevated-bowls-no-slip-non-tip-double-diner-stainless-steel-food-dish-with-stand-68f2bb41-7ddd-4f92-9c22-0833213bf36b). D'après la synthèse, l'acheteur « had bought another for a second cat ».
- C'est donc probablement un maître de **chat**. La note américaine, centrée sur les chiens, la classe dans le « soulagement après achat » sans le préciser. **Ce n'est pas une voix de maître de chien.**

**A8 — Fil chien.com t2146 : plausible**
- Revu (W6) : le fil et la comparaison au cochon. Ma requête contenait « il en fout partout » entre guillemets, et le moteur dit que le fil y « correspond exactement ».
- Pas réaffichés mot pour mot : « boit comme un cochon » et « il en fout partout ». La date de 2006 n'est pas réaffichée non plus.
- Fortement étayé, mais pas « confirmé ».

**A9 — Avis Zooplus « TERMINÉ!!! » et « Plus d'éclaboussures… » : plausible**
- Pas retrouvés à la phrase exacte (W5, W9).
- Point adverse : les deux avis portent sur **un substitut**, une gamelle de voyage anti-renversement (fiche 624018, 4,4/5 sur 8 avis selon la note sœur, prix non relevé). Ils prouvent la douleur. Ils montrent aussi qu'une simple gamelle l'a réglée pour ces maîtres. Ils plaident donc **contre** le besoin d'une station à 50 €, et ne peuvent pas servir de témoignage pour elle.

**A10 — Objection santé : confirmé**
- Revu (W7) :
  - [Vetcontact](https://www.vetcontact.com/en/art.php?a=214) résume Glickman et al. (2000), *JAVMA* 217(10):1492–1499 selon le moteur. La gamelle surélevée y expliquerait environ 20 % des cas de dilatation-torsion chez les grandes races et 52 % chez les races géantes. Plus de 1 600 chiens ont été suivis ;
  - la synthèse de Louise Buckley dans Veterinary Evidence ([copie distantreader](https://distantreader.org/stacks/journals/ve01/ve01-57.htm), [dépôt HAU](https://hau.repository.guildhe.ac.uk/15070)) :
    - l'effet dépend de la taille : risque avec une gamelle ≤ 1 pied chez les grandes races, > 1 pied chez les races géantes ;
    - aucune étude ne montre que la surélévation réduit le risque ;
    - risque relatif de 2,17 (IC 95 % 1,27–3,71), et environ 4 % de cas attribuables ;
    - conseil : nourrir au sol les chiens à risque ;
  - la [thèse de Purdue](https://docs.lib.purdue.edu/dissertations/AAI3099198), sur la même cohorte.
- Pas réaffiché : « only two studies… conflict », qui reste plausible. Les sources françaises (Purina Institute FR, conseils-animaux.fr) n'ont pas été revues.
- Non tranché : 20 et 52 % contre « environ 4 % ». Le moteur parle de deux mesures différentes, sans l'expliquer.
- Point adverse : la parade « retenir la plus faible hauteur » (objections §2) **ne désamorce pas l'objection pour les grandes races**. Dans le résumé de l'étude, c'est justement la classe ≤ 1 pied (30,5 cm) qui leur est associée au risque. La Deluxe L sert à 8 pouces (20,3 cm), 11 avec rallonges.

**A11 — Prix des substituts : confirmé**
- Revu (W10) : « Tapis pour gamelle en forme d'os, noir pour chien, L 51 x l 38 x h 1 cm, 8,19 € », en silicone, à bords surélevés, antidérapant — [Zooplus 2104097](https://www.zooplus.fr/shop/chiens/ecuelles_distributeur_nourriture_chien/set_de_table_chien/2104097). La version zooplus.com l'affiche à 6,49 €.
- Revu (W11) : « Love Story - Gamelle anti éclaboussures pour chien » à 14,49 € sur une page de liste Zooplus (page exacte incertaine), « Vendu et expédié par TOILINUX.COM » ; diamètre 17 cm, hauteur 8 cm, 0,47 kg — [Zooplus 9980060840](https://www.zooplus.fr/shop/chiens/bols_gamelles_fontaines/gamelles/9980060840). Sur la même liste, ZooVenture est à 25,99 €.
- [calc] 8,19 + 14,49 = 22,68 €, soit 45 % de 49,90 € : le calcul est juste.
- Ce qui joue pour la station : ces substituts sont petits pour un grand chien. Le tapis fait 1 cm de haut au total, la gamelle 17 cm de diamètre.
- Revu aussi : le bandeau Zooplus « LIVRAISON OFFERTE dès 59 € | Point relais dès 0,49 €* » (titres de pages, W10).

**A12 — Volume américain : confirmé (ordre de grandeur)**
- Revu (W12), sur des pages miroirs d'Amazon et non sur Amazon :
  - « 4.6 out of 5 stars (33,770) » sur une fiche que le moteur rattache au modèle Express (fiche exacte non identifiée) ;
  - pour le Deluxe : 4,7/5 sur 24 374 notes (shopabunda) ; 4,7/5 sur 21 711 avis (desertcart.lk) ; 4,6/5 sur 4 040 avis ([desertcart NI](https://www.desertcart.ni/products/7723851)) ;
  - Walmart, modèle Express : 4,6/5 sur 469 notes ([Walmart](https://www.walmart.com/ip/410938365)).
- Revu (W4) : [Hip2Save](https://hip2save.com/?p=10761399), « Mess-Free Deluxe Dog or Cat Feeder Just $20.84 on Amazon (Regularly $50) » ; le titre Yahoo « This Genius Amazon Product Will Stop Your Dog's Messy Drinking ».
- Nuances : les compteurs regroupent des variantes, et leurs dates sont inconnues. Une part des avis vient de foyers de chats (A7 ; note US §3).

## 2. Ce que les notes surévaluent, et ce qu'elles sous-évaluent
- **Surévalué** :
  - le classement américain, à lire comme deux thèmes dominants (A1) ;
  - le soulagement américain : la citation la plus forte vient d'un maître de chat, et le volume d'avis mêle chats et chiens (A7, A12) ;
  - la parade « hauteur basse » contre l'objection santé (A10).
- **Mal lu** : les deux soulagements français viennent d'acheteurs de substituts (A9). Ils prouvent la douleur, et ils montrent qu'un autre produit l'a réglée.
- **Peut-être sous-évalué** : l'intensité française, parce que le moteur indexe mal les avis et les forums français (A3). Aucune de mes requêtes ne permet de trancher.
- **Solide** : l'existence de substituts à 8–15 € (A11), l'objection santé (A10), et le parquet abîmé comme levier le plus fort (A5).

## 3. La douleur est-elle assez forte pour payer environ 50 € ?

### Ce qui plaide pour une douleur forte
1. **Les Américains paient déjà ce prix, alors que des substituts bon marché existent aussi chez eux.** Les fiches miroirs affichent des milliers à des dizaines de milliers de notes à 4,6–4,7/5, pour un prix courant d'environ 50 $ (A12). Des tapis WaterHog et des gamelles à flotteur y sont vendus (note US §4) : ils n'ont pas empêché ce marché.
2. **La gêne revient à chaque prise d'eau**, tous les jours. Elle devient coûteuse sur parquet ou stratifié : tache de 20 × 20 cm, ponçage ou lames à remplacer (A5, A2).
3. **Les substituts à 8–15 € sont dimensionnés pour des chiens moyens** : tapis de 1 cm de haut, gamelle de 17 cm de diamètre (A11). Les échecs relevés aux États-Unis touchent justement les gros buveurs : eau sous le tapis, disque refusé ou démonté, bol trop petit (note US §4).
4. **Des maîtres français bricolent déjà l'architecture de la station** : support « à hauteur de sa tête », rebord, gamelle fixée au sol ou au mur, béton coulé (note FR §1.3–1.4, plausible). La demande d'une solution intégrée existe à l'état latent.
5. **Le soulagement après achat se dit plus fort que la plainte** (« TERMINÉ!!! », « sooooo worth it »). Une démonstration avant/après a donc de quoi convertir.

### Ce qui plaide contre
1. **En France, la douleur est peu dite, et dite en riant.** L'essentiel tient en un fil de 2006, qui revient dans 7 requêtes sur 22 selon la note FR : un « barbare de la boisson » comparé à un cochon, et des réponses qui ne proposent rien (A3, A8). On n'y trouve ni « marre », ni « ras-le-bol », ni « cauchemar ». Les compteurs d'avis français sont minuscules : 8 et 23 avis.
2. **Un substitut à 8–15 € suffit à beaucoup.** Zooplus vend un tapis à bords surélevés à 8,19 € et une gamelle anti-éclaboussures à 14,49 €. Les deux coûtent 22,68 €, soit 45 % du prix visé (A11). Les seuls maîtres français soulagés qu'on a trouvés l'ont été par des substituts (A9), et des acheteurs de tapis sont satisfaits (« le rebord retient l'eau », note FR, plausible).
3. **Le mot « surélevée » déclenche une objection santé chez la cible même.** Glickman et al. (2000) attribue à la gamelle surélevée environ 20 % des cas de torsion chez les grandes races, et la synthèse vétérinaire conseille de nourrir au sol les chiens à risque (A10). Baisser la hauteur ne suffit pas chez les grandes races.
4. **La station ne règle pas le problème le plus vivement décrit** : la traînée du chien qui part en gouttant, la bave sur les murs (A4). Elle ajoute un bac à vider et occupe 53 × 33 cm au sol (objections §3.2).
5. **Le levier le plus fort aux États-Unis, le parquet abîmé, n'est pas documenté en France.** Les maîtres français ne citent que le carrelage (note FR §3). [H] Sur du carrelage, la flaque est une corvée, pas un dégât.
6. **Le volume américain surestime la douleur canine**, car une part des avis vient de maîtres de chats (A7, A12).

### Conclusion
- **Note : moyenne.** La douleur est réelle et quotidienne. Elle est d'intensité modérée pour la majorité des maîtres, et forte pour une niche.
- **Pour le maître français type d'un grand chien**, dont la gamelle est posée sur du carrelage, la douleur est plutôt faible. Un tapis à 8 € ou une gamelle à 14 € règle « assez » le problème, et le mot « surélevée » ajoute une crainte pour la santé. À 49,90 €, il n'achètera pas sans démonstration.
- **La douleur justifie 50 € quand trois conditions se cumulent** :
  - un grand chien qui boit salement ou bave beaucoup ;
  - un sol qui craint l'eau (parquet, stratifié), ou l'impossibilité de sortir la gamelle ;
  - des substituts bon marché déjà essayés sans succès.
- **Conséquence pour la publicité** [H] : il faut **montrer** le problème et la différence avec le tapis, au lieu de compter sur une frustration déjà vive. L'objection santé doit être traitée sur la page produit, sans aucune allégation de santé.

### Profils pour lesquels la douleur est la plus forte
1. Le maître d'un grand chien qui boit très salement ou bave beaucoup (labrador qui boit « comme un aspirateur », terre-neuve, dogue de Bordeaux, mastiff), dont la gamelle est posée sur du parquet ou du stratifié.
2. Le même maître après l'échec du tapis et de la gamelle à disque flottant : eau sous le tapis, disque refusé ou démonté, bol trop petit.
3. Le maître en appartement, sans extérieur ni garage où sortir la gamelle d'eau [H].
4. Le maître d'un chien qui gratte, vide ou renverse sa gamelle (berger australien, jeune chien joueur), à condition que les bols soient fixés dans le plateau.

**Mal servis** :
- les chiens barbus qui laissent une traînée en s'éloignant ;
- les molosses dont la bave atteint les murs ;
- les maîtres qui ont déjà sorti la gamelle dehors ;
- les maîtres de chiens à thorax profond inquiets du risque de torsion.

## 4. Verbatims pour les publicités

### Règles d'usage [H]
- Ce sont des **mots de maîtres** pour écrire des accroches. **Ce ne sont pas des témoignages** : aucun ne porte sur le produit de Pilou, et plusieurs portent sur un autre produit. Les présenter comme des avis de clients serait trompeur. Le cadre juridique (pratiques commerciales trompeuses, faux avis) et les règles de Meta n'ont pas été vérifiés ici.
- Ne reprendre que des problèmes que la station traite : l'eau et les croquettes **à la gamelle**. C'est pourquoi la traînée du goldendoodle et le museau essuyé du briard sont exclus.
- Seuls des verbatims « confirmé » ou « plausible » figurent ci-dessous. Un verbatim « plausible » doit être relu sur sa page avant usage.

### Français
| # | Verbatim | Statut | Source |
|---|---|---|---|
| 1 | « il en fout partout après avoir bu (de l'eau) » | plausible : fil revu en W6, mot à mot non réaffiché | [chien.com t2146](https://www.chien.com/forum/f6/peut-il-boire-proprement-t2146/) |
| 2 | « boit comme un cochon » | plausible : comparaison au cochon revue en W6 | [chien.com t2146](https://www.chien.com/forum/f6/peut-il-boire-proprement-t2146/) |
| 3 | « C'est par litres, que le dogue bave » | plausible : non revu | [chien.com t552](https://www.chien.com/forum/f50/question-bete-t552/) |
| 4 | « Mon Berger Australien passait son temps à vider la gamelle d'eau en grattant dedans. Mais avec cette gamelle, TERMINÉ!!! » | plausible : non retrouvé en W5 ; avis sur une autre gamelle | [Zooplus 624018](https://www.zooplus.fr/shop/chiens/ecuelles_distributeur_nourriture_chien/gamelle_voyage_chien/624018) |
| 5 | « La gamelle d'eau est dehors ou dans le garage! » | plausible : non revu | [chien.com t1409](https://www.chien.com/forum/f50/molosses-et-bave-comment-faites-vous-t1409/) |

En réserve, un fragment vu en W6 : « barbare de la boisson » (synthèse moteur du fil t2146, mot à mot non garanti).

### Anglais
| # | Verbatim | Statut | Source |
|---|---|---|---|
| 1 | « Wood floors has water damage from dog water bowl. Area approx 8" x 8" » | confirmé : titre de page revu en W3 | [Hometalk](https://www.hometalk.com/diy/floors-ceilings/q-wood-floors-has-water-damage-from-dog-water-bowl-area-approx-8-x-8-32956153) |
| 2 | « Expensive but sooooo worth it and a problem solver indeed!!! » | confirmé en W4. L'acheteur l'a racheté pour un second chat : ne pas l'attribuer à un maître de chien | [shopabunda](https://www.shopabunda.com/products/neater-pet-brands-neater-feeder-deluxe-for-dogs-mess-proof-elevated-bowls-no-slip-non-tip-double-diner-stainless-steel-food-dish-with-stand-68f2bb41-7ddd-4f92-9c22-0833213bf36b), attribution probable |
| 3 | « My dog always makes a mess with her water bowl. Ideas to stop the mess? » | plausible : titre de fil, non revu | [Canine Journal](https://www.caninejournal.com/forums/topic/my-dog-always-makes-a-mess-with-her-water-bowl-ideas-to-stop-the-mess/) |
| 4 | « contains all of his water mess, since the bowl is flush with the base » | plausible : non retrouvé en W8 ; mot à mot non garanti | [desertcart AR](https://www.desertcart.com.ar/products/7723846), attribution probable |

## 5. Lien avec la question de marge du propriétaire
- [H] Une douleur « moyenne » ne change rien au prix d'achat. Elle pèse sur deux autres choses :
  - le **taux de conversion**, donc le coût publicitaire de chaque vente ;
  - le **prix de vente possible**, plafonné par des substituts à 8–15 € et par l'original américain, à environ 50 $.
- Revendre à « fois 3 » le prix d'achat peut donc laisser peu de marge une fois la publicité payée. Le calcul n'est pas refait ici.

## Journal des requêtes (02/11/2026, WebSearch en mode « standard », 12 requêtes sur 12 autorisées, plus 1 WebFetch)
| # | Requête (verbatim) | Résultat clé |
|---|---|---|
| W1 | `"drips water from his beard all along the same stretch of hardwood"` | Aucune correspondance. Le fil Straight Dope « my dog is a sloppy drinker » (page 2) figure parmi les résultats |
| W2 | `"I had to jump up everytime he took a sip"` | Aucune correspondance |
| W3 | `"Wood floors has water damage from dog water bowl"` | Titre Hometalk mot pour mot ; serviette jamais changée, ponçage ou remplacement de lames, gamelle déplacée sur du carrelage (synthèse) ; fil Houzz « dog vs hardwood » ; guides : tapis étanche à rebord, carrelage ou vinyle |
| F1 | WebFetch `https://pubmed.ncbi.nlm.nih.gov/?term=Glickman+non-dietary+risk+factors+gastric+dilatation-volvulus+raised+feed+bowl` | **Échec** : `getaddrinfo ENOTFOUND pubmed.ncbi.nlm.nih.gov`, domaine hors du réseau autorisé. Aucune autre tentative, comme le demande le message d'erreur |
| W4 | `"sooooo worth it and a problem solver" Neater Feeder` | Phrase exacte sur une fiche revendeur (shopabunda probable), acheteur d'un second exemplaire pour un chat ; Hip2Save à 20,84 $ au lieu de 49,99 $ ; avis Express : un chien qui part en buvant mouille encore le sol ; titre Yahoo « Genius » |
| W5 | `"vider la gamelle d'eau en grattant dedans"` | Aucune correspondance ; pages sur les chats |
| W6 | `"il en fout partout" chien boit eau "peut-il boire proprement"` | Fil t2146 donné comme correspondance exacte ; « barbare de la boisson » comparé à un cochon ; réponses courtes, sans solution ; « plus le chien est gros, plus il s'abreuve en faisant de grosses éclaboussures » |
| W7 | `Glickman raised feed bowl "20 and 52%" gastric dilatation-volvulus large giant breed` | Vetcontact : 20 % et 52 %, plus de 1 600 chiens, *JAVMA* 217(10):1492–1499 ; Buckley : seuil de 1 pied, aucun effet protecteur, risque relatif de 2,17 (1,27–3,71), environ 4 %, nourrir au sol ; thèse de Purdue |
| W8 | `"contains all of his water mess"` | Aucune correspondance |
| W9 | `"plus d'eau transportée dans les babines"` | Aucune correspondance |
| W10 | `zooplus TIAKI tapis gamelle os 51 x 38 cm prix` | TIAKI 51 × 38 × 1 cm à 8,19 € (zooplus.fr) ; 6,49 € sur zooplus.com ; bandeau « Point relais dès 0,49 € » |
| W11 | `zooplus "Love Story" gamelle anti éclaboussures chien prix` | Love Story à 14,49 € (vendeur TOILINUX.COM), Ø 17 cm, hauteur 8 cm ; ZooVenture à 25,99 € |
| W12 | `"Neater Feeder" Deluxe amazon "4.6 out of 5" ratings` | « 4.6 out of 5 stars (33,770) » (fiche Express selon le moteur) ; Deluxe : 24 374 et 21 711 notes à 4,7/5, 4 040 avis à 4,6/5 ; Walmart Express : 469 notes à 4,6/5 |
