# Sourcing du jouet à lécher congelable et rechargeable (modèle Woof « Pupsicle ») : fabricants, matières, échantillons, coûts unitaires, personnalisation, emballage de marque, délais, risques qualité, conformité UE et recharges

*Notes des 2026-10-27 et 2026-10-28. Elles servent une marque française (boutique Shopify, publicité Meta) qui veut lancer, sans usine, un jouet à lécher congelable vendu comme « système » (jouet, moules, recettes, puis recharges). Elles complètent `fr_deep_jouet_lechage_congelable.md` (concurrence en France) et `us_verif_woof_pupsicle.md` (brevets US, plaintes, prix US) sans répéter leurs requêtes. Les chiffres de fret, de douane, de transport en France et de REP sont repris de `fr_couts_commerciaux.md` et `fr_costs_regulation.md` avec leurs sources. Ces reprises sont signalées « repris de … » et n'ont pas été revérifiées.*

*Méthode et limites, à lire avant d'utiliser un chiffre :*
- *Budget : 30 appels WebSearch, numérotés W1 à W30, tous en mode « standard » sauf W9 et W13 (« extended »).*
  - *W9 à W12 ont été refusés le 2026-10-27 par une limite d'usage, puis relancés à l'identique le 2026-10-28 (W13 à W16). Je les compte dans le budget par prudence.*
  - *Le budget est épuisé. Le journal complet figure en fin de document (section 4, Gaps).*
- *Preuve indirecte.*
  - *Aucune page n'a été ouverte : WebFetch, curl et les téléchargements sont exclus par la consigne.*
  - *Toutes les données viennent des titres, extraits et synthèses du moteur de recherche.*
  - *Quand la synthèse agrège plusieurs annonces, l'URL exacte d'un prix n'est pas toujours isolable : c'est signalé « extrait agrégé ».*
  - *Chaque chiffre est à confirmer en ouvrant l'URL, puis par devis écrit.*
- *1688.com n'est pas indexé par le moteur : W4 n'a renvoyé que des pages SHEIN Taïwan. Aucun prix 1688 n'a été obtenu.*
- *Prix fournisseurs.*
  - *Ce sont des prix « catalogue » affichés sur les places de marché B2B (Alibaba, Made-in-China, Global Sources), en dollars US et hors transport.*
  - *L'incoterm n'est pas visible (généralement EXW ou FOB). Ce ne sont pas des devis négociés.*
  - *La date de mise en ligne des annonces n'est pas visible (n.d.). La date indiquée est celle du relevé.*
- *Taux utilisé dans les calculs : 1 $ = 0,86 € [H], comme dans `fr_couts_commerciaux.md`.*
- *Étiquettes :*
  - *[F] : déclaration d'un fournisseur sur son annonce ou son site ;*
  - *[S] : source officielle (texte de loi, autorité, agence de l'UE) ;*
  - *[S2] : source secondaire (guide, blog, cabinet, presse, miroir de fiche) ;*
  - *[H] : hypothèse de travail non sourcée ;*
  - *[calc] : calcul explicite à partir de chiffres sourcés et d'hypothèses ;*
  - *[CJ] : connaissance juridique ou technique générale, **non vérifiée dans cette session**, à faire confirmer ;*
  - *« HISTORIQUE » : donnée antérieure à 2024 ; « n.d. » : date de publication non visible ; « n.o. » : donnée non obtenue.*
- *Correspondance avec les livrables demandés :*
  - *(1) tableau des fournisseurs : 1.1 ;*
  - *(2) intrants du coût rendu : 2.4 ;*
  - *(3) risques qualité et parades : 2.2, 2.3 et Inferences de la section 2 ;*
  - *(4) moule sur mesure : 2.1 et Inferences de la section 2 ;*
  - *(5) check-list de conformité : section 3 ;*
  - *(6) recharges et ventes additionnelles : section 4 ;*
  - *(7) emballage de marque : 2.5.*

---

## 1. Quels fabricants sérieux (Alibaba, 1688, Made-in-China, Global Sources, fabricants européens) produisent des jouets à lécher congelables ou des porte-friandises pour chiens, à quel MOQ et à quel prix unitaire, et proposent-ils échantillons et marque propre ?

### Takeaway
- **L'offre chinoise est abondante et bon marché, mais en petites tailles.**
  - Les balles porte-friandises en caoutchouc (naturel ou non précisé) ou en silicone s'affichent entre **0,60 et 3,80 $ pièce** [F], avec des **MOQ de 50 à 1 000 pièces**.
  - L'OEM/ODM et le logo sont courants.
  - Les échantillons coûtent 2 $ sur une annonce, ou 30 à 60 $ par design personnalisé, remboursables sur la commande (Wedogy).
  - La production annoncée va de 12 jours ouvrés à 45 jours après acompte.
- **Aucune annonce ne propose une taille XL d'environ 12 cm**, celle que Woof réserve aux chiens de plus de 34 kg.
  - Les tailles relevées plafonnent à 8 cm : 6, 7 et 8 cm chez Jiangyin Qianding ; 5, 6 et 7 cm sur une annonce Alibaba.
  - Pour viser les grands chiens, cible naturelle de Pilou, il faudra soit trouver par appel d'offres un fabricant qui possède déjà un moule plus grand, soit financer un moule (section 2).
- **Aucun fabricant européen de jouets en caoutchouc naturel en marque blanche n'est ressorti** (Italie et Sri Lanka testés). Croci, marque italienne, vend un os en caoutchouc naturel fabriqué en Chine.
- **Les certifications affichées ne prouvent pas grand-chose.**
  - EN71, ASTM F963, LFGB, CE et CPC visent les jouets d'enfants ou le contact alimentaire. Elles ne rendent pas un jouet pour chien conforme en soi.
  - Leurs rapports d'essais chimiques, s'ils sont authentiques, servent toutefois à documenter REACH (section 3).
  - Un fournisseur noté 1,0/5 affiche aussi ces mentions.
- **Fournisseurs à interroger en priorité (inférence) :**
  - Xiamen Newtop : balle en caoutchouc naturel avec bac en silicone, déjà un « système » de catalogue ;
  - Suzhou Becpet, iPetoy et Fujian SingYee : caoutchouc naturel ;
  - Ningbo General Union : MOQ de 50 pièces ;
  - Wedogy : petits MOQ et moules simples à 80–150 $, dont l'acheteur garde la propriété ;
  - Shenzhen LYA et Newtop Silicone : variante en silicone sans latex.

### Cited Findings

#### 1.1 Tableau des fournisseurs (livrable 1)
*Prix [F] en $ par pièce, hors transport. « n.o. » = non obtenu dans l'extrait. W = numéro de requête (journal en section 4, Gaps). Relevés du 2026-10-27 (W1 à W8) et du 2026-10-28 (W13 à W30).*

| # | Fournisseur (type si connu) | Plateforme | Produit (libellé verbatim ou abrégé) | Matière | Tailles | MOQ | Prix unitaire [F] | Échantillon (disponibilité, coût) | Personnalisation (logo, couleurs, moule) | Délai de production | Source, date de relevé |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Jiangyin Qianding Imp. & Exp. Trade Co., Ltd (raison sociale de négociant) | Made-in-China | « New Arrival Pet Treat Dispenser Rubber Fetch Ball Dog Toy » | Caoutchouc (naturel non précisé) | 6, 7 et 8 cm | 1 000 pièces (« Negotiable ») | 0,80 $ de 1 000 à 1 999 pièces ; 0,60 $ à partir de 2 000 (attribution probable à cette annonce) | n.o. | OEM et ODM acceptés ; certifications revendiquées ASTM, EN71 et « Asmt F963 » | 45 jours après l'acompte | [MIC, fiche](https://dogtoy.en.made-in-china.com/product/yOdaNsoDPMkT/China-New-Arrival-Pet-Treat-Dispenser-Rubber-Fetch-Ball-Dog-Toy.html) ; [MIC, catalogue](https://dogtoy.en.made-in-china.com/product-catalog/Dog-Toys-1.html) ; W6 (2026-10-27), W30 (2026-10-28) |
| 2 | Xiamen Newtop | Made-in-China | « Interactive Durable Tooth Cleaning Pet Dogs Feeder Leakage Food Treat Training Chew Snack Toys », décrit comme un ensemble jouet à mâcher et distributeur en caoutchouc naturel **avec bac à glaçons en silicone** | Caoutchouc naturel et silicone | n.o. | 1 000 | 1,77–1,88 $ | n.o. | n.o. | n.o. | Extrait agrégé, URL exacte non isolée : [MIC, Treat Dispenser Toy](https://www.made-in-china.com/products-search/hot-china-products/Treat_Dispenser_Toy.html) ; [MIC, dog treat food toy](https://www.made-in-china.com/manufacturers/dog-treat-food-toy.html) ; W2, W6 (2026-10-27) |
| 3 | Xiamen Newtop | Made-in-China | Balle distributrice en caoutchouc naturel | Caoutchouc naturel | n.o. | 100 | 3,80 $ | n.o. | n.o. | n.o. | Extrait agrégé : [MIC, dog treat food toy](https://www.made-in-china.com/manufacturers/dog-treat-food-toy.html) ; W30 (2026-10-28) |
| 4 | Ningbo General Union | Made-in-China | « Ultimate Durable Frozen Treat Dog Toy for Aggressive Chewers Anxiety Relief » ; balle distributrice en caoutchouc naturel | Caoutchouc naturel | n.o. | 50 | ≈2,62–3,56 $ | n.o. | n.o. | n.o. | Extrait agrégé : [MIC, dog ball price](https://www.made-in-china.com/manufacturers/dog-ball-price.html) ; [MIC, Treat Dispenser Toy](https://www.made-in-china.com/products-search/hot-china-products/Treat_Dispenser_Toy.html) ; W2, W6 (2026-10-27) |
| 5 | Anhui Joypaws | Made-in-China | « Sustainable Rubber Dog Toy for Pets with Treat Dispensing Function » | Caoutchouc | n.o. | 200 | 0,70–1,10 $ | n.o. | n.o. | n.o. | Extrait agrégé : [MIC, dog treat food toy](https://www.made-in-china.com/manufacturers/dog-treat-food-toy.html) ; W6 (2026-10-27) |
| 6 | iPetoy (Huizhou, Guangdong) | Made-in-China | Balle à friandises | Caoutchouc naturel (selon la synthèse) | n.o. | 1 000 | 1,97 $ | n.o. | ODM | n.o. | Extrait agrégé W30, URL non isolée : [MIC, wholesale pet chew toy](https://www.made-in-china.com/manufacturers/wholesale-pet-chew-toy.html) ; [MIC, rubber toy](https://www.made-in-china.com/manufacturers/rubber-toy.html) ; [MIC, dog toys](https://www.made-in-china.com/manufacturers/dog-toys.html) (2026-10-28) |
| 7 | Suzhou Becpet | Made-in-China | Balle distributrice en caoutchouc naturel, sur mesure | Caoutchouc naturel | n.o. | 1 000 | 1,53–2,29 $ | n.o. | Sur mesure (« custom ») | n.o. | Extrait agrégé W30, mêmes pages que la ligne 6 (2026-10-28) |
| 8 | Hangzhou Tianyuan Pet Products Co., Ltd | Made-in-China | « Cooling Dog Toy with Suction Cup Freezable Dog Chew Toy » et autres jouets congelables | n.o. | n.o. | n.o. | n.o. | n.o. | n.o. | n.o. | [MIC](https://tianyuanpet.en.made-in-china.com/product-group/UqRGplvOYPcT/Dog-Toy-1.html) ; W2 (2026-10-27) |
| 9 | Shenzhen LYA Silicone Rubber Products | Global Sources | « customizable small silicone squeaky IQ treat shake leaky silicone ball dog toy with holes » | Silicone | n.o. | 1 000 | 1,10–1,30 $ | n.o. | Personnalisable | n.o. | Extrait agrégé : [GS, rubber ball toy](https://www.globalsources.com/manufacturers/rubber-ball-toy.html) ; [GS, ball toys](https://www.globalsources.com/manufacturers/ball-toys.html) ; [GS, cat & dog toy balls](https://www.globalsources.com/category/cat-dog-toy-balls-for-sale-price_32936/#product-unavailable) ; W3 (2026-10-27) |
| 10 | Fujian SingYee Pet Product Co. | Global Sources | « durable rubber dog treat dispensing toy ball » ; « new natural rubber dog leaking food ball » | Caoutchouc ; caoutchouc naturel | n.o. | 500 (1re) ; n.o. (2e) | 1,55–2,00 $ ; 2,99–3,79 $ | n.o. | n.o. | n.o. | Comme la ligne 9 (W3, 2026-10-27) |
| 11 | Market Union Co. | Global Sources | « dog toys stretch rubber leaking ball » | Caoutchouc | n.o. | 240 | 0,76–0,87 $ | n.o. | n.o. | n.o. | Comme la ligne 9 (W3, 2026-10-27) |
| 12 | Jinjiang Naike EcoTechnology (groupe Naike, cité avec Quanzhou Huangbo Group parmi les fabricants OEM) | Global Sources | « dog liquid lick bowl » : bol à lécher, pas une balle | n.o. | n.o. | 1 000 | 1,19–1,31 $ | n.o. | OEM | n.o. | Comme la ligne 9 ; [GS, pet bowl](https://www.globalsources.com/manufacturers/pet-bowl.html) (W3, 2026-10-27) |
| 13 | Fournisseur non nommé | Alibaba | Balle à lécher « Freeze Treats » pour grands chiens | Silicone | « large dogs » | 200 | 1,85–3,70 $ | n.o. | n.o. | n.o. | [Alibaba, showroom « lick dog balls »](https://www.alibaba.com/showroom/lick-dog-balls.html) ; W30 (2026-10-28) |
| 14 | Fournisseur non nommé | Alibaba | Balle distributrice pour chiots « BPA-Free Natural Rubber », « OEM Wholesale » | Caoutchouc naturel | n.o. | 100 | n.o. | n.o. | OEM | n.o. | Comme la ligne 13 (W30, 2026-10-28) |
| 15 | Fournisseur non nommé | Alibaba | « OEM ODM Interactive Pet Toy Manufacturer Magic Rolling Dog Ball Slow Feeder Chew Pet Dog Toys Treat Dispenser Toy » | Caoutchouc naturel (« Natural Rubber », « Bpa-free ») | 5, 6 et 7 cm (attribution probable) | n.o. | n.o. | « Sample price: $2 », relevé sur une annonce de balle à friandises en caoutchouc (attribution à cette annonce non isolée) | OEM/ODM | n.o. | [Alibaba](https://www.alibaba.com/product-detail/OEM-Interactive-Pet-Toy-Manufacturer-Magic_1601178337444.html) ; W1, W6 (2026-10-27) |
| 16 | Fournisseur non nommé | Alibaba | « Freeze Ball Lick Treat-filled Chew Freezable Fillable Stuffable Frozen Dog Treat Toy For Dogs » | n.o. | n.o. | n.o. | n.o. | n.o. | n.o. | n.o. | [Alibaba](https://www.alibaba.com/product-detail/Freeze-Ball-Lick-Treat-filled-Chew_1601436443161.html) ; W1 (2026-10-27) |
| 17 | Fournisseur non nommé | Alibaba | « Silicone Dog Treat Dispensing Toy Slow Feeder Lick Toy Refillable Enrichment Chew Ball Daily Indoor Use For Medium Large Dogs » | Silicone | « Medium Large Dogs » | n.o. | n.o. | n.o. | n.o. | n.o. | [Alibaba](https://www.alibaba.com/product-detail/Silicone-Dog-Treat-Dispensing-Toy-Slow_1601925921523.html) ; W1 (2026-10-27) |
| 18 | Soleil China Ltd. (Guangdong) ; **note fournisseur 1,0/5, signal d'alerte** | Alibaba | Balle à friandises en caoutchouc (pas un clone de la Pupsicle) | Caoutchouc | n.o. | 499 | 0,75 $ | n.o. | Logo et emballage personnalisés à partir de 1 000 pièces ; EN71, REACH et ASTM revendiqués | n.o. | Repris de `us_verif_woof_pupsicle.md` : [Alibaba](https://www.alibaba.com/product-detail/rubber-dog-ball-pet-supplies-manufacturer_60781888382.html) ; relevé du 2026-10-27 |
| 19 | Wedogy (fabricant chinois de produits pour chiens sur mesure, site propre) | wedogy.com | Jouets pour chien personnalisés | Moule « Basic rubber mold » cité ; autres matières n.o. | n.o. | 50 pièces par design (en-tête) ou 100 (section des étapes, moins pour les modèles simples) ; 100 pour les jouets de Noël sur mesure ; articles en stock dès 1 pièce | n.o. | 3 à 5 jours ouvrés, 30 à 60 $ par design, remboursables sur la commande ; 15 jours ouvrés pour un échantillon sur mesure (page Noël) | Moule de base en caoutchouc 80–150 $, 4 à 6 jours, « Mold ownership: 100% yours » | 12 à 18 jours ouvrés ; 25 jours ouvrés (page Noël) | [Wedogy, dog toys](https://wedogy.com/dog-toys/) ; [Wedogy, Christmas dog toys](https://wedogy.com/christmas-dog-toys/) ; W13, W28 (2026-10-28) |
| 20 | Newtop Silicone (fabricant chinois de silicone, site propre) | newtopsilicone.com | Jouets pour animaux en silicone sur mesure | Silicone | n.o. | « every factory has a MOQ » pour couvrir la mise en route (montant n.o.) | n.o. | Prototypes coulés à la main dans un moule d'essai en aluminium ou imprimé en 3D | Moule de production en acier ; « a complex production mold might take around 4–6 weeks to build » | n.o. | [Newtop, guide](https://www.newtopsilicone.com/how-brands-can-create-their-own-custom-silicone-pet-toys-step-by-step-guide/) ; [Newtop, pet toys](https://www.newtopsilicone.com/silicone-pet-toys-manufacturing/) ; W13, W28 (2026-10-28) |
| 21 | Plusieurs fournisseurs de tapis à lécher en silicone (accessoire possible du kit) | Alibaba | « Custom Silicone Dog Lick Mat With Suction Cups Wholesale Food Grade Silicon… » et similaires | Silicone « food grade » [F] | n.o. | Base de 2 à 500 pièces (souvent 20–100 ; 48 sur une annonce) ; logo à partir de 200, 300 ou 500 ; emballage personnalisé à partir de 1 000 | Une annonce : 3,70 $ (50–499) à 3,50 $ (2 000 et plus) ; logo +0,20 $ pièce (MOQ 300) | Échantillons personnalisés avec logo en 7 jours | « OEM/ODM with free design and mold opening » (une annonce, MOQ de base de 10) ; LFGB, BPA-free, CE, CPC et EN71 revendiqués (une usine) | 5 jours (1–5 000 pièces) et 7 jours au-delà sur une annonce ; 10 jours (1–50) et 30 jours (51–1 000) sur une autre | Extrait agrégé W5 (2026-10-27) : [1](https://www.alibaba.com/product-detail/Custom-Silicone-Dog-Lick-Mat-with_1600535403683.html) ; [2](https://www.alibaba.com/product-detail/OEM-Custom-Silicone-Dog-Lick-Mat_1601273008711.html) ; [3](https://www.alibaba.com/product-detail/Custom-Dog-Lick-Mat-with-Suction_1600101385103.html) ; [4](https://www.alibaba.com/product-detail/New-Dog-Licking-Mat-Slow-Feeder_1601381559049.html) ; [5](https://www.alibaba.com/product-detail/2025-Type-Silicone-Dog-Lick-Mat_1601449605991.html) |
| 22 | Petopia (localisation non confirmée) | thingtesting.com | Jouets à mâcher en caoutchouc naturel et recyclé | Caoutchouc naturel ; recyclé | n.o. | n.o. | n.o. | n.o. | Vente en gros et marque blanche annoncées | n.o. | [thingtesting](https://thingtesting.com/brands/petopia) ; W7 (2026-10-27) |

- **Autre contact possible, sans données :** GUANGDONG VKING INTELLIGENT TECHNOLOGY CO., LTD, catalogue de jouets pour chien d'un industriel du caoutchouc ([MIC](https://vkingrubber.en.made-in-china.com/product-catalog/Dog-Toys-1.html), W6).

#### 1.2 Échantillons, personnalisation et délais : ce que disent les annonces
- **Échantillons.**
  - « Sample price: $2 » sur une annonce Alibaba de balle à friandises en caoutchouc (W6, extrait agrégé, voir ligne 15).
  - Wedogy : 30 à 60 $ par design, remboursables sur la commande, en 3 à 5 jours ouvrés, ou 15 jours ouvrés pour un échantillon sur mesure ([Wedogy](https://wedogy.com/dog-toys/) ; [Wedogy](https://wedogy.com/christmas-dog-toys/)).
  - Tapis à lécher : échantillons personnalisés avec logo en 7 jours (W5, ligne 21).
  - Le coût du transport express des échantillons n'a pas été trouvé.
- **Logo et emballage.**
  - Logo à partir de 200, 300 ou 500 pièces selon l'annonce, avec un supplément de +0,20 $ pièce sur l'une d'elles. Emballage personnalisé à partir de 1 000 pièces (W5, ligne 21).
  - Soleil : logo et emballage à partir de 1 000 pièces (ligne 18).
- **Petits MOQ.**
  - Une fiche Made-in-China indique « Contact us for lower MOQ » (W6, extrait agrégé).
  - Ningbo General Union vend dès 50 pièces (ligne 4), Wedogy dès 50 ou 100 pièces par design (ligne 19).
- **Délais de production annoncés :**
  - 45 jours après l'acompte (Jiangyin Qianding, ligne 1) ;
  - 12 à 18 jours ouvrés (Wedogy) ;
  - de 5 à 30 jours selon la quantité (tapis à lécher, ligne 21).
- **Ancienneté des annonces.** La synthèse de W6 précise que certaines annonces ont plus d'un an : prix et conditions sont à revérifier.
- **Certifications revendiquées :**
  - ASTM, EN71 et « Asmt F963 » (Jiangyin Qianding) ;
  - LFGB, BPA-free, CE, CPC et EN71 (une usine de tapis à lécher) ;
  - EN71, REACH et ASTM (Soleil, noté 1,0/5).

#### 1.3 Hors de Chine : Europe et Sri Lanka
- **Italie et Europe (W7).** Aucun fabricant italien de jouets en caoutchouc naturel proposant la marque blanche n'est ressorti.
  - **Croci S.p.A.** (Italie) vend sur Faire un os en caoutchouc naturel indiqué « Made in China » ([Faire](https://www.faire.com/product/p_87u9ts8jfr) ; [Faire](https://www.faire.com/product/p_4g49h5ey8p), attribution exacte non isolée).
  - **Smart Dog Srl** (Segrate, près de Milan) fabrique en Italie des jouets dans un composite d'aspect bois, pas en caoutchouc ([Zoomark 2025](https://www.zoomark.it/en/2025-exhibitors-catalogue/exhibitor-detail/?id=9921)).
  - **Antlerworld – El Abuelo** (Espagne) propose la « product customisation/Private label » pour des produits en bois de cerf et d'olivier ([Interzoo](https://interzoo.com/en/exhibitors-products/a/antlerworld-el-abuelo)).
  - **Funny Zoo** (Italie) travaille le cuir, le coton et le jute ([Creoate](https://www.creoate.com/product/natural-dog-toy-slippers)).
  - **Petopia** : voir ligne 22.
- **Sri Lanka (W8).** Aucun fabricant de jouets pour chien en sous-traitance n'a été trouvé.
  - **DSL Lanka** (marque Tikiri Toys) est présenté comme le principal exportateur sri-lankais de jouets bio. Il fabrique des jouets en caoutchouc naturel pour bébés et a été le premier fabricant de jouets en caoutchouc naturel accrédité GOLS (Global Organic Latex Standard). Sources : [Daily Mirror via PressReader, 30/03/2021](https://www.pressreader.com/sri-lanka/daily-mirror-sri-lanka/20210330/282166473972988) (HISTORIQUE) ; [Baby on Grand](https://babyongrand.com/products/tikiri-toys-puppy-organic-teether-rattle-bath-toy).
  - **Green Rubber Toys** fabrique au Sri Lanka, dans sa propre usine, des animaux en caoutchouc naturel ([Kids-world](https://www.kids-world.com/en/green-rubber-toys-c-12311.html)).
  - Une capacité OEM pour animaux de compagnie n'est confirmée chez aucun des deux.

#### 1.4 1688
- **W4** (`宠物 舔食球 冷冻 狗 天然橡胶 1688`) n'a renvoyé aucune page 1688, seulement des fiches de détail SHEIN Taïwan.
  - Exemple : une balle à lécher « 宠物慢食舔食球 » en PP de 180 ml à NT$116 ([SHEIN TW](https://www.shein.tw/Pet-Slow-Feeder-Licking-Ball-Universal-Anti-Slip-Design-Suitable-For-Cats-And-Dogs-Simulates-Natural-Licking-To-Slow-Down-Feeding-Speed-Prevent-Choking-And-Relieve-Pet-Anxiety-p-443905822.html)).
  - Une autre fiche indique « ABS » dans un champ et « 100% Polyvinyl Chloride » dans un autre.
- **Statut : non vérifié (accès impossible).**

#### 1.5 Repères : formats et prix des produits finis
- **Woof Pupsicle (repris de `us_verif_woof_pupsicle.md`).**
  - Tailles : S 2,9 po (≈7,4 cm) pour 4,5 à 11 kg ; L 3,6 po (≈9,1 cm) pour 11 à 34 kg ; XL 4,8 po (≈12,2 cm) pour 34 kg et plus.
  - Matière : caoutchouc naturel. Prix US : 17,99 à 24,99 $.
  - Sources : [Woof, tailles](https://support.mywoof.com/en-US/general-toy-sizing-and-dimensions-1208428) ; [Arcata Pet Supplies](https://www.arcatapet.com/m/item.cfm?cat=29874) (17,99 $) ; [BB Pet Stop](https://shop.bbpetstop.com/products/bb-pet-stop-inc/woof-the-pupsicle-treat-dispensing-dog-toy-exclusive-skyblue-4) (24,99 $).
  - Fabrication en Chine selon la FAQ Woof (repris de `us_feeding_cleaning_enrichment.md` : [FAQ Woof](https://help.mywoof.com/knowledge-base/article/general-faqs)).
  - Prix en France : environ 47 à 67 € en import sur Amazon.fr, selon la synthèse du moteur (repris de `fr_deep_jouet_lechage_congelable.md`).
- **Freezbone « Freezball », sur Faire (grossistes US).**
  - 100 % caoutchouc naturel. S de 2,5 po (≈6,4 cm, jusqu'à 25 lb, soit ≈11 kg) ; L de 3 po (≈7,6 cm, jusqu'à 40 lb, soit ≈18 kg).
  - Prix conseillé : 17,94 $. Fabriqué en Chine.
  - Apex Pet Products « FRODOG » : ouverture en tournant, « caoutchouc alimentaire », compatible lave-vaisselle.
  - Repris de `us_verif_woof_pupsicle.md`, correspondance produit/URL non vérifiable : [Faire](https://www.faire.com/product/p_48yvanxrjv) ; [Faire](https://www.faire.com/product/p_mhajdfn8dw) ; [Faire](https://faire.com/product/p_grtft4wz67).
- **SmoothieDog.** Balle de 9 cm en caoutchouc naturel avec moule en silicone de 5 portions (≈350 ml), à 29,90 € chez Cool4Pets (repris de `fr_deep_jouet_lechage_congelable.md` : [Cool4Pets](https://www.cool4pets.be/fr/smoothiedog-lickball)).
- **Marques d'enseigne (repris de `fr_deep_jouet_lechage_congelable.md`) :**
  - Summer Vibes : balle de 13,5 cm en polyuréthane, à 8,79 € chez Animalis ([Animalis](https://www.animalis.com/summer-vibes-balle-friandise-rafraichissante-pour-chiens-13-5cm-868746_M.html)) ;
  - AniOne : balle d'environ 6 cm en PP, chez Maxi Zoo ([Maxi Zoo](https://www.maxizoo.fr/p/anione-balle-de-jeu-rafrachissante-2439127/)).

### Inferences
- **Prix catalogue réaliste d'une balle de taille L avec logo [F] :**
  - **environ 1,5 à 2,5 $ FOB en caoutchouc naturel**, au MOQ de 1 000 (Suzhou Becpet 1,53–2,29 $ ; iPetoy 1,97 $ ; Xiamen Newtop 1,77–1,88 $ avec bac en silicone) ;
  - 0,60 à 1,10 $ en caoutchouc non précisé (Jiangyin Qianding, Anhui Joypaws).
  - Ces écarts reflètent probablement la matière (caoutchouc naturel ou mélange) et l'épaisseur des parois. Il faudra les vérifier en pesant les échantillons.
- **Les petits MOQ, de 50 à 200 pièces, permettent un test publicitaire avant engagement**, à un prix unitaire plus élevé : Ningbo General Union à 2,62–3,56 $ dès 50 pièces, Xiamen Newtop à 3,80 $ dès 100.
- **Traiter avec l'usine, pas avec un négociant, pour un moule propriétaire.**
  - Jiangyin Qianding a une raison sociale de négociant.
  - L'usine détient le moule et maîtrise la qualité. Il faut faire écrire que le moule appartient à la marque : Wedogy l'annonce d'emblée (« Mold ownership: 100% yours »).
- **Un produit de catalogue ne différencie pas.**
  - Les mêmes balles de 6 à 8 cm alimentent déjà les clones d'Amazon.fr (YANGUN, Qaestuan, DKIIL NOIYB : voir `fr_deep_jouet_lechage_congelable.md`).
  - Le catalogue sert à tester vite la demande, pas à construire la marque.
- **« Fabriqué en Europe » n'est pas une piste réaliste au lancement** pour le caoutchouc naturel : aucune usine européenne n'a été trouvée. La différenciation passera par la taille, la fermeture, la sécurité, le système de recettes et la marque.
- **Exiger les rapports d'essais originaux [H].** Il faut obtenir le laboratoire, le numéro et la date du rapport et l'échantillon testé, puis vérifier le rapport sur le portail du laboratoire. Un logo « EN71 » sur une annonce ne prouve rien : Soleil, noté 1,0/5, en affiche un.

### Gaps
- **1688** : non indexé par le moteur. Il faut passer par un agent ; prix non vérifiés.
- **Devis réels** : prix FOB, incoterm, conditions de paiement et validité non obtenus. Aucun prix n'est apparu pour les annonces Alibaba « Freeze Ball » (ligne 16) et silicone « Medium Large Dogs » (ligne 17), ni pour Hangzhou Tianyuan.
- **Taille XL (11 cm et plus) en catalogue** : aucun fournisseur trouvé. Seule une annonce en silicone vise les « large dogs », sans dimension.
- **Couleurs** : aucune information sur le MOQ par couleur (teinte Pantone) ou sur les couleurs exclusives.
- **Échantillons** : coût de l'envoi express non sourcé.
- **Statut usine ou négociant**, audits et ancienneté des fournisseurs : non vérifiés.
- **Autres pays producteurs de caoutchouc naturel** (Inde, Vietnam, Thaïlande, Malaisie) : non cherchés, faute de budget. Les listes d'exposants d'Interzoo et de Zoomark n'ont pas été exploitées pour les jouets en caoutchouc.
- **URL exactes** de plusieurs prix : non isolées (extraits agrégés W3, W5, W6, W30).

---

## 2. Combien coûterait le développement (moule sur mesure) et la production d'une version différenciée, plus sûre et plus durable ?

### Takeaway
- **Outillage.**
  - Un moule de compression pour un corps en caoutchouc coûte **500 à 3 500 $ par jeu** chez des moulistes chinois. Une autre source donne 3 000 à 12 000 $.
  - Wedogy annonce des moules simples à **80 à 150 $**, en 4 à 6 jours.
  - L'injection de silicone liquide (LSR) coûte **5 000 à 50 000 $** : c'est à éviter au lancement.
  - Délais : 7 jours à 4 semaines pour un outil prototype, 2 à 8 semaines pour un moule de production.
- **Coût d'une gamme propriétaire.** Pour deux tailles (L et XL) avec une fermeture sans filetage, l'outillage seul représenterait **environ 1 000 à 21 000 $, soit 0,9 à 18 k€ [calc]**. Le design, les prototypes et les essais ne sont pas chiffrés (non sourcés).
- **Matière.** Les sources (blogs commerciaux, preuves faibles) convergent :
  - le **caoutchouc naturel** est le meilleur compromis entre durabilité et préservation des dents pour les gros mâcheurs, mais il contient du latex ;
  - le **TPR** convient aux mâcheurs modérés ;
  - le **nylon** est le plus dur et le plus exposé aux fractures dentaires ;
  - aucune source n'a été trouvée sur le silicone.
- **Sécurité.**
  - Le risque le mieux documenté est la **langue aspirée dans un jouet qui n'a qu'une ouverture**. Les vétérinaires recommandent un second trou d'air ; cas en 2008, 2015 et 2024.
  - S'y ajoutent les plaintes contre Woof : fermeture vissée qui grippe, jouet détruit par les gros mâcheurs, étouffement avec les recharges, dent cassée, latex.
- **Coût rendu.**
  - Une Woof L pèse environ 289 g.
  - En aérien DDP à 5–9 $/kg, le fret d'une balle L emballée revient à environ **1,5 à 2,6 € [calc]**. En groupage maritime, il ne coûte que quelques centimes, plus des frais fixes non sourcés.
  - Un **kit L de catalogue** (balle, logo, moule silicone, boîte) reviendrait à **environ 4,8 à 6,3 € rendu en France par avion [calc]**, hors agent, contrôle et logistique.
  - Une XL pleine dépasserait probablement 500 g et changerait de tranche postale.
- **Emballage.**
  - Les fabricants chinois proposent des boîtes imprimées à fenêtre de **0,12 à 0,80 $**, avec un MOQ de 500 à 1 000.
  - Packhelp (Pologne) imprime des boîtes d'expédition **dès 30 pièces**. Les boîtes non imprimées coûtent environ **1,53 £ pièce** par lot de 1 500.

### Cited Findings

#### 2.1 Outillage : coûts et délais (livrable 4)
*Attribution d'après les renvois numérotés de la synthèse de W13 (extended, 2026-10-28). Pages de moulistes ou de fabricants (marketing [F]/[S2]), n.d. sauf mention.*

| Source (type) | Outil | Coût | Délai | Remarques |
|---|---|---|---|---|
| [Wedogy](https://wedogy.com/dog-toys/) (fabricant de jouets pour chien) | « Basic rubber mold » | 80–150 $ | 4–6 jours | « Mold ownership: 100% yours ». La portée exacte (pièce simple, logo ?) n'est pas précisée. |
| [Melon Rubber](https://www.melon-rubber.com/custom-rubber-mould-manufacturer-injection-mould-of-custom-rubber-part-from-china-p-3.html) ; [Melon Rubber, moules de compression](https://www.melon-rubber.com/25-cav-precision-rubber-injection-moldprototype-silicone-rubber-compression-molds-for-rubber-seal-and-gasket-p-276.html) (mouliste chinois) | Moule de compression, prix « per set » | ≈500–3 500 $ | 7 jours (prototype) ; 14 jours (production) | — |
| [Senses Mold](https://senses-mold.com/molding-tool/rubber-mold/compression-mold/) (mouliste) | Compression ou injection LSR | Compression 500–3 000 $ ; injection LSR 5 000–50 000 $ | n.o. | Moules de compression adaptés au silicone, à l'EPDM et au caoutchouc naturel. La compression convient aux mélanges de dureté moyenne. |
| [LANPDT](https://lanpdt.com/compression-molding-vs-injection-molding/) (guide) | Compression | 3 000–12 000 $ | n.o. | Fourchette plus haute que celle des moulistes. |
| [Qualiform](https://qualiformrubbermolding.com/company/rubber-manufacturer/rubber-compression-molding/) (mouleur de caoutchouc, probablement américain [H]) | Prototype ou production | n.o. | 2–4 semaines (prototype) ; 6–8 semaines (production en compression) | — |
| [GC Indus](https://gcindus.com/rubber-compression-molds-a-complete-guide/) (guide) | Compression | n.o. | 2–6 semaines ; 3–6 semaines pour un moule de production en acier trempé | — |
| [Newtop Silicone](https://www.newtopsilicone.com/how-brands-can-create-their-own-custom-silicone-pet-toys-step-by-step-guide/) | Prototype en aluminium ou impression 3D, puis acier | n.o. | « around 4–6 weeks » pour un moule de production complexe | Prototypes coulés à la main, moule en acier pour les grandes séries. |
| [HB Silicone](https://www.hbsilicone.com/how-much-is-the-tooling-cost-for-my-silicone-project/) ; [Meitu-Engelhardt, « Custom Rubber Molding Cost: 2026 Pricing Guide »](https://meitu-engelhardt.com/custom-rubber-molding-cost/) | Facteurs de coût | — | — | Le coût dépend surtout de la complexité et de la précision de la pièce, du procédé, de l'acier et du nombre d'empreintes, plus que de la matière. |

- **« Moule offert ».** Une annonce de tapis à lécher en silicone affiche « OEM/ODM with free design and mold opening » (W5, ligne 21 du tableau 1.1). Il faut faire préciser trois points : l'amortissement dans le prix unitaire, le volume minimum et la propriété du moule.

#### 2.2 Matières (livrable 3)
*Preuves faibles : blogs commerciaux et guides de fournisseurs, sans essai de laboratoire ni source vétérinaire (W14, 2026-10-28).*
- **Caoutchouc naturel.**
  - Un guide fournisseur sur Alibaba le décrit comme « highly durable and elastic, ideal for aggressive chewers, and resistant to splitting ». Il cite deux inconvénients : il retient les odeurs et se décolore au soleil. Source : [Alibaba, product insights](https://www.alibaba.com/product-insights/bowling-ball-dog-toy.html) (attribution probable, W1) [F].
  - Les blogs le décrivent comme élastique et résilient, avec du « give » qui ménage les dents. Il résisterait aux perforations et aux déchirures. Ils recommandent une construction monobloc, notent que la formulation détermine la résistance et signalent le risque d'allergie au latex. Sources : [Joybuy](https://www.joybuy.de/blog/durable-dog-chew-toys-buyers-guide/C5iOcy4B) ; [Joybuy](https://www.joybuy.de/blog/best-durable-dog-chew-toys/ere6AXF1) ; [DEV Community](https://dev.to/furryfable_/aggressive-chewers-what-actually-stops-them-destroying-toys-16j6) ; [HD Supply](https://csr.hdsupply.com/?p=14693) (n.d., extrait agrégé).
  - Beco présente le caoutchouc naturel, issu du tronc de l'hévéa, comme « ideal for dog toys » pour sa résistance et son élasticité ([Kiwipetz, Beco](https://kiwipetz.co.nz/products/beco-fetch-ball), W4).
- **Latex.** Woof recommande aux personnes allergiques au latex d'éviter la Pupsicle (repris de `us_verif_woof_pupsicle.md` : [Chewy](https://www.chewy.com/woof-pupsicle-power-chewer-refillable/dp/1206830)).
- **TPR.** Plus souple que le caoutchouc naturel, il est conseillé pour les chiots, les chiens âgés et les mâcheurs modérés, pas pour les gros mâcheurs (mêmes blogs).
- **Nylon.** C'est la matière la plus dure et la plus durable, mais la fracture dentaire est « the most commonly documented risk ». Usage sous surveillance uniquement ([Plastic Ranger](https://plasticranger.com/are-nylon-dog-bones-safe/) ; [Plastic Ranger](https://plasticranger.com/?p=18780), n.d.).
- **Silicone.** Aucun résultat sur sa durabilité ni sur les dents (W14).
- **Construction.** Les blogs citent la combinaison d'une âme en nylon et d'une enveloppe en caoutchouc comme compromis. Ils notent que les jouets creux se perforent plus facilement (mêmes sources). Un chiffre attribué à l'AVMA sur les traumatismes buccaux n'a pas pu être vérifié et a été écarté.
- **Bas de gamme en France :** polyuréthane (Summer Vibes) et PP (AniOne) pour les balles « rafraîchissantes » (repris de `fr_deep_jouet_lechage_congelable.md`).

#### 2.3 Risques de sécurité et de qualité documentés (livrable 3)
- **Langue aspirée par effet ventouse (W15, 2026-10-28).**
  - Une vétérinaire (Kinship, Royaume-Uni) explique qu'un jouet à une seule ouverture peut aspirer la langue, que le gonflement empêche ensuite de la dégager, et qu'un second trou d'air empêche le vide : « When buying these toys for your dog, check to make sure there is a second hole to stop this vacuum being created. » ([Kinship](https://www.kinship.com/uk/dog-health/fillable-dog-toy-dangers), n.d.).
  - **Cas documentés :**
    - « pimple ball » Four Paws en 2008, langue amputée ([Snopes](https://www.snopes.com/fact-check/pimple-ball/), HISTORIQUE) ;
    - balle Kong à une seule ouverture liée à la mort d'un rottweiler en 2015 ([iHeartDogs](https://iheartdogs.com/warning-to-pet-owners-dog-dies-after-tongue-gets-stuck-in-popular-brand-name-toy/), HISTORIQUE) ;
    - pit-bull Arai, partie de la langue perdue ([UC Davis](https://behavior.vetmed.ucdavis.edu/node/17031), n.d.) ;
    - springer dont la langue s'est coincée dans le trou laissé par le bouchon d'un couineur ([The Chronicle, 23/02/2024](https://www.pressreader.com/uk/the-chronicle-south-tyneside-and-durham/20240223/281522231020749)).
  - Voir aussi [Vets Now](https://www.vets-now.com/?p=43342) (jouets usés et cassés) et [LAist](https://laist.com/news/dog-tongue-kong).
  - **Conseils** : vérifier la présence d'un second trou d'air, retirer les jouets abîmés ou dont le couineur est sorti, surveiller le chien.
- **Fermeture vissée qui grippe (repris de `us_verif_woof_pupsicle.md`).**
  - Chez Woof : fond vissé « very hard to open » après usage ; l'eau bouillante et l'huile d'olive ne suffisent pas, certains clients finissent à la pince ([Chewy](https://www.chewy.com/woof-pupsicle-tough-squeaky-power/dp/1206854)). « the plastic container did not open or close easily » ([Chewy, Party Pupsicle](https://www.chewy.com/woof-party-pupsicle-treat-dispensing/dp/1023510)).
  - Chez les copies de type « Yipetor » : « got jammed up », et les astuces d'ouverture ne marchent plus après le lave-vaisselle ([desertcart](https://www.desertcart.uy/products/540791283)).
  - En France : « difficile de visser le bouchon » sur la petite taille ([Dog'N'Fun](https://shop.dognfun.net/produit/pupsicule/), repris de `fr_deep_jouet_lechage_congelable.md`).
- **Durabilité.** Des Labradors et des pit-bulls détruisent la Pupsicle « within minutes to hours ». La version noire « Power Chewer » « still chipped quickly » ([Chewy](https://www.chewy.com/woof-pupsicle-power-chewer-refillable/dp/1206830), repris).
- **Étouffement avec les recharges.** Des avis Chewy de fin 2025 à début 2026 décrivent :
  - une manœuvre de Heimlich, la friandise étant « too slippery to dig out » ;
  - un chihuahua étouffé par un « holder » trop gros.
  - Sources : [Chewy, Pops L](https://www.chewy.com/woof-pupsicle-pops-refills-beef/dp/1024046) ; [Chewy, Pops XL](https://www.chewy.com/woof-pupsicle-pops-refills-beef/dp/3283638) (repris).
- **Dent cassée** : un avis sur une fiche revendeur (repris, attribution probable : [Tractor Supply](https://www.tractorsupply.com/tsc/product/woof-pupsicle-green-small-2456837?store=2547)).
- **Nettoyage.** Le Kong est jugé difficile à nettoyer, la nourriture restant coincée au fond. Le Toppl est apprécié pour sa large ouverture ([CNN Underscored](https://amp.cnn.com/cnn/cnn-underscored/reviews/west-paw-zogoflex-toppl-dog-toy), repris).
- **Mentions déjà affichées en France.** Les fiches françaises de jouets congelables précisent qu'aucun jouet n'est indestructible et qu'il faut surveiller le chien ([PetSafe FR](https://www.petsafe.com/fr/product/jouet-a-friandises-congelable-pour-chiens-frosty-cone) ; [zooplus.fr](https://www.zooplus.fr/shop/chiens/bols_gamelles_fontaines/gamelles/9980063505), repris de `us_feeding_cleaning_enrichment.md`).

#### 2.4 Intrants du coût rendu en France (livrable 2)

| Poste | Valeur | Statut, date | Source |
|---|---|---|---|
| Poids de la Woof Pupsicle L (ASIN B0C15QKM3X) | 10,2 oz ≈ **289 g** ; une variante affiche 11,36 oz ≈ 322 g | [S2] miroirs de fiche Amazon, n.d., relevé du 2026-10-28 (W25) | [desertcart ZA](https://www.desertcart.co.za/products/537931284-woof-pupsicle-large-25-75-lbs-long-lasting-dog-toy) ; [desertcart MA](https://www.desertcart.ma/products/537931284) ; [desertcart TH](https://www.desertcart.co.th/products/529579564-pupsicle-long-lasting-interactive-dog-ball-toy-to-keep-your) (extrait agrégé) |
| Dimensions de la Woof L sur la fiche | 4,6 × 3 × 4,6 po = 11,68 × 7,62 × 11,68 cm. **Incohérent avec le diamètre officiel de 3,6 po (9,1 cm)** : forme aplatie, emballage ou erreur de fiche ; à mesurer sur un échantillon | [S2], idem | idem |
| Diamètres Woof par taille | S 7,4 cm ; L 9,1 cm ; XL 12,2 cm | [S] Woof, repris | [Woof](https://support.mywoof.com/en-US/general-toy-sizing-and-dimensions-1208428) |
| Tailles catalogue chinoises | 5 à 8 cm | [F] | Tableau 1.1, lignes 1 et 15 |
| Fret aérien (indice) | ≈4,88 $/kg (semaine du 08/09/2026), d'aéroport à aéroport, hors frais annexes | [S2], repris de `fr_couts_commerciaux.md` | [DocShipper](https://china.docshipper.com/en/?p=30165) |
| Aérien DDP | 5–9 $/kg au-delà de 100 kg palettisés, « from $6/kg for small parcels » ; 5,70–6,40 $/kg à partir de 45 kg, en 8 à 10 jours | [S2] 2026, repris | [Dantful](https://www.dantful.com/ddp-shipping-from-china-to-france/) ; [Viputrans](https://www.viputrans.com/shipping-from-china-to-france-2026-guide-to-importing-goods.html) ; [Weilong](https://www.weilong-sz.com/ddp-shipping-from-china-to-france/) |
| Express | 7,75 $/kg (octobre 2026) ; ≈11,35 $/kg (guide de juin 2026) | [S2], repris | [Sino-Shipping](https://www.sino-shipping.com/country-guides/shipping-from-china-to-france/) ; [Goodhope](https://www.goodhopefreight.com/freight/freight-price-list-from-china-to-france.html) (rattachement non isolé) |
| Groupage maritime (LCL) | 30–60 $/m³ pour le fret seul, 15 à 45 jours de transit, plus de 30 % de hausse en haute saison (août à octobre) | [S2] T2 2026, repris | [Sino-Shipping](https://www.sino-shipping.com/fr/freight-costs-from-china/overview/) |
| Conteneur de 40 pieds Shanghai–Rotterdam | 3 944 $ (08/07/2026) ; aucun relevé d'octobre | [S2], repris | [The Logistics World](https://thelogisticsworld.com/actualidad-logistica/world-container-index-de-drewry-se-mantiene-a-la-baja) |
| Ferroviaire | 250–450 $/m³ (même source contradictoire sur l'écart avec le maritime) | [S2], repris | [Sino-Shipping](https://www.sino-shipping.com/fr/freight-costs-from-china/overview/) |
| Agent de sourcing | 3 à 10 % de la commande (5 à 10 % le plus cité, jusqu'à 15 % sur les petites commandes) ; environ 100 $ par jour de visite d'usine | [S2] 2026, repris | [Epic Sourcing](https://www.epicsourcing.co.uk/post/china-sourcing-agent-cost-uk-2026) ; [Supplyia](https://www.supplyia.com/China-sourcing-agent/) |
| Droits de douane, import de stock | 3926 90 97 (autres ouvrages en plastique) : **6,5 %**. Taux UE de la position 4016 (caoutchouc vulcanisé) : n.o. Une balle en caoutchouc pour chien est classée 4016.99.20 (« toys for pets ») aux USA et 4016 99 97 90 (balle de tennis pour chien) au Royaume-Uni | [S2] TARIC miroir 2026 ; [S] décisions US et UK ; repris | [tariffnumber.com](https://www.tariffnumber.com/2026/39269097) ; [CBP NY N012649](https://www.customsmobile.com/rulings/docview?doc_id=NY+N012649) ; [HMRC ATaR 600013614](https://www.tax.service.gov.uk/search-for-advance-tariff-rulings/ruling/600013614) |
| Droit forfaitaire de 3 € et frais de 2 € | Ils ne visent que les envois B2C d'au plus 150 € (dropshipping) : 3 € par article distinct depuis le 01/07/2026, 2 € de frais de traitement attendus au 01/11/2026. Ils ne visent pas un import de stock B2B (inférence de la note source) | [S]/[S2], repris de `fr_costs_regulation.md` | [Guide de la Commission](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf) ; [Revenue (Irlande)](https://www.revenue.ie/en/corporate/press-office/press-releases/2026/pr-092926-handling-fee.aspx) |
| Livraison au client en France | Mondial Relay en point relais : 4,15 € TTC jusqu'à 500 g, 5,99 € jusqu'à 1 kg (grille du 15/06/2026). Colissimo à domicile : 7,59 € à 500 g, 9,59 € à 1 kg (01/01/2026) | [S]/[S2], repris de `fr_couts_commerciaux.md` | [ShippyPro](https://www.shippypro.com/blog/fr/envoyer-un-colis-prix-et-tarifs-2026-des-transporteurs-en-france) ; [La Poste](https://www.laposte.fr/colissimo-en-ligne/tarifs) |
| REP emballages | Forfait Citeo de 80 € HT par an sous 10 000 UVC (2025) ; 110 € selon une source secondaire (conflit) ; carton ondulé à 0,177 €/kg | [S]/[S2], repris | [Citeo](https://bo.citeo.com/sites/default/files/2025-04/20241219_MAJ_Tarif_EM_2025-FR.pdf) ; [EPR Representative](https://eprrepresentative.com/blog/bareme-emballages-menagers-2027-citeo-leko) ; [AuditREP](https://auditrep.fr/blog/tarif-citeo-bareme-emballages-2026) |

#### 2.5 Emballage de marque : fournisseurs et coûts (livrable 7)
- **Boîtes imprimées chez les fabricants chinois (W27, 2026-10-28) :**
  - **Shanghai Hongyun** : boîte en carton ondulé avec fenêtre en plastique PET, impression offset CMJN, **0,35–0,80 $ pièce, MOQ de 1 000**, minimum justifié par « machine setup cost and freight » ([MIC](https://sh-hongyun.en.made-in-china.com/product/TFaQsuHDOxci/China-Wholesale-Custom-Kids-Plush-Doll-Gift-Corrugated-Window-Toy-Box-Packaging-with-Plastic-Pet.html)) [F] ;
  - autres boîtes de jouet à fenêtre sur Made-in-China : 0,25–0,70 $ (MOQ de 1 000) et 0,12–0,46 $ (MOQ de 500) ([MIC, Toy Window Box](https://www.made-in-china.com/products-search/hot-china-products/Toy_Window_Box.html), attribution probable) [F] ;
  - boîtes transparentes en PVC pour chien et chat : 0,10–0,23 $, MOQ non visible ; boîte à fenêtre pour vêtements de chien : 0,19–0,59 $, MOQ de 1 000 ([Alibaba, pet window packaging box](https://www.alibaba.com/showroom/pet-window-packaging-box.html) ; [Alibaba, pvc dog box](https://www.alibaba.com/showroom/pvc-dog-box.html), attribution non isolée) [F].
- **Emballage personnalisé par le fabricant du produit** : à partir de 1 000 pièces (tapis à lécher, W5 ; Soleil, ligne 18 du tableau 1.1) [F].
- **Packhelp (Pologne, site britannique ; W24, 2026-10-28) :**
  - boîtes d'expédition imprimées **à partir de 30 pièces** ;
  - impression recto verso et finitions (dorure à chaud, gaufrage) en option, avec un MOQ de 1 500 ;
  - FAQ : 1 500 boîtes standard non imprimées (FEFCO 427) coûtent environ 2 300 £, **soit 1,53 £ pièce** ;
  - prix 2026 en petite quantité : n.o. (le configurateur n'est pas lisible dans les extraits) ;
  - sources : [Packhelp UK, mailer boxes](https://packhelp.co.uk/shop/boxes/mailer-boxes) ; [Packhelp UK, types](https://packhelp.co.uk/shop/boxes/type/mailer-boxes/) (n.d.).
  - En 2017, les prix démarraient à « .43 cents per box » ([TechCrunch](https://techcrunch.com/2017/04/07/packhelp-raises-e350000-to-make-your-boxes-pretty/), HISTORIQUE).
- **Estimation d'un concurrent de Packhelp** : boîtes d'expédition kraft de 0,40 à 1,50 $ pièce en gros, plus chères en petite quantité ([Custom Box Makers](https://www.customboxmakers.com/?p=45316), contenu commercial) [S2].

### Inferences

#### A. Cahier des charges d'une version différenciée (à valider par prototypes)
1. **Fermeture sans filetage fin.** Trois options, de la plus simple à la plus « boule » :
   - **(a) Pas de fermeture.** Une coupe à large ouverture et contre-dépouille, sur le modèle du Toppl : la préparation congelée reste prise dans la forme. Rien ne peut gripper, et le nettoyage est facile.
   - **(b) Bouchon élastomère à pression**, sans rotation, sur le modèle du « Toppl Stopper ». Le bouchon doit être imperdable ou trop gros pour être avalé [H].
   - **(c) Baïonnette quart de tour** à ergots larges, moulés dans un insert rigide (PP ou POM [H]) entièrement noyé dans le caoutchouc, pour qu'aucune arête dure ne soit exposée aux dents.
   - **Pourquoi le filetage grippe [CJ] :** frottement élastomère contre élastomère, déformation à la chaleur du lave-vaisselle, résidus alimentaires et glace dans les filets. C'est cohérent avec les plaintes contre Woof et ses copies.
   - **Protocole de validation [H] :** 100 cycles de lave-vaisselle, 50 cycles de congélation et décongélation, mesure de la force d'ouverture avant et après, chute à −18 °C, essai de mâchage.
   - Une promesse du type « s'ouvre encore après 100 lavages », prouvée en vidéo, devient un argument publicitaire (piste déjà notée dans `us_verif_woof_pupsicle.md`).
2. **Anti-ventouse.** Chaque cavité doit avoir **au moins deux ouvertures**, sur la recommandation des vétérinaires (2.3), et aucune pièce amovible ne doit laisser un trou d'une taille où la langue peut se coincer.
3. **Matière.**
   - Corps en caoutchouc naturel pour la gamme « grands chiens » : dureté Shore A et épaisseur de paroi à fixer par les essais [H] ; colorants conformes REACH.
   - Mention « contient du caoutchouc naturel (latex) ».
   - Variante en silicone, sans latex, réservée aux « lécheurs » [H] : la résistance au déchirement du silicone n'est pas documentée ici (gap).
   - Nylon exclu des surfaces mâchées.
4. **Tailles.**
   - Elles s'inscrivent dans les repères Woof : L de 9,1 cm pour 11 à 34 kg, XL de 12,2 cm pour 34 kg et plus.
   - Pour la clientèle de Pilou (grands chiens à sous-poil), on peut **lancer avec deux tailles, L et XL**, ce qui réduit le nombre de moules (inférence).
   - Tableau des tailles par poids **en kilos**, avec la règle « le jouet ne doit jamais entrer entièrement dans la gueule » [H].
5. **Recharges et anti-étouffement.**
   - Une recharge ou un noyau congelé doit rester **prisonnier** du jouet, c'est-à-dire plus large que les ouvertures [H].
   - Pas de palet dur et glissant, à cause des cas d'étouffement Woof (2.3).
   - Portion calibrée par taille.
6. **Hygiène et usage.**
   - Pas de recoin aveugle (plainte contre le Kong) ; passage au lave-vaisselle, panier du haut [H].
   - Base qui tient debout pour limiter les salissures (piste de `fr_deep_jouet_lechage_congelable.md`).
   - Couleur vive pour repérer les fragments [H].
7. **Traçabilité.** Numéro de lot moulé ou gravé sur le produit, mentions GPSR sur la boîte (section 3) [H].

#### B. Budget de développement [calc]
- **Moules.**
  - Deux tailles (L et XL), avec un corps en une ou deux pièces et une pièce de fermeture : 2 à 6 jeux de moules de compression à 500–3 500 $ (Melon Rubber), **soit 1 000 à 21 000 $, ou 860 à 18 060 €**.
  - Avec des moules « basiques » à la Wedogy (80–150 $), on descendrait à 160–900 $. Mais leur durée de vie et leur précision sont inconnues, et la portée du prix n'est pas claire.
  - Le moule d'injection d'un insert rigide en PP ou POM n'est pas chiffré (gap).
  - L'injection LSR (5 000–50 000 $) n'est pas justifiée au lancement.
- **Autres postes non sourcés :** design industriel et CAO, prototypes en impression 3D, essais de laboratoire REACH, essais d'usage. Ils sont à chiffrer par devis.
- **Échantillons** : 30–60 $ par design (Wedogy), plus le transport express (n.o.).

#### C. Coût unitaire et coût rendu indicatifs [calc]
*Hypothèses de poids [H] :*
- *boîte de vente ≈0,05 kg ;*
- *moule en silicone ≈0,10 kg ;*
- *balle L ≈0,289 kg (poids Woof sourcé) ;*
- *carton de 12 × 12 × 9 cm ≈0,0013 m³.*

*Le poids volumétrique aérien (L × l × h / 6 000) vaut environ 0,17 kg (dimensions de la fiche Woof, 1 040 cm³) à 0,22 kg (carton de 12 × 12 × 9 cm, 1 296 cm³). Il reste inférieur au poids réel, qui sert donc de base.*
- **Fret aérien DDP par unité :**
  - balle L en boîte (0,34 kg) : 1,70 $ à 5 $/kg (1,46 €), 2,04 $ à 6 $/kg (1,75 €), 3,06 $ à 9 $/kg (2,63 €) ;
  - kit L avec moule (0,44 kg) : 2,20 $ (1,89 €), 2,64 $ (2,27 €), 3,96 $ (3,41 €).
- **Groupage maritime :** 0,04 à 0,08 $ par carton de 0,0013 m³ pour le fret seul. Les frais fixes d'origine, de port, de dédouanement et de livraison ne sont pas sourcés et dominent sur un petit envoi.
- **Exemple : kit L de catalogue, rendu en France par avion.**
  - Balle en caoutchouc naturel : 1,53–2,29 $ [F] (Suzhou Becpet).
  - Logo : +0,20 $ [F] (relevé sur un tapis à lécher, transposition [H]).
  - Moule silicone avec logo : 0,87–1,36 $ [F] (Xiamen Hands Chain, section 4).
  - Boîte imprimée : 0,35–0,80 $ [F] (Shanghai Hongyun).
  - Sous-total : 2,95–4,65 $.
  - Fret à 6 $/kg × 0,44 kg : 2,64 $.
  - **Total : environ 5,59 à 7,29 $, soit 4,81 à 6,27 € par kit**, hors commission d'agent (5 à 10 %), inspection, échantillons, droits éventuellement non inclus dans l'offre DDP et logistique en France.
- **Poids d'une XL [calc].** Si la géométrie du L est conservée, le volume est multiplié par (12,2 / 9,1)³ ≈ 2,41, soit ≈697 g de caoutchouc. Si l'épaisseur des parois n'augmente pas, le poids est plus faible : environ **0,5 à 0,7 kg [H]**.
  - Une XL emballée dépasserait donc 500 g : Mondial Relay passe de 4,15 € à 5,99 €, Colissimo de 7,59 € à 9,59 € (repris de `fr_couts_commerciaux.md`).
  - Le fret aérien de la XL coûterait environ 3,51 € (6 $/kg) à 5,26 € (9 $/kg) pour 0,68 kg [calc].
- **Version XL propriétaire [H] :** prix FOB de 3 à 7 $ pour le corps et l'insert. C'est une hypothèse de travail à remplacer par des devis : les prix catalogue relevés (0,60–3,80 $) portent sur des balles de 8 cm au plus.

#### D. Brevets Woof : rester à distance
- Woof détient aux USA les brevets d'utilité **US 12 402 601 B2** et **US 12 582 096** (« Treat retaining pet toy »). Le second est résumé dans l'extrait comme « a cylindrical body with an open bottom end and a core member holding a treat container » (repris de `us_verif_woof_pupsicle.md` : [Justia](https://patents.justia.com/assignee/woof-pet-inc)).
- **Aucune demande EP, WO ou FR n'a été trouvée** (non vérifié dans Espacenet).
- **Inférences [CJ], à valider par un conseil en propriété industrielle :**
  - pour la France, le risque brevet paraît faible ;
  - il faut néanmoins éviter de copier la forme, les fentes, les couleurs et le vocabulaire de la Pupsicle (droit d'auteur, concurrence déloyale et parasitisme) ;
  - une fermeture différente (options a à c) et une architecture sans « core member » inséré par un fond ouvert éloignent aussi le produit des brevets US, si la marque vend un jour aux USA ;
  - les revendications n'ont pas été lues.

### Gaps
- **Devis réels de moules** : nombre d'empreintes, acier, durée de vie en cycles, propriété ; coût d'un moule d'injection plastique pour un insert. Non obtenus.
- **Coûts non sourcés** : design industriel, prototypes, essais de laboratoire (REACH, HAP, phtalates) et essais d'usage.
- **Silicone** : résistance au déchirement, tenue aux mâcheurs, comportement au congélateur. Aucune source.
- **TPR au froid** : fragilité éventuelle au congélateur, non recherchée.
- **Dureté Shore et épaisseurs de parois** des produits Woof et des concurrents : non trouvées.
- **Poids réels** d'une XL et des moules en silicone : non trouvés (hypothèses [H]).
- **Freinte et défauts** : taux de rebut et AQL usuels pour le caoutchouc moulé, non recherchés.
- **Frais fixes d'un groupage** porte-à-porte Chine–France : non sourcés (déjà en gap de `fr_couts_commerciaux.md`).
- **Taux de droit UE pour la position 4016** (jouet pour chien en caoutchouc) : non trouvé. Demander un RTC (renseignement tarifaire contraignant).

---

## 3. Quelles sont les exigences de conformité UE et françaises, et quel délai réaliste faut-il compter de l'échantillon au premier stock en France ?

### Takeaway
- **Pas de marquage CE ni de norme harmonisée pour un jouet pour chien, mais un socle obligatoire.**
  - **GPSR (UE) 2023/988** : la marque est le fabricant. Elle doit tenir une analyse de risques et une documentation technique, assurer la traçabilité par lot, indiquer son nom et ses adresses, rédiger les avertissements en français et publier les informations requises sur la fiche produit.
  - **REACH, annexe XVII** : HAP limités à 1 mg/kg dans les caoutchoucs et plastiques en contact avec la peau ; phtalates DEHP, DBP, BBP et DIBP sous 0,1 % dans les articles en général.
  - Obligations françaises sur les emballages (REP, IDU, Triman et Info-tri) et formalités de douane.
- **Contact alimentaire : aucune source ne tranche** si le règlement (CE) 1935/2004 s'applique au contact avec la nourriture pour animaux. Mon analyse est non vérifiée [CJ] :
  - le **jouet** n'y serait pas soumis, car la nourriture pour chien est un « aliment pour animaux » et non une « denrée alimentaire » ;
  - un **moule en silicone vendu pour la cuisine** peut, lui, « raisonnablement » entrer en contact avec des denrées humaines, ce qui le ferait entrer dans le champ du règlement ;
  - **bonne pratique : exiger une déclaration de conformité contact alimentaire et des essais de migration pour les moules.**
- **Délai de l'échantillon au premier stock en France [calc] :**

  | Cas | Aérien | Maritime |
  |---|---|---|
  | Produit de catalogue avec logo | 10 à 20 semaines (2,5 à 5 mois) | 12 à 26 semaines |
  | Moule propriétaire | 15 à 36 semaines | 16 à 42 semaines |

  Le Nouvel An chinois (6 février 2027 [CJ]) allongera tout projet lancé cet hiver.

### Cited Findings

#### 3.1 GPSR (repris de `fr_costs_regulation.md`, non revérifié)
- **Champ.** Les produits pour animaux relèvent du GPSR lorsqu'ils sont mis à disposition comme produits de consommation. TÜV SÜD cite les jouets et les gamelles parmi les produits à évaluer au titre du GPSR, de REACH et de RoHS ([TÜV SÜD, 05/2026](https://www.tuvsud.com/en/newsroom/press-releases/2026/may/tuev-sued-eu-requirements-enhance-safety-and-transparency-for-consumers) ; [TÜV SÜD Italie, 03/2026](https://www.tuvsud.com/it-it/news-e-comunicati-stampa/2026/march/regolamento-ue-2023-988-sicurezza-dei-prodotti-e-accessori-nella-pet-economy)).
- **Fiche produit en ligne (art. 19).** Elle doit indiquer :
  - le nom ou la marque du fabricant et ses adresses postale et électronique ;
  - la personne responsable dans l'UE si le fabricant est hors UE ;
  - l'identification du produit (image, type, lot ou autre identifiant) ;
  - les avertissements dans la langue du pays.
  - Ces informations doivent figurer **sur la page produit elle-même**.
  - Sources : [eugpsr.de](https://eugpsr.de/en/blog/gpsr-online-sales-required-info) ; [Xictron](https://www.xictron.com/en/blog/gpsr-product-safety-regulation-online-shop-2026/) ; [EU Seller Kit](https://eusellerkit.com/en/gpsr-responsible-person/article-19).
- **Date d'application** : depuis le 13/12/2024 ([Wikipedia](https://en.wikipedia.org/wiki/General_Product_Safety_Regulation)).
- **Articulation** : le GPSR couvre les risques non couverts par une législation sectorielle de l'Union ([MCCAA](https://mccaa.org.mt/technical-regulation/general-product-safety/)).
- **[CJ]** :
  - analyse de risques et documentation technique conservée 10 ans (art. 9) ;
  - déclaration des accidents via le Safety Business Gateway (art. 20) ;
  - une marque française qui vend sous son nom est le « fabricant ».
  - La directive 2009/48/CE sur la sécurité des jouets ne vise que les jouets d'enfants, pas les jouets pour animaux (déjà signalé en [CJ] dans `us_feeding_cleaning_enrichment.md`).

#### 3.2 REACH (W18, 2026-10-28)
- **Entrée 50 (HAP).** Guide de l'ECHA : « Articles shall not be placed on the market for supply to the general public, if any of their rubber or plastic components that come into direct as well as prolonged or short-term repetitive contact with the human skin or the oral cavity, under normal or reasonably foreseeable conditions of use, contain more than 1 mg/kg » de l'un des huit HAP listés.
  - Les jouets, y compris d'activité, et les articles de puériculture sont soumis à une limite de **0,5 mg/kg**.
  - La Commission a demandé à l'ECHA de réexaminer l'entrée 50 : les limites pourraient changer.
  - Sources : [ECHA, guide de l'entrée 50](https://echa.europa.eu/documents/10162/15792/guideline_entry_50_PAHs_en.pdf/f12ac8e7-51b3-5cd3-b3a4-57bfc2405d04) ; [ECHA, guide du champ](https://echa.europa.eu/documents/10162/13641/scope_restriction_guideline_pahs_en.pdf/e62efb0b-96e7-2f72-7027-13f553f9669b) ; [Règl. (UE) 1272/2013](https://www.legislation.gov.uk/eur/2013/1272/data.xht). Textes de 2013 et après (HISTORIQUE par la date, restriction en vigueur).
- **Entrée 51 (phtalates).** Le règlement (UE) 2018/2005, publié le 18/12/2018, remplace l'entrée 51 :
  - il ajoute le DIBP au DEHP, au DBP et au BBP ;
  - il étend le champ des jouets et articles de puériculture aux articles en général.
  - Selon SGS, les nouvelles règles « took effect January 7, 2019 ». **Conflit de date** : à ma connaissance [CJ], c'est la date d'entrée en vigueur, et l'application aux articles date du 07/07/2020. La formulation exacte de la limite de 0,1 % (« individually or in any combination », en masse de matière plastifiée) est aussi à vérifier [CJ].
  - Sources : [SGS, 01/2019](https://www.sgs.com/en-iq/news/2019/01/safeguards-00219-eu-expands-restriction-of-phthalates-under-reach) (HISTORIQUE) ; [Règl. (UE) 2018/2005, annexe](https://legislation.gov.uk/eur/2018/2005/annex?view=plain).
- **Jouets pour animaux.** Ils ne sont pas nommés dans ces sources (W18). Il reste à vérifier s'ils relèvent de la limite « jouets » (0,5 mg/kg) ou de la limite générale (1 mg/kg).
- **SVHC au-delà de 0,1 %** : information des clients et notification SCIP (repris de `fr_costs_regulation.md` : [ComplianceGate](https://www.compliancegate.com/reach-svhc-substance-list/)).

#### 3.3 Contact alimentaire (W16, W17, 2026-10-28)
- **Champ du règlement (CE) 1935/2004.** Il vise les matériaux et objets destinés à entrer en contact avec des denrées alimentaires, ou dont on peut raisonnablement s'attendre à ce qu'ils le soient dans des conditions normales d'emploi. Ils doivent être assez inertes pour ne pas céder de substances en quantité dangereuse ni modifier les denrées. Les États membres peuvent adopter des mesures nationales en l'absence de mesures spécifiques de l'UE. Sources : [FSAI](https://www.fsai.ie/enforcement-and-legislation/legislation/food-legislation/materials-and-articles-in-contact-with-foodstuffs/legislation) ; [EUR-Lex, synthèse](https://eur-lex.europa.eu/DE/legal-content/summary/food-safety-safe-food-contact-materials.html) ; [EUR-Lex, texte consolidé](https://eur-lex.europa.eu/eli/reg/2004/1935/2009-08-07) ; [AGRINFO](https://agrinfo.eu/book-of-reports/food-contact-materials-explained/translate/fr). Texte de 2004, en vigueur.
- **Nourriture pour animaux : aucune source.** Deux requêtes n'ont fait ressortir aucun texte ni guide sur les gamelles ou les jouets pour animaux.
- **[CJ] Points à faire confirmer :**
  - le règlement (CE) 178/2002 exclut l'« aliment pour animaux » de la définition de « denrée alimentaire » (art. 2) ;
  - la France a des règles nationales sur les élastomères de silicone au contact des denrées (arrêté du 25/11/1992) ;
  - l'Allemagne applique la recommandation XV du BfR.
- **Allégations des fournisseurs** : « food grade » et LFGB sont fréquents sur les annonces de silicone (W5, W23). Il faut demander les rapports d'essais (FDA ou LFGB selon la synthèse de W23).

#### 3.4 Avertissements, langue, emballages
- **Avertissements déjà d'usage en France** : « aucun jouet n'est indestructible » et surveillance du chien ([PetSafe FR](https://www.petsafe.com/fr/product/jouet-a-friandises-congelable-pour-chiens-frosty-cone) ; [zooplus.fr](https://www.zooplus.fr/shop/chiens/bols_gamelles_fontaines/gamelles/9980063505), repris).
- **Conseils des vétérinaires** : second trou d'air, retrait des jouets abîmés, surveillance (2.3).
- **Latex** : avertissement de Woof (2.2).
- **REP emballages (repris de `fr_costs_regulation.md`)** :
  - la marque est « producteur » d'emballages ménagers et adhère à Citeo ou à Léko : [Citeo, tarif 2025](https://bo.citeo.com/sites/default/files/2025-04/20241219_MAJ_Tarif_EM_2025-FR.pdf) ;
  - identifiant unique (IDU, art. L. 541-10-13 du Code de l'environnement) à afficher dans les CGV et sur le site : [GHR, fiche IDU](https://www.ghr.fr/IMG/pdf/fiche_memo_-_idu_fr.pdf) ;
  - Triman et Info-tri [CP de la note source].
- **[CJ]** : langue française obligatoire (loi n° 94-665, dite loi Toubon). Le règlement (UE) 2025/40 sur les emballages (PPWR) s'applique depuis le 12/08/2026 ; non recherché.

#### 3.5 Douane (repris de `fr_costs_regulation.md`)
- **Import de stock en B2B** : droits ad valorem plus TVA à l'import autoliquidée [CP].
  - 3926 90 97 : 6,5 % ([tariffnumber.com](https://www.tariffnumber.com/2026/39269097)).
  - Taux pour la position 4016 : n.o.
  - Classements étrangers d'une balle pour chien en 4016 : [CBP NY N012649](https://www.customsmobile.com/rulings/docview?doc_id=NY+N012649) ; [HMRC ATaR 600013614](https://www.tax.service.gov.uk/search-for-advance-tariff-rulings/ruling/600013614).
- **Dropshipping B2C (envois d'au plus 150 €)** :
  - 3 € par article distinct depuis le 01/07/2026 ([Guide de la Commission](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)) ;
  - 2 € de frais de traitement attendus au 01/11/2026 ([Revenue, Irlande](https://www.revenue.ie/en/corporate/press-office/press-releases/2026/pr-092926-handling-fee.aspx)).

#### 3.6 Composantes de délai sourcées
- **Échantillons :**
  - 3 à 5 jours ouvrés, ou 15 jours ouvrés sur mesure ([Wedogy](https://wedogy.com/dog-toys/) ; [Wedogy](https://wedogy.com/christmas-dog-toys/)) ;
  - 7 jours avec logo (tapis à lécher, W5).
- **Outillage :**
  - 4 à 6 jours pour un moule simple (Wedogy) ;
  - 7 jours (prototype) et 14 jours (production) chez Melon Rubber ;
  - 2 à 4 semaines (prototype) et 6 à 8 semaines (production) chez Qualiform ;
  - 3 à 6 semaines pour un moule en acier trempé (GC Indus) ;
  - environ 4 à 6 semaines pour un moule complexe (Newtop).
  - Sources : section 2.1.
- **Production :**
  - 12 à 18 jours ouvrés ou 25 jours ouvrés (Wedogy) ;
  - 5 à 30 jours selon la quantité (tapis à lécher, W5) ;
  - 45 jours après l'acompte (Jiangyin Qianding, W6, W30).
- **Transport (repris de `fr_couts_commerciaux.md`) :**
  - aérien DDP en 8 à 10 jours ([Viputrans](https://www.viputrans.com/shipping-from-china-to-france-2026-guide-to-importing-goods.html)) ;
  - groupage maritime en 15 à 45 jours de transit ([Sino-Shipping](https://www.sino-shipping.com/fr/freight-costs-from-china/overview/)).

### Inferences

#### Check-list de conformité (livrable 5)

| # | Exigence | Base | Jouet | Moule en silicone | Preuve à obtenir ou action | Statut de la source |
|---|---|---|---|---|---|---|
| 1 | Analyse de risques et documentation technique ; la marque est le fabricant | GPSR, art. 9 [CJ] | Oui | Oui | Dossier : usages prévisibles (gros mâcheur, chiot, congélation, lave-vaisselle), risques (ventouse, étouffement, dents, latex), mesures prises, essais ; conservation 10 ans [CJ] | Repris [S2] et [CJ] |
| 2 | Identification : type ou modèle et lot sur le produit ou l'emballage ; nom, marque, adresses postale et électronique | GPSR | Oui | Oui | Lot moulé ou gravé [H] ; mentions sur la boîte | Repris [S2] |
| 3 | Avertissements et mode d'emploi en français | GPSR ; loi Toubon [CJ] | Oui | Oui | Texte ci-dessous | Repris [S2] et [CJ] |
| 4 | Fiche produit en ligne : fabricant, adresses, image, type, lot ou identifiant, avertissements | GPSR, art. 19 | Oui | Oui | Gabarit de fiche Shopify | Repris [S2] |
| 5 | Accidents et rappels (Safety Business Gateway), registre des réclamations | GPSR, art. 20 [CJ] | Oui | Oui | Procédure interne | [CJ] |
| 6 | HAP ≤ 1 mg/kg ; 0,5 mg/kg si le produit est considéré comme un jouet | REACH, annexe XVII, entrée 50 | Oui : le caoutchouc est manipulé par le maître [inférence] | Oui | Rapport de laboratoire par matière et par couleur ; viser 0,5 mg/kg par prudence [H] | [S] ECHA |
| 7 | DEHP, DBP, BBP et DIBP sous 0,1 % de la matière plastifiée | REACH, entrée 51 (règl. 2018/2005) | Oui si la matière est plastifiée (TPR, PVC) ; peu probable pour du caoutchouc naturel ou du silicone [CJ] | Idem | Rapport de laboratoire | [S2] SGS et [CJ] |
| 8 | SVHC au-delà de 0,1 % : information (art. 33) et notification SCIP | REACH | Oui | Oui | Déclaration du fournisseur contrôlée contre la liste SVHC à jour | Repris [S2] |
| 9 | Contact alimentaire | Règl. 1935/2004 ; règles nationales sur le silicone [CJ] | Probablement non (aliment pour animaux) [CJ] | Probablement oui s'il est vendu pour la cuisine ou utilisable avec des denrées [inférence] | Déclaration de conformité et essais de migration (LFGB ou règles françaises) ; pas de symbole « verre et fourchette » sans preuve [H] | [S] champ ; [CJ] application |
| 10 | Directive 2009/48/CE (jouets) | — | Non : elle vise les jouets d'enfants [CJ] | Non | Ne pas présenter le produit comme un jouet d'enfant [H] | [CJ] |
| 11 | REP emballages (Citeo ou Léko), IDU affiché, Triman et Info-tri | Code de l'environnement (loi AGEC) | Emballage | Emballage | Adhésion, IDU dans les CGV et sur le site, maquette Triman et Info-tri | Repris [S] et [CP] |
| 12 | Règlement emballages (PPWR) (UE) 2025/40 | Applicable depuis le 12/08/2026 [CJ] | Emballage | Emballage | À analyser (non recherché) | [CJ] |
| 13 | Douane : classement (4016 ou 3926), droits, EORI, TVA à l'import | Code des douanes de l'Union ; TARIC | Oui | Oui | RTC en cas de doute ; transitaire | Repris [S2] et [CP] |
| 14 | Responsabilité du fait des produits défectueux | Directive (UE) 2024/2853, transposition au plus tard le 09/12/2026 [CJ] | Oui | Oui | Assurance responsabilité civile produits [H] | [CJ] |
| 15 | Allégations (« sans BPA », « non toxique », « alimentaire », « anti-stress ») | Pratiques commerciales trompeuses [CJ] | Oui | Oui | Preuve écrite pour chaque allégation | [CJ] |
| 16 | Recharges alimentaires | Règl. 767/2009 et 183/2005 | — | — | Voir section 4 | [S] |

**Avertissements à prévoir sur la boîte et la fiche** (inférence à partir de 2.3 et 3.4) :
- « Surveillez toujours votre chien pendant l'utilisation. »
- « Aucun jouet n'est indestructible : retirez-le dès qu'il est abîmé ou qu'un morceau se détache. »
- « Choisissez la taille selon le poids de votre chien (tableau en kg) ; le jouet ne doit jamais entrer entièrement dans la gueule. »
- « Contient du caoutchouc naturel (latex) », si c'est le cas.
- « Ne garnissez qu'avec des aliments adaptés au chien ; jamais de xylitol. » Le xylitol est cité par la vidéo @colzouti, voir `fr_deep_jouet_lechage_congelable.md`. D'autres aliments toxiques (raisin, chocolat, oignon) sont à faire valider par un vétérinaire [CJ].

#### Calendrier réaliste, de l'échantillon au premier stock en France [calc]
*Composantes sourcées en 3.6 ; étapes [H] marquées comme telles. Les totaux additionnent les bornes basses puis les bornes hautes.*

**Scénario A : produit de catalogue avec logo et boîte personnalisée, sans nouveau moule**

| Étape | Durée | Statut |
|---|---|---|
| Appel d'offres et sélection (5 à 10 fournisseurs) | 1 à 2 semaines | [H] |
| Préparation des échantillons | 1 à 3 semaines (3 jours ouvrés à 15 jours ouvrés) | [F] Wedogy ; W5 |
| Envoi express des échantillons | ≈1 semaine | [H] |
| Essais internes (congélation, lave-vaisselle, chiens) | 2 à 3 semaines | [H] |
| Production | 3 à 7 semaines (12 jours ouvrés à 45 jours) | [F] |
| Inspection avant expédition | 0 à 0,5 semaine | [H] |
| Aérien DDP | 1,5 à 2 semaines (8 à 10 jours, plus l'enlèvement) | Repris [S2] et [H] |
| Ou maritime LCL | 3 à 8,5 semaines (15 à 45 jours de transit, plus 1 à 2 semaines de formalités) | Repris [S2] et [H] |
| Réception en logistique et mise en ligne | ≈1 semaine | [H] |
| **Total** | **≈10,5 à 19,5 semaines en aérien ; ≈12 à 26 semaines en maritime** | [calc] |

**Scénario B : design propriétaire (XL, fermeture sans filetage) avec moules neufs**

| Étape | Durée | Statut |
|---|---|---|
| Cahier des charges, design et CAO | 2 à 4 semaines | [H] |
| Prototype (impression 3D ou outil prototype) | 1 à 4 semaines | [S2] Melon Rubber, Qualiform, Newtop |
| Essais des prototypes (chiens, lavages, congélation) | 3 à 6 semaines | [H] |
| Moule de production | 2 à 8 semaines | [S2] Melon Rubber, GC Indus, Newtop, Qualiform |
| Échantillons de série (T1) et retouches | 1 à 3 semaines | [H] |
| Production, inspection, transport, réception | Comme le scénario A | — |
| **Total** | **≈14,5 à 35,5 semaines en aérien (3,5 à 8 mois) ; ≈16 à 42 semaines en maritime (4 à 10 mois)** | [calc] |

#### Conséquence pour la saison 2027 (inférence)
- **Projection à partir d'aujourd'hui (2026-10-28) [calc] :**
  - scénario A : stock entre mi-janvier et mi-mars 2027 en aérien ; entre fin janvier et fin avril 2027 en maritime ;
  - scénario B : stock entre début février et début juillet 2027 en aérien ; jusqu'à mi-août 2027 en maritime.
- **Effet du Nouvel An chinois.** Il tombe le 6 février 2027 [CJ], avec des fermetures d'usines de 2 à 4 semaines [H]. Elles s'ajoutent à tout calendrier qui traverse février.
- **Ce qu'il faut en retenir.** Le pic d'été français (juin à août, hypothèse de `fr_deep_jouet_lechage_congelable.md`) n'est atteignable avec un moule propriétaire que si le design démarre en **novembre 2026** et si le premier lot part en aérien. Sinon, le lancement propriétaire visera la rentrée et Noël 2027, avec un positionnement « chien seul et apaisement ».
- **Option intermédiaire.** Un petit lot de catalogue (50 à 200 pièces, Ningbo General Union ou Wedogy) en aérien au premier trimestre 2027 permettrait de tester la demande avec les publicités Meta pendant le développement. Ce lot reste générique et donc copiable.

### Gaps
- **Bases officielles non consultées** : EUR-Lex (accès indirect seulement), TARIC, ECHA (version à jour de l'entrée 50), guides DGCCRF. Toutes les réponses viennent d'extraits.
- **Contact alimentaire et aliments pour animaux** : aucune source ne tranche. À faire valider par un juriste ou un laboratoire (SGS, Intertek, Bureau Veritas, TÜV).
- **Norme volontaire** de sécurité des jouets pour animaux, en Europe ou ailleurs : non recherchée.
- **Coût des essais** : HAP, phtalates et migration des moules non chiffrés.
- **PPWR, directive 2024/2853, loi Toubon, arrêté sur le silicone de 1992** : relèvent de [CJ], non vérifiés dans cette session.
- **Date du Nouvel An chinois 2027 et durée des fermetures d'usines** : relèvent de [CJ] et [H].

---

## 4. Comment construire une ligne de réachat (moules, recettes, recharges) sans lourde charge réglementaire ?

### Takeaway
- **Le réachat peut démarrer sans droit de l'alimentation animale.** Le **palier 0** comprend :
  - des moules en silicone, entre **0,28 et 3,60 $ pièce** sur Alibaba, avec logo dès 20 à 200 pièces ;
  - un livret et des vidéos de recettes ;
  - des accessoires.
  - Ce palier n'est soumis qu'au GPSR, et par prudence aux règles de contact alimentaire pour les moules.
- **Les recharges alimentaires changent le statut de la marque.**
  - Le règlement (CE) 767/2009 s'applique aux aliments pour animaux familiers. La marque sous le nom de laquelle l'aliment est vendu est responsable de son étiquetage [CJ].
  - En revanche, **le commerce de détail d'aliments pour animaux familiers est exclu du champ du règlement (CE) 183/2005** (art. 2, § 2, e), sous réserve de règles nationales (art. 2, § 3).
  - Un formulaire français de notification à la DD(ETS)PP existe. Il faut faire confirmer par la DDPP si une marque e-commerce qui fait fabriquer sous son nom doit se déclarer.
- **Façonniers européens repérés :**
  - **PAEX** (Allemagne) : lyophilisé, recettes personnalisées « even for small purchase quantities » ;
  - **Loupas** (France) : friandises lyophilisées, emballage en marque de distributeur ;
  - **Animille** (Pologne) : friandises séchées ;
  - **Rondo Food** (Allemagne) : friandises extrudées ou **moulées par injection** ;
  - annuaire Wonnda : Heristo, MERA, PPF Europe.
  - **Aucun MOQ ni prix n'a été obtenu.**
- **Glace pour chien.** Cold & Dog (Berlin) en fabrique, sans marque blanche confirmée. BeG Buddy vend des **préparations en poudre** et des moules à glace.
- **Formats compatibles avec un envoi simple** : lyophilisé, poudre à mélanger et à congeler à la maison, friandises sèches. Le surgelé est exclu en e-commerce (inférence).

### Cited Findings

#### 4.1 Moules en silicone (W23, 2026-10-28, extrait agrégé d'annonces Alibaba)

| Fournisseur | Produit | MOQ | Prix [F] | Personnalisation |
|---|---|---|---|---|
| Non nommé | Moule pattes et os « Customized Logo » | 50 lots (« packs ») | 1,42–3,60 $ | Logo |
| Non nommé | Moule pattes « Custom Logo Moulds » | 20 pièces | 0,40–0,60 $, plus un port de 1,12 $ par pièce | Logo, peut-être non standard (article prêt à expédier) |
| Xiamen Hands Chain | Moule pattes et os OEM/ODM | 200 pièces | 0,87–1,36 $ | OEM et ODM |
| Non nommé | Moule pattes « custom design » | 10 pièces | 0,35–0,42 $ | Design |
| Divers, dont un fournisseur de Dongguan | Moules standards | 10 à 100 pièces | 0,28–0,65 $ ; 0,60–0,90 $ (MOQ de 100) | Aucune |

- **Sources :** [Alibaba, wholesale](https://www.alibaba.com/wholesale/silicon-molds-dog-treats.html) ; [showroom silicone dog paws bone mold](https://www.alibaba.com/showroom/silicone-dog-paws-bone-mold.html) ; [showroom silicone mold dog bone](https://www.alibaba.com/showroom/silicone-mold-dog-bone.html) ; [showroom dog bone shape silicone ice cube tray](https://www.alibaba.com/showroom/dog-bone-shape-silicone-ice-cube-tray.html) ; [annonce 6 empreintes pattes](https://www.alibaba.com/pla/6-Cavity-Cat-Dog-Paw-Print-Silicone_1601143473946.html?mark=google_shopping&biz=pla&searchText=cake+tools&product_id=1601143473946&pcy=nl_nl).
- **Mises en garde de la synthèse de W23 :**
  - « food grade » n'est qu'une allégation du fournisseur ;
  - le logo exige souvent un MOQ plus élevé et des frais de mise en route ou d'outillage, qui ne sont pas indiqués.
- **Repères de vente (repris) :**
  - moule Woof « Treat Tray » à environ 38 € sur Amazon.fr, selon la synthèse du moteur (`fr_deep_jouet_lechage_congelable.md`) ;
  - moule SmoothieDog de 5 portions (≈350 ml) inclus dans le kit à 29,90 € ;
  - ensemble catalogue Xiamen Newtop (balle en caoutchouc naturel et bac en silicone) à 1,77–1,88 $ (tableau 1.1, ligne 2).
- **Moules à glace en silicone BeG Buddy** vendus en Autriche ([Shop Apotheke](https://www.shop-apotheke.at/tiergesundheit/upmEYUUMT/beg-buddy-hundeeis-am-stiel-eisform-hund-eis-fuer-hunde-abkuehlung-hund-sommer-silikonform.htm)).

#### 4.2 Fabricants de friandises en marque blanche (W20, W21, 2026-10-28)
- **PAEX GmbH** (nord de l'Allemagne). Il fabrique des produits BARF pour chiens et chats et « all kinds of freeze-dried petfood ». Selon sa fiche : « specialized or personalized recipes are available even for small purchase quantities ». Source : [Interzoo, PAEX](https://www.interzoo.com/en/exhibitors/paex-gmbh-2541768) [F].
- **Loupas** (Loupas Négoce SARL, France, activités en France, en Italie et en Allemagne). Il propose des friandises lyophilisées pour chien et un emballage en marque de distributeur. Sources : [Interzoo, Loupas Négoce](https://www.interzoo.com/en/exhibitors/loupas-negoce-sarl-2496939) ; [Interzoo, Loupas Dog Treats](https://www.interzoo.com/en/exhibitors/loupas-dog-treats-hundesnacks-2496939) [F].
- **Animille** (Pologne). Il travaille en marque de distributeur en Pologne et en Europe, sur des friandises séchées à mâcher (pas du lyophilisé). Il propose le choix des produits, des poids et des emballages, la création d'étiquettes et l'expédition. Attribution probable : [Zoomark 2025](https://www.zoomark.it/en/2025-exhibitors-catalogue/exhibitor-detail/?id=9696) [F].
- **Rondo Food** (Krefeld, Allemagne). Il fabrique et distribue en marque de distributeur des friandises pour chiens et chats : extrudées, viande séchée ou formée, **moulées par injection**, spécialités. URL exacte non isolée dans l'extrait agrégé de W21 [F].
- **Annuaire Wonnda.** Il liste des fabricants d'aliments pour animaux en marque blanche, dont Heristo Group, MERA et PPF Europe. Les champs MOQ et délai sont vides ([Wonnda](https://wonnda.com/product-types/pet-food-manufacturers/)). Fides Petfood apparaît aussi, sans détail ([Interzoo](https://www.interzoo.com/en/exhibitors/fides-petfood-2227649)).
- **France (W20) :**
  - **Made in Pet** (Béziers) : biscuiterie artisanale de friandises « pâtissières » pour chiens et chats ; aucune marque blanche mentionnée ([Les Pépites Tech](https://lespepitestech.com/startup-de-la-french-tech/made-pet)) ;
  - **Fin Museau** : friandises bio et sans céréales, fabriquées artisanalement en France, marque propre ([Greenweez](https://www.greenweez.com/marque/fin-museau)) ;
  - annuaire chien.com : 1 010 fabricants et magasins d'aliments pour chiens en France ([chien.com](https://www.chien.com/adresse/4-0-0-73-0-fabricant-ou-magasin-d-alimentation-pour-chien-france-1.php)) ;
  - un guide des grossistes, mis à jour en mai 2026, définit la marque blanche sans citer de fournisseur ([Comdewouf](https://comdewouf.fr/?p=11702)).
- **MOQ, prix et délais** : aucun n'a été obtenu pour ces façonniers.

#### 4.3 Glaces, smoothies et préparations pour chien (W22, 2026-10-28, et reprises)
- **Cold & Dog GmbH** (Berlin). Elle se présente comme « Europe's First Dog Ice Cream », exportée dans 19 autres pays, avec du yaourt sans lactose et des viandes bio ; c'est du discours commercial. Une offre en marque blanche n'est pas confirmée. Source : [Interzoo, Cold & Dog](https://www.interzoo.com/en/exhibitors/colddog-gmbh-2496716/dogicecream-2326336).
- **BeG Buddy** :
  - moules à glace à bâtonnet en silicone ;
  - préparation en poudre « ICE ICE Buddy », sans gluten, végane, sans sucre ajouté ;
  - le fabricant est indiqué comme BeG Buddy GmbH ou Schecker GmbH selon la fiche.
  - Sources : [Shop Apotheke, moule](https://www.shop-apotheke.at/tiergesundheit/upmEYUUMT/beg-buddy-hundeeis-am-stiel-eisform-hund-eis-fuer-hunde-abkuehlung-hund-sommer-silikonform.htm) ; [Shop Apotheke, préparation](https://www.shop-apotheke.at/tiergesundheit/upmTH7L7W/beg-buddy-eis-fuer-hunde-hundeeis-zum-selbermachen-dog-ice-abkuehlung-hund-eis-kokos-erdbeere.htm) ; [Shop Apotheke, ICE ICE Buddy](https://www.shop-apotheke.at/tiergesundheit/upmFZ77YP/ice-ice-buddy-hundeeis-aus-glutenfreien-zutaten-vegan-ohne-zuckerzusatz.htm).
- **Glaciers allemands** :
  - glace pour chien à Trier ([Wochenblatt](https://www.wochenblatt-reporter.de/c-ausgehen-geniessen/hundeeis-im-eiscaf-in-trier-vierbeiner-bekommen-eigene-kugel_a786274)) ;
  - à Birkenfeld depuis 2014, avec un « Dog Gelato » livré à d'autres glaciers ([Nordkurier](https://www.nordkurier.de/panorama/wenn-eisdielen-auf-den-hund-kommen-4610491) ; [Volksstimme](https://www.volksstimme.de/panorama/wenn-eisdielen-auf-den-hund-kommen-4258542)).
- **Ben & Jerry's** a lancé ses « Doggie Desserts » en 2021 ([RetailDetail](https://www.retaildetail.eu/?p=12822), HISTORIQUE).
- **Action « Hundeeis »** ([Action CH](https://www.action.com/de-ch/p/3224481/hundeeis/)) : même référence que les « Glaces pour chien » vendues 1,99 € les 5 en France (repris de `fr_deep_jouet_lechage_congelable.md`).
- **Recharges déjà vendues (repris) :**
  - smoothies SmoothieDog de 250 ml à 7,40 € chez Truffaut ([Truffaut](https://www.truffaut.com/smoothie-dog-smoothie-pour-chiens-250ml-boeuf.html)) ;
  - recharges PetSafe Busy Buddy de 8,90 à 14,90 € chez Zoomalia ([Zoomalia](https://www.zoomalia.com/animalerie/recharge-friandises-pour-jouet-bristle-et-bouncy-bone-p-23795.html)) ;
  - recharges Woof Pops à 14,99 $ le sachet et 31,99 $ les 10 en XL aux USA ([Tractor Supply](https://www.tractorsupply.com/tsc/product/woof-chicken-refill-pops-small-2457771) ; [Chewy](https://www.chewy.com/woof-pupsicle-pops-refills-beef/dp/3283638)).

#### 4.4 Ce qu'impose la vente de recharges alimentaires (W19, W26, W29, 2026-10-28)
- **Règlement (CE) 183/2005, art. 2 (texte de 2005 en vigueur).**
  - Le paragraphe 2, point e, exclut du champ « the retailing of pet food ».
  - Le paragraphe 3 prévoit : « Member States may establish rules and guidance governing the activities referred to in paragraph 2. Such national rules and guidance shall ensure the achievement of the objectives of this Regulation. »
  - Sources : [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2005/183) ; [legislation.gov.uk, art. 2](https://legislation.gov.uk/eur/2005/183/article/2/data.pdf) ; [copie FSSAI](https://cdd.fssai.gov.in/viewFile.php?id=209) ; [note explicative galloise](https://www.legislation.gov.uk/cy/wsi/2005/3368/note/made/data.htm).
  - La version britannique a supprimé l'art. 2, § 3, au 31/12/2020, ce qui est sans effet pour la France.
- **Règlement (CE) 767/2009 (texte de 2009 en vigueur).**
  - Il s'applique aux aliments pour animaux producteurs de denrées et non producteurs de denrées, étiquetage, emballage et présentation compris. Les animaux de compagnie sont des « non-food producing animals ».
  - Considérant : les responsabilités des exploitants prévues par les règlements 178/2002 et 183/2005 « should apply, mutatis mutandis » aux aliments pour animaux non producteurs de denrées. Une disposition renvoie à l'art. 4, § 1, du règlement 183/2005.
  - Étiquetage : quand le producteur n'est pas le responsable de l'étiquetage, il faut indiquer le nom et l'adresse du producteur ou son numéro d'agrément (extrait agrégé, article exact non isolé).
  - Sources : [legislation.gov.uk, chapitre 1](https://www.legislation.gov.uk/eur/2009/767/chapter/1/data.pdf) ; [introduction](https://legislation.gov.uk/eur/2009/767/introduction/data.pdf) ; [art. 21](https://www.legislation.gov.uk/eur/2009/767/article/21/data.htm?view=plain) ; [APPA, ressources UE](https://americanpetproducts.org/law-library/eu-pet-food-regulations-resources).
- **Formulaire français « NOTIFICATION A LA DD(ETS)PP DE L'ACTIVITÉ EN ALIMENTATION ANIMALE D'UN ETABLISSEMENT ».**
  - Il est fondé sur le règlement 183/2005 et prévoit une déclaration initiale, une modification ou une cessation. L'envoi dématérialisé via l'annuaire des DDPP est recommandé.
  - Il distingue la production, le stockage et le commerce de gros ou de détail, et cite les animaux familiers parmi les espèces.
  - L'extrait est coupé à la mention de la vente au détail, qui **semble exclure les animaux familiers**. À lire en entier.
  - Source : [agriculture.gouv.fr](https://agriculture.gouv.fr/telecharger/143976).
- **Arrêtés français (HISTORIQUE, vigueur non vérifiée).** L'arrêté du 28/02/2000 sur l'agrément et l'enregistrement de certains établissements et intermédiaires du secteur de l'alimentation animale exclut l'enregistrement des fabricants d'aliments destinés exclusivement aux animaux de compagnie, qui relève d'un arrêté du 02/05/1994. Sources : [Ecolex](https://www.ecolex.org/details/legislation/arrete-du-28-fevrier-2000-relatif-a-lagrement-et-a-lenregistrement-de-certains-etablissements-et-intermediaires-dans-le-secteur-de-lalimentation-animale-lex-faoc019393/) ; [UNEP LEAP](https://leap.unep.org/en/countries/fr/national-legislation/arrete-du-28-fevrier-2000-relatif-lagrement-et-lenregistrement-de).
- **Contrôles.** Ils sont assurés par les DDPP ou DDETSPP ; les autorités compétentes sont la DGAL et la DGCCRF. Sources : réponses à des questions écrites de la 15e législature (2017–2022, HISTORIQUE, attribution probable) : [AN, QE 24497](https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE24497.pdf) ; [AN, QE 26060](https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE26060.pdf).
- **Signal d'un guide e-commerce.** Minea conseille de se méfier des produits réglementés comme les aliments (repris de `fr_deep_jouet_lechage_congelable.md` : [Minea](https://www.minea.com/fr/produit-gagnant-dropshipping/meilleurs-niche-produits-dropshipping/comment-dropshipper-produits-pour-animaux)).

### Inferences

#### Échelle de charge réglementaire, par palier

| Palier | Offre | Statut de la marque | Obligations principales | Charge | Exemples de fournisseurs |
|---|---|---|---|---|---|
| 0 | Moules en silicone, livret et vidéos de recettes, accessoires non alimentaires | Vendeur de produits de consommation | GPSR ; contact alimentaire recommandé pour les moules (section 3) ; pas de droit de l'alimentation animale | **Faible** | Alibaba (Xiamen Hands Chain, 0,87–1,36 $, MOQ de 200) ; moule assorti au jouet par un moule de compression (section 2) |
| 1 | Revente d'aliments d'une autre marque, déjà étiquetés : smoothies, poudres, lyophilisés | Détaillant d'aliments pour animaux familiers | Exclu du règlement 183/2005 (art. 2, § 2, e), sauf règles nationales (art. 2, § 3) ; l'étiquetage reste à la charge de la marque du produit [CJ] ; stockage correct | **Faible à moyenne**, à confirmer avec la DDPP | SmoothieDog, BeG Buddy « ICE ICE Buddy » (sous réserve de leur accord) |
| 2 | Recharges en marque propre, fabriquées par un façonnier de l'UE enregistré ou agréé | Responsable de l'étiquetage au sens du règlement 767/2009 [CJ] | Étiquette complète ; allégations justifiées, sans allégation médicale [CJ] ; nom et adresse ou numéro d'agrément du fabricant ; traçabilité ; notification éventuelle à la DDPP ; agrément du fabricant pour les sous-produits animaux [CJ] | **Moyenne** | PAEX, Loupas, Animille, Rondo Food |
| 3 | Fabrication en propre ou import d'aliments hors UE | Fabricant ou importateur | Enregistrement ou agrément, HACCP, contrôles vétérinaires aux frontières pour les produits d'origine animale [CJ] | **Forte** | À éviter |

#### Séquence recommandée (inférence)
1. **Au lancement : palier 0.**
   - Proposer le jouet, un ou deux moules en silicone aux formes de la cavité, et des recettes validées par un vétérinaire (sans xylitol ni ingrédient toxique).
   - Produire du contenu vidéo, ce que les acheteurs de Woof recherchent déjà sur TikTok (requêtes « recipe », voir `us_verif_woof_pupsicle.md`).
   - **La marge est forte sur les moules** : 0,3 à 3,6 $ d'achat [F], contre environ 38 € pour le moule Woof sur Amazon.fr (synthèse).
2. **Après des premiers signaux de réachat : palier 1 à l'essai.** Revendre une recharge stable à température ambiante d'une marque partenaire, après confirmation écrite de la DDPP sur l'exclusion du commerce de détail.
3. **Puis palier 2.** Lancer des recharges propres avec un façonnier de l'UE, au format **stable à température ambiante** :
   - lyophilisé (PAEX, Loupas) ;
   - poudre à mélanger et congeler (modèle BeG Buddy) ;
   - friandise moulée par injection à la forme exacte de la cavité (Rondo Food), à la manière des Pops de Woof.
   - Le surgelé est exclu en e-commerce : chaîne du froid coûteuse, ce qui contredit le critère « envoi simple ».
4. **Allégations.** Éviter les allégations « anti-stress » ou « apaisant » sur une recharge (Woof vend des Pops « Calming » aux USA) tant qu'elles ne sont pas validées au regard du règlement 767/2009 [CJ]. Rester sur « occupation » et « plaisir de lécher ».
5. **Abonnement.**
   - Abonnement transparent, résiliable en ligne (« résiliation en 3 clics » [CJ], déjà signalée dans `us_verif_woof_pupsicle.md`).
   - Garantie à vie du jouet liée à l'abonnement, comme le fait le revendeur britannique wooof.co.uk ([wooof.co.uk](https://wooof.co.uk/products/woof-pupsicle-toy-refill-pops), repris).

### Gaps
- **Façonniers de l'UE** : MOQ, prix, délais, durée de conservation et numéros d'agrément de PAEX, Loupas, Animille et Rondo Food non obtenus. URL exacte de Rondo Food et attribution d'Animille non certaines.
- **Marque blanche en glace ou préparation pour chien** (Cold & Dog, BeG Buddy) : non confirmée.
- **DDPP** : aucune confirmation officielle sur le statut d'une marque e-commerce qui fait fabriquer sous son nom puis vend au détail, ni sur le stockage dans un entrepôt logistique. Le formulaire n'a pas été lu en entier.
- **Sous-produits animaux** (règlement (CE) 1069/2009) : obligations d'un distributeur ou d'un donneur d'ordre de friandises à base de viande non recherchées.
- **Liste des mentions d'étiquetage obligatoires** d'un aliment complémentaire (règlement 767/2009, art. 17 à 22, et code FEDIAF) et règles d'allégation (art. 13) : non lues dans cette session.
- **Aucune donnée de réachat** (fréquence, panier) pour des recharges en France.

#### Journal des 30 appels WebSearch
*Mode « standard » sauf mention contraire. W1 à W12 : 2026-10-27 ; W13 à W30 : 2026-10-28.*

| # | Requête (verbatim) | Domaines filtrés | Résultat principal |
|---|---|---|---|
| W1 | `frozen treat dog lick ball refillable natural rubber` | alibaba.com | Annonces « Freeze Ball », balle en silicone « Medium Large Dogs », balle roulante en caoutchouc naturel de 5, 6 et 7 cm ; guide fournisseur sur le caoutchouc naturel ; aucun prix |
| W2 | `dog lick ball frozen treat toy` | made-in-china.com | Hangzhou Tianyuan, Ningbo General Union, ensemble caoutchouc naturel et bac silicone ; aucun prix |
| W3 | `frozen treat dog toy lick ball supplier` | globalsources.com | Shenzhen LYA, Market Union, Fujian SingYee, Jinjiang Naike : prix et MOQ |
| W4 | `宠物 舔食球 冷冻 狗 天然橡胶 1688` | aucun | Aucune page 1688 : fiches SHEIN Taïwan et Beco |
| W5 | `pupsicle style dog lick ball with silicone tray mold custom logo MOQ` | alibaba.com | Tapis à lécher en silicone : logo dès 200, 300 ou 500 pièces, emballage dès 1 000, +0,20 $, 3,50–3,70 $, échantillon en 7 jours, délais de 5 à 30 jours |
| W6 | `dog toy freezable treat holder natural rubber OEM factory price per piece minimum order sample` | alibaba.com, made-in-china.com, globalsources.com | Xiamen Newtop (1,77–1,88 $), Ningbo General Union (MOQ de 50), Anhui Joypaws, 0,60–0,80 $ ; échantillon à 2 $ ; 45 jours |
| W7 | `natural rubber dog toys manufacturer Europe made in Italy private label` | aucun | Aucun fabricant européen en caoutchouc naturel ; Petopia, Croci (fabriqué en Chine), Smart Dog, Antlerworld, Funny Zoo |
| W8 | `Sri Lanka natural rubber dog toy manufacturer OEM private label` | aucun | DSL Lanka (Tikiri), Green Rubber Toys ; pas de jouets pour chien en sous-traitance |
| W9 | `custom rubber dog toy compression mold cost tooling fee lead time natural rubber silicone mould price` (**extended**) | aucun | **Refusé (limite d'usage)** |
| W10 | `natural rubber vs TPR vs silicone vs nylon dog chew toy durability tooth fracture` | aucun | **Refusé (limite d'usage)** |
| W11 | `dog ball single hole suction tongue stuck vet warning two holes` | aucun | **Refusé (limite d'usage)** |
| W12 | `pet food bowls food contact materials regulation 1935/2004 animal feed not covered EU` | aucun | **Refusé (limite d'usage)** |
| W13 | = W9 (**extended**) | aucun | Wedogy (80–150 $), moulistes (500–3 500 $ ; 500–3 000 $ ; 3 000–12 000 $ ; LSR 5 000–50 000 $), délais de 7 jours à 8 semaines |
| W14 | = W10 | aucun | Blogs : nylon et fractures dentaires, caoutchouc naturel et TPR ; rien sur le silicone |
| W15 | = W11 | aucun | Kinship (second trou), cas de 2008, 2015 et 2024, UC Davis, Vets Now |
| W16 | = W12 | aucun | Champ du règlement 1935/2004 (FSAI, EUR-Lex) ; rien sur la nourriture pour animaux |
| W17 | `pet bowls EU food contact materials regulation apply pet food is feed not food 178/2002` | aucun | Rien sur la nourriture pour animaux ; AGRINFO, guides contact alimentaire |
| W18 | `REACH Annex XVII entry 51 phthalates all articles 2018/2005 entry 50 PAH rubber 1 mg/kg pet toys` | aucun | ECHA, entrée 50 (1 et 0,5 mg/kg) ; SGS, entrée 51 (DIBP, articles en général) |
| W19 | `enregistrement établissement alimentation animale DDPP distributeur aliments pour animaux de compagnie marque` | aucun | Formulaire de notification DD(ETS)PP ; arrêtés de 2000 et 1994 ; questions écrites à l'Assemblée nationale |
| W20 | `fabricant friandises chien marque blanche France petite série` | aucun | Made in Pet, Fin Museau, annuaire chien.com ; aucune marque blanche confirmée |
| W21 | `private label dog treats manufacturer Europe low MOQ freeze-dried white label` | aucun | PAEX, Loupas, Animille, Rondo Food, Wonnda ; aucun MOQ |
| W22 | `Hundeeis Hersteller Eigenmarke private label dog ice cream Europe` | aucun | Cold & Dog, BeG Buddy, Ben & Jerry's, glaciers ; aucune marque blanche confirmée |
| W23 | `silicone dog treat mold tray custom logo food grade MOQ price` | alibaba.com | Moules de 0,28 à 3,60 $, MOQ de 10 à 200, Xiamen Hands Chain |
| W24 | `Packhelp mailer box price per unit 2026 small quantity custom printed` | aucun | Packhelp : dès 30 pièces ; 1 500 boîtes non imprimées à 1,53 £ ; prix de 2017 (HISTORIQUE) |
| W25 | `Woof Pupsicle Large item weight ounces product dimensions` | aucun | 10,2 oz (289 g) ; 4,6 × 3 × 4,6 po |
| W26 | `Regulation 183/2005 scope excludes retailing of pet food registration 767/2009 labelling responsible person pet treats` | aucun | Champ et considérants du règlement 767/2009 ; exclusion du 183/2005 non confirmée dans cette requête |
| W27 | `custom printed color box packaging pet toy price per piece 1000 pcs window box` | alibaba.com, made-in-china.com | Shanghai Hongyun (0,35–0,80 $, MOQ de 1 000) ; autres boîtes de 0,10 à 0,70 $ |
| W28 | `custom dog toys MOQ sample time mass production lead time mold` | wedogy.com, newtopsilicone.com | Wedogy : MOQ de 50 ou 100, échantillons de 30 à 60 $ en 3 à 5 jours, production en 12 à 18 jours ; Newtop : moule de 4 à 6 semaines |
| W29 | `"retailing of pet food" Regulation 183/2005 article 2 feed hygiene shall not apply` | aucun | Exclusion confirmée (art. 2, § 2, e) ; art. 2, § 3 (règles nationales) |
| W30 | `XL lick ball large dogs frozen treat dispenser 12 cm natural rubber wholesale OEM` | alibaba.com, made-in-china.com, globalsources.com | Pas de 12 cm ; Jiangyin Qianding de 6 à 8 cm, balle silicone « Freeze Treats » à 1,85–3,70 $, iPetoy, Xiamen Newtop, Suzhou Becpet |

#### Requêtes non lancées (budget épuisé)
- 1688 par un autre moyen (`1688 舔食球 源头工厂`, agent d'achat) : prix d'usine chinois.
- `TPR brittle freezer temperature` ; `silicone tear strength dog chew` : tenue au froid et au mâchage.
- `pet toy safety standard Europe` : norme volontaire éventuelle.
- `TARIC 4016 99 97 duty rate` : droit UE d'un jouet pour chien en caoutchouc.
- `SGS REACH PAH phthalate test price` ; `QIMA inspection price 2026` : coût des essais et des inspections.
- `Espacenet "Woof Pet"` ; `DesignView lick ball` ; lecture des revendications de US 12 582 096 : liberté d'exploitation.
- `règlement 1069/2009 friandises distributeur enregistrement` : sous-produits animaux.
- `étiquetage aliment complémentaire chien mentions obligatoires` : contenu exact de l'étiquette d'une recharge.
- `PPWR emballage e-commerce 2026` : règlement emballages.
- `emballage carton personnalisé fabricant France petite série prix` : fournisseurs d'emballage français.
- `Vietnam OR Thailand natural rubber pet toy manufacturer OEM` : autres pays producteurs.
- `Loupas friandises lyophilisées MOQ` ; `PAEX freeze-dried private label MOQ` : conditions des façonniers.
