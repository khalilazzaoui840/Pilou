# Coûts et obligations réglementaires d'une petite marque française d'accessoires chien/chat (Shopify, sourcing Chine ou UE), état au 27/10/2026

**Note de méthode (à lire avant d'utiliser ces notes).**
1. **Accès aux sources.** La politique réseau de la session bloquait WebFetch (échec DNS sur taxation-customs.ec.europa.eu, consilium.europa.eu et economie.gouv.fr). Elle bloquait aussi curl vers tous les sites testés : eur-lex, TARIC, shopify.com/fr, laposte.fr, legifrance, bofip, douane.gouv.fr, citeo.com, paypal.com, data.consilium et access2markets. Toutes les constatations ci-dessous viennent donc des **résumés de résultats WebSearch**, qui lisent les pages côté serveur. Ce sont des preuves indirectes. Il faut relire la page source avant toute publication. Pour faire des lectures directes à l'avenir, il faudrait autoriser ces domaines dans les paramètres réseau de la session.
2. **Budget de recherche.** Le budget de recherche web de la session (200 requêtes partagées entre tous les agents) s'est **épuisé** avant que je couvre les coûts commerciaux : Shopify, PayPal, Alma/Klarna, tarifs Colissimo/Mondial Relay, 3PL, fret Chine, agents de sourcing, benchmarks Meta/TikTok, taux de retour et de chargeback, panier moyen. Ces lignes figurent **uniquement comme hypothèses de travail non sourcées** et sont listées dans les sections Gaps. Une passe de recherche complémentaire est nécessaire.
3. **Légende des marqueurs.**
   - **[S]** : source officielle (UE, Conseil, Commission, BOFiP, DGCCRF, douane, éco-organisme).
   - **[S2]** : source secondaire (cabinet, blog spécialisé, base tarifaire tierce reprenant TARIC).
   - **[H]** : hypothèse du chercheur, **non sourcée**.
   - **[CP]** : connaissance préalable du chercheur, en général une règle juridique stable, **non revérifiée en ligne dans cette session**.
   - Une donnée antérieure à 2024 est signalée « historique ».

## Q1 : TVA. Taux applicable aux accessoires et aliments, calcul depuis un prix TTC

### Takeaway
Les accessoires pour animaux relèvent du taux normal de TVA de 20 %, et les aliments pour chiens et chats aussi. Le taux de 5,5 % est réservé à l'alimentation des animaux producteurs de denrées. À partir d'un prix TTC, on calcule HT = TTC / 1,20 et TVA = TTC / 6, soit 16,67 % du TTC.

### Cited Findings
- **Aliments pour animaux de compagnie.** Le BOFiP (BOI-TVA-LIQ-30-10-20) indique que les aliments destinés aux animaux **non producteurs de denrées alimentaires** relèvent du **taux normal de 20 %**. Le taux de 5,5 % vise les denrées destinées aux animaux producteurs de denrées pour la consommation humaine : bétail, volailles, poissons d'élevage. [S] Version indexée du 02/08/2023. Le résumé ne permet pas de confirmer qu'il s'agit de la version la plus récente. [BOFiP BOI-TVA-LIQ-30-10-20](https://bofip.impots.gouv.fr/bofip/273-PGP.html/identifiant=BOI-TVA-LIQ-30-10-20-20230802)
- « TVA à 20 % pour les denrées destinées à l'alimentation des animaux de compagnie ». [S2, date non visible] [LégiFiscal](https://www.legifiscal.fr/actualites-fiscales/525-tva-taux-applicable-pour-lalimentation-animale-et-les-appats-pour-la-peche.html)
- Le taux de 20 % concerne les animaux de compagnie (chiens, chats, lapins nains, etc.). [S2] [Bonnet & Associés](https://www.bonnet-associes.com/actualites/intrants-agricole-et-alimentation-animale-quel-taux-de-tva)
- Une proposition de loi sénatoriale visait à uniformiser à 5,5 % le taux de TVA de tous les aliments pour animaux. Son existence confirme que le régime actuel est différent. Son statut n'a pas été vérifié. [S, historique : session 2018-2019] [Sénat PPL n° 94](https://www.senat.fr/leg/ppl18-094.html)

### Inferences
- **Accessoires.** Je n'ai trouvé aucun taux réduit visant les accessoires : laisses, harnais, brosses, couchages, jouets, gamelles, appareils. Ils relèvent donc du taux normal de 20 %. Le caractère limitatif des taux réduits relève de [CP].
- **Calcul depuis le TTC.** TVA = TTC × 20/120 = TTC/6 (calcul).
  - 35,00 € TTC donne 29,17 € HT et 5,83 € de TVA.
  - 39,90 € TTC donne 33,25 € HT et 6,65 € de TVA.
  - 45,00 € TTC donne 37,50 € HT et 7,50 € de TVA.
- **Frais de port.** Les frais de port facturés au client suivent le taux du bien livré, soit 20 % [CP].
- **Frais de paiement.** Les commissions de paiement (Shopify Payments, PayPal) sont des services financiers exonérés. Elles ne portent pas de TVA récupérable [CP].
- **Compléments alimentaires pour chiens et chats.** Par la même logique, ils relèvent vraisemblablement aussi de 20 %. C'est à confirmer par le chercheur chargé des compléments.

### Gaps
- **Régime fiscal du client inconnu.** S'il est en micro-entreprise en **franchise en base de TVA**, il ne collecte pas de TVA mais ne déduit rien. Il doit probablement **autoliquider sans pouvoir déduire** la TVA sur les services achetés à un prestataire UE (Meta Platforms Ireland), ce qui renchérit la publicité d'environ 20 % [CP]. Les seuils de franchise 2026 n'ont pas été vérifiés. À valider avec un expert-comptable.
- La version 2026 du BOFiP n'a pas été consultée directement.

## Q2 : Douane. Droits TARIC, fin de la franchise de 150 €, droit forfaitaire de 3 €, frais de traitement de 2 €, taxe française « petits colis », IOSS ; dropshipping ou stock

### Takeaway
- **Depuis le 1er juillet 2026**, la franchise de droits de douane de 150 € est supprimée. Tout envoi B2C d'au plus 150 € venant d'un pays tiers paie un **droit forfaitaire temporaire de 3 € par « article »**. L'« article » correspond à chaque sous-position tarifaire distincte, c'est-à-dire chaque ligne de déclaration. Ce n'est ni chaque unité ni chaque colis. Ce régime court jusqu'au 1er juillet 2028 (règlement (UE) 2026/382).
- **Frais de traitement de 2 €.** S'y ajoute un « Union handling fee » de **2 € par article** sur les ventes à distance importées. L'acte délégué C(2026) 6694 a été adopté le 21/09/2026. L'application est **attendue au 1er novembre 2026**, sous réserve de non-objection du Parlement européen et du Conseil, à confirmer.
- **Taxe française.** La taxe française de 2 € par article (art. 82 de la LFI 2026) a été en vigueur du 1er mars au 30 juin 2026. Elle est **suspendue depuis le 1er juillet 2026**.
- **Import de stock.** En import B2B au-delà de 150 €, les droits ad valorem normaux s'appliquent :
  - 2,7 % pour 4201 ;
  - environ 3,7 % pour 9603 90 99 ;
  - 6,3 % pour 6307 90 98 ;
  - 6,5 % pour 3926 90 97 ;
  - 2,7 % pour 8516 31 00.

### Cited Findings
**Droit forfaitaire de 3 € (en vigueur)**
- **Accord politique.** Le Conseil a convenu le 12/12/2025 d'appliquer un droit fixe de 3 € aux petits colis de moins de 150 € à partir du 1er juillet 2026, à titre temporaire. [S] [Consilium, communiqué du 12/12/2025](https://www.consilium.europa.eu/en/press/press-releases/2025/12/12/customs-council-agrees-to-levy-customs-duty-on-small-parcels-as-of-1-july-2026/)
- **Adoption formelle.** Le feu vert final du Conseil date du 11/02/2026. Il s'agit du **règlement (UE) 2026/382 du Conseil du 11 février 2026**. [S] [Consilium, 11/02/2026](https://www.consilium.europa.eu/en/press/press-releases/2026/02/11/council-gives-final-green-light-to-new-customs-duty-rules-for-small-parcels/pdf), [EUR-Lex OJ L 2026/382](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202600382), [vatcalc](https://www.vatcalc.com/eu/eu-e3-levy-low-value-e-commerce-import-package-july-2026/)
- **Durée.** Le droit s'applique du 1er juillet 2026 au 1er juillet 2028. Ensuite, les droits normaux s'appliquent selon le type de bien. [S] [Commission, actualité du 08/06/2026](https://taxation-customs.ec.europa.eu/news/guidance-and-legal-text-temporary-flat-fee-low-value-imports-which-will-apply-until-1-july-2028-2026-06-08_en), [Avalara](https://www.avalara.com/us/en/blog/eu-end-150-customs-duty-exemption-2026.html)
- **Base juridique.** Le règlement supprime le chapitre V du titre II du règlement (CE) 1186/2009, qui portait la franchise pour les envois de valeur négligeable. [S] [Guide douanier de la Commission sur le droit de 3 €, version du 2 juin 2026](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)
- **Mode de calcul.** Le droit est dû **par article, pas par colis**. Il s'applique par sous-position tarifaire, et le regroupement est interdit. En calcul automatique, le montant dû est égal au nombre de lignes de déclaration multiplié par 3 €. [S] [Guide de la Commission](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)
- **Exemples officiels.**
  - Cinq t-shirts identiques donnent un seul droit de 3 €. Un t-shirt et une montre donnent 6 € (exemple de la Commission repris par [Avalara](https://www.avalara.com/us/en/blog/eu-end-150-customs-duty-exemption-2026.html)).
  - Un smartphone, un chargeur et des écouteurs donnent 9 €. [S2] [Landmark Global](https://landmarkglobal.com/eu/en/news-insights/eu-customs-reform-2026-3-euro-import-duty/), [nShift](https://nshift.com/blog/eu-customs-changes-ecommerce-2026)
  - Le calcul se fait par catégorie (code SH6) : dix t-shirts identiques font un seul droit. [S2] [lesfrancais.press](https://lesfrancais.press/taxe-sur-les-petits-colis-extra-europeens-en-2026-quel-impact-pour-les-francais-de-letranger-et-le-e-commerce/)
- **Seuil.** La « faible valeur » correspond à une valeur intrinsèque d'au plus 150 €, soit le prix des marchandises seul, hors transport et assurance. [S2] [Avalara](https://www.avalara.com/us/en/blog/eu-end-150-customs-duty-exemption-2026.html)
- **Champ et articulation avec l'IOSS.**
  - Selon le guide de la Commission, le droit vise tous les biens en envois d'au plus 150 € vendus à distance, **quel que soit le régime TVA**.
  - Si l'IOSS est utilisé, l'importation est exonérée de TVA à l'import. Le déclarant est la partie qui utilise le numéro IOSS, et c'est elle qui est débitrice des 3 €.
  - Hors IOSS, les 3 € entrent dans la base de la TVA à l'import.
  - [S] [Guide de la Commission](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf). Le traitement TVA est détaillé dans un addendum aux notes explicatives TVA e-commerce, révisé le 21/08/2026 et non lu en entier : [addendum TVA](https://vat-one-stop-shop.ec.europa.eu/document/download/3086db0e-7b4a-4202-9f38-d32bd774f5a8_en?filename=20260821_VAT+guidelines-3+EUR+Customs+duty_revised.pdf)
- **Qui paie.** Un cabinet indique que le droit est facturé à l'entreprise (vendeur, importateur ou représentant) et n'est pas collecté auprès du consommateur à la porte. [S2] [Baker Tilly SEE](https://bakertillysee.com/insights/major-eu-customs-update-e3-duty-on-low-value-e-commerce-imports-starting-july-2026/)
- Un retour d'expérience après deux mois d'application confirme le principe « par article, pas par colis ». [S2] [European Fulfillment Centers](https://europeanfulfillmentcenters.com/blog/eur-3-duty-two-months-in/)

**« Union handling fee » de 2 € (adopté, application attendue au 01/11/2026)**
- **Accord du 26/03/2026.** Le Conseil et le Parlement se sont accordés sur la réforme douanière. Elle crée des frais de traitement UE sur les petits colis, dont le niveau est fixé par acte délégué de la Commission et qui s'appliquent **au plus tard le 1er novembre 2026**. [S] [Consilium, 26/03/2026](https://www.consilium.europa.eu/en/press/press-releases/2026/03/26/eu-customs-council-and-parliament-agree-on-landmark-reform/)
- **Approbation finale le 03/09/2026.** Le Conseil confirme les frais d'ici au 1er novembre 2026 et précise que la Commission en fixe le niveau. [S] [Consilium, 03/09/2026](https://www.consilium.europa.eu/en/press/press-releases/2026/09/03/eu-customs-council-greenlights-landmark-reform/)
- **Base légale.** Le nouveau code des douanes de l'Union est le **règlement (UE) 2026/2108**, publié le 19/09/2026. Son article 20 crée les frais. [S2] [Global Law Experts](https://globallawexperts.com/eu-customs-reform/), [Dimweigh](https://dimweigh.com/blog/eu-2-euro-handling-fee-november-2026)
- **Montant.** Le 21/09/2026, la Commission a adopté l'**acte délégué C(2026) 6694** fixant **2 € par article**. Le Conseil l'a enregistré le 22/09/2026 sous le document ST 13480/26. Selon le projet : « A Union handling fee of EUR 2 per item is considered commensurate with the approximate costs closely connected to the customs supervision of such goods ». [S/S2] [Conseil, doc. ST 13480/26](https://data.consilium.europa.eu/doc/document/ST-13480-2026-INIT/en/pdf), [VitalLaw](https://www.vitallaw.com/news/eu-confirms-new-e-commerce-handling-fee-will-be-eur2-per-item/gdn01174716), [AX Holding](https://www.axholdinggroup.com/en/blog/eu-customs-handling-fee)
- **Date d'application.** Elle est attendue au **1er novembre 2026**, une fois l'acte publié et si ni le Parlement ni le Conseil ne s'y opposent. Les sources divergent sur l'état d'avancement : certaines décrivent l'acte comme encore en examen. [S2] [AX Holding](https://www.axholdinggroup.com/en/blog/eu-customs-handling-fee), [page réforme de la Commission](https://taxation-customs.ec.europa.eu/customs/eu-customs-reform_en)
- **Champ.** Les frais visent toutes les ventes à distance importées dans l'UE, **y compris au-delà de 150 €**, et ne sont pas remboursables. L'exposé des motifs indique que ces ventes « are also subject to the handling fee ». Les coûts sont revus tous les deux ans. [S2] [Dimweigh](https://dimweigh.com/blog/eu-2-euro-handling-fee-november-2026), [AX Holding](https://www.axholdinggroup.com/en/blog/eu-customs-handling-fee)
- **Source contradictoire.** VAT Update évoquait le 06/09/2026, avant l'adoption, « 2 € par colis » avec des réductions possibles par envoi. Cette version est probablement dépassée par l'acte du 21/09, mais reste à vérifier. [S2] [VAT Update](https://www.vatupdate.com/2026/09/06/eu-to-confirm-e2-customs-fee-on-low-value-parcels-by-2026/)

**Taxe française « petits colis » (suspendue)**
- **Création.** La taxe a été créée par l'**article 82 de la loi de finances pour 2026** et est **entrée en vigueur le 1er mars 2026**. Son montant était de **2 € par article** pour les envois d'au plus 150 € venant de pays hors UE. [S/S2] [economie.gouv.fr](https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/tout-savoir-sur-la-taxe-sur-les-petits-colis), [info.gouv.fr](https://www.info.gouv.fr/actualite/taxe-sur-les-petits-colis-comment-ca-marche), [CCI Lyon Métropole](https://www.lyon-metropole.cci.fr/actualite/taxe-2-euros-sur-les-petits-colis-entree-en-vigueur-mars-2026), [LégiFiscal](https://www.legifiscal.fr/actualites-fiscales/4550-taxe-petits-colis-france-suspend-prelevement-2-profit-nouveau-droit-douane-europeen.html)
- **Suspension.** Elle est **suspendue depuis le 1er juillet 2026** pour éviter le cumul avec le droit européen de 3 € (communiqué de presse du 30/06/2026, n° 850). [S2] [L-Expert-comptable](https://www.l-expert-comptable.com/a/suspension-taxe-petits-colis), [Éditions JFA](https://www.editions-jfa.com/le-gouvernement-suspend-la-taxe-sur-les-petits-colis-a-compter-du-1er-juillet-2026/), [Kohen Avocats](https://kohenavocats.fr/2026/07/01/taxe-petits-colis-suspendue-1er-juillet-2026-droit-douane-europeen/), [Univers Colis](https://www.universcolis.fr/actualites/taxe-2-euros-petits-colis-2026)
- **Importations antérieures.** La taxe reste due pour les importations du 1er mars au 30 juin 2026. [S2] [Mathez Compliance](https://www.mathez-compliance.com/reforme-taxe-petits-colis/)
- **Point ambigu.** Un cabinet cite le **décret n° 2026-589 du 3 juillet 2026** et indique que le droit est « dû par les plateformes de vente en ligne concernées ». On ne sait pas si cela vise le droit UE de 3 € ou la taxe française. À vérifier. [S2] [Bonnet & Associés](https://www.bonnet-associes.com/actualites/petits-colis-importes-la-france-suspend-sa-taxe-nationale)

**Droits ad valorem (import de stock en B2B ou envois au-delà de 150 €). Taux tiers « erga omnes » via des miroirs TARIC, à revérifier dans TARIC**
- **4201 00 00** (« Saddlery and harness for any animal », y compris laisses, muselières, manteaux pour chiens, toute matière) : **2,7 %**. Le taux est de 0 % sous SPG+ et SPG-TSA. [S2] [tariffnumber.com, page 2023 (historique, confirmée par la page 2024)](https://www.tariffnumber.com/2023/42010000), [tariffnumber.com 2024](https://www.tariffnumber.com/2024/4201), [Celna24](https://celna24.pl/en/customs-tariff/4201000090)
- **9603 90 99** (balais et brosses non dénommés ailleurs, position probable d'une brosse pour animaux) : **3,7 %** selon la fiche 2024. D'autres résumés indiquent une fourchette de 0 à 3,7 % ou de 0 à 4,7 %, d'où une divergence à lever. [S2] [tariffnumber.com 2024](https://www.tariffnumber.com/2024/96039099), [Celna24, position 9603](https://celna24.pl/en/customs-tariff/9603)
- **6307 90 98** (autres articles textiles confectionnés) : **6,3 %** (taux NPF). [S2] [Celna24](https://celna24.pl/en/customs-tariff/63079098)
  - Le règlement d'exécution (UE) n° 349/2014 a classé un **panier textile réversible pour animal** en 6307 90 98, en excluant les positions 9403 (meubles) et 9404 (literie). [S, historique 2014, précédent de classement] [Règl. 349/2014](https://www.legislation.gov.uk/eur/2014/349/data.html)
  - Aux États-Unis, certains lits à ressorts ou en mousse sont classés en 9404. Le classement dépend donc de la construction. [S2, droit américain, par analogie seulement]
- **3926 90 97** (autres ouvrages en plastique) : **6,5 %**. Données TARIC mises à jour le 24/10/2026. [S2] [tariffnumber.com 2026](https://www.tariffnumber.com/2026/39269097)
- **3924 90 00** (articles de ménage en plastique) : **sources contradictoires**. Une fiche TARIC affiche 0 % en « ERGA OMNES », alors que Celna24 donne 6,5 % pour la position 3924. La même fiche mentionne un **droit antidumping de 42,3 %** visant un producteur chinois précis, sur un périmètre produit inconnu. À vérifier dans TARIC. [S2] [tariffnumber.com 2026](https://www.tariffnumber.com/2026/39249000), [Celna24, position 3924](https://celna24.pl/en/customs-tariff/3924)
- **8516 31 00** (sèche-cheveux, à vérifier pour un séchoir pour animaux) : **2,7 %**. [S2] [tariffnumber.com 2026](https://www.tariffnumber.com/2026/85163100)
- **8509 80 00** (autres appareils électromécaniques domestiques) : le taux n'apparaît pas dans les résultats. [S2] [tariffnumber.com 2026](https://www.tariffnumber.com/2026/85098000)
- **Jouets pour animaux.**
  - Aux États-Unis, une balle en caoutchouc pour chien est classée en 4016.99.20 « toys for pets ». [S2, droit américain] [CBP NY N012649](https://www.customsmobile.com/rulings/docview?doc_id=NY+N012649)
  - Au Royaume-Uni, un renseignement tarifaire a classé une balle de tennis pour chien en 4016 99 97 90. [S, droit britannique] [HMRC ATaR 600013614](https://www.tax.service.gov.uk/search-for-advance-tariff-rulings/ruling/600013614)
  - Le taux UE n'a pas été trouvé.
- **Mesure de contrôle.** Les fiches 4201 et 9603 affichent un contrôle à l'import sur la **fourrure de chat et de chien** (règlement (CE) 1523/2007, interdiction). [S2] [tariffnumber.com, 9603 90 99](https://www.tariffnumber.com/2024/96039099)

### Inferences
- **Coût réglementaire en dropshipping.** Pour un envoi direct de Chine vers la France contenant un seul article :
  - 3 € de droit forfaitaire depuis le 01/07/2026 ;
  - 2 € de frais de traitement attendus à partir du 01/11/2026 ;
  - soit **5 € par article distinct**, TVA non comprise.
  - Cela représente 13 à 17 % d'un prix de 29 à 37 € HT. En comparaison, un droit ad valorem de 2,7 à 6,5 % sur un produit acheté 5 à 8 € coûte environ 0,15 à 0,50 €. **La réforme pénalise d'abord les colis bon marché à article unique.**
- **Lots d'articles identiques.** Plusieurs unités identiques (même sous-position) ne paient qu'un seul droit de 3 € (exemple officiel). Pour les frais de 2 €, on ne sait pas si l'« item » est l'unité ou la ligne tarifaire (voir Gaps). L'avantage des lots reste donc incertain pour les 2 €.
- **Import de stock dans un entrepôt français.**
  - Le droit ad valorem porte sur la valeur en douane, soit environ le coût du produit plus le fret jusqu'à la frontière UE. Exemples : 2,7 % × 6 € = 0,16 € ; 6,5 % × 6 € = 0,39 € par unité.
  - Les frais de traitement visent les ventes à distance. Ils ne devraient donc pas s'appliquer à un import B2B en vrac (inférence tirée de la description du champ, à confirmer).
  - La TVA à l'import est neutre en trésorerie grâce à l'**autoliquidation obligatoire depuis le 01/01/2022** pour les opérateurs identifiés à la TVA en France [CP].
- **IOSS en dropshipping.** Si la marque française vend directement depuis la Chine des envois d'au plus 150 €, elle a intérêt à utiliser l'**IOSS** :
  - la TVA française de 20 % est collectée au moment du paiement en ligne ;
  - le client ne paie ni TVA ni frais de dédouanement à la livraison, ce qui limite les refus de colis ;
  - une entreprise établie dans l'UE s'immatricule à l'IOSS sans intermédiaire [CP].
- **Sourcing UE.** Un sourcing dans l'UE, ou depuis un stock fournisseur déjà dédouané dans l'UE, n'entraîne ni droit forfaitaire, ni frais de traitement, ni formalité douanière par commande. L'importateur de ce stock a payé les droits normaux (inférence).

### Gaps
- **TARIC.** La consultation directe de TARIC était bloquée. Tous les taux viennent de miroirs tiers. Il faut confirmer chaque code dans TARIC avec l'origine Chine, et demander un **RTC (renseignement tarifaire contraignant)** pour sécuriser le classement, notamment entre 9404 et 6307 pour les couchages [CP : le RTC est gratuit].
- **Frais de 2 €.** Le statut au 27/10/2026 n'est pas confirmé : publication au Journal officiel et fin du délai d'objection. Il faut aussi savoir si l'« item » est l'unité ou la ligne tarifaire.
- **Champ du droit de 3 €.** Les premières communications du Conseil parlaient de vendeurs **inscrits à l'IOSS** [CP]. Le guide de la Commission dit « quel que soit le régime TVA ». À confirmer pour les envois hors IOSS.
- **Autres frais.** Les frais de dédouanement facturés par La Poste ou les transporteurs aux destinataires hors IOSS n'ont pas été recherchés. Le statut de la redevance de 0,50 € pour les colis destinés aux entrepôts, présente dans la proposition initiale de la Commission de 2025 [CP], est inconnu. Le calendrier de l'EU Customs Data Hub (2028) relève de [CP].

## Q3 : Conformité produit. GPSR, REACH, appareils électroniques (CE, RED, CEM, DBT), batteries

### Takeaway
- **Accessoires non électroniques.** Un accessoire pour animal vendu à des particuliers est un produit de consommation soumis au **GPSR (UE) 2023/988**. La marque française qui vend sous son nom doit fournir :
  - l'identité et les adresses postale et électronique du fabricant ou de la personne responsable dans l'UE ;
  - l'identification du produit et les avertissements en français, sur le produit **et** sur la fiche en ligne (art. 19).
- **REACH** encadre les textiles, plastiques, caoutchoucs et cuirs : colorants azoïques, NPE, phtalates, HAP, information sur les substances SVHC au-delà de 0,1 %.
- **Appareils électroniques.** Il faut ajouter :
  - le marquage CE et la déclaration UE de conformité ;
  - la directive RED, avec la cybersécurité obligatoire **depuis le 01/08/2025** pour les appareils connectés ;
  - la CEM, la DBT et RoHS [CP] ;
  - le règlement Batteries : piles portables amovibles et remplaçables **au 18/02/2027**, et étiquetage à partir du 18/08/2026 au plus tôt, probablement plus tard.

### Cited Findings
**GPSR**
- **Fiche produit en ligne (art. 19).** Toute offre à distance doit indiquer :
  - le nom, la raison sociale ou la marque du fabricant, avec ses adresses postale et électronique ;
  - si le fabricant est hors UE, le nom et les adresses de la **personne responsable** dans l'UE ;
  - l'identification du produit : image, type, autre identifiant tel que le lot ou le numéro de série ;
  - les avertissements et informations de sécurité dans la langue de l'État membre.
  - [S2] [eugpsr.de](https://eugpsr.de/en/blog/gpsr-online-sales-required-info), [Xictron](https://www.xictron.com/en/blog/gpsr-product-safety-regulation-online-shop-2026/), [EU Seller Kit](https://eusellerkit.com/en/gpsr-responsible-person/article-19), [Prym eCommerce](https://prymecommerce.com/gpsr-product-page-requirements/)
- **Emplacement.** Ces informations doivent figurer **sur la page produit elle-même**. Selon les chambres de commerce allemandes (IHK), un renvoi vers les CGV ou une sous-page ne suffit pas. [S2] [Xictron](https://www.xictron.com/en/blog/gpsr-product-safety-regulation-online-shop-2026/)
- **Produits pour animaux.** Ils relèvent du GPSR lorsqu'ils sont mis à disposition comme produits de consommation. TÜV SÜD cite les textiles, jouets, appareils électroniques, gamelles, sacs de transport, tapis et produits de toilettage et d'hygiène, à évaluer au titre du GPSR, de REACH et de RoHS. [S2, laboratoire, mai 2026] [TÜV SÜD, communiqué 05/2026](https://www.tuvsud.com/en/newsroom/press-releases/2026/may/tuev-sued-eu-requirements-enhance-safety-and-transparency-for-consumers), [TÜV SÜD Italie, 03/2026](https://www.tuvsud.com/it-it/news-e-comunicati-stampa/2026/march/regolamento-ue-2023-988-sicurezza-dei-prodotti-e-accessori-nella-pet-economy)
- **Articulation avec les textes sectoriels.** Le GPSR ne couvre que les risques non couverts par une législation sectorielle de l'Union. [S, autorité maltaise, guide non contraignant] [MCCAA](https://mccaa.org.mt/technical-regulation/general-product-safety/)
- **Date d'application.** Le GPSR s'applique depuis le 13/12/2024. [S2, page non lue en entier] [Wikipedia, GPSR](https://en.wikipedia.org/wiki/General_Product_Safety_Regulation)
- **Personne responsable.** Le concept de « Responsible Person » ou d'opérateur économique établi dans l'UE est présenté par [European Fulfillment Centers](https://europeanfulfillmentcenters.com/blog/gpsr-european-responsible-person-consumer-brands/) [S2]. Le détail de l'article 4 n'apparaissait pas dans les résultats.

**REACH**
- **Phtalates (entrées 51 et 52 de l'annexe XVII).** La limite est de 0,1 % en masse de la matière plastifiée. Le résumé citait les jouets et articles de puériculture. [S2] [ComplianceGate, annexe XVII](https://www.compliancegate.com/reach-annex-xvii-substances-list/). Voir Gaps sur l'extension aux articles en général.
- **Textiles.** Les colorants azoïques (entrée 43) et les éthoxylates de nonylphénol (NPE, entrée 46a) sont les restrictions notables. [S2] [ComplianceGate](https://www.compliancegate.com/reach-annex-xvii-substances-list/), [TÜV SÜD, mise à jour de l'annexe XVII (2021, historique)](https://www.tuvsud.com/hu-hu/e-ssentials-newsletter/consumer-products-and-retail-essentials/e-ssentials-1-2021/eu-reach-various-entries-of-annex-xvii-are-updated)
- **HAP (entrée 50).** Limite de 1 mg/kg dans les composants en caoutchouc ou plastique en contact avec la peau, et de 0,5 mg/kg pour les jouets. [S2, page de laboratoire] [HQTS](https://www.hqts.com/vi/dich-vu/thu-nghiem/reach/)
- **SVHC au-delà de 0,1 %.** Le fournisseur doit transmettre des informations aux clients professionnels, et aux consommateurs sur demande. Il doit aussi notifier la base SCIP. [S2] [ComplianceGate, SVHC](https://www.compliancegate.com/reach-svhc-substance-list/)

**Électronique**
- **RED, cybersécurité.** Le règlement délégué (UE) 2022/30 (art. 3.3 d, e et f de la RED) est **obligatoire depuis le 01/08/2025** pour les équipements radio connectés : maison connectée, objets portés, jouets connectés.
  - Les normes harmonisées sont **EN 18031-1, -2 et -3**. Leur citation au JO par la décision d'exécution (UE) 2025/138 du 28/01/2025 est rapportée par UL. Les dates des différentes sources ne concordent pas entièrement.
  - La documentation technique et la déclaration UE de conformité doivent être mises à jour.
  - [S2] [QIMA](https://www.qima.com/consumer-products/lab-testing/cybersecurity/red-cybersecurity-requirements), [UL](https://www.ul.com/insights/new-cybersecurity-requirements-radio-equipment-directive), [UL (FR)](https://www.ul.com/fr/services/ul-solutions-cybersecurity-advisory-red-compliance), [CEN-CENELEC](https://www.cencenelec.eu/news-events/news/2025/newsletter/ots-59-cybersecurity-standards/)

**Batteries, règlement (UE) 2023/1542**
- **Étiquetage (art. 13).** Il s'applique **au 18/08/2026 ou 18 mois après l'acte d'exécution prévu à l'art. 13(10), la date la plus tardive étant retenue**. Au 18/10/2026, cet acte n'était pas adopté : la date pourrait glisser à fin 2027. D'autres sites présentent le 18/08/2026 comme une date ferme : **les sources se contredisent**. [S2] [Pryor](https://www.pryormarking.com/18-august-2026-and-the-eu-battery-regulation-what-the-date-actually-means/), [Noknots](https://www.noknots.com/en/blog/battery-regulation-2023-1542-practice)
- **Amovibilité (art. 11).** Les piles portables intégrées aux appareils doivent être amovibles et remplaçables par l'utilisateur **à partir du 18/02/2027**. Les pièces détachées doivent rester disponibles au moins 5 ans. [S2] [Spilma](https://www.spilma.com/en/actualites/battery-regulation-removable-batteries-2027), [Westwood Sourcing](https://www.westwoodsourcing.com/blog/services-14/eu-battery-regulation-consumer-products-193)
- **QR code.** Il est obligatoire sur toutes les batteries à partir du 18/02/2027. [S2] [DPP Tool](https://dpp-tool.com/en/guide/eu-battery-regulation/)

### Inferences
- **Marque propre.** Une marque française qui commercialise sous son nom est en pratique le « fabricant » au sens du GPSR [CP : définition de l'art. 3] et l'opérateur établi dans l'UE. Elle n'a pas besoin d'une personne responsable externe. Elle porte en revanche toute la conformité : analyse de risques, documentation technique, traçabilité, avertissements en français.
- **Dropshipping depuis la Chine.** La marque reste responsable sans contrôler physiquement le produit ni l'étiquetage. Elle doit obtenir du fournisseur que son adresse UE, le numéro de lot et les avertissements en français soient imprimés. Elle doit aussi organiser elle-même le contrôle qualité et les rappels. C'est un risque plus élevé qu'en stock contrôlé à réception.
- **Accessoires non électroniques.** Il n'y a ni marquage CE ni test obligatoire *ex ante*. La bonne pratique consiste à exiger des rapports de test REACH du fournisseur : HAP et phtalates sur les poignées et pièces en caoutchouc ou plastique, azoïques et NPE sur les textiles. Ils permettent de documenter l'analyse de risques. Le coût n'est pas sourcé.
- **Appareils électroniques.** Fontaines à pompe, distributeurs automatiques, traceurs GPS, jouets laser, séchoirs et tondeuses cumulent les obligations :
  - dossier technique CE et tests éventuels ;
  - REP DEEE ;
  - règlement Batteries ;
  - cybersécurité RED s'ils sont connectés.
  - L'exigence d'amovibilité des piles au 18/02/2027 peut disqualifier de nombreux gadgets à batterie scellée. Une dérogation existe pour les appareils conçus pour un environnement humide (éclaboussures, immersion) [CP], ce qui peut concerner les fontaines.

### Gaps
- **GPSR, à vérifier [CP].**
  - Art. 4 : un opérateur économique établi dans l'UE est obligatoire.
  - Art. 9 : analyse de risques interne et documentation technique conservée 10 ans.
  - Art. 20 : déclaration des accidents via le **Safety Business Gateway**.
  - Rappels et procédures.
- **Règlement (UE) 2019/1020, art. 4 [CP].** Un opérateur UE identifié est requis pour les produits relevant de la RED, de la CEM, de la DBT et de RoHS. Les résultats ne l'ont pas couvert.
- **Autres textes électriques [CP], non recherchés.**
  - DBT : 50 à 1 000 V en alternatif, 75 à 1 500 V en continu, donc les chargeurs secteur.
  - CEM 2014/30/UE et RoHS 2011/65/UE.
  - Écoconception des alimentations externes : règlement (UE) 2019/1782.
- **Phtalates [CP].** Le règlement (UE) 2018/2005 a étendu la restriction de DEHP, DBP, BBP et DIBP au-delà de 0,1 % à la plupart des articles à partir du 07/07/2020. Le résumé obtenu ne parlait que des jouets. À vérifier.
- **PFAS [CP].** La loi française n° 2025-188 du 27/02/2025 interdit les PFAS dans les textiles d'habillement depuis le 01/01/2026, avec une extension à tous les textiles annoncée pour 2030. Le champ applicable aux textiles pour animaux n'est pas vérifié. La restriction UE sur le PFHxA (règlement (UE) 2024/2462) n'a pas été recherchée.
- **Coûts non trouvés.** Tests de laboratoire (REACH, CEM/RED/DBT) et services de personne responsable.
- **Bien-être animal.** Les restrictions éventuelles (colliers électriques, par exemple) n'ont pas été recherchées.

## Q4 : REP françaises (emballages, ameublement, DEEE, textiles), identifiant unique, Triman

### Takeaway
- **Emballages.** La marque qui met des produits emballés sur le marché français est « producteur » au titre de la REP emballages ménagers. Elle adhère à Citeo ou à Léko. Le forfait Citeo était de **80 € HT par an sous 10 000 UVC** en 2025.
- **Identifiant unique.** Elle doit obtenir et **afficher l'identifiant unique (IDU)** de l'ADEME dans ses CGV et sur son site. Elle appose aussi Triman et Info-tri [CP].
- **Ameublement.** Les **arbres à chat, matelas, coussins et hamacs pour animaux** sont explicitement dans le périmètre de la REP éléments d'ameublement (Ecomaison).
- **Électronique et piles.** Les appareils électriques relèvent de la REP DEEE, et les piles de la REP piles et accumulateurs [CP, non revérifié].

### Cited Findings
- **Forfait Citeo.** En dessous de 10 000 UVC par an, le producteur paie un **montant forfaitaire de 80 € HT**, qui inclut les services compris dans la contribution. [S] [Citeo, tarif emballages ménagers 2025, mis à jour le 19/12/2024](https://bo.citeo.com/sites/default/files/2025-04/20241219_MAJ_Tarif_EM_2025-FR.pdf)
- **Montant contradictoire.** Une source secondaire affirme que « le forfait de 110 € est inchangé » dans un barème révisé par Citeo le 08/10/2026. L'année d'application est floue et il y a **conflit avec les 80 €** ci-dessus. [S2] [EPR Representative, comparatif Citeo/Léko 2027](https://eprrepresentative.com/blog/bareme-emballages-menagers-2027-citeo-leko)
- **Barème au poids 2026 (sources divergentes).**
  - Carton ondulé à 0,177 €/kg (exemple : 1 000 kg par an pour 177 €) et PET clair à 0,399 €/kg. [S2] [AuditREP](https://auditrep.fr/blog/tarif-citeo-bareme-emballages-2026)
  - Une autre source donne 148,69 €/t pour le carton ondulé, avec des unités ou une année différentes. [S2] [AuditREP, stratégies](https://auditrep.fr/blog/reduire-ecocontributions-emballages-strategies-citeo-2026), [Circultrak](https://www.circultrak.fr/blog-eco-contributions-rep-2026.html)
- **Emballages professionnels.** L'offre Citeo Pro, distincte, prévoit un forfait de 125 € HT par an en dessous de 2 tonnes. Elle ne concerne pas les emballages ménagers. [S2] [EPR Representative, REP emballages professionnels](https://eprrepresentative.com/blog/bareme-rep-emballages-professionnels-2026)
- **Ecomaison.** C'est l'éco-organisme agréé pour les éléments d'ameublement, les articles de bricolage et de jardin, et les jouets. [S] [Ecomaison/ESS France, livret REP](https://www.ess-france.org/system/files/inline-files/Livret%20REP%20et%20ESS_Ecomaison_Ameublement_VF.pdf)
- **Produits pour animaux dans la REP ameublement.** La grille d'éco-participation Ecomaison (applicable à partir de 2025) contient une catégorie « mobilier d'extérieur et d'animaux ».
  - Sont visés les produits « pour les animaux (arbres à chat, matelas, coussins, hamacs, meubles d'aquarium sans l'aquarium…) ».
  - Les **paniers** ne sont pas nommés dans les extraits.
  - Les produits exclusivement professionnels sont exclus.
  - Seuils mentionnés : les pièces de moins de 2 kg sont « éligibles » dans une limite de 15 tonnes par an ; au-delà de 2 kg, la limite est de 1 000 pièces dans les mêmes 15 tonnes. Il s'agit vraisemblablement de l'éligibilité à un régime simplifié, interprétation à confirmer.
  - [S] [Ecomaison, grille 2025](https://ecomaison.com/wp-content/uploads/2024/08/Grille-des-tarifs-deco-participation-%E2%80%93-Applicables-a-partir-de-2025.pdf), [Ecomaison, guide des éco-modulations 2026](https://ecomaison.com/wp-content/uploads/2026/04/Guide-des-eco-modulations-2026_MAJ-mars-2026.pdf)
- **Coussin pour animaux.** Les consignes de tri Ecomaison classent le « coussin pour animaux domestiques » en literie et textile. [S] [Ecomaison, consignes de tri, janvier 2026](https://ecomaison.com/wp-content/uploads/2023/06/PRO_Consignes-de-tri-et-gestion-des-contenants-Ecomaison_REP-Mobilier-Jouets-BricoJardin_Janvier-2026.pdf)
- **IDU, base et obtention.** L'identifiant unique repose sur l'art. **L. 541-10-13 du Code de l'environnement** (loi AGEC). Il est généré par l'ADEME et transmis au producteur ou à son éco-organisme. Il est obligatoire depuis le 01/01/2022 et le registre public est SYDEREP. [S/S2] [GHR, fiche mémo IDU](https://www.ghr.fr/IMG/pdf/fiche_memo_-_idu_fr.pdf), [Ecologic, FAQ IDU et places de marché](https://www.ecologic-france.com/images/medias/document/18204/faqidentifiant-unique-et-places-de-marche-v10.pdf), [Projet Celsius](https://projetcelsius.com/blog/identifiant-unique-rep/)
- **IDU, affichage.** Le producteur indique son IDU **dans ses CGV** ou, à défaut, dans tout document contractuel remis à l'acheteur. Sur le site, il le communique dans les mêmes conditions que les mentions de l'article 19 de la LCEN. [S2] [Lettre des Réseaux](https://www.lettredesreseaux.com/identifiant-unique-mention-obligatoire-dans-les-cgv.html), [Projet Celsius](https://projetcelsius.com/blog/identifiant-unique-rep/)
- **Places de marché.** Une place de marché devient redevable de la REP d'un vendeur tiers sauf si elle détient la preuve que ce vendeur remplit ses obligations. L'IDU vaut preuve, et les plateformes peuvent suspendre les offres sans IDU. [S] [Adelphe, fiche réflexe](https://cdn.adelphe.fr/IDENTIFIANT_UNIQUE/ADELPHE_FICHE_REFLEXE_ID_UNIQUE_MARKETPLACE.pdf), [Ecologic, FAQ](https://www.ecologic-france.com/images/medias/document/18204/faqidentifiant-unique-et-places-de-marche-v10.pdf)
- **Sanction.** Une source unique évoque une amende administrative jusqu'à 30 000 € pour un producteur sans IDU, en renvoyant à l'art. L. 541-9-5. Ce n'est pas confirmé. [S2] [Projet Celsius](https://projetcelsius.com/blog/identifiant-unique-rep/)

### Inferences
- **Boutique Shopify en propre.** La marque est elle-même « producteur ». Elle doit :
  - adhérer à Citeo ou Léko pour ses emballages, y compris les sacs et cartons d'expédition (vraisemblablement des emballages ménagers, à confirmer avec Citeo) ;
  - adhérer à Ecomaison si elle vend un arbre à chat, un coussin ou un matelas ;
  - afficher ses IDU dans les CGV et les mentions légales.
- **Coût par commande de la REP emballages.** Il est négligeable à faible volume : un forfait de 80 à 110 € par an représente **0,05 à 0,20 € par commande** pour 500 à 2 000 commandes par an (calcul).
- **Dropshipping.** Les emballages livrés depuis la Chine au consommateur français sont mis sur le marché français par la marque. La REP emballages s'applique donc à la marque (inférence, à confirmer).

### Gaps
- **Triman et Info-tri [CP].** Art. L. 541-9-3 du Code de l'environnement et décret n° 2021-835. Ils sont obligatoires depuis 2022 sur les produits et emballages soumis à REP, avec des cas de dématérialisation limités. Non revérifié.
- **REP DEEE [CP].** Éco-organismes ecosystem et Ecologic. L'affichage de l'éco-participation est obligatoire. Barèmes non trouvés.
- **REP piles et accumulateurs [CP].** Corepile, Screlec/Batribox. Non recherché.
- **Champ d'autres REP.** Celui de la REP TLC (Refashion) pour les textiles pour animaux et celui de la REP jouets (Ecomaison) pour les jouets pour animaux restent inconnus. Les jouets pour animaux ne sont probablement pas des « jouets » au sens de la directive 2009/48/CE [CP].
- **Montants non trouvés.** Tarifs Léko, montants d'éco-participation Ecomaison pour un arbre à chat ou un coussin. Le montant du forfait Citeo 2026 hésite entre 80 € et 110 €.

## Q5 : Droit de la consommation. Prix de référence et prix barrés, « Made in France », garantie légale et rétractation

### Takeaway
- **Annonces de réduction.** Le prix de référence doit être **le prix le plus bas pratiqué dans les 30 jours précédant la réduction** (art. L. 112-1-1 du Code de la consommation, depuis le 28/05/2022). Un manquement est sanctionné comme pratique commerciale trompeuse.
- **« Fabriqué en France ».** L'allégation suppose que la **dernière transformation substantielle** ait lieu en France. Un produit chinois simplement emballé ou étiqueté en France ne peut pas la porter, et même un drapeau tricolore peut être trompeur.
- **Garantie et rétractation.** La garantie légale de 2 ans et la rétractation de 14 jours sont des règles stables, non revérifiées en ligne ici [CP].

### Cited Findings
- **Règle des 30 jours.** Depuis le 28/05/2022, l'art. L. 112-1-1 impose d'indiquer comme prix antérieur le prix le plus bas pratiqué auprès de tous les consommateurs pendant les 30 derniers jours.
  - En cas de réductions successives, la référence est le prix d'avant la première baisse.
  - La présentation est libre : pourcentage, montant ou prix barré.
  - La règle s'applique en ligne comme en magasin.
  - Deux exceptions existent : les produits périssables, et la comparaison avec les prix d'autres professionnels, qui doit être présentée clairement comme telle.
  - [S] [DGCCRF, fiche « Annonces de réduction de prix », écrite le 25/08/2026](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/annonces-de-reduction-de-prix-ce-que-vous-devez-savoir), [INC, tableau Omnibus (2022)](https://inc-conso.fr/sites/default/files/pdf/tableau-omnibus-inc-2022.pdf)
- **Sanction.** Un manquement est une pratique commerciale trompeuse (L. 121-2). La DGCCRF indique deux ans d'emprisonnement et 300 000 € d'amende. Des analyses juridiques évoquent 1,5 M€ pour les personnes morales, sans le préciser explicitement. [S/S2] [DGCCRF](https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/annonces-de-reduction-de-prix-ce-que-vous-devez-savoir), [Deloitte Avocats](https://blog.avocats.deloitte.fr/reduction-de-prix-et-pratiques-commerciales-trompeuses-la-dgccrf-maintient-sa-vigilance/)
- **Exemples de contrôle.**
  - Sanction de 1,3 M€ contre PrettyLittleThing pour des réductions trompeuses. La date n'apparaît pas dans le résumé. [S2] [Deloitte Avocats](https://blog.avocats.deloitte.fr/reduction-de-prix-et-pratiques-commerciales-trompeuses-la-dgccrf-maintient-sa-vigilance/)
  - Conforama a fait l'objet d'une injonction de cessation. [S2] [EconomieMatin](https://www.economiematin.fr/?p=231494)
- **Origine des produits non alimentaires.** Elle se détermine selon les règles douanières européennes. Un produit peut être dit « Fabriqué en France » si sa dernière transformation substantielle y a eu lieu, même avec des composants étrangers. La douane délivre gratuitement et de façon facultative un avis sur l'origine. [S] [Douane, dépliant « Fabriqué en France »](https://WWW.DOUANE.GOUV.FR/sites/default/files/2022-10/24/depliant-fabrique-en-france.pdf), [DGCCRF, flyer n° 173 (février 2024)](https://artois.ufcquechoisir.fr/wp-content/uploads/sites/115/2026/02/DGCCRF-N°-173-flyer-fabrique-en-france-Fevrier-2024.pdf), [INC](https://www.inc-conso.fr/content/quelles-sont-les-garanties-proposees-par-les-mentions-fabrique-en-france-et-origine-france)
- **Contrôle DGCCRF sur un drapeau tricolore.** Après une plainte, la DGCCRF a contrôlé un site d'outillage qui affichait le drapeau tricolore sur des outils importés de Chine. Le fondement retenu était L. 121-2. [S] Rapporté via des questions et réponses parlementaires ou le flyer DGCCRF ; la source exacte n'est pas identifiable dans le résumé : [AN, question QE38768 (15e législature, historique)](https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE38768.pdf)
- **Critère de valeur ajoutée.** Une question parlementaire juge le critère trop extensif : elle évoque une dernière transformation en France représentant au moins 45 % de la valeur ajoutée. [S, historique, 15e législature 2017-2022] [AN, question QE17850](https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE17850.pdf)
- **« Conçu en France ».** Cette mention relève d'autres règles mais ne doit pas tromper. Un guide pratique DGCCRF sur le « Fabriqué en France » existe. [S2] [Bpifrance Création](https://bpifrance-creation.fr/entrepreneur/actualites/fabrique-france-regles-a-connaitre)

### Inferences
- **Produit sourcé en Chine.** Il faut proscrire « Made in France », les drapeaux et toute formulation ambiguë. « Marque française » ou « conçu en France » ne sont utilisables que si c'est exact et sans suggérer une fabrication française.
- **Prix barré au lancement.** Une nouvelle marque qui n'a jamais vendu au prix « avant » ne peut pas l'afficher comme référence. Un faux « au lieu de 59,90 € » est un risque juridique direct.

### Gaps (règles stables connues mais non revérifiées en ligne [CP])
- **Rétractation de 14 jours** (L. 221-18). Les frais de retour sont à la charge du consommateur **s'il en a été informé avant la commande** ; sinon, le professionnel les paie (L. 221-23).
- **Remboursement** sous 14 jours, frais de livraison initiaux standard inclus (L. 221-24). Si l'information sur la rétractation est absente, le délai est prolongé de 12 mois (L. 221-20).
- **Garantie légale de conformité** de 2 ans, avec présomption d'antériorité du défaut pendant 24 mois pour un bien neuf (L. 217-3 et suivants). Garantie des vices cachés (art. 1641 du Code civil). Les mentions doivent être présentées de façon encadrée.
- **Délai de livraison.** Il doit être indiqué ; à défaut, il est de 30 jours (L. 216-1). C'est un point sensible en dropshipping.
- **Autres obligations.** Médiateur de la consommation obligatoire (L. 612-1), coût d'adhésion non trouvé. La plateforme européenne de RLL a fermé le 20/07/2025, si bien que le lien n'est plus requis. Mentions légales, CGV, RGPD et cookies.
- **Sanction propre au prix de référence.** Une éventuelle amende administrative spécifique au défaut d'information sur le prix de référence n'a pas été vérifiée.

## Q6 : Coûts opérationnels 2025-2026 (Shopify, paiements, transport France, 3PL, fret Chine, agents de sourcing)

### Takeaway
**Aucun de ces coûts n'a pu être sourcé dans cette session**, faute de budget de recherche. Le Livrable 1 contient des **hypothèses de travail [H]**. Elles reposent sur la connaissance préalable du chercheur (données au plus tard mi-2026), ne sont pas revérifiées et doivent être confirmées avant tout usage. Les pages à consulter en priorité sont listées en Gaps.

### Cited Findings
- Aucune donnée sourcée n'a été collectée sur ces postes. Seuls les coûts réglementaires liés à la commande (droit de 3 €, frais de 2 €, REP emballages) sont sourcés : voir Q2 et Q4.

### Inferences
- Par ordre d'impact sur la marge par commande d'un accessoire à 35-45 € :
  1. le coût d'acquisition publicitaire (CPA) ;
  2. le coût du produit ;
  3. le transport (ligne Chine ou colis France) ;
  4. les 5 € réglementaires par article en envoi direct de Chine (sourcés) ;
  5. les frais de paiement ;
  6. le 3PL en modèle stock.
- Les coûts fixes mensuels (abonnement Shopify, applications) pèsent fortement par commande à faible volume. Ils doivent être répartis selon un volume hypothétique explicite.

### Gaps
Pages à vérifier en priorité, avec relevé daté :
- **Shopify France.** Plans Basic, Grow et Advanced, et taux Shopify Payments pour les cartes EEE et hors EEE. Frais de transaction appliqués en cas de passerelle tierce. Frais de litige (chargeback).
- **Paiement alternatif.** Grille PayPal France. Commissions marchands Alma (paiement en 3 ou 4 fois) et Klarna France.
- **Transport France.** Tarifs Colissimo 2026 au guichet et en tarif pro ou via agrégateur. Mondial Relay, Chronopost et Relais Colis pour des colis de 0,25 à 2 kg, via Boxtal, Sendcloud ou Packlink.
- **3PL.** Grilles Cubyn et Bigblue, ou comparatifs : préparation par commande, stockage par palette ou m³, réception, emballage, minimums mensuels.
- **Fret Chine.** Lignes YunExpress et CJ vers la France (prix par colis de 0,2 à 0,5 kg, délais, conditions DDP/IOSS après le 01/07/2026). Fret aérien, maritime LCL/FCL et ferroviaire Chine-France : coût au kg ou au m³ et délais (indices Drewry ou Freightos).
- **Agents de sourcing.** Commission (pourcentage de la commande) et frais d'inspection.

## Q7 : Benchmarks publicitaires Meta et TikTok en France (CPM, CTR, CPC, conversion, CPA, ROAS)

### Takeaway
**Non sourcé dans cette session** (budget de recherche épuisé). Je fournis uniquement la mécanique de calcul et des valeurs d'illustration [H]. Avec 15 € par jour et par ensemble de publicités, le volume de conversions est trop faible pour juger statistiquement un produit en quelques jours (voir Inferences).

### Cited Findings
- Aucune donnée sourcée n'a été collectée. Les études à consulter sont WordStream/LocaliQ, Bïrch (ex-Revealbot), Varos, Superads, Statista et les benchmarks TikTok.

### Inferences
- **Formules (calcul).**
  - CPA = CPM / (1 000 × CTR × taux de conversion de la page).
  - ROAS de point mort = prix TTC / marge de contribution avant publicité.
- **Illustration de sensibilité [H].** Ces entrées ne sont pas des benchmarks.

| Hypothèse | CPM | CTR lien | Conversion | CPA obtenu |
|---|---|---|---|---|
| Prudente | 10 € | 1,0 % | 1,5 % | **66,67 €** |
| Centrale | 8 € | 1,2 % | 2,0 % | **33,33 €** |
| Optimiste | 6 € | 1,5 % | 3,0 % | **13,33 €** |

  Le CPA varie donc d'un facteur 5 selon des hypothèses plausibles. **Il faut mesurer le CPA réel** plutôt que l'emprunter à un benchmark.
- **Budget de 15 € par jour et par ensemble.** Avec un CPA de 20 à 33 €, on obtient environ 0,5 à 0,75 achat par jour, soit 3 à 5 par semaine. Meta indique qu'il faut environ **50 événements d'optimisation sur 7 jours** pour sortir de la phase d'apprentissage [CP, Meta Business Help Center, non revérifié]. Les ensembles restent donc durablement en « apprentissage limité ». Des décisions fondées sur moins de 10 conversions sont statistiquement fragiles.
- **Meta et TVA.** Les factures Meta proviennent de Meta Platforms Ireland. Pour une société assujettie, la TVA est autoliquidée et déductible, donc neutre. Pour une micro-entreprise en franchise, voir Q1 [CP].

### Gaps
- CPM, CTR, CPC, taux de conversion, CPA et ROAS pour Meta France 2025-2026, et si possible pour la catégorie animaux.
- Les mêmes indicateurs pour TikTok Ads France.
- Taux de conversion moyen d'une boutique Shopify (benchmarks Littledata ou Shopify).

## Q8 : Retours, remboursements, chargebacks et panier moyen (animaux, France)

### Takeaway
**Non sourcé dans cette session.** Les taux de retour et de chargeback et le panier moyen d'une animalerie en ligne française restent à rechercher, par exemple chez Fevad, Statista, Chargebacks911 ou dans les seuils des programmes Visa et Mastercard. Le Livrable 1 utilise des hypothèses [H] explicites.

### Cited Findings
- Aucune donnée sourcée n'a été collectée.

### Inferences
- **Modélisation des retours.** On les modélise comme une provision par commande égale au taux de retour multiplié par la perte nette par retour.
  - En dropshipping depuis la Chine, le retour vers le fournisseur n'est généralement pas rentable. La perte par retour s'approche alors du coût rendu complet du produit, frais réglementaires compris.
  - En stock France, le produit retourné est souvent revendable. La perte porte surtout sur l'aller payé et la préparation, plus une part d'invendables.
  - Les frais de retour peuvent être laissés au client **s'il en a été informé** [CP, L. 221-23].
- **Panier moyen.** Les coûts réglementaires et logistiques sont fixes par colis ou par article. Augmenter le panier (lots, deuxième article) est donc le principal levier de marge (inférence tirée de Q2).

### Gaps
- Taux de retour en e-commerce animalier (France ou UE).
- Taux de chargeback e-commerce et seuils des programmes Visa et Mastercard en 2025-2026.
- Frais de litige par chargeback (Shopify Payments, PayPal).
- Panier moyen d'une animalerie en ligne française (Fevad 2025-2026, rapports annuels de pure players comme Zooplus ou Wanimo).

## Livrable 1 : Tableau des paramètres (bas / central / haut)

### Takeaway
Seuls les postes fiscaux et réglementaires (TVA, droit de 3 €, frais de 2 €, taux ad valorem, forfait REP) sont sourcés. Tous les postes commerciaux sont des **hypothèses [H] à vérifier**, présentées comme telles. « Bas, central, haut » s'entend en **niveau de coût** : bas est favorable, haut est défavorable.

### Cited Findings

| # | Poste | Bas | Central | Haut | Statut | Source, date ou base de l'hypothèse |
|---|---|---|---|---|---|---|
| 1 | TVA, accessoires et appareils | 20 % | 20 % | 20 % | [S] | BOFiP BOI-TVA-LIQ-30-10-20 (taux normal 20 %, version 02/08/2023) ; TVA = TTC/6 |
| 2 | TVA, aliments et compléments animaux de compagnie | 20 % | 20 % | 20 % | [S] aliments, [inférence] compléments | BOFiP ; LégiFiscal |
| 3 | Droit UE forfaitaire, envoi au plus 150 € depuis pays tiers | 3 € par sous-position | 3 € | 3 € | [S] | Règl. (UE) 2026/382, du 01/07/2026 au 01/07/2028 ; guide de la Commission (02/06/2026) |
| 4 | « Union handling fee », ventes à distance importées | 0 € si report | 2 € par article | 2 € par article (voire par unité ?) | [S/S2] provisoire | Acte délégué C(2026) 6694 du 21/09/2026, application attendue au 01/11/2026 |
| 5 | Taxe française « petits colis » | 0 € | 0 € | 0 € | [S2] | Suspendue depuis le 01/07/2026 (2 € par article du 01/03 au 30/06/2026) |
| 6 | Droit ad valorem, import de stock (valeur en douane) | 2,7 % (4201 ; 8516 31) | 3,7 % (9603 90 99) | 6,3 à 6,5 % (6307 90 98 ; 3926 90 97) | [S2] | Miroirs TARIC (tariffnumber.com, Celna24), 2024-2026, à confirmer dans TARIC |
| 7 | Abonnement Shopify | environ 27 € par mois (Basic, annuel) | environ 36 € par mois (Basic, mensuel) | environ 79 à 105 € par mois (Grow) | **[H]** | Connaissance préalable (grille 2024-2025), non revérifiée |
| 8 | Applications Shopify | 0 € par mois | environ 40 € par mois | environ 100 € par mois | **[H]** | Hypothèse |
| 9 | Paiement, taux combiné (Shopify Payments, PayPal) | 1,5 % + 0,25 € | 2,0 % + 0,25 € | 2,9 % + 0,35 € | **[H]** | PayPal France 2,90 % + 0,35 € [CP] ; taux Shopify Payments non vérifié |
| 10 | Frais Shopify en cas de passerelle tierce | 0,6 % (Advanced) | 1 % (Grow) | 2 % (Basic) | **[H]/[CP]** | Grille 2024-2025, non revérifiée |
| 11 | Paiement fractionné (Alma, Klarna), commission marchand | environ 3 % | environ 3,5 à 4 % | environ 4,5 % ou plus | **[H]** | Non sourcé |
| 12 | Colis France de 0,25 à 2 kg, point relais | environ 3,5 € | environ 4,5 € | environ 6 € | **[H]** | Ordre de grandeur via agrégateur, non sourcé |
| 13 | Colis France de 0,25 à 2 kg, domicile Colissimo sans signature | environ 5,5 € | environ 6,5 € | environ 9,5 € | **[H]** | Non sourcé |
| 14 | Express (Chronopost) | environ 9 € | environ 11 € | environ 15 € | **[H]** | Non sourcé |
| 15 | 3PL, préparation par commande (premier article) | 1,8 € | 2,5 € | 3,5 € | **[H]** | Non sourcé ; article supplémentaire environ 0,2 à 0,6 € [H] |
| 16 | 3PL, stockage et réception ramenés à l'unité | 0,15 € | 0,30 € | 0,50 € | **[H]** | Non sourcé (environ 10 à 25 € par palette et par mois [H]) |
| 17 | Emballage et encart | 0,20 € | 0,30 à 0,40 € | 0,60 € | **[H]** | Non sourcé |
| 18 | Ligne de dropshipping Chine-France, 0,2 à 0,5 kg (hors 3 € et 2 €) | 4,5 € | 6,5 € | 8 € | **[H]** | Non sourcé ; délai environ 7 à 15 jours [H] |
| 19 | Fret international ramené à l'unité, modèle stock | 0,40 € (maritime) | 1,00 € | 2,50 € (aérien) | **[H]** | Non sourcé ; délais [H] : maritime 30 à 45 jours, ferroviaire 18 à 25 jours, aérien 5 à 10 jours |
| 20 | Dédouanement et transitaire ramenés à l'unité | 0,10 € | 0,30 € | 0,60 € | **[H]** | Non sourcé |
| 21 | Agent de sourcing | 5 % | 7 % | 10 % du coût produit | **[H]** | Non sourcé |
| 22 | REP emballages ménagers | 0,05 € par commande | 0,10 € | 0,20 € | [S] forfait, [H] volume | Citeo, forfait 80 € HT par an sous 10 000 UVC (2025), 110 € selon une source secondaire ; divisé par 500 à 2 000 commandes par an |
| 23 | REP ameublement (arbre à chat, coussin) | n.d. | n.d. | n.d. | [S] champ / montant non trouvé | Grille Ecomaison 2025 |
| 24 | CPA publicitaire Meta | 10 à 13 € | 20 à 33 € | 40 à 67 € | **[H]** | Calcul CPM / (1 000 × CTR × CVR) à partir d'entrées non sourcées (Q7) |
| 25 | Taux de retour ou remboursement | 3 % | 5 % | 8 % | **[H]** | Non sourcé |
| 26 | Taux de chargeback (frais de litige environ 15 €) | 0,2 % | 0,5 % | 1 % | **[H]** | Non sourcé |
| 27 | Panier moyen d'une animalerie en ligne française | n.d. | n.d. | n.d. | Gap | Non trouvé |

### Inferences
- Les lignes 3 et 4 (5 € par article au total) constituent le **seul changement structurel 2026 sourcé**. Elles touchent quasi exclusivement le modèle d'envoi direct depuis la Chine.
- Les lignes [H] doivent être remplacées par des relevés datés avant de construire les scénarios définitifs.

### Gaps
- Toutes les lignes [H] : voir les Gaps de Q6, Q7 et Q8.
- Le montant du forfait Citeo 2026 (80 € ou 110 €).
- Les tarifs d'Ecomaison et du DEEE.

## Livrable 2 : Checklist de conformité (obligation, qui est concerné, coût estimé, effort)

### Takeaway
Pour un accessoire non électronique sous marque propre, les obligations structurantes sont les suivantes :
- TVA, et IOSS en cas d'envoi direct de Chine ;
- droit de 3 € et frais de 2 € par article ;
- GPSR (étiquetage et fiche produit) ;
- REACH (preuves fournisseur) ;
- REP emballages et IDU, plus Ecomaison pour un couchage ou un arbre à chat ;
- règles de prix, d'origine et de vente à distance.

Pour un appareil électronique, il faut ajouter le CE (RED, CEM, DBT, RoHS), le DEEE, le règlement Batteries et un opérateur UE identifié.

### Cited Findings

Légende de la colonne « Concerné » : **M** = marque propre, quel que soit le modèle ; **D** = dropshipping depuis la Chine ; **S** = import de stock ; **E** = électronique uniquement.

| # | Obligation | Base | Concerné | Légal ou bonne pratique | Coût estimé | Effort | Statut |
|---|---|---|---|---|---|---|---|
| 1 | Collecter et déclarer la TVA à 20 % | CGI ; BOFiP | M (hors franchise) | Légal | Honoraires comptables non sourcés | Mensuel | [S] taux |
| 2 | IOSS pour les envois de 150 € maximum | Directive TVA e-commerce | D | Légal (sinon TVA et frais réclamés au client à la livraison) | Inscription gratuite pour une entreprise établie dans l'UE [CP] | Déclaration mensuelle | [S] mention / [CP] |
| 3 | Droit forfaitaire de 3 € par article | Règl. (UE) 2026/382 | D | Légal, du 01/07/2026 au 01/07/2028 | 3 € par sous-position | Intégré au prix de la ligne DDP | [S] |
| 4 | Frais de traitement UE de 2 € | Règl. (UE) 2026/2108, acte délégué C(2026) 6694 | D (et toute vente à distance importée) | Légal, à partir du 01/11/2026 sous réserve | 2 € par article | Aucun effort propre | [S/S2] provisoire |
| 5 | Droits ad valorem, dédouanement, EORI, autoliquidation de la TVA import | Code des douanes de l'Union ; TARIC | S | Légal | 2,7 à 6,5 % de la valeur en douane, plus transitaire | Par expédition | [S2] taux / [CP] |
| 6 | Interdiction de la fourrure de chat et de chien | Règl. (CE) 1523/2007 | M | Légal | 0 € | Vérification matière | [S2] |
| 7 | GPSR : opérateur UE, analyse de risques, documentation technique, traçabilité (type, lot), étiquette avec nom et adresses postale et électronique, avertissements en français | Règl. (UE) 2023/988 | M (D plus difficile) | Légal | Temps interne ; personne responsable externe inutile si la marque est établie en France [inférence] | Initial moyen, puis continu | [S2] / [CP] |
| 8 | GPSR, art. 19 : informations sur la fiche produit en ligne | Règl. (UE) 2023/988 | M | Légal | Environ 0 € | Faible | [S2] |
| 9 | GPSR : signalement des accidents (Safety Business Gateway) et rappels | Règl. (UE) 2023/988 | M | Légal | Variable | En cas d'incident | [CP] |
| 10 | REACH annexe XVII (azoïques, NPE, phtalates, HAP) et SVHC/SCIP | Règl. (CE) 1907/2006 | M (textile, plastique, caoutchouc, cuir) | Légal ; tests = bonne pratique | Rapports de test, coût non sourcé | Moyen | [S2] |
| 11 | CE, déclaration UE de conformité, dossier technique : RED (cybersécurité depuis le 01/08/2025 si connecté), CEM, DBT, RoHS | Directives 2014/53, 2014/30, 2014/35, 2011/65 ; Règl. délégué 2022/30 | E | Légal | Tests en laboratoire, coût non sourcé | Élevé | [S2] RED / [CP] reste |
| 12 | Opérateur UE identifié pour les produits CE | Règl. (UE) 2019/1020, art. 4 | E | Légal | Environ 0 € si la marque est établie en France | Faible | [CP] |
| 13 | Batteries : étiquetage (à partir du 18/08/2026 ou plus tard), QR code et amovibilité (18/02/2027), REP piles | Règl. (UE) 2023/1542 | E | Légal (en partie futur) | Reconception éventuelle | Élevé si batterie scellée | [S2] / [CP] |
| 14 | REP emballages ménagers (Citeo ou Léko) | Code de l'environnement (AGEC) | M (D compris, à confirmer) | Légal | Forfait 80 € HT par an sous 10 000 UVC (2025) | Déclaration annuelle | [S] |
| 15 | REP ameublement (arbre à chat, matelas, coussin, hamac pour animaux) | REP EA (Ecomaison) | M si produit concerné | Légal | Éco-participation non trouvée | Déclaration | [S] champ |
| 16 | REP DEEE et éco-participation visible | Code de l'environnement | E | Légal | Non trouvé | Déclaration | [CP] |
| 17 | Identifiant unique (IDU) à afficher dans les CGV et sur le site | L. 541-10-13 du Code de l'environnement | M | Légal | 0 € pour l'IDU lui-même [CP] | Faible | [S2] |
| 18 | Triman et Info-tri | L. 541-9-3 du Code de l'environnement ; décret 2021-835 | M | Légal | Conception de l'emballage | Faible | [CP] |
| 19 | Interdiction de détruire les invendus non alimentaires | Loi AGEC | S | Légal | Coût du don ou du recyclage | Faible | [CP] |
| 20 | Prix de référence au plus bas des 30 derniers jours | L. 112-1-1 du Code de la consommation | M | Légal | 0 € (processus) | Faible | [S] |
| 21 | Pas d'origine trompeuse (« Made in France », drapeau) | L. 121-2 du Code de la consommation ; règles d'origine douanières | M | Légal si allégation | 0 € (avis d'origine douane gratuit) | Faible | [S] |
| 22 | Garantie légale de conformité (2 ans) et vices cachés ; information encadrée | L. 217-3 et suivants du Code de la consommation ; art. 1641 du Code civil | M | Légal | Provision service après-vente | Faible | [CP] |
| 23 | Rétractation de 14 jours ; frais de retour au client s'il en est informé | L. 221-18, L. 221-23, L. 221-24 du Code de la consommation | M | Légal | Provision de retours | Faible | [CP] |
| 24 | Délai de livraison affiché (30 jours par défaut) | L. 216-1 du Code de la consommation | M (surtout D) | Légal | 0 € | Faible | [CP] |
| 25 | Médiateur de la consommation | L. 612-1 du Code de la consommation | M | Légal | Adhésion, coût non trouvé | Faible | [CP] |
| 26 | Mentions légales, CGV, RGPD et cookies | LCEN ; RGPD | M | Légal | Modèles ou juriste | Faible | [CP] |
| 27 | Information environnementale (AGEC, art. 13) | Décret 2022-748 | Non applicable sous environ 10 M€ de CA | — | — | — | [CP] |
| 28 | Accessibilité (EAA) | Directive (UE) 2019/882 | Microentreprises de services exemptées | — | — | — | [CP] |
| 29 | Renseignement tarifaire contraignant (RTC) pour sécuriser le code SH | Code des douanes de l'Union | S/D | Bonne pratique | Gratuit [CP] | Faible | [CP] |
| 30 | Contrôle qualité avant expédition, échantillons, tests indépendants | — | M | Bonne pratique | Non sourcé | Moyen | [H] |
| 31 | Assurance responsabilité civile produits | — | M | Bonne pratique | Non sourcé | Faible | [H] |

### Inferences
- **Hiérarchie des risques.** En dropshipping depuis la Chine, le risque juridique principal tient à la combinaison de trois facteurs :
  - la responsabilité GPSR et REACH sans contrôle physique du produit ;
  - les délais de livraison et l'information du consommateur ;
  - les 5 € par article de coûts douaniers.

  En import de stock, le risque se déplace vers le capital immobilisé, les invendus et l'interdiction de les détruire.

### Gaps
- Coûts des tests, de la médiation, de l'assurance, d'un expert-comptable et des éco-participations DEEE et ameublement.

## Livrable 3 : Exemple chiffré illustratif d'une commande (accessoire hypothétique à 39,90 € TTC)

### Takeaway
**ILLUSTRATIF, ce n'est pas une prévision.** Pour un accessoire vendu 39,90 € TTC, port inclus pour le client (hypothèse), et un article par commande :

| Modèle | Prudent | Central | Optimiste |
|---|---|---|---|
| A. Dropshipping Chine (DDP/IOSS) | 5,23 € | 11,30 € | 16,70 € |
| B. Stock en France et 3PL | 6,59 € | 15,68 € | 20,50 € |

Ces montants sont la **marge de contribution avant publicité**, par commande et hors TVA. Ils correspondent aussi au **CPA maximal de point mort**. En scénario central, le ROAS de point mort (sur le CA TTC) est de **3,53 en dropshipping** et de **2,54 en stock**.

Ces marges sont **avant** coûts fixes, impôts et rémunération du dirigeant. **Ce n'est en aucun cas un bénéfice net.**

### Cited Findings
**Entrées sourcées :**
- TVA de 20 % (BOFiP) ;
- droit forfaitaire de 3 € par article (Règl. 2026/382) ;
- frais de traitement de 2 € par article, à partir du 01/11/2026 sous réserve (C(2026) 6694) ;
- taux ad valorem de 2,7 % (4201) et 6,5 % (3926 90 97), via miroirs TARIC ;
- forfait Citeo de 80 € HT par an (2025).

**Toutes les autres entrées sont des hypothèses [H].**

**Base de calcul.** Prix 39,90 € TTC, soit **33,25 € HT** et **6,65 € de TVA** collectée (TTC/6). La TVA est reversée et n'est pas un revenu.

**Modèle A : dropshipping Chine vers France, envoi DDP avec TVA collectée via IOSS, un article par colis (€ HT par commande)**

| Poste | Prudent | Central | Optimiste | Statut |
|---|---|---|---|---|
| Produit (prix fournisseur) | 9,00 | 7,00 | 5,00 | [H] |
| Ligne d'expédition Chine-France | 8,00 | 6,50 | 4,50 | [H] |
| Droit UE forfaitaire | 3,00 | 3,00 | 3,00 | [S] |
| Frais de traitement UE (à partir du 01/11/2026) | 2,00 | 2,00 | 2,00 | [S] provisoire |
| Paiement (2,9 % + 0,35 € ; 2,0 % + 0,25 € ; 1,5 % + 0,25 €, appliqués au TTC) | 1,51 | 1,05 | 0,85 | [H] |
| Shopify et applications (50, 100 ou 250 commandes par mois) | 1,50 | 0,80 | 0,40 | [H] |
| Emballage et encart | 0,50 | 0,30 | 0,20 | [H] |
| REP emballages (forfait divisé par le volume) | 0,20 | 0,10 | 0,05 | [S] forfait / [H] volume |
| Provision retours (8 %, 5 % ou 3 % × coût rendu, sans revente) | 1,76 | 0,93 | 0,44 | [H] |
| Provision chargebacks (1 %, 0,5 % ou 0,2 % × (prix + 15 € de frais)) | 0,55 | 0,27 | 0,11 | [H] |
| **Total des coûts variables hors publicité** | **28,02** | **21,95** | **16,55** | |
| **Marge de contribution avant publicité** | **5,23** | **11,30** | **16,70** | |
| Part du prix TTC | 13,1 % | 28,3 % | 41,9 % | |
| **ROAS de point mort (CA TTC / dépense publicitaire)** | **7,63** | **3,53** | **2,39** | |

**Modèle B : stock importé en France (fret consolidé), 3PL, colis national (€ HT par commande)**

| Poste | Prudent | Central | Optimiste | Statut |
|---|---|---|---|---|
| Produit (prix de volume) | 7,00 | 5,50 | 4,50 | [H] |
| Fret international ramené à l'unité | 2,50 (aérien) | 1,00 | 0,40 (maritime) | [H] |
| Droit ad valorem × (produit + fret) | 0,62 (6,5 %) | 0,42 (6,5 %) | 0,13 (2,7 %) | [S] taux / [H] base |
| Dédouanement et transitaire | 0,60 | 0,30 | 0,10 | [H] |
| 3PL, réception et stockage | 0,50 | 0,30 | 0,15 | [H] |
| 3PL, préparation de commande | 3,50 | 2,50 | 1,80 | [H] |
| Emballage | 0,60 | 0,40 | 0,25 | [H] |
| Colis France (domicile, point relais, point relais) | 6,50 | 4,50 | 3,80 | [H] |
| Paiement | 1,51 | 1,05 | 0,85 | [H] |
| Shopify et applications | 1,50 | 0,80 | 0,40 | [H] |
| REP emballages | 0,20 | 0,10 | 0,05 | [S]/[H] |
| Provision retours (taux × (aller + préparation + part invendable du produit : 50 %, 30 %, 30 %)) | 1,08 | 0,43 | 0,21 | [H] |
| Provision chargebacks | 0,55 | 0,27 | 0,11 | [H] |
| **Total des coûts variables hors publicité** | **26,66** | **17,57** | **12,75** | |
| **Marge de contribution avant publicité** | **6,59** | **15,68** | **20,50** | |
| Part du prix TTC | 16,5 % | 39,3 % | 51,4 % | |
| **ROAS de point mort (CA TTC / dépense publicitaire)** | **6,05** | **2,54** | **1,95** | |

**Contribution après publicité (scénario central) selon le CPA effectivement mesuré**

| CPA | 10 € | 15 € | 20 € | 30 € | 40 € |
|---|---|---|---|---|---|
| A. Dropshipping (11,30 €) | +1,30 | −3,70 | −8,70 | −18,70 | −28,70 |
| B. Stock (15,68 €) | +5,68 | +0,68 | −4,32 | −14,32 | −24,32 |

**Sensibilité au prix (scénario central, même méthode)**

| Prix | HT | TVA | Contribution avant publicité, A | Contribution avant publicité, B | ROAS de point mort |
|---|---|---|---|---|---|
| 34,90 € TTC | 29,08 € | 5,82 € | 7,25 € | 11,63 € | 4,81 (A) / 3,00 (B) |
| 44,90 € TTC | 37,42 € | 7,48 € | 15,34 € | 19,72 € | 2,93 (A) / 2,28 (B) |

### Inferences
- **Les droits de 2026 ont un poids décisif en dropshipping.** Sans les frais de 2 € (report éventuel), la contribution centrale du modèle A passe de 11,30 € à 13,30 €. Les 5 € réglementaires pèsent autant que le coût d'un produit bon marché.
- **Panier et lots.** Un lot de 2 unités identiques dans un seul colis ne paie qu'un droit de 3 € (sourcé). Les frais de 2 € pourraient être dus par unité, ce qui reste à confirmer. Augmenter le panier est donc le levier n° 1.
- **À 39,90 €, le modèle stock supporte un CPA d'environ 15 € et le dropshipping d'environ 11 €.** Les CPA d'illustration de Q7 (13 à 67 €) montrent que **la rentabilité dès la première commande n'est pas acquise**. Il faut mesurer le CPA réel avant d'engager du stock.
- **Éléments non inclus.** Le résultat ci-dessus n'intègre pas :
  - le stock immobilisé (minimum de commande × coût rendu) et les invendus qu'il est interdit de détruire ;
  - les créatifs publicitaires, échantillons et tests ;
  - la conformité (tests, médiateur, assurance) et l'expert-comptable ;
  - les frais bancaires, l'impôt sur les sociétés ou les cotisations sociales, et la rémunération du dirigeant ;
  - la valeur client sur la durée (réachat), à documenter séparément.

  **Il ne faut donc jamais présenter la contribution comme un bénéfice net.**

### Gaps
- Toutes les entrées [H] sont à remplacer par des relevés datés (voir Q6, Q7 et Q8).
- Le régime TVA du client (franchise ou non) peut modifier le calcul. En franchise, il n'y a pas de TVA collectée, mais pas de déduction, et la TVA autoliquidée sur Meta devient un coût [CP].
- La règle exacte de l'« item » pour les frais de 2 € (unité ou ligne tarifaire) change le calcul des lots.
