# Analyse financière des 5 finalistes : économie unitaire, valeur client et budgets de test (état au 28/10/2026)

*Note du 28/10/2026 pour le rapport final du projet « produit animalier gagnant pour la France ». Elle chiffre, pour les 5 finalistes, la rentabilité d’une commande, la valeur d’un client sur 6 et 12 mois et le budget minimal d’un test sérieux. C’est un travail de calcul sur les notes de recherche existantes, pas une nouvelle étude de marché.*

**Méthode et limites (à lire avant d’utiliser un chiffre).**
1. **Données d’entrée.** Les paramètres viennent des notes `fr_couts_commerciaux.md`, `fr_costs_regulation.md`, `verification_jouet_lechage.md`, `sourcing_jouet_lechage.md`, `fr_deep_jouet_lechage_congelable.md`, `fr_demande_jouet_lechage.md`, `pub_jouet_lechage.md`, `deep_support_nerf_de_boeuf.md`, `faisabilite_litiere_et_bouchees.md`, `deep_boite_puzzle_chat.md` et `pub_litiere_et_bouchees.md`. Chaque chiffre repris porte sa note et l’URL d’origine citée par cette note. Ces notes reposent elles-mêmes sur des extraits de moteur de recherche (preuve indirecte) : il faut ouvrir l’URL avant de montrer un chiffre au client.
2. **Trois recherches complémentaires (WebSearch, mode « standard », 3 sur 5 autorisées).** Deux paramètres qui décident des conclusions manquaient dans toutes les notes : (a) la rétention et le taux de réachat d’un client e-commerce animalier, qui décident du délai de récupération du coût d’acquisition ; (b) le prix d’un essai de laboratoire REACH, qui pèse dans le budget de test. Les résultats sont des **synthèses de moteur** (sites d’éditeurs et de prestataires, méthodologies hétérogènes) : ils sont utilisés comme ordres de grandeur et signalés « SOURCÉ (recherche du 28/10) ». Aucun WebFetch ni curl.
3. **Calculs.** Tous les montants sont calculés en Python (`/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance/model.py` pour les paramètres et formules, `/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance/report.py` pour les tableaux ; dossier de travail temporaire de la session). Chaque ligne affichée est arrondie au centime **avant** les totaux : les tableaux s’additionnent au centime près (contrôle automatique effectué).
4. **Conventions.**
   - Montants en **€ HT par commande**, sauf mention « TTC ». La TVA collectée (20 %, soit TTC ÷ 6) est reversée à l’État : ce n’est pas un revenu.
   - On suppose une **entreprise assujettie à la TVA** (TVA sur achats récupérable, publicité Meta et Shopify facturées HT par autoliquidation). La variante « franchise en base » est chiffrée au §2.7.
   - **Prudent** = toutes les valeurs défavorables des notes appliquées en même temps : c’est un plancher, un test de résistance, pas un scénario probable. **Intermédiaire** = valeurs centrales : c’est le scénario de référence pour décider. **Optimiste** = toutes les valeurs favorables en même temps.
   - Taux de change : 1 $ = 0,86 € (HYPOTHÈSE reprise de toutes les notes, à remplacer par le taux BCE du jour).
5. **Ce que les marges ne sont pas.** La « marge contributive » et la « marge après publicité » sont calculées **avant** les coûts fixes et de lancement (création de la marque, échantillons, stock invendu, contenus, outils hors Shopify, comptable, assurance), avant l’impôt, les cotisations, la rémunération du dirigeant et le financement du stock. **Aucune n’est un bénéfice net.**
6. **Statuts.** **SOURCÉ** : chiffre repris d’une note (avec l’URL d’origine) ou d’une recherche de cette session. **HYPOTHÈSE** : valeur non sourcée, avec son raisonnement. **CALCUL** : résultat d’une formule sur des entrées sourcées ou supposées. Les prix fournisseurs sont des prix d’annonce (souvent FOB, non négociés), pas des devis.

## 1. Tableau unique des hypothèses

### 1.1 Paramètres communs aux 5 finalistes

| # | Paramètre | Prudent | Intermédiaire | Optimiste | Statut | Source (note → URL d’origine) ou raisonnement |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| H1 | TVA sur accessoires, aliments et compléments pour animaux de compagnie | 20 % | 20 % | 20 % | SOURCÉ | `fr_costs_regulation.md` Q1 → [BOFiP BOI-TVA-LIQ-30-10-20](https://bofip.impots.gouv.fr/bofip/273-PGP.html/identifiant=BOI-TVA-LIQ-30-10-20-20230802). HT = TTC ÷ 1,2. |
| H2 | Taux de change | 1 $ = 0,86 € | 1 $ = 0,86 € | 1 $ = 0,86 € | HYPOTHÈSE | Repris de toutes les notes (non sourcé) ; à remplacer par le taux BCE. |
| H3 | Frais d’encaissement (mix de paiement appliqué au TTC) | 2,64 % + 0,28 € (60 % carte standard 1,5 % + 0,25 € ; 10 % carte internationale 2,7 % + 0,25 € ; 25 % PayPal + 2 % de frais Shopify de passerelle, soit 4,9 % + 0,35 € ; 5 % Klarna 4,99 % + 0,35 €) | 1,77 % + 0,265 € (80 % carte standard ; 5 % internationale ; 15 % PayPal 2,9 % + 0,35 €) | 1,50 % + 0,25 € (100 % carte standard, Shopify Payments Basic) | SOURCÉ (taux) + HYPOTHÈSE (mix) | Taux : `fr_couts_commerciaux.md` Q1 → [Kanal, Shopify Payments](https://getkanal.com/fr/blog/shopify-payments-frais), [PayPal FR (taux)](https://www.paypal.com/fr/business/paypal-business-fees), [PayPal FR (fixe)](https://www.paypal.com/fr/webapps/mpp/merchant-fees), [Kanal, Klarna/Alma](https://getkanal.com/fr/blog/paiement-plusieurs-fois-shopify.md), [Kanal, passerelle tierce](https://getkanal.com/fr/blog/prix-shopify). Mix : celui de la note (central « 80/5/15 »). |
| H4 | Shopify et applications, ramenés à la commande (inclus dans « frais de plateforme ») | 1,52 € (36 € + 40 €, 50 commandes/mois) | 0,76 € (100 commandes/mois) | 0,30 € (250 commandes/mois) | SOURCÉ (Basic 36 €/mois) + HYPOTHÈSE (applications 40 €/mois, volumes) | `fr_couts_commerciaux.md` P1–P3 → [Kanal, prix Shopify 2026](https://getkanal.com/fr/blog/prix-shopify), [Sellfy](https://sellfy.com/fr/blog/tarifs-shopify/). C’est un coût fixe réparti : au lancement (10 à 35 commandes/mois au rythme du test), il pèse 2 à 8 € par commande ; il est aussi compté dans les budgets de test (§5). |
| H5 | Transport France, colis ≤ 500 g (€ HT) | 5,74 € | 3,66 € | 3,46 € | SOURCÉ + HYPOTHÈSE (choix du transporteur, H9) | Colissimo point de retrait 6,89 € TTC ([La Poste, 01/01/2026](https://www.laposte.fr/colissimo-en-ligne/tarifs)) ; Mondial Relay point relais 4,15 € TTC ([ShippyPro, grille du 15/06/2026](https://www.shippypro.com/blog/fr/envoyer-un-colis-prix-et-tarifs-2026-des-transporteurs-en-france)) + 0,20 € d’agrégateur ([Margeo](https://margeoapp.com/blog/calculateur-frais-mondial-relay-colissimo-2026)). |
| H6 | Transport France, colis ≤ 1 kg | 7,41 € | 5,19 € | 3,89 € | SOURCÉ | Colissimo retrait 8,89 € TTC ; Mondial Relay 5,99 € TTC + 0,20 € ; Mondial Relay pro « dès 3,89 € » ([comptes pros anonymisés, 02/2026](https://artisansdeuxpointzero.fr/mondial-relay-tarif-pro-artisan), statut HT/TTC non précisé). |
| H7 | Transport France, colis ≤ 2 kg | 8,74 € | 6,86 € | 4,89 € | SOURCÉ | Colissimo retrait 10,49 € TTC ; Mondial Relay 7,99 € TTC + 0,20 € ; Mondial Relay pro observé 4,89 € HT (1–2 kg). |
| H8 | Transport France, colis ≤ 5 kg | 13,91 € | 13,53 € | 6,25 € | SOURCÉ | Colissimo retrait 16,69 € TTC ; Mondial Relay 15,99 € TTC + 0,20 € ; Mondial Relay pro observé 6,25 € HT (2–5 kg), source secondaire non officielle. |
| H9 | Règle de choix du transporteur et du poids | Colissimo point de retrait (proxy des suppléments, de la hausse 2027 et d’un tarif non négocié) ; poids volumétrique (L × l × h ÷ 5 000) appliqué | Mondial Relay point relais, tarif public + agrégateur | Mondial Relay public (≤ 500 g) ou pro observé (au-delà) | HYPOTHÈSE | Le point relais par défaut est la recommandation de `fr_couts_commerciaux.md` Q2. Poids d’expédition = poids des articles + sachet (60 / 40 / 30 g). Risque de hausse : Arcep +7,5 %/an en moyenne 2026–2029 ([avis 26-1295](https://www.arcep.fr/uploads/tx_gsavis/26-1295.pdf)) ; supplément volumétrique Mondial Relay ([Sendcloud](https://support.sendcloud.com/hc/fr/articles/360036521531-Mondial-Relay-Suppl%C3%A9ments-Tarifaires-et-Restrictions)). Le statut de TVA des tarifs Colissimo n’est pas vérifié (s’ils sont exonérés, le prudent est encore plus cher). |
| H10 | Préparation de commande, premier article | 5,25 € (lecture « coût complet », stockage inclus) | 1,75 € | 1,00 € | SOURCÉ | `fr_couts_commerciaux.md` P18 et P20 → [Logily 2026](https://logily.fr/tarif-logistique-ecommerce-2026/), [Alolog](https://alolog.fr/cout-externalisation-logistique-ecommerce/), [EightX, indice 3PL UE](https://eightx.co/blog/eu-3pl-cost-index). Le contenu exact du « coût complet » (3,50 à 7 €) n’est pas publié : à trancher par deux devis. En prudent, l’emballage (H14) est compté en plus (double compte possible, assumé par prudence). |
| H11 | Article supplémentaire dans la commande | 0,70 € | 0,50 € | 0,30 € | SOURCÉ | `fr_couts_commerciaux.md` P19 (mêmes sources). |
| H12 | Stockage et réception, par unité stockée | inclus dans H10 | 0,23 € | 0,02 € | CALCUL sur SOURCÉ + HYPOTHÈSE | P23 : (17,50 € × 2 mois + 11,50 €) ÷ 200 unités par palette ([tarif-logistique.fr](https://tarif-logistique.fr/prix-stockage-palette-mois/)). Multiplié par volume ÷ 0,006 m³ pour un article encombrant (boîte chat : × 1,31). |
| H13 | Auto-expédition (alternative au 3PL) | — | — | proche de la colonne optimiste | HYPOTHÈSE | Préparer soi-même ne coûte que l’emballage, mais le temps du dirigeant n’est pas valorisé ; la colonne optimiste (1 € par commande) sert d’approximation. À partir de 5 à 10 commandes par jour, le 3PL devient la norme. |
| H14 | Emballage d’expédition et encart (recettes, notice) | 0,60 € | 0,35 € | 0,20 € | HYPOTHÈSE | `fr_couts_commerciaux.md` P24 (non sourcé). L’emballage de vente (boîte imprimée) est compté dans le coût d’achat de l’article. |
| H15 | REP emballages (Citeo ou Léko), par commande | 0,20 € | 0,10 € | 0,05 € | SOURCÉ (forfait) + HYPOTHÈSE (volume) | Forfait de 80 € HT/an sous 10 000 UVC ([Citeo, tarif 2025](https://bo.citeo.com/sites/default/files/2025-04/20241219_MAJ_Tarif_EM_2025-FR.pdf)) ou 110 € ([EPR Representative](https://eprrepresentative.com/blog/bareme-emballages-menagers-2027-citeo-leko)) ÷ 500 à 2 000 commandes/an (`fr_costs_regulation.md` Q4). |
| H16 | Commission d’agent de sourcing (% du prix d’achat) | 15 % | 7,5 % | 3 % | SOURCÉ | `fr_couts_commerciaux.md` P25 → [Epic Sourcing 2026](https://www.epicsourcing.co.uk/post/china-sourcing-agent-cost-uk-2026), [Supplyia](https://www.supplyia.com/China-sourcing-agent/). |
| H17 | Fret international du stock (Chine → France) | ferroviaire 450 $/m³ | groupage maritime 60 $/m³ (haut de fourchette, haute saison) | groupage maritime 30 $/m³ | SOURCÉ (tarifs) + HYPOTHÈSE (mode par scénario) | `fr_couts_commerciaux.md` Q4, P27 → [Sino-Shipping](https://www.sino-shipping.com/fr/freight-costs-from-china/overview/). Le 1er lot en aérien DDP (5 / 6 / 9 $/kg : [Dantful](https://www.dantful.com/ddp-shipping-from-china-to-france/), [Viputrans](https://www.viputrans.com/shipping-from-china-to-france-2026-guide-to-importing-goods.html)) est chiffré à part (§4.3, §5). Le central de P27 (ferroviaire) sert ici de prudent, car un réassort régulier passe en maritime. |
| H18 | Dédouanement, transitaire et frais fixes de groupage, par unité importée | 0,60 € | 0,30 € | 0,10 € | HYPOTHÈSE | `fr_couts_commerciaux.md` P28 (non sourcé ; ils dominent sur un petit envoi). |
| H19 | Droits de douane ad valorem (import de stock) | 6,5 % sur tout le kit (risque de classement) | 4016 99 97 (caoutchouc) 2,5 % ; 3924 10 00 et 3926 90 97 (plastiques, silicone) 6,5 % ; carton et granulés 4 % | idem, carton et granulés 0 % | SOURCÉ (taux) + HYPOTHÈSE (carton, granulés) | `verification_jouet_lechage.md` §5 → [Celna24, 4016 99 97](https://celna24.pl/en/customs-tariff/4016999790), [The Trade Hub, 3924 10 00](https://www.thetradehub.eu/en/customs/nomenclature/392410000080) ; `fr_costs_regulation.md` → [tariffnumber, 3926 90 97](https://www.tariffnumber.com/2026/39269097). Assiette : achat + fret. À sécuriser par un RTC (gratuit). |
| H20 | Droit forfaitaire UE de 3 € par ligne tarifaire + frais de traitement de 2 € par article | — | 0 € en stock UE ; en envoi direct de Chine : 3 € × lignes + 2 € × articles | — | SOURCÉ | Règl. (UE) 2026/382, du 01/07/2026 au 01/07/2028 ([guide de la Commission](https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf)) ; règl. délégué (UE) 2026/2152, à partir du 01/11/2026 ([Commission, réforme douanière](https://taxation-customs.ec.europa.eu/customs/eu-customs-reform_en), [lookuptax](https://lookuptax.com/tax-changes/european-union/union-handling-fee-delegated-reg-2026-2152), [Revenue Irlande](https://www.revenue.ie/en/corporate/press-office/press-releases/2026/pr-092926-handling-fee.aspx)). Ne concernent que le dropshipping (§4.3). |
| H21 | Ligne de dropshipping Chine → France (0,3 à 1 kg, hors 3 € et 2 €) | 8,00 € | 6,50 € | 4,50 € | HYPOTHÈSE | `fr_couts_commerciaux.md` P29 : aucun prix 2026 trouvé ; délai CJPacket 6 à 14 jours ([TrackingMore](https://www.trackingmore.com/review-cj-dropshipping.html?p=10)). |
| H22 | Taux de retours et remboursements (% des commandes) | 24 % | 12 % | 5 % | SOURCÉ (24 %, 12 %) + HYPOTHÈSE (5 %) | `fr_couts_commerciaux.md` P38 : animalerie 12 % ([Wisepim, 07/05/2026](https://wisepim.com/fr/ecommerce-industry-insights/pet-supplies), périmètre géographique non précisé) ; France tous secteurs, mode compris, 24 % ([blog Shopify citant la Fevad](https://www.shopify.com/fr/blog/retour-e-commerce), test de résistance) ; 5 % pour un accessoire non textile avec retour à la charge du client. |
| H23 | Part invendable d’un article retourné | durable 75 % ; consommable 100 % | durable 50 % ; consommable 100 % | durable 30 % ; consommable 100 % | HYPOTHÈSE | Un jouet léché ou mâché ne se revend pas ; un aliment ouvert non plus (exception d’hygiène au droit de rétractation, `faisabilite_litiere_et_bouchees.md` §2.3). Le tour 1 retenait 30 à 50 %. |
| H24 | Part des retours dont la marque paie l’étiquette retour | 50 % | 25 % | 0 % | HYPOTHÈSE | Rétractation : port retour à la charge du client s’il en est informé (art. L. 221-23, [CP] des notes) ; défaut ou erreur : à la charge de la marque. |
| H25 | Rétrofacturations : taux × (TTC + frais par litige) | 1,0 % × (TTC + 25,80 €) | 0,26 % × (TTC + 15,00 €) | 0,1 % × (TTC + 15,00 €) | SOURCÉ (0,26 %, frais) + HYPOTHÈSE (0,1 % et 1 %) | `fr_couts_commerciaux.md` P10, P39 → [chargeback.io (Sift, T3 2025)](https://www.chargeback.io/fr/blog/average-e-commerce-chargeback-rate), [blog Shopify, ≈ 15 €](https://shopify.com/fr/blog/retrofacturation), [Chargeflow, 20–30 $](https://www.chargeflow.io/fr/blog/shopify-chargebacks-guide). |
| H26 | CPM Meta France | 20,00 € | 13,00 € | 8,00 € | SOURCÉ | P31 : 8–18 € ([La Fabrique du Net 2026](https://www.lafabriquedunet.fr/logiciels/tendances/facebook-linkedin-instagram-twitter-quel-est-le-cout-dune-annonce)) ; 12–20 € ([Adintime](https://adintime.com/en/blog?id=311)) ; pic de 21,74 en 07/2026 ([Superads](https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/france)). |
| H27 | Taux de clic (CTR) | 1,51 % | 1,63 % | 2,19 % | SOURCÉ | P32 : moyenne toutes industries 1,51 % et animaux 1,63 % ([WordStream 2025](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025), [MegaDigital](https://megadigital.ai/en/blog/facebook-ad-benchmarks/)) ; médiane e-commerce 2,19 % ([Adamigo](https://www.adamigo.ai/blog/meta-ads-benchmarks-2026-by-objective-and-placement)). |
| H28 | Taux de conversion du site | 1,4 % | 2,0 % | 2,6 % | SOURCÉ | P34 : bas Shopify 1,4 % ([Launchtip](https://www.launchtip.com/fr/blog/benchmarks-taux-conversion-shopify-par-secteur-2026-statistiques-fourchettes-bon)) ; France 2 % ([La Fabrique du Net](https://www.lafabriquedunet.fr/logiciels/tendances/taux-de-conversion-ecommerce-statistiques-et-benchmarks)) ; animalerie 2,6 % ([Wisepim](https://wisepim.com/fr/ecommerce-industry-insights/pet-supplies)). |
| H29 | CPA Meta (coût par premier achat) = CPM ÷ (1 000 × CTR × conversion) | 94,61 € | 39,88 € | 14,05 € | CALCUL | Voir §1.2. Identique pour tous les produits (aucun benchmark par catégorie en France). |
| H30 | Remise d’abonnement ou de fidélité sur les réachats | 10 % | 10 % | 10 % | SOURCÉ (pratique du marché) | Woof : recharges 14,99 $ → 13,49 $ en abonnement ([mywoof.com](https://mywoof.com/collections/refills)) ; Bow Wow Labs : −30 % puis −10 % ([bowwowlabs.com](https://bowwowlabs.com/products/bully-sticks)). |
| H31 | Coût de relance par commande de réachat (e-mail, SMS, reciblage) | 2,00 € | 1,00 € | 0,50 € | HYPOTHÈSE | Non sourcé ; évite de présenter le réachat comme gratuit. |
| H32 | Attrition mensuelle des abonnés (consommables) | 10 % | 7,1 % | 5 % | SOURCÉ (recherche du 28/10) + HYPOTHÈSE | Panel Recharge 2024 : 7,1 %/mois (4,1 % volontaire + 3,0 % involontaire), rapporté par [Eightx](https://www.eightx.co/blog/average-subscription-churn-rate-by-category) ; consommables de réapprovisionnement, animaux compris : 5 à 8 %/mois ([Eightx, indice 2026](https://eightx.co/blog/dtc-subscription-churn-index-2026)). 10 % = prudence pour une marque nouvelle. |
| H33 | Taux de réachat à 12 mois (part des clients qui recommandent au moins une fois) | consommables 30 % ; durables 5 à 10 % | consommables 40 % ; durables 10 à 20 % | consommables 50 % ; durables 20 à 30 % | SOURCÉ (repères) + HYPOTHÈSE (valeurs) | Repères (recherche du 28/10, méthodes hétérogènes) : ≈ 28 % des clients e-commerce recommandent sous 12 mois ([Mobiloud](https://www.mobiloud.com/blog/repeat-customer-rate-ecommerce), [Metricrig](https://metricrig.pages.dev/answers/repeat-purchase-rate-ecommerce-benchmark-2026)) ; consommables (compléments, aliments, animaux) 30–40 % ([Eightx](https://eightx.co/blog/average-repeat-purchase-rate-by-vertical)), 35–55 % ([Eightx 2026](https://eightx.co/blog/average-ecommerce-repeat-purchase-rate-by-vertical-2026)) ; animaux 30–45 % ([Foundry CRO](https://foundrycro.com/blog/dtc-pet-marketing-benchmarks-2026/)). Le 72 % de Wisepim (animalerie) vise des enseignes multi-produits, définition inconnue : non retenu. Détail par produit au §3.1. |
| H34 | Volume mensuel servant à répartir les fixes | 50 commandes | 100 commandes | 250 commandes | HYPOTHÈSE | Voir H4. |

**Formule de la provision pour retours et remboursements (H22 à H25).** La ligne « chiffre d’affaires HT » est brute (avant remboursements). La provision doit donc contenir le prix remboursé, diminué de ce qui est récupéré :

`Provision = taux de retour × [prix HT remboursé − (1 − part invendable) × coût rendu de l’article durable + part payée par la marque × port retour] + taux de rétrofacturation × (TTC + frais de litige)`

Les frais déjà engagés sur une commande remboursée (port aller, préparation, encaissement non remboursé) restent comptés dans les autres lignes. Les notes amont ne provisionnaient que ces frais (≈ 1 € par commande) et gardaient le chiffre d’affaires : c’est pourquoi les marges ci-dessous sont plus basses de 1 à 3 € que dans `deep_support_nerf_de_boeuf.md`, `faisabilite_litiere_et_bouchees.md` et `deep_boite_puzzle_chat.md`.

### 1.2 Dérivation des trois CPA à partir des benchmarks

Formule : **CPA = CPM ÷ (1 000 × CTR × taux de conversion)**, c’est-à-dire le coût de 1 000 impressions divisé par le nombre d’achats qu’elles produisent.

| Scénario | CPM | CTR | Clics pour 1 000 impressions | CPC implicite | Conversion | Achats pour 1 000 impressions | CPA | Achats par jour à 15 €/jour | Achats par semaine à 15 €/jour |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Prudent | 20,00 € | 1,51 % | 15,1 | 1,32 € | 1,4 % | 0,2114 | 20 ÷ (15,1 × 0,014) = **94,61 €** | 0,16 | 1,1 |
| Intermédiaire | 13,00 € | 1,63 % | 16,3 | 0,80 € | 2,0 % | 0,3260 | 13 ÷ (16,3 × 0,020) = **39,88 €** | 0,38 | 2,6 |
| Optimiste | 8,00 € | 2,19 % | 21,9 | 0,37 € | 2,6 % | 0,5694 | 8 ÷ (21,9 × 0,026) = **14,05 €** | 1,07 | 7,5 |

- **Cohérence avec l’estimation centrale de ≈ 40 €** : le CPA intermédiaire vaut 39,88 €, comme dans `fr_couts_commerciaux.md` (P35, 39,9 €). Il est gardé tel quel.
- **Contrôle par le CPC** : CPA = CPC ÷ conversion. Avec le CPC animaux de 0,78 $ (≈ 0,67 €, [WordStream 2025](https://www.wordstream.com/blog/facebook-ads-benchmarks-2025)) et 2 % de conversion : 33,54 €. Le CPC implicite du scénario intermédiaire (0,80 €) est dans la fourchette française de 0,40 à 1,80 € ([La Fabrique du Net](https://www.lafabriquedunet.fr/logiciels/tendances/facebook-linkedin-instagram-twitter-quel-est-le-cout-dune-annonce)).
- **Contrôle par le panier et le ROAS** : CPA = panier moyen ÷ ROAS. Panier animalerie de 71 € ([Wisepim](https://wisepim.com/fr/ecommerce-industry-insights/pet-supplies)) ÷ ROAS médian animalerie de 1,78 ([Superscale](https://superscale.ai/learn/roas-benchmarks-by-industry/)) = 39,89 € ; ÷ ROAS de 2,19 toutes industries ([Varos via Flable](https://flable.ai/blog/meta-ads-profitability-benchmarks-d2c)) = 32,42 €.
- **Ce que ces CPA impliquent au budget actuel du client** (15 €/jour par ensemble de publicités) : 0,38 achat par jour en intermédiaire, soit 2,6 par semaine, très loin des ≈ 50 événements par semaine qui font sortir Meta de la phase d’apprentissage ([CP] rappelé dans `fr_couts_commerciaux.md`). Il faut regrouper le budget ou optimiser d’abord sur l’ajout au panier (§5.2).
- **Limite.** Aucun CPM, CTR ni taux de conversion propre aux animaux en France n’existe dans les notes ; le même CPA est appliqué aux 5 produits. En pratique, un lot plus cher convertit un peu moins bien : l’avantage des lots calculé plus bas est donc un maximum.

### 1.3 Hypothèses propres à chaque produit (coûts d’achat, poids, prix de vente)

| Produit | Paramètre | Prudent | Intermédiaire | Optimiste | Statut | Source ou raisonnement |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Jouet à lécher | Balle L en caoutchouc naturel, FOB | 2,29 $ | 1,91 $ | 1,53 $ | SOURCÉ [F] | Suzhou Becpet 1,53–2,29 $, MOQ 1 000 (`sourcing_jouet_lechage.md` §1.1 → [Made-in-China, extrait agrégé](https://www.made-in-china.com/manufacturers/wholesale-pet-chew-toy.html)). Taille maximale en catalogue : 8 cm (Woof L : 9,1 cm). |
| Jouet à lécher | Logo sur la balle | 0,20 $ | 0,20 $ | 0,20 $ | SOURCÉ par transposition | +0,20 $ relevé sur un tapis à lécher, MOQ 300 ([Alibaba](https://www.alibaba.com/product-detail/Custom-Silicone-Dog-Lick-Mat-with_1600535403683.html)) ; transposé à la balle (HYPOTHÈSE). |
| Jouet à lécher | Moule silicone avec logo | 1,36 $ | 1,115 $ | 0,87 $ | SOURCÉ [F] | Xiamen Hands Chain 0,87–1,36 $, MOQ 200 (`sourcing_jouet_lechage.md` §4.1 → [Alibaba, vitrine moules](https://www.alibaba.com/showroom/silicone-dog-paws-bone-mold.html)). |
| Jouet à lécher | Boîte de vente imprimée | 0,80 $ | 0,575 $ | 0,35 $ | SOURCÉ [F] | Shanghai Hongyun 0,35–0,80 $, MOQ 1 000 ([Made-in-China](https://sh-hongyun.en.made-in-china.com/product/TFaQsuHDOxci/China-Wholesale-Custom-Kids-Plush-Doll-Gift-Corrugated-Window-Toy-Box-Packaging-with-Plastic-Pet.html)). |
| Jouet à lécher | Poids du kit L (balle + moule + boîte) | 0,52 kg | 0,44 kg | 0,40 kg | SOURCÉ + HYPOTHÈSE | Balle Woof L 289 g, variante 322 g ([desertcart](https://www.desertcart.co.za/products/537931284-woof-pupsicle-large-25-75-lbs-long-lasting-dog-toy)) ; moule ≈ 100 g et boîte ≈ 50 g supposés. Le prudent franchit le seuil de 500 g. |
| Jouet à lécher | Kit XL : balle sur moule propriétaire (FOB) ; outillage | 7,00 $ ; 10 500 $ (3 jeux à 3 500 $) | 5,00 $ ; 4 000 $ (2 jeux à 2 000 $) | 3,00 $ ; 500 $ (1 jeu) | HYPOTHÈSE (prix) + SOURCÉ (outillage) | 3 à 7 $ supposés dans `sourcing_jouet_lechage.md` §2 C ; moule de compression 500–3 500 $ par jeu ([Melon Rubber](https://www.melon-rubber.com/custom-rubber-mould-manufacturer-injection-mould-of-custom-rubber-part-from-china-p-3.html), [Senses Mold](https://senses-mold.com/molding-tool/rubber-mold/compression-mold/)). Amorti sur 1 000 kits. Moule et boîte XL : × 1,3 ; poids XL 0,65 à 0,90 kg (HYPOTHÈSE). |
| Jouet à lécher | Tapis de léchage avec logo (kit complet) | 3,90 $ | 3,80 $ | 3,70 $ | SOURCÉ [F] | 3,50–3,70 $ + 0,20 $ de logo ([Alibaba](https://www.alibaba.com/product-detail/Custom-Silicone-Dog-Lick-Mat-with_1600535403683.html)). |
| Support nerf de bœuf | Support nylon L/XL, FOB (+ 0,20 $ logo + boîte 0,35–0,80 $) | 3,19 $ | 2,50 $ | 1,67 $ | SOURCÉ [F] + HYPOTHÈSE | Fourchette 0,95–3,19 $ chez 6 usines (`deep_support_nerf_de_boeuf.md` §3.1 → [Hongzhou](https://www.alibaba.com/product-detail/Bully-Stick-Bolt-for-Dogs-Dog_1601152729471.html), [Alibaba, supports](https://www.alibaba.com/wholesale/chew-stick-holder-dog.html)) ; modèle L/XL renforcé pris dans la moitié haute. Poids 0,15–0,25 kg (non relevé). |
| Support nerf de bœuf | Nerf de bœuf 15 cm, prix d’achat livré | 1,00 € | 0,60 € | 0,40 € | HYPOTHÈSE | Aucun prix de gros trouvé ; repère de détail ≈ 1,37 € la pièce (Trixie 12 cm × 8, [Zoomalia](https://www.zoomalia.com/animalerie/trixie-nerf-de-b-uf-a-macher-pour-chien-p-13761.html)). Poids d’un nerf épais pour grand chien : 60 / 45 / 30 g (HYPOTHÈSE). |
| Additif litière | Dose mensuelle (granulés, sachet, nuancier) | 3,00 € | 1,50 € | 0,80 € | HYPOTHÈSE | `faisabilite_litiere_et_bouchees.md` §1.8 : aucun prix B2B de granulés seuls. Fret aérien 9 / 6 / 5 $/kg ; droits 6,5 / 4 / 0 % (classement non vérifié). |
| Additif litière | Poids d’une dose mensuelle | 184 g | 100 g | 40 g | SOURCÉ + HYPOTHÈSE | Arm & Hammer 6,5 oz ≈ 184 g pour 4 usages ([PetSmart](https://www.petsmart.com/cat/litter-and-waste-disposal/litter/arm-and-hammer--health-iq-cat-litter-additive-83471.html)) ; Tigerino 4 × 10 g ([zooplus.fr](https://www.zooplus.fr/shop/chats/litiere_chat/litiere_tigerino_chat/tigerino_vet/2190817)) ; central supposé. |
| Litière (version abonnement) | Sac de 1,8 kg rendu entrepôt | 4,40 € | 2,24 € | 1,27 € | CALCUL de la note | `faisabilite_litiere_et_bouchees.md` §1.9 (FOB 1,20–1,99 $ le sac, conteneur ou groupage) → [Darling Pet](https://darlingpet.en.made-in-china.com/product/bflpCEQHXdWy/China-Wholesale-0-5-2mm-pH-Silica-Gel-Cat-Litter-of-Health-Monitoring-Crystal-Sand.html). |
| Bouchées | Pot de 60 bouchées départ usine UE + transport UE | 6,00 € + 0,30 € | 4,50 € + 0,15 € | 3,00 € + 0,10 € | HYPOTHÈSE | `faisabilite_litiere_et_bouchees.md` §1.8 : aucun prix UE publié ; repères chinois 2,20–4,50 $ la « pièce » ([Alibaba](https://www.alibaba.com/product-detail/Boot-Scoot-Soft-Chew-Treats-for_1601727274552.html)). Pot ≈ 0,30 kg (60 bouchées Glandex = 240 g, [Tom&Co](https://www.tomandco.com/fr-fr/glandex-soft-chew-240g-60-chews.html)). |
| Boîte chat | Boîte-labyrinthe en carton imprimé, FOB | 7,26 $ | 5,23 $ (= 4,50 €) | 3,00 $ | SOURCÉ [F] + HYPOTHÈSE | Griffoir carton avec logo 7,26 $ (MOQ 500), modèles simples 1–3 $ (`deep_boite_puzzle_chat.md` §3.1 → [Made-in-China](https://www.made-in-china.com/products-search/hot-china-products/Wholesale_Cat_Cardboard.html), [Alibaba](https://www.alibaba.com/showroom/cat-scratch-box-cardboard.html)) ; central de la note. Livrée à plat 45 × 25 × 7 cm ([Alibaba](https://www.alibaba.com/product-detail/Cat-Maze-scratcher-Box-with-Ball_1600953742091.html)) : 0,0079 m³ ; poids réel 0,6–0,9 kg supposé, poids volumétrique 1,58 kg. |
| Boîte chat | Pack de 3 inserts de rechange, rendu | 4,50 € | 3,00 € | 2,10 € | HYPOTHÈSE | 1,00 € l’insert dans `deep_boite_puzzle_chat.md` §3. |

**Prix de vente retenus** (HYPOTHÈSES de positionnement, appuyées sur les prix relevés en France) :
- Jouet à lécher : kit L **29,90 €** (Pupsicle d’origine 19,90–26,90 € chez [Manavibe](https://manavibe.fr/products/pupsicle-lechage-chien) ; Freezball XL 29,90 € chez [A Pet Store](https://apetstore.com/products/freezball-jouet-denrichissement-a-congeler-pour-chien) ; SmoothieDog 29,90 € chez [Cool4Pets](https://www.cool4pets.be/fr/smoothiedog-lickball)) ; duo 49,90 € ; kit complet 39,90 € ; kit + support 44,90 € ; XL 34,90 €.
- Support : **29,90 €** seul (Chewise ≈ 35,10 € sur [Amazon.fr](https://www.amazon.fr/Dispositif-s%C3%A9curis%C3%A9-l%C3%A9touffement-Compatible-b%C3%A2tonnets/dp/B0CQX8TRL2) ; génériques 18–28 € sur [Fruugo](https://www.fruugo.fr/bully-stick-holder-durable-dog-chew-holder-for-safe-anti-choking-chew-toy-for-aggressive-chewers-3-in-1-dog-enrichment-toy-dishwasher-safe/p-433628060-910266805)) ; kit + 8 nerfs 49,90 € ; recharge de 12 nerfs 29,90 € −10 %.
- Additif : **39,90 €** le coffret de 3 mois (Tigerino 16,49 € la boîte de 4 × 10 g, [zooplus.fr](https://www.zooplus.fr/shop/chats/litiere_chat/litiere_tigerino_chat/tigerino_vet/2190817)) ; 69,90 € les 6 mois. Litière : 19,90 € par mois ou 34,90 € les 2 sacs (Nullodor 6,49 € le sac de 1,5 kg, [zooplus.fr](https://www.zooplus.fr/shop/chats/litiere_chat/litiere_nullodor_chat/435914)).
- Bouchées : **34,90 €** le pot de 60 (Glandex 22,99 € les 30, 54,16 € les 120 en abonnement, [Amazon.fr](https://www.amazon.fr/Vetnique-pour-Chiens-Royaume-Uni-v%C3%A9t%C3%A9rinaires/dp/B0FMFDLMP5)) ; 64,90 € les 2 pots.
- Boîte chat : **39,90 €** (Cat Amazing Classic 51,40 € sur [Amazon.fr](https://www.amazon.fr/Cat-Impressionnante-jamais-Interactive-Puzzle/dp/B009R3SFBC) ; boîtes en bois 19,99–25 € ; labyrinthe carton 2,99 € chez [Action](https://www.action.com/fr-fr/p/3207939/labyrinthe-a-balles-pour-chat-pet-dreamteam/)) ; boîte + 3 inserts 49,90 € ; pack d’inserts 19,90 €.

## 2. Rentabilité de la première commande : les 8 lignes demandées, par finaliste

**Définition des lignes** (toutes en € HT par commande, sauf le prix) :
1. **Prix de vente TTC** : prix payé par le client, livraison en point relais offerte.
2. **Chiffre d’affaires HT estimé par commande** = TTC ÷ 1,2 (la TVA, TTC ÷ 6, est reversée).
3. **Coût du produit livré** = coût rendu entrepôt de l’article (achat, agent, fret, frais fixes, droits) + préparation et stockage + emballage d’expédition, encart et REP + transport jusqu’au client. Le détail est donné sous chaque tableau.
4. **Frais de paiement et de plateforme** = encaissement (H3) + Shopify et applications (H4).
5. **Provision estimée pour retours et remboursements** = remboursements nets + rétrofacturations (formule au §1.1).
6. **Marge contributive avant publicité** = ligne 2 − lignes 3 à 5. C’est aussi le **CPA d’équilibre** de la première commande.
7. **Coût d’acquisition client cible** = CPA attendu du scénario (H29), le même pour l’offre simple et le lot.
8. **Marge estimée après publicité** = ligne 6 − ligne 7, pour une **première commande d’un nouveau client**. Ce n’est pas un bénéfice net (voir la méthode).
- **ROAS d’équilibre** = chiffre d’affaires ÷ marge contributive : c’est le ROAS minimal, sur la première commande, en dessous duquel chaque euro de publicité perd de l’argent. Meta affiche un ROAS sur le TTC ; la version HT est donnée pour mémoire.

**Formules appliquées** (paramètres H1 à H34) :
- Coût rendu entrepôt d’un article importé = FOB × 0,86 × (1 + commission d’agent) + volume × tarif de fret × 0,86 + frais fixes par unité + taux de droit × (FOB × 0,86 + fret) [+ amortissement d’outillage pour la XL]. Article fabriqué ou acheté dans l’UE : prix livré, sans agent ni droit.
- Préparation et stockage = premier article + article supplémentaire × (articles − 1) + stockage par unité × unités (× volume ÷ 0,006 m³ si l’article est encombrant).
- Transport = tarif de la tranche de poids (H5 à H8) ; poids = poids des articles + sachet d’expédition (et poids volumétrique en prudent).
- Encaissement = taux du mix × TTC + fixe du mix (H3) ; plateforme = (36 € + 40 €) ÷ commandes par mois (H4).
- Provision = taux de retour × [HT − (1 − part invendable) × coût rendu des articles durables + part de port retour payée × port] + taux de rétrofacturation × (TTC + frais de litige).

### 2.1 Jouet à lécher congelable (modèle Woof « Pupsicle »)

**Offres comparées** : « Kit L (balle + moule + recettes) » (29,90 € TTC) et « Duo (2 kits L) » (49,90 € TTC). Stock importé (ou fabriqué) dans l’UE, expédié depuis la France.

*Coût rendu entrepôt des articles* (« Kit L » = balle L avec logo + moule silicone + boîte imprimée) :

| Coût rendu entrepôt (€ HT par unité) | Kit L · Prudent | Kit L · Intermédiaire | Kit L · Optimiste |
| :--- | ---: | ---: | ---: |
| Achat (FOB × 0,86 ou prix livré UE) | 4,00 | 3,27 | 2,54 |
| Commission d’agent | 0,60 | 0,25 | 0,08 |
| Fret international | 0,77 | 0,10 | 0,05 |
| Dédouanement et frais fixes | 0,60 | 0,30 | 0,10 |
| Droits de douane | 0,31 | 0,12 | 0,10 |
| **= Coût rendu entrepôt** | **6,28** | **4,04** | **2,87** |

*Les 8 lignes demandées, trois scénarios :*

| Ligne (€ par commande) | Kit L 29,90 € · Prudent | Kit L 29,90 € · Intermédiaire | Kit L 29,90 € · Optimiste | Duo 49,90 € · Prudent | Duo 49,90 € · Intermédiaire | Duo 49,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 29,90 | 29,90 | 29,90 | 49,90 | 49,90 | 49,90 |
| 2. Chiffre d’affaires HT estimé par commande | 24,92 | 24,92 | 24,92 | 41,58 | 41,58 | 41,58 |
| 3. Coût du produit livré | 19,74 | 10,13 | 7,60 | 28,05 | 16,43 | 11,22 |
| 4. Frais de paiement et de plateforme | 2,59 | 1,55 | 1,00 | 3,12 | 1,91 | 1,30 |
| 5. Provision estimée pour retours et remboursements | 7,05 | 2,98 | 1,19 | 11,03 | 4,83 | 1,94 |
| **6. Marge contributive avant publicité** | **−4,46** | **10,26** | **15,13** | **−0,62** | **18,41** | **27,12** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−99,07** | **−29,62** | **1,08** | **−95,23** | **−21,47** | **13,07** |
| CPA d’équilibre (1re commande) | aucun (marge ≤ 0) | 10,26 | 15,13 | aucun (marge ≤ 0) | 18,41 | 27,12 |
| ROAS d’équilibre (CA TTC ÷ pub) | n.a. (marge ≤ 0) | 2,91 | 1,98 | n.a. (marge ≤ 0) | 2,71 | 1,84 |
| ROAS d’équilibre (CA HT ÷ pub) | n.a. (marge ≤ 0) | 2,43 | 1,65 | n.a. (marge ≤ 0) | 2,26 | 1,53 |
| Marge contributive en % du CA HT | −18 % | 41 % | 61 % | −1 % | 44 % | 65 % |

*Détail des lignes 3 à 5 :*

| Détail (€ HT) | Kit L 29,90 € · Prudent | Kit L 29,90 € · Intermédiaire | Kit L 29,90 € · Optimiste | Duo 49,90 € · Prudent | Duo 49,90 € · Intermédiaire | Duo 49,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 6,28 | 4,04 | 2,87 | 12,56 | 8,08 | 5,74 |
| Préparation et stockage | 5,25 | 1,98 | 1,02 | 5,95 | 2,71 | 1,34 |
| Emballage d’expédition, encart, REP | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 7,41 (≤ 1 kg) | 3,66 (≤ 500 g) | 3,46 (≤ 500 g) | 8,74 (≤ 2 kg) | 5,19 (≤ 1 kg) | 3,89 (≤ 1 kg) |
| **= Coût du produit livré** | **19,74** | **10,13** | **7,60** | **28,05** | **16,43** | **11,22** |
| Encaissement | 1,07 | 0,79 | 0,70 | 1,60 | 1,15 | 1,00 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **2,59** | **1,55** | **1,00** | **3,12** | **1,91** | **1,30** |
| Remboursements nets | 6,49 | 2,86 | 1,15 | 10,27 | 4,66 | 1,88 |
| Rétrofacturations | 0,56 | 0,12 | 0,04 | 0,76 | 0,17 | 0,06 |
| **= Provision retours et remboursements** | **7,05** | **2,98** | **1,19** | **11,03** | **4,83** | **1,94** |
| Poids d’expédition retenu (kg) | 0,58 | 0,48 | 0,43 | 1,10 | 0,92 | 0,83 |

**Lecture.**
- **Offre simple à 29,90 €** : 10,26 € de marge contributive en intermédiaire (41 % du HT), soit un CPA d’équilibre de 10,26 € face à un CPA attendu de 39,88 € : **−29,62 € par première commande**. Seul l’optimiste équilibre (+1,08 €).
- **Duo à 49,90 €** : la marge contributive passe à 18,41 € (+8,15 €), car le port, la préparation et les frais fixes sont partagés ; il reste −21,47 € après publicité en intermédiaire, et +13,07 € en optimiste.
- **Postes les plus sensibles après le CPA** : la provision de remboursement (2,98 € à 12 % de retours ; 5,84 € à 24 %, autres coûts inchangés) et le seuil de 500 g : passer à la tranche de 1 kg coûte 1,53 € en intermédiaire. Le coût de l’objet lui-même (4,04 € rendu) n’est pas le facteur limitant.
- En prudent, la marge contributive est négative (−4,46 €) : 3PL « coût complet », Colissimo, 24 % de remboursements et 50 commandes par mois suffisent à consommer tout le prix, avant même la publicité.

### 2.2 Support de nerf de bœuf (modèle Bow Wow Labs « Bow Wow Buddy »)

**Offres comparées** : « Support seul L/XL » (29,90 € TTC) et « Kit support + 8 nerfs » (49,90 € TTC). Stock importé (ou fabriqué) dans l’UE, expédié depuis la France.

*Coût rendu entrepôt des articles* (« Support » = support L/XL avec logo + boîte imprimée ; « 8 nerfs » = sachet de 8 nerfs de bœuf achetés à une marque de l’UE) :

| Coût rendu entrepôt (€ HT par unité) | Support · Prudent | Support · Intermédiaire | Support · Optimiste | 8 nerfs · Prudent | 8 nerfs · Intermédiaire | 8 nerfs · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Achat (FOB × 0,86 ou prix livré UE) | 3,60 | 2,82 | 1,91 | 8,15 | 4,90 | 3,25 |
| Commission d’agent | 0,54 | 0,21 | 0,06 | 0,00 | 0,00 | 0,00 |
| Fret international | 0,58 | 0,08 | 0,04 | 0,00 | 0,00 | 0,00 |
| Dédouanement et frais fixes | 0,60 | 0,30 | 0,10 | 0,00 | 0,00 | 0,00 |
| Droits de douane | 0,27 | 0,19 | 0,13 | 0,00 | 0,00 | 0,00 |
| **= Coût rendu entrepôt** | **5,59** | **3,60** | **2,24** | **8,15** | **4,90** | **3,25** |

*Les 8 lignes demandées, trois scénarios :*

| Ligne (€ par commande) | Support 29,90 € · Prudent | Support 29,90 € · Intermédiaire | Support 29,90 € · Optimiste | Kit + 8 nerfs 49,90 € · Prudent | Kit + 8 nerfs 49,90 € · Intermédiaire | Kit + 8 nerfs 49,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 29,90 | 29,90 | 29,90 | 49,90 | 49,90 | 49,90 |
| 2. Chiffre d’affaires HT estimé par commande | 24,92 | 24,92 | 24,92 | 41,58 | 41,58 | 41,58 |
| 3. Coût du produit livré | 17,38 | 9,69 | 6,97 | 27,90 | 16,85 | 10,54 |
| 4. Frais de paiement et de plateforme | 2,59 | 1,55 | 1,00 | 3,12 | 1,91 | 1,30 |
| 5. Provision estimée pour retours et remboursements | 6,89 | 3,00 | 1,21 | 11,29 | 5,10 | 2,06 |
| **6. Marge contributive avant publicité** | **−1,94** | **10,68** | **15,74** | **−0,73** | **17,72** | **27,68** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−96,55** | **−29,20** | **1,69** | **−95,34** | **−22,16** | **13,63** |
| CPA d’équilibre (1re commande) | aucun (marge ≤ 0) | 10,68 | 15,74 | aucun (marge ≤ 0) | 17,72 | 27,68 |
| ROAS d’équilibre (CA TTC ÷ pub) | n.a. (marge ≤ 0) | 2,80 | 1,90 | n.a. (marge ≤ 0) | 2,82 | 1,80 |
| ROAS d’équilibre (CA HT ÷ pub) | n.a. (marge ≤ 0) | 2,33 | 1,58 | n.a. (marge ≤ 0) | 2,35 | 1,50 |
| Marge contributive en % du CA HT | −8 % | 43 % | 63 % | −2 % | 43 % | 67 % |

*Détail des lignes 3 à 5 :*

| Détail (€ HT) | Support 29,90 € · Prudent | Support 29,90 € · Intermédiaire | Support 29,90 € · Optimiste | Kit + 8 nerfs 49,90 € · Prudent | Kit + 8 nerfs 49,90 € · Intermédiaire | Kit + 8 nerfs 49,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 5,59 | 3,60 | 2,24 | 13,74 | 8,50 | 5,49 |
| Préparation et stockage | 5,25 | 1,98 | 1,02 | 5,95 | 2,71 | 1,34 |
| Emballage d’expédition, encart, REP | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 5,74 (≤ 500 g) | 3,66 (≤ 500 g) | 3,46 (≤ 500 g) | 7,41 (≤ 1 kg) | 5,19 (≤ 1 kg) | 3,46 (≤ 500 g) |
| **= Coût du produit livré** | **17,38** | **9,69** | **6,97** | **27,90** | **16,85** | **10,54** |
| Encaissement | 1,07 | 0,79 | 0,70 | 1,60 | 1,15 | 1,00 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **2,59** | **1,55** | **1,00** | **3,12** | **1,91** | **1,30** |
| Remboursements nets | 6,33 | 2,88 | 1,17 | 10,53 | 4,93 | 2,00 |
| Rétrofacturations | 0,56 | 0,12 | 0,04 | 0,76 | 0,17 | 0,06 |
| **= Provision retours et remboursements** | **6,89** | **3,00** | **1,21** | **11,29** | **5,10** | **2,06** |
| Poids d’expédition retenu (kg) | 0,31 | 0,24 | 0,18 | 0,79 | 0,60 | 0,42 |

**Lecture.**
- **Support seul à 29,90 €** : 10,68 € de marge contributive, −29,20 € après un CPA de 39,88 € (+1,69 € en optimiste). Le coût rendu du support (3,60 €) est faible ; c’est le prix de vente bas qui limite.
- **Kit support + 8 nerfs à 49,90 €** : 17,72 € de marge contributive (+7,04 €), −22,16 € après publicité. Les nerfs ajoutent du chiffre d’affaires mais aussi un coût d’achat élevé (4,90 € les 8, hypothèse faute de prix de gros) et font passer le colis au-dessus de 500 g.
- Écart avec `deep_support_nerf_de_boeuf.md` (13,41 € et 22,07 €) : coût rendu du support recalculé à partir des composants (boîte et logo compris), remboursement du prix compté dans la provision, nerfs épais plus lourds (tranche de 1 kg).
- Vendre des nerfs dans un kit fait entrer la marque dans le palier 1 (revente de nerfs déjà étiquetés d’une marque de l’UE) : à faire confirmer par écrit par la DDPP (`deep_support_nerf_de_boeuf.md` §3.4).

### 2.3 Litière indicatrice de santé, version additif léger (granulés indicateurs)

**Offres comparées** : « Coffret trimestriel (3 doses + nuancier) » (39,90 € TTC) et « Coffret 6 mois (6 doses) » (69,90 € TTC). Stock importé (ou fabriqué) dans l’UE, expédié depuis la France.

*Coût rendu entrepôt des articles* (« Coffret 3 doses » = 3 doses mensuelles + nuancier ; « Coffret 6 doses ») :

| Coût rendu entrepôt (€ HT par unité) | Coffret 3 doses · Prudent | Coffret 3 doses · Intermédiaire | Coffret 3 doses · Optimiste | Coffret 6 doses · Prudent | Coffret 6 doses · Intermédiaire | Coffret 6 doses · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Achat (FOB × 0,86 ou prix livré UE) | 9,00 | 4,50 | 2,40 | 18,00 | 9,00 | 4,80 |
| Commission d’agent | 1,35 | 0,33 | 0,06 | 2,70 | 0,66 | 0,12 |
| Fret international | 4,26 | 1,56 | 0,51 | 8,52 | 3,12 | 1,02 |
| Dédouanement et frais fixes | 0,60 | 0,30 | 0,09 | 1,20 | 0,60 | 0,18 |
| Droits de douane | 0,87 | 0,24 | 0,00 | 1,74 | 0,48 | 0,00 |
| **= Coût rendu entrepôt** | **16,08** | **6,93** | **3,06** | **32,16** | **13,86** | **6,12** |

*Les 8 lignes demandées, trois scénarios :*

| Ligne (€ par commande) | Coffret 3 mois 39,90 € · Prudent | Coffret 3 mois 39,90 € · Intermédiaire | Coffret 3 mois 39,90 € · Optimiste | Coffret 6 mois 69,90 € · Prudent | Coffret 6 mois 69,90 € · Intermédiaire | Coffret 6 mois 69,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 39,90 | 39,90 | 39,90 | 69,90 | 69,90 | 69,90 |
| 2. Chiffre d’affaires HT estimé par commande | 33,25 | 33,25 | 33,25 | 58,25 | 58,25 | 58,25 |
| 3. Coût du produit livré | 29,54 | 13,02 | 7,79 | 46,95 | 21,48 | 10,85 |
| 4. Frais de paiement et de plateforme | 2,86 | 1,73 | 1,15 | 3,65 | 2,26 | 1,60 |
| 5. Provision estimée pour retours et remboursements | 9,53 | 4,24 | 1,71 | 15,99 | 7,37 | 2,99 |
| **6. Marge contributive avant publicité** | **−8,68** | **14,26** | **22,60** | **−8,34** | **27,14** | **42,81** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−103,29** | **−25,62** | **8,55** | **−102,95** | **−12,74** | **28,76** |
| CPA d’équilibre (1re commande) | aucun (marge ≤ 0) | 14,26 | 22,60 | aucun (marge ≤ 0) | 27,14 | 42,81 |
| ROAS d’équilibre (CA TTC ÷ pub) | n.a. (marge ≤ 0) | 2,80 | 1,77 | n.a. (marge ≤ 0) | 2,58 | 1,63 |
| ROAS d’équilibre (CA HT ÷ pub) | n.a. (marge ≤ 0) | 2,33 | 1,47 | n.a. (marge ≤ 0) | 2,15 | 1,36 |
| Marge contributive en % du CA HT | −26 % | 43 % | 68 % | −14 % | 47 % | 73 % |

*Détail des lignes 3 à 5 :*

| Détail (€ HT) | Coffret 3 mois 39,90 € · Prudent | Coffret 3 mois 39,90 € · Intermédiaire | Coffret 3 mois 39,90 € · Optimiste | Coffret 6 mois 69,90 € · Prudent | Coffret 6 mois 69,90 € · Intermédiaire | Coffret 6 mois 69,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 16,08 | 6,93 | 3,06 | 32,16 | 13,86 | 6,12 |
| Préparation et stockage | 5,25 | 1,98 | 1,02 | 5,25 | 1,98 | 1,02 |
| Emballage d’expédition, encart, REP | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 7,41 (≤ 1 kg) | 3,66 (≤ 500 g) | 3,46 (≤ 500 g) | 8,74 (≤ 2 kg) | 5,19 (≤ 1 kg) | 3,46 (≤ 500 g) |
| **= Coût du produit livré** | **29,54** | **13,02** | **7,79** | **46,95** | **21,48** | **10,85** |
| Encaissement | 1,34 | 0,97 | 0,85 | 2,13 | 1,50 | 1,30 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **2,86** | **1,73** | **1,15** | **3,65** | **2,26** | **1,60** |
| Remboursements nets | 8,87 | 4,10 | 1,66 | 15,03 | 7,15 | 2,91 |
| Rétrofacturations | 0,66 | 0,14 | 0,05 | 0,96 | 0,22 | 0,08 |
| **= Provision retours et remboursements** | **9,53** | **4,24** | **1,71** | **15,99** | **7,37** | **2,99** |
| Poids d’expédition retenu (kg) | 0,61 | 0,34 | 0,15 | 1,16 | 0,64 | 0,27 |

**Lecture.**
- **Coffret de 3 mois à 39,90 €** (13,30 € par mois) : 14,26 € de marge contributive, −25,62 € après publicité (+8,55 € en optimiste). **Coffret de 6 mois à 69,90 €** : 27,14 €, −12,74 € après publicité, l’une des deux meilleures premières commandes de l’étude avec le lot de bouchées.
- Le poids est réglé par l’envoi groupé : 3 doses tiennent sous 500 g (3,66 € de port, soit 1,22 € par mois). Mais **le coût des granulés est une hypothèse** (1,50 € la dose) et aucun fournisseur de granulés seuls n’a été trouvé : ces chiffres sont conditionnels.
- En prudent, une dose lourde (184 g) et chère (3 €) fait passer le coffret à 16,08 € rendu et la marge contributive à −8,68 €.

**Version litière en abonnement (pour mémoire, brièvement).** Même méthode ; un sac de 1,8 kg par chat et par mois.

| Ligne (€ par commande) | Mensuelle 19,90 € · Interm., tarif public | Mensuelle 19,90 € · Interm., tarif pro | Bimestrielle 34,90 € · Interm., tarif public | Bimestrielle 34,90 € · Interm., tarif pro | Bimestrielle · Prudent | Bimestrielle · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 19,90 | 19,90 | 34,90 | 34,90 | 34,90 | 34,90 |
| 2. Chiffre d’affaires HT | 16,58 | 16,58 | 29,08 | 29,08 | 29,08 | 29,08 |
| 3. Coût du produit livré | 11,53 | 9,56 | 21,17 | 13,89 | 29,46 | 10,38 |
| dont transport | 6,86 | 4,89 | 13,53 | 6,25 | 13,91 | 6,25 |
| 4. Frais de paiement et de plateforme | 1,38 | 1,38 | 1,64 | 1,64 | 2,72 | 1,07 |
| 5. Provision retours et remboursements | 2,29 | 2,23 | 4,03 | 3,81 | 9,26 | 1,50 |
| 6. Marge contributive avant publicité | 1,38 | 3,41 | 2,24 | 9,74 | −12,36 | 16,13 |
| 7. CPA cible | 39,88 | 39,88 | 39,88 | 39,88 | 94,61 | 14,05 |
| 8. Marge après publicité | −38,50 | −36,47 | −37,64 | −30,14 | −106,97 | 2,08 |

- **La litière en abonnement est écrasée par le transport** : un colis de 2 kg coûte 6,86 € HT au tarif public, soit 41 % du prix HT d’un mois à 19,90 €, et il ne reste que 1,38 € de marge contributive par mois. Même au tarif pro observé (source secondaire non officielle) et en envoi bimestriel, elle plafonne à 9,74 € par envoi, pour un prix de 17,45 € par mois, 1,5 à 3 fois le prix d’un sac en rayon (6,49 à 11,99 €).
- C’est pourquoi le finaliste est évalué dans sa version additif ; le sourcing des granulés reste le verrou.

### 2.4 Bouchées fibres « glandes anales » (modèle Glandex), façonnier UE

**Offres comparées** : « Pot de 60 bouchées » (34,90 € TTC) et « Lot de 2 pots » (64,90 € TTC). Stock importé (ou fabriqué) dans l’UE, expédié depuis la France.

*Coût rendu entrepôt des articles* (« Pot de 60 » = pot de 60 bouchées fabriqué dans l’UE) :

| Coût rendu entrepôt (€ HT par unité) | Pot de 60 · Prudent | Pot de 60 · Intermédiaire | Pot de 60 · Optimiste |
| :--- | ---: | ---: | ---: |
| Achat (FOB × 0,86 ou prix livré UE) | 6,30 | 4,65 | 3,10 |
| **= Coût rendu entrepôt** | **6,30** | **4,65** | **3,10** |

*Les 8 lignes demandées, trois scénarios :*

| Ligne (€ par commande) | Pot 34,90 € · Prudent | Pot 34,90 € · Intermédiaire | Pot 34,90 € · Optimiste | Lot 2 pots 64,90 € · Prudent | Lot 2 pots 64,90 € · Intermédiaire | Lot 2 pots 64,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 34,90 | 34,90 | 34,90 | 64,90 | 64,90 | 64,90 |
| 2. Chiffre d’affaires HT estimé par commande | 29,08 | 29,08 | 29,08 | 54,08 | 54,08 | 54,08 |
| 3. Coût du produit livré | 18,09 | 10,74 | 7,83 | 26,76 | 17,65 | 11,68 |
| 4. Frais de paiement et de plateforme | 2,72 | 1,64 | 1,07 | 3,52 | 2,17 | 1,52 |
| 5. Provision estimée pour retours et remboursements | 8,28 | 3,73 | 1,50 | 14,78 | 6,86 | 2,78 |
| **6. Marge contributive avant publicité** | **−0,01** | **12,97** | **18,68** | **9,02** | **27,40** | **38,10** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−94,62** | **−26,91** | **4,63** | **−85,59** | **−12,48** | **24,05** |
| CPA d’équilibre (1re commande) | aucun (marge ≤ 0) | 12,97 | 18,68 | 9,02 | 27,40 | 38,10 |
| ROAS d’équilibre (CA TTC ÷ pub) | n.a. (marge ≤ 0) | 2,69 | 1,87 | 7,20 | 2,37 | 1,70 |
| ROAS d’équilibre (CA HT ÷ pub) | n.a. (marge ≤ 0) | 2,24 | 1,56 | 6,00 | 1,97 | 1,42 |
| Marge contributive en % du CA HT | 0 % | 45 % | 64 % | 17 % | 51 % | 70 % |

*Détail des lignes 3 à 5 :*

| Détail (€ HT) | Pot 34,90 € · Prudent | Pot 34,90 € · Intermédiaire | Pot 34,90 € · Optimiste | Lot 2 pots 64,90 € · Prudent | Lot 2 pots 64,90 € · Intermédiaire | Lot 2 pots 64,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 6,30 | 4,65 | 3,10 | 12,60 | 9,30 | 6,20 |
| Préparation et stockage | 5,25 | 1,98 | 1,02 | 5,95 | 2,71 | 1,34 |
| Emballage d’expédition, encart, REP | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 5,74 (≤ 500 g) | 3,66 (≤ 500 g) | 3,46 (≤ 500 g) | 7,41 (≤ 1 kg) | 5,19 (≤ 1 kg) | 3,89 (≤ 1 kg) |
| **= Coût du produit livré** | **18,09** | **10,74** | **7,83** | **26,76** | **17,65** | **11,68** |
| Encaissement | 1,20 | 0,88 | 0,77 | 2,00 | 1,41 | 1,22 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **2,72** | **1,64** | **1,07** | **3,52** | **2,17** | **1,52** |
| Remboursements nets | 7,67 | 3,60 | 1,45 | 13,87 | 6,65 | 2,70 |
| Rétrofacturations | 0,61 | 0,13 | 0,05 | 0,91 | 0,21 | 0,08 |
| **= Provision retours et remboursements** | **8,28** | **3,73** | **1,50** | **14,78** | **6,86** | **2,78** |
| Poids d’expédition retenu (kg) | 0,38 | 0,34 | 0,31 | 0,70 | 0,64 | 0,59 |

**Lecture.**
- **Pot de 60 à 34,90 €** : 12,97 € de marge contributive, −26,91 € après publicité (+4,63 € en optimiste). **Lot de 2 pots à 64,90 €** : 27,40 €, −12,48 € après publicité.
- Le produit rendu ne pèse que 16 % du HT (4,65 €, sans droits ni agent puisqu’il est fabriqué dans l’UE) ; mais ce coût est une hypothèse, aucun façonnier n’ayant publié de prix.
- Pour un consommable ouvert, rien n’est récupérable en cas de remboursement : la provision atteint 3,73 € à 12 %. Une garantie « satisfait ou remboursé », utile vu le délai d’effet de 3 à 5 semaines, se paie ici.
- Le pot de 60 dure 2 mois pour un chien de moins de 10 kg (1 bouchée par jour et par 10 kg, Treatsy), mais 15 à 20 jours pour un chien de 30 à 40 kg : le produit est économiquement adapté aux petites races, pas à la clientèle Pilou de grands chiens.

### 2.5 Boîte-puzzle à friandises pour chat (modèle Cat Amazing), livrée à plat

**Offres comparées** : « Boîte-labyrinthe seule » (39,90 € TTC) et « Boîte + 3 inserts » (49,90 € TTC). Stock importé (ou fabriqué) dans l’UE, expédié depuis la France.

*Coût rendu entrepôt des articles* (« Boîte » = boîte-labyrinthe imprimée livrée à plat ; « 3 inserts » = pack de 3 inserts de rechange) :

| Coût rendu entrepôt (€ HT par unité) | Boîte · Prudent | Boîte · Intermédiaire | Boîte · Optimiste | 3 inserts · Prudent | 3 inserts · Intermédiaire | 3 inserts · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Achat (FOB × 0,86 ou prix livré UE) | 6,24 | 4,50 | 2,58 | 4,50 | 3,00 | 2,10 |
| Commission d’agent | 0,94 | 0,34 | 0,08 | 0,00 | 0,00 | 0,00 |
| Fret international | 3,05 | 0,41 | 0,20 | 0,00 | 0,00 | 0,00 |
| Dédouanement et frais fixes | 0,60 | 0,30 | 0,10 | 0,00 | 0,00 | 0,00 |
| Droits de douane | 0,60 | 0,20 | 0,00 | 0,00 | 0,00 | 0,00 |
| **= Coût rendu entrepôt** | **11,43** | **5,75** | **2,96** | **4,50** | **3,00** | **2,10** |

*Les 8 lignes demandées, trois scénarios :*

| Ligne (€ par commande) | Boîte 39,90 € · Prudent | Boîte 39,90 € · Intermédiaire | Boîte 39,90 € · Optimiste | Boîte + 3 inserts 49,90 € · Prudent | Boîte + 3 inserts 49,90 € · Intermédiaire | Boîte + 3 inserts 49,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1. Prix de vente TTC | 39,90 | 39,90 | 39,90 | 49,90 | 49,90 | 49,90 |
| 2. Chiffre d’affaires HT estimé par commande | 33,25 | 33,25 | 33,25 | 41,58 | 41,58 | 41,58 |
| 3. Coût du produit livré | 26,22 | 13,44 | 8,13 | 31,42 | 17,17 | 10,55 |
| 4. Frais de paiement et de plateforme | 2,86 | 1,73 | 1,15 | 3,12 | 1,91 | 1,30 |
| 5. Provision estimée pour retours et remboursements | 9,00 | 3,94 | 1,61 | 10,83 | 4,79 | 1,96 |
| **6. Marge contributive avant publicité** | **−4,83** | **14,14** | **22,36** | **−3,79** | **17,71** | **27,77** |
| 7. Coût d’acquisition client cible (CPA) | 94,61 | 39,88 | 14,05 | 94,61 | 39,88 | 14,05 |
| **8. Marge estimée après publicité (1re commande)** | **−99,44** | **−25,74** | **8,31** | **−98,40** | **−22,17** | **13,72** |
| CPA d’équilibre (1re commande) | aucun (marge ≤ 0) | 14,14 | 22,36 | aucun (marge ≤ 0) | 17,71 | 27,77 |
| ROAS d’équilibre (CA TTC ÷ pub) | n.a. (marge ≤ 0) | 2,82 | 1,78 | n.a. (marge ≤ 0) | 2,82 | 1,80 |
| ROAS d’équilibre (CA HT ÷ pub) | n.a. (marge ≤ 0) | 2,35 | 1,49 | n.a. (marge ≤ 0) | 2,35 | 1,50 |
| Marge contributive en % du CA HT | −15 % | 43 % | 67 % | −9 % | 43 % | 67 % |

*Détail des lignes 3 à 5 :*

| Détail (€ HT) | Boîte 39,90 € · Prudent | Boîte 39,90 € · Intermédiaire | Boîte 39,90 € · Optimiste | Boîte + 3 inserts 49,90 € · Prudent | Boîte + 3 inserts 49,90 € · Intermédiaire | Boîte + 3 inserts 49,90 € · Optimiste |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| Article(s) rendu(s) entrepôt | 11,43 | 5,75 | 2,96 | 15,93 | 8,75 | 5,06 |
| Préparation et stockage | 5,25 | 2,05 | 1,03 | 5,95 | 2,78 | 1,35 |
| Emballage d’expédition, encart, REP | 0,80 | 0,45 | 0,25 | 0,80 | 0,45 | 0,25 |
| Transport jusqu’au client | 8,74 (≤ 2 kg) | 5,19 (≤ 1 kg) | 3,89 (≤ 1 kg) | 8,74 (≤ 2 kg) | 5,19 (≤ 1 kg) | 3,89 (≤ 1 kg) |
| **= Coût du produit livré** | **26,22** | **13,44** | **8,13** | **31,42** | **17,17** | **10,55** |
| Encaissement | 1,34 | 0,97 | 0,85 | 1,60 | 1,15 | 1,00 |
| Shopify et applications | 1,52 | 0,76 | 0,30 | 1,52 | 0,76 | 0,30 |
| **= Frais de paiement et de plateforme** | **2,86** | **1,73** | **1,15** | **3,12** | **1,91** | **1,30** |
| Remboursements nets | 8,34 | 3,80 | 1,56 | 10,07 | 4,62 | 1,90 |
| Rétrofacturations | 0,66 | 0,14 | 0,05 | 0,76 | 0,17 | 0,06 |
| **= Provision retours et remboursements** | **9,00** | **3,94** | **1,61** | **10,83** | **4,79** | **1,96** |
| Poids d’expédition retenu (kg) | 1,57 | 0,74 | 0,63 | 1,57 | 0,89 | 0,75 |

**Lecture.**
- **Boîte seule à 39,90 €** : 14,14 € de marge contributive, −25,74 € après publicité (+8,31 € en optimiste). **Boîte + 3 inserts à 49,90 €** : 17,71 €, −22,17 €.
- Le volume pèse : stockage 1,31 fois plus cher qu’un petit article, et en prudent le poids volumétrique (1,58 kg) fait passer le colis en tranche de 2 kg (8,74 €) et le fret ferroviaire à 3,05 € par boîte.
- Écart avec `deep_boite_puzzle_chat.md` (16,27 € et 20,97 €) : même méthode de provision que pour les autres produits (prix remboursé compté).

### 2.6 Sensibilité au taux de retours et remboursements (coûts intermédiaires, offres principales)

| Offre | Marge contributive à 5 % | à 12 % (référence) | à 24 % | Écart 24 % − 12 % |
| :--- | ---: | ---: | ---: | ---: |
| Jouet à lécher congelable — Kit L 29,90 € | 11,93 | 10,26 | 7,40 | −2,86 |
| Support de nerf de bœuf — Support 29,90 € | 12,36 | 10,68 | 7,79 | −2,89 |
| Litière indicatrice de santé, version additif léger — Coffret 3 mois 39,90 € | 16,65 | 14,26 | 10,16 | −4,10 |
| Bouchées fibres « glandes anales » — Pot 34,90 € | 15,07 | 12,97 | 9,37 | −3,60 |
| Boîte-puzzle à friandises pour chat — Boîte 39,90 € | 16,36 | 14,14 | 10,34 | −3,80 |

Passer de 12 % à 24 % de remboursements coûte 2,86 € à 4,10 € par commande, soit 27 % à 29 % de la marge contributive ; descendre de 12 % à 5 % en rapporte 1,67 € à 2,39 €. Le remboursement est le deuxième levier après le CPA ; il se pilote par la qualité (solidité, fermeture, appétence), une notice claire et la règle du port retour à la charge du client en cas de rétractation.

### 2.7 Variante : micro-entreprise en franchise en base de TVA (coûts intermédiaires)

Si la nouvelle marque était portée par une micro-entreprise en franchise, elle ne collecterait pas de TVA (le prix affiché devient entièrement son chiffre d’affaires) mais ne déduirait rien : tous les achats soumis à TVA coûtent 20 % de plus, y compris la publicité Meta et Shopify (TVA autoliquidée non déductible, [CP] de `fr_costs_regulation.md`). Les commissions de paiement, exonérées, ne changent pas. Les seuils de la franchise ne sont pas vérifiés ; à valider avec un expert-comptable.

| Offre | Assujetti : marge contributive | Assujetti : après CPA 39,88 | Franchise : marge contributive | Franchise : CPA TTC | Franchise : après publicité |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Kit L 29,90 € | 10,26 | −29,62 | 12,49 | 47,86 | −35,37 |
| Duo 49,90 € | 18,41 | −21,47 | 22,36 | 47,86 | −25,50 |
| Support 29,90 € | 10,68 | −29,20 | 12,99 | 47,86 | −34,87 |
| Kit + 8 nerfs 49,90 € | 17,72 | −22,16 | 21,53 | 47,86 | −26,33 |
| Coffret 3 mois 39,90 € | 14,26 | −25,62 | 17,33 | 47,86 | −30,53 |
| Coffret 6 mois 69,90 € | 27,14 | −12,74 | 32,93 | 47,86 | −14,93 |
| Pot 34,90 € | 12,97 | −26,91 | 15,77 | 47,86 | −32,09 |
| Lot 2 pots 64,90 € | 27,40 | −12,48 | 33,22 | 47,86 | −14,64 |
| Boîte 39,90 € | 14,14 | −25,74 | 17,19 | 47,86 | −30,67 |
| Boîte + 3 inserts 49,90 € | 17,71 | −22,17 | 21,53 | 47,86 | −26,33 |

La franchise améliore la marge avant publicité (pas de TVA reversée sur le prix) mais renchérit le CPA de 20 % : **après publicité, chaque première commande perd 2,16 € à 5,75 € de plus**. Pour une marque financée par la publicité, le régime réel est plus favorable.

## 3. Vue par client : réachats sur 6 et 12 mois et récupération du coût d’acquisition

### 3.1 Hypothèses de réachat (toutes des HYPOTHÈSES, faute de donnée de rétention propre à ces produits)

Modèle : le client est acquis au mois 0 (première commande, CPA payé). Une part **p2** des clients passe au moins une commande de réachat ; pour les consommables, les abonnés restent ensuite d’un cycle à l’autre avec une attrition mensuelle **c** (H32) ; pour les produits durables, une seconde commande de réachat a lieu chez 30 % des réacheteurs. Chaque commande de réachat rapporte la marge contributive de l’offre de réachat (remise de 10 % et coût de relance déduits, mêmes paramètres de coûts que la première commande). On calcule l’**espérance** par client acquis :

`Cumul(T) = (M1 − CPA) + Σ (commandes de réachat passées avant le mois T) probabilité × Mr`, avec, pour un consommable de cycle k mois, une probabilité de p2 × (1 − c)^(n × k) pour la (n + 1)-ième recharge.

Les fenêtres « 6 mois » et « 12 mois » comptent les commandes passées aux mois 0 à 5 et 0 à 11.

| Produit | Commande de réachat (TTC) | Marge contributive du réachat P / I / O (€) | p2 : part des clients qui réachètent P / I / O | Rythme | Attrition mensuelle P / I / O | Fondement |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Jouet à lécher congelable | 1 kit L à −10 % (26,91 €) | −8,25 / 7,13 / 12,32 | 8 % / 15 % / 25 % | mois 4, puis mois 10 (30 % des réacheteurs) | — | Produit durable sans aliment au lancement (palier 0) : réachat = 2e kit (rotation, 2e chien, cadeau, remplacement après usure). Sous le repère de ≈ 28 % tous e-commerces, faute de consommable. |
| Support de nerf de bœuf | recharge 12 nerfs à −10 % (26,91 €) | −14,49 / 2,05 / 10,24 | 10 % / 20 % / 30 % | tous les 2 mois dès le mois 2 | 10,0 % / 7,1 % / 5,0 % | Recharge de nerfs (consommable) : repère consommables 30–40 %, mais le support fonctionne avec n’importe quel nerf vendu partout (Maxi Zoo, Zoomalia, Amazon.fr) : forte substitution. |
| Litière indicatrice de santé, version additif léger | coffret trimestriel à −10 % (35,91 €) | −13,06 / 10,41 / 18,99 | 30 % / 40 % / 50 % | tous les 3 mois dès le mois 3 | 10,0 % / 7,1 % / 5,0 % | Consommable en abonnement : repère consommables et animaux 30–45 % ; attrition 7,1 %/mois (Recharge). Risque propre : « rien ne change de couleur » = impression d’inutilité. |
| Bouchées fibres « glandes anales » | 1 pot en abonnement à −10 % (31,41 €) | −4,08 / 9,49 / 15,47 | 30 % / 40 % / 50 % | tous les 2 mois dès le mois 2 | 10,0 % / 7,1 % / 5,0 % | Consommable : repère 30–45 % ; petit chien = 1 pot tous les 2 mois. Risque propre : arrêt quand le problème disparaît, ou effet non perçu (3 à 5 semaines). |
| Boîte-puzzle à friandises pour chat | pack de 3 inserts (19,90 €) | −8,90 / 3,10 / 7,61 | 5 % / 10 % / 20 % | mois 3, puis mois 8 (30 % des réacheteurs) | — | Inserts optionnels ; Cat Amazing ne vend pas de recharges ; lassitude du chat signalée dans les avis : réachat faible. |

Repères sourcés (recherches du 28/10) : ≈ 28 % des clients e-commerce passent une 2e commande sous 12 mois ([Mobiloud](https://www.mobiloud.com/blog/repeat-customer-rate-ecommerce)) ; consommables et animaux 30 à 45 % ([Eightx](https://eightx.co/blog/average-repeat-purchase-rate-by-vertical), [Foundry CRO](https://foundrycro.com/blog/dtc-pet-marketing-benchmarks-2026/)) ; attrition des abonnés 5 à 8 %/mois, 7,1 % pour le panel Recharge ([Eightx](https://www.eightx.co/blog/average-subscription-churn-rate-by-category)). Ce sont des moyennes de marques établies, souvent américaines : pour une marque nouvelle acquise sur Meta, la réalité sera plutôt dans la moitié basse.

### 3.2 Résultats par client acquis (offre principale en première commande)

| Produit | Scénario | Marge 1re commande | CPA | Solde après 1re commande | Réachats espérés sur 6 mois | Cumul par client à 6 mois | Réachats espérés sur 12 mois | Cumul par client à 12 mois | Récupération du CPA | CPA maximal récupéré en 12 mois |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Jouet à lécher congelable | Prudent | −4,46 | 94,61 | −99,07 | 0,08 | −99,73 | 0,10 | −99,93 | > 36 mois | aucun (marge ≤ 0) |
|  | Intermédiaire | 10,26 | 39,88 | −29,62 | 0,15 | −28,55 | 0,20 | −28,23 | > 36 mois | 11,65 |
|  | Optimiste | 15,13 | 14,05 | 1,08 | 0,25 | 4,16 | 0,33 | 5,08 | dès la 1re commande | 19,13 |
| Support de nerf de bœuf | Prudent | −1,94 | 94,61 | −96,55 | 0,18 | −99,17 | 0,34 | −101,52 | > 36 mois | aucun (marge ≤ 0) |
|  | Intermédiaire | 10,68 | 39,88 | −29,20 | 0,37 | −28,44 | 0,76 | −27,64 | > 36 mois | 12,24 |
|  | Optimiste | 15,74 | 14,05 | 1,69 | 0,57 | 7,53 | 1,23 | 14,33 | dès la 1re commande | 28,38 |
| Litière indicatrice de santé, version additif léger | Prudent | −8,68 | 94,61 | −103,29 | 0,30 | −107,21 | 0,68 | −112,15 | > 36 mois | aucun (marge ≤ 0) |
|  | Intermédiaire | 14,26 | 39,88 | −25,62 | 0,40 | −21,46 | 0,98 | −15,44 | > 36 mois | 24,44 |
|  | Optimiste | 22,60 | 14,05 | 8,55 | 0,50 | 18,05 | 1,30 | 33,17 | dès la 1re commande | 47,22 |
| Bouchées fibres « glandes anales » | Prudent | −0,01 | 94,61 | −94,62 | 0,54 | −96,84 | 1,03 | −98,82 | > 36 mois | aucun (marge ≤ 0) |
|  | Intermédiaire | 12,97 | 39,88 | −26,91 | 0,75 | −19,84 | 1,52 | −12,46 | > 36 mois | 27,42 |
|  | Optimiste | 18,68 | 14,05 | 4,63 | 0,95 | 19,35 | 2,06 | 36,46 | dès la 1re commande | 50,51 |
| Boîte-puzzle à friandises pour chat | Prudent | −4,83 | 94,61 | −99,44 | 0,05 | −99,88 | 0,07 | −100,02 | > 36 mois | aucun (marge ≤ 0) |
|  | Intermédiaire | 14,14 | 39,88 | −25,74 | 0,10 | −25,43 | 0,13 | −25,34 | > 36 mois | 14,54 |
|  | Optimiste | 22,36 | 14,05 | 8,31 | 0,20 | 9,83 | 0,26 | 10,29 | dès la 1re commande | 24,34 |

« Cumul » = marge de la 1re commande − CPA + marges espérées des réachats. « Récupération du CPA » = mois de la commande après laquelle le cumul espéré devient positif (horizon 36 mois). « CPA maximal récupéré en 12 mois » = CPA que la marge de 12 mois peut payer.

### 3.3 Variante : première commande en lot

| Produit et lot en 1re commande | Cumul à 6 mois P / I / O | Cumul à 12 mois P / I / O | Récupération du CPA P / I / O | CPA maximal récupéré en 12 mois (I) |
| :--- | ---: | ---: | ---: | ---: |
| Jouet à lécher congelable — Duo 49,90 € | −95,89 / −20,40 / 16,15 | −96,09 / −20,08 / 17,07 | > 36 mois / > 36 mois / dès la 1re commande | 19,80 |
| Support de nerf de bœuf — Kit + 8 nerfs 49,90 € | −97,96 / −21,40 / 19,47 | −100,31 / −20,60 / 26,27 | > 36 mois / > 36 mois / dès la 1re commande | 19,28 |
| Litière indicatrice de santé, version additif léger — Coffret 6 mois 69,90 € (réachats décalés : 1er au mois 6) | −102,95 / −12,74 / 28,76 | −109,72 / −5,24 / 46,40 | > 36 mois / mois 18 / dès la 1re commande | 34,64 |
| Bouchées fibres « glandes anales » — Lot 2 pots 64,90 € (réachats décalés : 1er au mois 4) | −86,81 / −8,68 / 31,79 | −89,26 / −0,14 / 50,75 | > 36 mois / mois 12 / dès la 1re commande | 39,74 |
| Boîte-puzzle à friandises pour chat — Boîte + 3 inserts 49,90 € | −98,85 / −21,86 / 15,24 | −98,98 / −21,77 / 15,70 | > 36 mois / > 36 mois / dès la 1re commande | 18,11 |

Pour le lot de bouchées, le cumul des mois 0 à 11 reste juste négatif (−0,14 €) ; c’est la recharge espérée du mois 12 qui le fait passer au-dessus de zéro.

### 3.4 Seuils : quel réachat faudrait-il pour récupérer un CPA de 39,88 € en 12 mois ?

| Produit (coûts intermédiaires) | p2 nécessaire, offre principale en 1re commande | p2 nécessaire, lot en 1re commande | p2 supposé | Cumul à 12 mois d’un client fidèle (p2 = 100 %, sans attrition) | Réachats de ce client fidèle en 12 mois |
| :--- | ---: | ---: | ---: | ---: | ---: |
| Jouet à lécher congelable | 320 % (impossible) | 232 % (impossible) | 15 % | −15,36 | 2 |
| Support de nerf de bœuf | 374 % (impossible) | 284 % (impossible) | 20 % | −18,95 | 5 |
| Litière indicatrice de santé, version additif léger | 101 % (impossible) | 68 % | 40 % | 5,61 | 3 |
| Bouchées fibres « glandes anales » | 75 % | 40 % | 40 % | 20,54 | 5 |
| Boîte-puzzle à friandises pour chat | 639 % (impossible) | 550 % (impossible) | 10 % | −19,54 | 2 |

**Lecture.**
- **Au CPA intermédiaire, aucun finaliste ne récupère son coût d’acquisition en 12 mois avec l’offre simple.** Les cumuls à 12 mois vont de −28,23 € à −12,46 € par client acquis.
- **Les consommables vendus en lot sont les seuls à s’en approcher** : lot de 2 pots de bouchées, −0,14 € à 12 mois et récupération au mois 12 ; coffret de 6 mois d’additif, −5,24 € à 12 mois, récupération au mois 18. Ils supposent 40 % de clients qui se réabonnent, ce qui est le haut des repères pour une marque nouvelle.
- **Les produits durables (jouet, support, boîte chat) ne vivent que de la première commande** : même un client fidèle à 100 % ne les rentabilise pas en 12 mois au CPA central (2 réachats pour le jouet, cumul −15,36 € ; 2 pour la boîte, −19,54 € ; 5 recharges de nerfs à 2,05 € de marge pour le support, −18,95 €). Pour le jouet, la part de réacheteurs nécessaire dépasserait 100 % (320 %) : sa rentabilité dépend entièrement d’un CPA bas (≤ 11,65 € pour le kit L, ≤ 19,80 € si le client prend le duo).
- **En optimiste, tous les finalistes récupèrent le CPA dès la première commande** (CPA de 14,05 €) ; en prudent, aucun ne le récupère, même en 36 mois.
- Les recharges alimentaires du jouet (paliers 1 et 2 de `sourcing_jouet_lechage.md`) ne sont pas modélisées, faute de coût et de MOQ chez les façonniers. Ordre de grandeur : pour combler l’écart restant du kit L à 12 mois (28,23 €) avec des recharges rapportant 5 à 8 € de marge, il faudrait 3,5 à 5,6 recharges par client acquis en 12 mois, au-dessus de tous les repères de réachat.

## 4. Jouet à lécher : prix à tester, structures d’offre, stock ou dropshipping, moule XL

### 4.1 Prix à tester pour le kit L (24,90 / 29,90 / 34,90 €)

| Prix TTC | CA HT | Marge contributive P / I / O | CPA d’équilibre (I) | ROAS d’équilibre TTC (I) | Conversion d’équilibre (CPM 13 €, CTR 1,63 %) | Marge après CPA 14,05 (coûts I) | après CPA 39,88 | après CPA 94,61 | Conversion nécessaire par rapport à 29,90 € pour gagner autant par euro de publicité |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 24,90 € | 20,75 | −7,45 / 6,69 / 11,25 | 6,69 | 3,72 | 11,9 % | −7,36 | −33,19 | −87,92 | +53 % |
| 29,90 € | 24,92 | −4,46 / 10,26 / 15,13 | 10,26 | 2,91 | 7,8 % | −3,79 | −29,62 | −84,35 | référence |
| 34,90 € | 29,08 | −1,48 / 13,82 / 19,01 | 13,82 | 2,53 | 5,8 % | −0,23 | −26,06 | −80,79 | −26 % |

**Lecture.**
- Chaque palier de 5 € ajoute 3,56 € de marge contributive (le prix supplémentaire moins la TVA, l’encaissement et la provision de remboursement).
- **À 24,90 €, il faudrait convertir 53 % de mieux qu’à 29,90 € pour gagner autant par euro de publicité.** À 34,90 €, une baisse de conversion jusqu’à 26 % reste neutre. À trafic égal, 34,90 € est donc l’option la plus rentable si la conversion ne chute pas de plus d’un quart ; 24,90 € ne se justifie que comme prix d’appel avec un lot en montée en gamme.
- **Repères de prix** : 34,90 € dépasse toutes les balles concurrentes vendues seules en France (Freezball XL 29,90 €, SmoothieDog 29,90 à 35 €, Toppl XL ≈ 31,70 € sur [Amazon.fr](https://www.amazon.fr/WEST-PAW-Zogoflex-Distributeur-friandises/dp/B09VJ1JPRT)) ; 24,90 € est au niveau de la Pupsicle d’origine (19,90 à 26,90 €). `verification_jouet_lechage.md` recommande de rester entre 24,90 et 29,90 € pour un jouet avec moule, ou de justifier 34,90 € par une valeur perçue nette (XL testée, fermeture qui ne grippe pas, garantie).
- **Aucun des trois prix n’équilibre un CPA de 39,88 €** : la conversion d’équilibre (5,8 % à 11,9 %) vaut 2,9 à 6,0 fois la conversion de référence de 2 %. Même au CPA optimiste de 14,05 €, avec des coûts intermédiaires, seul 34,90 € approche l’équilibre (−0,23 €). Le test de prix sert donc à mesurer la conversion relative et à orienter vers le lot, pas à trouver un prix qui rendrait l’offre simple rentable.
- Protocole suggéré : deux ensembles de publicités identiques (même créa, même audience) vers deux pages à 29,90 € et 34,90 €, 40 à 50 achats par page si possible (§5.2). Ne pas présenter 24,90 € comme une promotion sur un prix barré fictif : le prix de référence d’une réduction est le plus bas des 30 derniers jours (art. L. 112-1-1 du Code de la consommation, `fr_costs_regulation.md`).

### 4.2 Structures d’offre

| Offre | Prix TTC | Poids d’expédition (I) | Coût du produit livré (I) | Marge contributive P / I / O | CPA d’équilibre (I) | ROAS d’équilibre TTC (I) | Marge après pub (coûts I, CPA 39,88) | Marge après pub (coûts I, CPA 14,05) | Marge après pub (scénario O) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Kit simple | 29,90 € | 0,48 kg (≤ 500 g) | 10,13 | −4,46 / 10,26 / 15,13 | 10,26 | 2,91 | −29,62 | −3,79 | 1,08 |
| Duo (rotation : une balle au congélateur, une en service ; ou 2 chiens) | 49,90 € | 0,92 kg (≤ 1 kg) | 16,43 | −0,62 / 18,41 / 27,12 | 18,41 | 2,71 | −21,47 | 4,36 | 13,07 |
| Kit complet (2 moules, tapis de léchage, livret) | 39,90 € | 0,75 kg (≤ 1 kg) | 16,69 | −4,29 / 11,09 / 18,18 | 11,09 | 3,60 | −28,79 | −2,96 | 4,13 |
| Kit + support nerf de bœuf (vente croisée) | 44,90 € | 0,68 kg (≤ 1 kg) | 15,99 | −1,47 / 15,26 / 23,86 | 15,26 | 2,94 | −24,62 | 1,21 | 9,81 |
| Kit XL, moule propriétaire amorti sur 1 000 kits | 34,90 € | 0,81 kg (≤ 1 kg) | 18,58 | −15,70 / 5,74 / 16,53 | 5,74 | 6,08 | −34,14 | −8,31 | 2,48 |

**Lecture.**
- **Le duo est la meilleure structure** : +8,15 € de marge contributive par rapport au kit simple pour +20 € de prix, parce que le port (1 kg au lieu de 500 g : +1,53 €) et la préparation (+0,73 €) augmentent peu. Son CPA d’équilibre (18,41 €) reste la moitié du CPA central ; avec la vente croisée, ce sont les deux seules structures positives au CPA de 14,05 € quand les coûts sont intermédiaires (+4,36 € et +1,21 €).
- **Le kit complet à 39,90 € est décevant** (11,09 €) : le tapis de léchage coûte ≈ 3,80 $ et fait passer le colis à 1 kg ; il ajoute 10 € de prix mais seulement 0,83 € de marge. À ne garder que si le tapis est un cadeau d’appel pour les fêtes, ou s’il est remplacé par un 2e moule (plus léger).
- **La vente croisée avec le support** (15,26 € à 44,90 €) fait mieux que le kit complet mais moins bien que le duo : le support est un 2e article à préparer et une 2e référence à stocker. Elle a un intérêt d’image (« mastication sécurisée ») et prépare l’abonnement aux nerfs.
- **Le kit XL à 34,90 €** ne dégage que 5,74 € avec l’outillage amorti sur 1 000 kits ; voir §4.4.
- Panier conseillé pour la page : kit simple en prix d’ancrage, duo mis en avant (« le plus choisi »), XL en option pour les chiens de plus de 34 kg dès qu’il existe.

### 4.3 Stock importé dans l’UE ou dropshipping depuis la Chine (règles douanières 2026)

Depuis le 01/07/2026, un envoi direct de Chine à un particulier paie **3 € par ligne tarifaire** (règlement (UE) 2026/382) et, à partir du 01/11/2026, **2 € de frais de traitement par article** (règlement délégué (UE) 2026/2152). Un kit balle (4016) + moule (3924) compte 2 lignes, sauf si la douane le classe comme un assortiment unique (règle générale 3 b), à confirmer par un RTC : d’où 10 € en intermédiaire et prudent, 5 € en optimiste. Un stock importé en B2B ne paie que les droits ad valorem (≈ 0,1 à 0,3 € par kit).

| Kit L à 29,90 € (coûts intermédiaires) | Stock UE, réassort maritime | Stock UE, lot aérien | Dropshipping Chine | Remarques |
| :--- | ---: | ---: | ---: | :--- |
| Achat + commission d’agent | 3,52 | 3,52 | 4,16 | Petits MOQ en dropshipping (balle 3,09 $ au lieu de 1,91 $ + logo), boîte générique |
| Fret international / ligne d’expédition | 0,10 | 2,27 | 6,50 | Groupage 60 $/m³ ; aérien DDP 6 $/kg × 0,44 kg ; ligne Chine-France 6,50 € (HYPOTHÈSE P29) |
| Frais fixes, droits ad valorem | 0,42 | 0,20 | 0,00 | Aérien DDP : dédouanement inclus, droits ajoutés par prudence |
| Droit forfaitaire 3 € + frais de traitement 2 € | 0,00 | 0,00 | 10,00 | 2 lignes × 3 € + 2 articles × 2 € |
| Préparation et stockage | 1,98 | 1,98 | 1,00 | Dropshipping : préparation par l’agent (HYPOTHÈSE 1 €) |
| Emballage, encart, REP | 0,45 | 0,45 | 0,10 | La REP s’applique aussi aux colis envoyés de Chine |
| Transport France | 3,66 | 3,66 | 0,00 | Inclus dans la ligne en dropshipping |
| **= Coût du produit livré** | **10,13** | **12,08** | **21,76** |  |
| Frais de paiement et de plateforme | 1,55 | 1,55 | 1,55 |  |
| Provision retours et remboursements | 2,98 | 2,86 | 3,21 | Dropshipping : aucun retour en Chine, rétrofacturations 0,5 % (colis « non reçus ») |
| **= Marge contributive avant publicité (I)** | **10,26** | **8,43** | **−1,60** |  |
| Marge contributive prudent / optimiste | −4,46 / 15,13 | −7,15 / 13,56 | −9,46 / 9,31 | Dropshipping optimiste : kit classé sur une seule ligne (5 €) |
| Marge après CPA 39,88 (I) | −29,62 | −31,45 | −41,48 |  |
| Délai de livraison au client | 2 à 5 jours | 2 à 5 jours | 6 à 14 jours (CJPacket) |  |

**Lecture.**
- **Le dropshipping n’est plus viable à ce prix** : il perd 1,60 € par commande avant toute publicité en intermédiaire ; les 10 € de droit forfaitaire et de frais de traitement représentent à eux seuls 40 % du prix HT. Même en optimiste (kit sur une seule ligne), il ne laisse que 9,31 €, contre 15,13 € en stock. S’y ajoutent un délai de 6 à 14 jours, l’absence de boîte de marque et un risque de litiges « non reçu ».
- **Un lot en aérien coûte 1,95 € de plus par kit qu’un lot maritime** (8,43 € de marge au lieu de 10,26 €) ; sur 1 000 kits, ≈ 1 950 €. D’après le calendrier de `sourcing_jouet_lechage.md` §3, un produit de catalogue arrive entre mi-janvier et mi-mars 2027 en aérien, entre fin janvier et fin avril 2027 en maritime : les deux tiennent avant l’été. L’aérien n’est qu’une assurance contre les retards (Nouvel An chinois le 6 février 2027) ; le budget central du §5 retient donc le maritime.
- Conclusion conforme à `verification_jouet_lechage.md` §5 : **stock en France ou dans l’UE obligatoire**.

### 4.4 Effet d’un moule XL sur mesure sur le coût unitaire

Aucune balle de catalogue ne dépasse 8 cm ; une vraie XL (≈ 12 cm, chiens de plus de 34 kg, cœur de la clientèle Pilou) demande un moule propriétaire. Outillage : 1 à 3 jeux de moules de compression à 500–3 500 $ (HYPOTHÈSE du nombre de jeux : corps et pièce de fermeture). Le moule d’injection d’un insert rigide (fermeture baïonnette) n’est pas chiffré dans les notes.

| Série amortissant l’outillage | Prudent : amortissement / coût rendu / marge à 34,90 € | Intermédiaire : amortissement / coût rendu / marge à 34,90 € | Optimiste : amortissement / coût rendu / marge à 34,90 € | Marge à 39,90 € (I) |
| :--- | ---: | ---: | ---: | ---: |
| 500 kits | 18,06 / 30,44 / −24,19 | 6,88 / 14,40 / 2,51 | 0,86 / 5,42 / 16,12 | 6,08 |
| 1 000 kits | 9,03 / 21,41 / −15,70 | 3,44 / 10,96 / 5,74 | 0,43 / 4,99 / 16,53 | 9,31 |
| 3 000 kits | 3,01 / 15,39 / −10,04 | 1,15 / 8,67 / 7,89 | 0,14 / 4,70 / 16,81 | 11,46 |

**Lecture.**
- Hors outillage, un kit XL revient à 7,52 € rendu en intermédiaire, contre 4,04 € pour le kit L ; il passe aussi en tranche de 1 kg (+1,53 € de port). L’outillage intermédiaire (4 000 $, ≈ 3 440 €) ajoute 3,44 € par kit sur 1 000 unités, 1,15 € sur 3 000.
- **À 34,90 €, le kit XL rapporte moins que le kit L à 29,90 €** (5,74 € contre 10,26 € sur 1 000 kits). Il faut **39,90 €** pour retrouver une marge comparable (9,31 €), ce qui place la XL au-dessus de la Freezball XL (29,90 €) : la solidité prouvée sur gros mâcheurs doit justifier l’écart.
- Le moule sur mesure est un investissement de différenciation, pas d’économie : à engager seulement après un test concluant sur le kit L (§5), et en négociant par écrit la propriété du moule (« Mold ownership: 100% yours », Wedogy).

## 5. Budget minimal d’un test sérieux

Le budget est une **sortie de trésorerie** : stock, création, conformité, contenus, outils et publicité. Une partie revient par les ventes du test (marge contributive des commandes) et le stock non vendu reste un actif, sous réserve de l’interdiction de détruire les invendus (loi AGEC).

### 5.1 Jouet à lécher : budget détaillé

Trois niveaux : **bas** = test de demande sur 200 kits génériques améliorés (pas de différenciation) ; **central** = test sérieux sur 1 000 kits L de marque ; **haut** = test sérieux + développement de la XL propriétaire. Délai de l’échantillon au stock en France (`sourcing_jouet_lechage.md` §3) : 10,5 à 19,5 semaines en aérien, 12 à 26 en maritime pour un produit de catalogue ; 14,5 à 42 semaines avec un moule propriétaire.

| Poste (€ HT) | Bas | Central | Haut | Statut | Détail et source |
| :--- | ---: | ---: | ---: | :--- | :--- |
| Échantillons (balles, moules, tapis) | 174 | 670 | 1 228 | SOURCÉ (prix) + HYPOTHÈSE (port) | 4 / 8 / 11 fournisseurs × (échantillon 10 / 45 / 60 $ + envoi express 35 / 45 / 60 €). Prix : 2 $ sur une annonce ([Alibaba](https://www.alibaba.com/product-detail/OEM-Interactive-Pet-Toy-Manufacturer-Magic_1601178337444.html)), 30–60 $ par design remboursables (Wedogy, [wedogy.com](https://wedogy.com/dog-toys/)). Port express non sourcé. |
| Premier stock au MOQ | 1 784 | 4 340 | 14 990 | CALCUL sur SOURCÉ + HYPOTHÈSE | Bas : 200 kits « test » à petits MOQ (balle 3,80 $ dès 100, Newtop, [Made-in-China](https://www.made-in-china.com/manufacturers/dog-treat-food-toy.html) ; moule 1,36 $ dès 200 ; boîte générique + autocollant), aérien, 8,17 € le kit + 150 € de dossier (HYPOTHÈSE). Central : 1 000 kits L au MOQ catalogue (balle MOQ 1 000, [Made-in-China](https://www.made-in-china.com/manufacturers/wholesale-pet-chew-toy.html)), groupage maritime, 4,04 € le kit + 300 € de dossier ; en aérien, 5,99 € le kit, soit ≈ 1 950 € de plus. Haut : 1 000 kits L en aérien + 500 kits XL en maritime (7,52 € hors outillage) + outillage XL 4 000 $ + conception et prototypes 1 500 € (HYPOTHÈSE). |
| Emballage de marque (création + sachets d’expédition) | 40 | 950 | 2 025 | HYPOTHÈSE | Création graphique 0 / 600 / 1 500 € (non sourcé) ; sachets et encarts 0,20–0,35 € pièce. Les boîtes imprimées (MOQ 1 000, 0,35–0,80 $, [Hongyun](https://sh-hongyun.en.made-in-china.com/product/TFaQsuHDOxci/China-Wholesale-Custom-Kids-Plush-Doll-Gift-Corrugated-Window-Toy-Box-Packaging-with-Plastic-Pet.html)) sont dans le stock ; boîtes d’expédition imprimées dès 30 pièces chez [Packhelp](https://packhelp.co.uk/shop/boxes/mailer-boxes). |
| Conformité et étiquetage | 551 | 2 089 | 4 244 | SOURCÉ (essais HAP, Citeo) + HYPOTHÈSE (reste) | Essai HAP REACH 184 € HT par échantillon + 97 € par commande ([Measurlabs](https://measurlabs.com/products/polycyclic-aromatic-hydrocarbons-pahs-in-plastic-and-rubber-reach), recherche du 28/10) : 1 / 3 / 5 échantillons (matière × couleur) ; phtalates en haut : 4 × 130 $ ([CAPLINQ](https://caplinq.com/reach-svhc-testing-pricelist.html)) ; essai de migration du moule 0 / 400 / 800 € (HYPOTHÈSE ; 200–600 € par analyse chez [PEPTLAB](https://www.peptlab.unifi.it/upload/sub/1%20versione_Tariffario%20EDCs_PEPTLAB_2024_Inglese.pdf)) ; Citeo 80 / 110 / 110 € ; assurance RC produits 0 / 400 / 800 € et dépôt de marque INPI 190 / 230 / 270 € (HYPOTHÈSES, à vérifier) ; relecture juridique (allégations, CGV, fiche GPSR) 0 / 300 / 800 €. RTC et IDU gratuits [CP]. |
| Photos et vidéos UGC | 970 | 2 755 | 4 886 | SOURCÉ (UGC) + HYPOTHÈSE (photos, envois) | UGC : 5 vidéos × 170 € (moyenne Takema) / 8 × 250 € (lot Plateya) / 10 × 320 € (médiane unitaire Plateya), + 12 / 15 / 18 % de coûts cachés (droits, révisions) ([Plateya](https://www.plateya.fr/blog/detail/couts-moyens-createur-ugc-2026-grille-tarifaire-plateya), [Takema](https://takema-studio.com/marques/prix-video-ugc-en-france-le-guide-complet-pour-2026)). Photos produit 0 / 400 / 1 000 € (HYPOTHÈSE). Kits offerts à 5 / 15 / 30 micro-créateurs de grands chiens : port seulement (kits pris dans le stock). |
| Shopify, applications, domaine et thème (3 mois) | 123 | 243 | 980 | SOURCÉ (Shopify) + HYPOTHÈSE | Basic 36 €/mois sans application payante / Basic + 40 € d’applications / Grow 105 € + 100 € ([Kanal](https://getkanal.com/fr/blog/prix-shopify)) ; domaine 15 € et thème payant 350 € (HYPOTHÈSES). |
| Publicité de test (détail au §5.2) | 630 | 2 520 | 4 270 | CALCUL | Plans ci-dessous. |
| Imprévus (10 %) | 427 | 1 357 | 3 262 | HYPOTHÈSE | Réexpéditions, casse, essai supplémentaire, frais bancaires. |
| **Total** | **4 700** | **14 923** | **35 885** |  |  |

- **Ce qui revient pendant le test** (budget central) : 63 commandes attendues au CPA intermédiaire, soit ≈ 648 € de marge contributive (kit L, coûts intermédiaires) ; 179 commandes et ≈ 2 714 € dans le scénario optimiste. La trésorerie réellement exposée est donc le total moins ce montant, moins la valeur du stock restant (937 kits invendus à la fin du test au CPA central).
- **Version minimale sans stock de marque** : un test de demande avec le seul budget publicitaire bas (630 €), des visuels tournés avec les échantillons et une liste d’attente ou une précommande (délai de livraison obligatoirement affiché) coûterait ≈ 1 756 €. Il mesure le coût par ajout au panier, pas un vrai CPA.

### 5.2 Plan publicitaire et nombre d’achats nécessaires pour juger

| Budget | Phase | Ensembles de publicités | Budget par jour et par ensemble | Jours | Dépense (€) | Achats attendus (CPA 94,61) | Achats attendus (CPA 39,88) | Achats attendus (CPA 14,05) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bas | Angles créatifs | 2 | 15 € | 21 | 630 | 6,7 | 15,8 | 44,8 |
| **Bas : total** |  |  |  |  | **630** | **7** | **16** | **45** |
| Central | A. Tri des angles créatifs | 3 | 15 € | 14 | 630 | 6,7 | 15,8 | 44,8 |
| Central | B. Test de prix ou d’offre (29,90 € contre 34,90 €, ou kit contre duo) | 2 | 30 € | 21 | 1 260 | 13,3 | 31,6 | 89,7 |
| Central | C. Validation sur l’angle et le prix gagnants | 1 | 45 € | 14 | 630 | 6,7 | 15,8 | 44,8 |
| **Central : total** |  |  |  |  | **2 520** | **27** | **63** | **179** |
| Haut | A. Tri des angles créatifs | 4 | 20 € | 14 | 1 120 | 11,8 | 28,1 | 79,7 |
| Haut | B. Test de prix (24,90 / 29,90 / 34,90 €) | 3 | 30 € | 21 | 1 890 | 20,0 | 47,4 | 134,5 |
| Haut | C. Validation et premier passage à l’échelle | 1 | 60 € | 21 | 1 260 | 13,3 | 31,6 | 89,7 |
| **Haut : total** |  |  |  |  | **4 270** | **45** | **107** | **304** |

Le plan bas garde le rythme actuel du client (15 €/jour par ensemble). Le plan central est dimensionné pour le seul cas où le produit est rentable : si le CPA est proche de 14,05 €, la phase B apporte ≈ 45 achats par variante (630 € par variante), assez pour comparer deux prix ; si le CPA est proche de 39,88 €, l’échec se voit dès la phase A.

**Combien d’achats faut-il pour conclure ?** Le nombre d’achats suit une loi de Poisson ; l’intervalle de confiance du vrai CPA autour du CPA observé se resserre lentement :

| Achats observés | Intervalle à 95 % du vrai CPA (multiple du CPA observé) | Exemple : CPA observé de 40 € |
| :--- | ---: | ---: |
| 5 | 0,43 × à 3,08 × | 17 € à 123 € |
| 10 | 0,54 × à 2,09 × | 22 € à 83 € |
| 15 | 0,61 × à 1,79 × | 24 € à 71 € |
| 20 | 0,65 × à 1,64 × | 26 € à 65 € |
| 30 | 0,70 × à 1,48 × | 28 € à 59 € |
| 50 | 0,76 × à 1,35 × | 30 € à 54 € |
| 100 | 0,82 × à 1,23 × | 33 € à 49 € |

| Écart à détecter entre le CPA d’équilibre et un CPA trop élevé | Achats attendus au CPA d’équilibre (5 % d’erreur, 80 % de puissance) | Seuil de décision (achats observés) | Dépense nécessaire, kit L (CPA d’équilibre 10,26 €) | Dépense nécessaire, duo (18,41 €) |
| :--- | ---: | ---: | ---: | ---: |
| 1,5 × | 46,5 | 41 | 477 | 856 |
| 2,0 × | 19,5 | 16 | 200 | 359 |
| 3,0 × | 9,5 | 7 | 97 | 175 |

**Règles de décision proposées (inférences du calcul).**
- **Couper un ensemble de publicités** qui a dépensé 3 fois le CPA cible sans aucun achat : si le vrai CPA était égal à la cible, ce cas n’arriverait que 5 fois sur 100 (e⁻³). Avec une cible de 15 €, cela fait 45 € par ensemble.
- **Juger un angle créatif** après 15 à 20 achats : assez pour distinguer un CPA du simple au double.
- **Juger un prix ou une offre** après 40 à 50 achats par variante : assez pour distinguer un écart de 50 %. Au CPA central, cela coûte 1 600 à 2 000 € par variante ; au CPA optimiste, 560 à 700 €.
- **Décision finale pour le jouet** : poursuivre si, après ≈ 50 achats, le CPA observé reste sous ≈ 18 € à 20 € (équilibre du duo sur la 1re commande et sur 12 mois) ; entre ≈ 20 et 30 €, retravailler l’offre (duo par défaut, 34,90 €, vente croisée) ; au-delà de ≈ 30 €, arrêter. Au CPA central de 39,88 €, l’écart avec l’équilibre du kit simple (×3,9) se voit dès ≈ 10 achats : un échec se constate vite et pour peu d’argent ; c’est un succès qui coûte cher à confirmer.
- **Phase d’apprentissage Meta** : ≈ 50 événements en 7 jours ([CP]) exigeraient ≈ 285 € par jour au CPA central. Pendant le test, optimiser sur l’ajout au panier (événement 5 à 10 fois plus fréquent, ordre de grandeur non sourcé) ou regrouper le budget dans un seul ensemble « Advantage+ ».

### 5.3 Versions courtes pour les quatre autres finalistes

**Support nerf de bœuf**

| Poste (€ HT) | Bas | Central | Haut | Statut | Détail et source |
| :--- | ---: | ---: | ---: | :--- | :--- |
| Échantillons (petites séries de 20 à 24 pièces) | 136 | 234 | 465 | SOURCÉ + HYPOTHÈSE | MOQ 20–24 à 0,95–2,82 $ (Ningbo Sincere, Zuowu, `deep_support_nerf_de_boeuf.md` §3.1 → [Alibaba](https://www.alibaba.com/wholesale/chew-stick-holder-dog.html)) ; port express non sourcé. |
| Premier stock (supports + nerfs pour les kits) | 581 | 2 345 | 4 512 | CALCUL | 100 supports en aérien (4,31 €) / 500 au MOQ courant en maritime (3,60 €) + 50 sachets de 8 nerfs / 1 000 supports + 125 sachets. |
| Emballage de marque | 40 | 775 | 1 850 | HYPOTHÈSE | Création 0 / 600 / 1 500 € + sachets. |
| Conformité (HAP, essais d’arrachement et d’usure, RC, Citeo, marque, DDPP pour les nerfs) | 551 | 1 505 | 2 429 | SOURCÉ (HAP, Citeo) + HYPOTHÈSE | Essais d’arrachement non sourcés (0 / 300 / 600 €) ; confirmation écrite de la DDPP gratuite. |
| Photos et UGC | 952 | 1 838 | 4 021 | SOURCÉ + HYPOTHÈSE | Démonstration en 3 gestes, facile à filmer. |
| Shopify et outils (3 mois) | 123 | 243 | 980 | SOURCÉ + HYPOTHÈSE | Comme le jouet. |
| Publicité de test | 630 | 2 520 | 4 270 | CALCUL | Même plan que le jouet ; le message doit d’abord éduquer au risque (CPA probablement plus élevé). |
| Imprévus (10 %) | 301 | 946 | 1 853 | HYPOTHÈSE | Réexpéditions, casse, essai supplémentaire, frais bancaires. |
| **Total** | **3 314** | **10 406** | **20 380** |  |  |

**Additif litière (budget conditionnel : aucun fournisseur de granulés identifié)**

| Poste (€ HT) | Bas | Central | Haut | Statut | Détail et source |
| :--- | ---: | ---: | ---: | :--- | :--- |
| Recherche du fournisseur de granulés et échantillons | 200 | 500 | 1 000 | HYPOTHÈSE | Aucun fournisseur de granulés seuls trouvé ; Blücare (lié à Royal Canin et Intersand) à approcher. |
| Validation technique (lecture sur urines de référence, laboratoire ou vétérinaire) | 500 | 1 500 | 3 000 | HYPOTHÈSE | Non sourcé ; indispensable vu l’absence de données de validation des granulés chinois. |
| Premier stock (doses) | 1 305 | 2 610 | 7 230 | CALCUL sur HYPOTHÈSE | 500 / 1 000 / 3 000 doses à 2,31 € la dose rendue (I). Si les granulés ne sont vendus que dans une litière complète, la seule MOQ trouvée est de 20 000 sacs (32 680 à 39 560 €, [Made-in-China](https://38e011064c1f9659.en.made-in-china.com/product/XwrtZVITbDUp/China-Tofu-Cat-Litter-Occult-Blood-Test-Vacuum-Packing-Ultra-Absorbent-and-Fast-Drying-Tofu-Cat-Litter-Selected-Quality-Pea-Dregs-Solubility-in-Water-Vacuum.html)) : le projet change d’échelle. |
| Emballage (sachets, nuancier, coffret) | 300 | 800 | 1 500 | HYPOTHÈSE | Le nuancier imprimé est au cœur du produit. |
| Conformité (FDS du réactif, relecture des allégations « alerte, pas diagnostic », RC, Citeo, marque) | 570 | 1 640 | 3 180 | HYPOTHÈSE + SOURCÉ (Citeo) | Risque de requalification en dispositif de diagnostic si le discours dérape (`faisabilite_litiere_et_bouchees.md` §2.4). |
| Photos et UGC | 952 | 1 838 | 4 021 | SOURCÉ + HYPOTHÈSE | Démonstration difficile (alertes rares) : plus de créations explicatives. |
| Shopify et outils (3 mois) | 123 | 243 | 980 | SOURCÉ + HYPOTHÈSE | Application d’abonnement comprise dans les 40 €. |
| Publicité de test | 630 | 2 520 | 4 270 | CALCUL | Même plan. |
| Imprévus (10 %) | 458 | 1 165 | 2 518 | HYPOTHÈSE | Réexpéditions, casse, essai supplémentaire, frais bancaires. |
| **Total** | **5 038** | **12 816** | **27 699** |  |  |

**Bouchées glandes anales**

| Poste (€ HT) | Bas | Central | Haut | Statut | Détail et source |
| :--- | ---: | ---: | ---: | :--- | :--- |
| Échantillons et tests d’appétence | 100 | 300 | 600 | HYPOTHÈSE | Formule de catalogue d’un façonnier UE. |
| Premier stock (pots de 60) | 3 100 | 4 650 | 11 625 | CALCUL sur HYPOTHÈSE | MOQ ≈ 1 000 pour une formule de catalogue (DAT Supply, 5 à 12 semaines, [dat.supply](https://dat.supply/eu/en/pet-supplement-manufacturer/)) ; 2 500 en marque blanche (Merywood, [merywood.com](https://merywood.com/pet-supplement-manufacturer/)). Coût du pot non publié : 3,10 € / 4,65 € (HYPOTHÈSE). |
| Étiquetage et dossier d’allégations (règlement 767/2009, code FEDIAF) | 300 | 800 | 1 500 | HYPOTHÈSE | Appui annoncé par les façonniers ; notification à la DD(ETS)PP : frais non trouvés (supposés nuls). |
| Emballage de marque et autres frais de conformité (RC, Citeo, marque) | 270 | 1 340 | 2 680 | HYPOTHÈSE + SOURCÉ (Citeo) | Étiquette en français obligatoire. |
| Photos et UGC | 952 | 2 300 | 4 776 | SOURCÉ + HYPOTHÈSE | Pas de démonstration instantanée : plus de témoignages (8 à 10 vidéos). |
| Shopify et outils (3 mois) | 123 | 243 | 980 | SOURCÉ + HYPOTHÈSE | Application d’abonnement comprise. |
| Publicité de test | 630 | 2 520 | 4 270 | CALCUL | Même plan. |
| Imprévus (10 %) | 548 | 1 215 | 2 643 | HYPOTHÈSE | Réexpéditions, casse, essai supplémentaire, frais bancaires. |
| **Total** | **6 022** | **13 368** | **29 074** |  |  |

**Boîte-puzzle chat**

| Poste (€ HT) | Bas | Central | Haut | Statut | Détail et source |
| :--- | ---: | ---: | ---: | :--- | :--- |
| Échantillons (stock gratuit chez certains fabricants, puis échantillon personnalisé en 5 à 7 jours) | 90 | 187 | 386 | SOURCÉ + HYPOTHÈSE | Échantillons de stock gratuits (Shanghai Woods), personnalisé en 5–7 jours ([Hangzhou Jie Feng](https://hzjiefeng.en.made-in-china.com/product/eNFxAiOGyshd/China-Cheap-Corrugated-Cardboard-Cat-Toy-Mouse-Cat-Scratcher-Toy.html)) ; port non sourcé. |
| Forme de découpe et prototype | 0 | 400 | 1 000 | HYPOTHÈSE | Non sourcé. |
| Premier stock | 1 630 | 3 175 | 7 550 | CALCUL | MOQ 500 (Jiang-house, Jie Feng, Bright Sea) ; 2,96 € / 5,75 € la boîte rendue ; haut : 1 000 boîtes + 500 packs d’inserts. |
| Conformité (HAP papier-carton, encres et colles, RC, Citeo, marque) | 551 | 1 021 | 1 645 | SOURCÉ (HAP, Citeo) + HYPOTHÈSE | Prix HAP papier-carton supposé égal au caoutchouc ; appartenance à Ecomaison à vérifier. |
| Photos et UGC | 952 | 1 838 | 4 021 | SOURCÉ + HYPOTHÈSE | « La patte qui pêche » se filme facilement. |
| Shopify et outils (3 mois) | 123 | 243 | 980 | SOURCÉ + HYPOTHÈSE | Comme le jouet. |
| Publicité de test | 630 | 2 520 | 4 270 | CALCUL | Même plan. |
| Imprévus (10 %) | 398 | 938 | 1 985 | HYPOTHÈSE | Réexpéditions, casse, essai supplémentaire, frais bancaires. |
| **Total** | **4 374** | **10 321** | **21 837** |  |  |

## 6. Comparaison des 5 finalistes et principaux risques financiers

### 6.1 Tableau comparatif

| Finaliste | Offre principale / lot | Marge contributive de l’offre principale P / I / O | Marge après pub, 1re commande, offre principale P / I / O | Lot : marge après pub (I) | CPA d’équilibre 1re commande (I) : offre / lot | ROAS d’équilibre TTC (I) : offre / lot | Cumul par client à 12 mois (I) : offre / lot en 1re commande | Récupération du CPA (I) : offre / lot | CPA maximal récupéré en 12 mois (I) : offre / lot |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Jouet à lécher congelable | Kit L 29,90 € / Duo 49,90 € | −4,46 / 10,26 / 15,13 | −99,07 / −29,62 / 1,08 | −21,47 | 10,26 / 18,41 | 2,91 / 2,71 | −28,23 / −20,08 | > 36 mois / > 36 mois | 11,65 / 19,80 |
| Support de nerf de bœuf | Support 29,90 € / Kit + 8 nerfs 49,90 € | −1,94 / 10,68 / 15,74 | −96,55 / −29,20 / 1,69 | −22,16 | 10,68 / 17,72 | 2,80 / 2,82 | −27,64 / −20,60 | > 36 mois / > 36 mois | 12,24 / 19,28 |
| Litière indicatrice de santé, version additif léger | Coffret 3 mois 39,90 € / Coffret 6 mois 69,90 € | −8,68 / 14,26 / 22,60 | −103,29 / −25,62 / 8,55 | −12,74 | 14,26 / 27,14 | 2,80 / 2,58 | −15,44 / −5,24 | > 36 mois / mois 18 | 24,44 / 34,64 |
| Bouchées fibres « glandes anales » | Pot 34,90 € / Lot 2 pots 64,90 € | −0,01 / 12,97 / 18,68 | −94,62 / −26,91 / 4,63 | −12,48 | 12,97 / 27,40 | 2,69 / 2,37 | −12,46 / −0,14 | > 36 mois / mois 12 | 27,42 / 39,74 |
| Boîte-puzzle à friandises pour chat | Boîte 39,90 € / Boîte + 3 inserts 49,90 € | −4,83 / 14,14 / 22,36 | −99,44 / −25,74 / 8,31 | −22,17 | 14,14 / 17,71 | 2,82 / 2,82 | −25,34 / −21,77 | > 36 mois / > 36 mois | 14,54 / 18,11 |

En prudent, aucun finaliste ne récupère le CPA (94,61 €), même en 36 mois ; en optimiste, tous le récupèrent dès la première commande (CPA de 14,05 €).

### 6.2 Potentiel de lot, de vente additionnelle et de réachat

| Finaliste (coûts intermédiaires) | Gain de marge du lot par rapport à l’offre simple | Marge moyenne de 1re commande si 30 % prennent le lot | Après CPA 39,88 | Part des clients qui réachètent (p2) | Réachats espérés en 12 mois | Marge par réachat | Ventes additionnelles naturelles |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| Jouet à lécher congelable | +8,15 € | 12,70 € | −27,18 € | 15 % | 0,20 | 7,13 € | Duo (rotation congélateur), 2e moule, support nerf de bœuf (+5,00 € de marge à 44,90 €), brosse Pilou (« brossé pendant qu’il lèche ») ; recharges alimentaires plus tard (paliers 1 et 2). |
| Support de nerf de bœuf | +7,04 € | 12,79 € | −27,09 € | 20 % | 0,76 | 2,05 € | Nerfs de bœuf (kit, abonnement), taille XL, pièces de rechange ; vente croisée avec le jouet. |
| Litière indicatrice de santé, version additif léger | +12,88 € | 18,12 € | −21,76 € | 40 % | 0,98 | 10,41 € | Coffret 6 mois, foyers à plusieurs chats (2 coffrets) ; rien d’autre de naturel (marque mono-produit chat). |
| Bouchées fibres « glandes anales » | +14,43 € | 17,30 € | −22,58 € | 40 % | 1,52 | 9,49 € | Lot de 2 pots, abonnement ; lingettes ou soins d’hygiène (non chiffrés). |
| Boîte-puzzle à friandises pour chat | +3,57 € | 15,21 € | −24,67 € | 10 % | 0,13 | 3,10 € | Inserts de rechange, 2e boîte, friandises compatibles (aliment = palier réglementaire supérieur). |

Le taux de prise du lot (30 %) est une HYPOTHÈSE de lecture. **Les lots sont le levier le plus fiable** (ils jouent dès la première commande) ; le réachat ne compte vraiment que pour les deux consommables (additif, bouchées) ; pour le jouet, la boîte chat et le support, il reste marginal tant qu’aucune recharge propre n’existe. Levier non chiffré : la base clients de Pilou (propriétaires de grands chiens à sous-poil, cible naturelle du jouet et du support) peut apporter des premières commandes presque sans CPA (e-mail, encart dans les colis) ; chacune rapporte alors directement sa marge contributive (10,26 € pour le kit L, 18,41 € pour le duo). La taille de cette base n’est pas connue ici.

### 6.3 Sensibilité au CPA (coûts intermédiaires, première commande)

| Offre (coûts intermédiaires) | CPA 10,00 | CPA 14,05 | CPA 20,00 | CPA 25,00 | CPA 30,00 | CPA 39,88 | CPA 60,00 | CPA 94,61 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Kit L 29,90 € | 0,26 | −3,79 | −9,74 | −14,74 | −19,74 | −29,62 | −49,74 | −84,35 |
| Duo 49,90 € | 8,41 | 4,36 | −1,59 | −6,59 | −11,59 | −21,47 | −41,59 | −76,20 |
| Support 29,90 € | 0,68 | −3,37 | −9,32 | −14,32 | −19,32 | −29,20 | −49,32 | −83,93 |
| Kit + 8 nerfs 49,90 € | 7,72 | 3,67 | −2,28 | −7,28 | −12,28 | −22,16 | −42,28 | −76,89 |
| Coffret 3 mois 39,90 € | 4,26 | 0,21 | −5,74 | −10,74 | −15,74 | −25,62 | −45,74 | −80,35 |
| Coffret 6 mois 69,90 € | 17,14 | 13,09 | 7,14 | 2,14 | −2,86 | −12,74 | −32,86 | −67,47 |
| Pot 34,90 € | 2,97 | −1,08 | −7,03 | −12,03 | −17,03 | −26,91 | −47,03 | −81,64 |
| Lot 2 pots 64,90 € | 17,40 | 13,35 | 7,40 | 2,40 | −2,60 | −12,48 | −32,60 | −67,21 |
| Boîte 39,90 € | 4,14 | 0,09 | −5,86 | −10,86 | −15,86 | −25,74 | −45,86 | −80,47 |
| Boîte + 3 inserts 49,90 € | 7,71 | 3,66 | −2,29 | −7,29 | −12,29 | −22,17 | −42,29 | −76,90 |

Chaque euro de CPA en plus retire un euro de marge : la sensibilité est la même pour tous. Ce qui distingue les finalistes, c’est le **CPA d’équilibre** (de 10,26 € pour le kit L à 29,90 € à 27,40 € pour le lot de 2 pots de bouchées) et la **marge de réachat**, qui dit combien de CPA un client peut rembourser plus tard. Le même CPA a été appliqué à tous, faute de données ; en réalité, il dépendra de la force de la démonstration publicitaire de chaque produit (`pub_jouet_lechage.md`, `pub_litiere_et_bouchees.md`), qui n’est pas chiffrable ici.

### 6.4 Trésorerie immobilisée par le minimum de commande

| Finaliste | Stock au MOQ | Coût rendu unitaire (I) | Trésorerie immobilisée | Mois pour écouler le MOQ au CPA 39,88 : 1res commandes seules / avec réachats espérés | Mois pour l’écouler dans le scénario optimiste (avec réachats) | Source du MOQ | Conservation |
| :--- | :--- | ---: | ---: | ---: | ---: | :--- | :--- |
| Jouet à lécher congelable | 1 000 kits L | 4,04 € | 4 040 € | 29 / 25 | 9 | MOQ catalogue 1 000 (balle), 200 (moule), 1 000 (boîte) ; maritime (aérien : 5 990 €) | durable |
| Support de nerf de bœuf | 500 supports | 3,60 € | 1 800 € | 15 / 15 | 5 | MOQ courant 500 (20 à 1 000 selon l’usine) ; les recharges de nerfs sont un autre article | durable |
| Litière indicatrice de santé, version additif léger | 1 000 doses | 2,31 € | 2 310 € | 10 / 7 | 3 | MOQ inconnue (HYPOTHÈSE de 1 000 doses, soit 333 coffrets) ; 20 000 sacs si litière complète | conservation 2 ans (Blücare) |
| Bouchées fibres « glandes anales » | 1 000 pots de 60 | 4,65 € | 4 650 € | 29 / 15 | 7 | MOQ catalogue ≈ 1 000 (DAT Supply) ; 2 500 en marque blanche | conservation ≈ 24 mois (repère chinois) |
| Boîte-puzzle à friandises pour chat | 500 boîtes | 5,75 € | 2 875 € | 15 / 15 | 5 | MOQ 500 ; les inserts sont un autre article | durable, encombrant |

Rythme du test : 3 ensembles × 15 €/jour = 1 369 € par mois, soit 34,3 nouveaux clients par mois au CPA central et 97,4 au CPA optimiste ; les réachats suivent les hypothèses du §3. **Au rythme actuel du client, un MOQ de 1 000 kits représente plus de 2 ans de ventes** (25 mois avec réachats) : le risque de trésorerie tient moins au montant (1 800 € à 4 650 €) qu’à la durée d’écoulement. Pour les bouchées, seuls les réachats ramènent l’écoulement (15 mois) sous la durée de conservation (≈ 24 mois) ; sans eux (29 mois), une partie du lot périmerait.

### 6.5 Principaux risques financiers par finaliste

| Finaliste | Remboursements | Guerre des prix | Transport | Trésorerie (MOQ, stock) |
| :--- | :--- | :--- | :--- | :--- |
| Jouet à lécher | Fermeture qui grippe, destruction par les gros mâcheurs, risque « langue aspirée » (Woof, `sourcing_jouet_lechage.md` §2.3) : un jouet léché est invendable ; 24 % de remboursements font tomber la marge de 10,26 € à 7,40 €. Rappel possible (Purina Australie, 02/2026, `verification_jouet_lechage.md`). | Fort : Pupsicle d’origine 19,90–26,90 €, Freezball 23,90–29,90 €, SmoothieDog 29,90 € ; bas de gamme PetSafe 7,99 € ([PetSafe](https://www.petsafe.com/fr/product/jouet-a-friandises-congelable-pour-chiens-frosty-cone)), glaces Action 1,99 € les 5 ([Action](https://www.action.com/fr-fr/p/3224481/glaces-pour-chien/)), marques d’enseigne (AniOne chez [Maxi Zoo](https://www.maxizoo.fr/p/anione-balle-de-jeu-rafrachissante-2439127/)). Une entrée officielle de Woof en Europe serait le déclencheur le plus grave. | Seuil de 500 g à tenir pour le kit L (+1,53 € au-delà) ; XL et duo en tranche de 1 kg. | 1 000 kits ≈ 4 040 € en maritime, 5 990 € en aérien ; outillage XL 430 € à 9 030 € ; 25 mois d’écoulement au rythme du test ; saisonnalité (pic d’été, CPM au plus haut en juillet). |
| Support nerf de bœuf | Produit présenté comme « de sécurité » : un support qui cède expose la marque (RC produits) ; ajustement aux nerfs (« trop fins ou mal calibrés » dans les avis français, compatibilité non garantie par Bow Wow Labs). | Fort : usines à 1–3 $, génériques 18–28 € ([Fruugo](https://www.fruugo.fr/bully-stick-holder-durable-dog-chew-holder-for-safe-anti-choking-chew-toy-for-aggressive-chewers-3-in-1-dog-enrichment-toy-dishwasher-safe/p-433628060-910266805)), Chewise ≈ 35 €, Bow Wow Labs sur Amazon.fr ; copie facile, brevets seulement US. | Support seul sous 500 g ; kits et recharges de nerfs épais en tranche de 1 kg. | Faible : 500 supports ≈ 1 800 € ; nerfs à acheter à une marque de l’UE (prix de gros inconnu). |
| Additif litière | « Rien ne change de couleur » = sentiment d’inutilité ; faux positifs et anxiété (Tufts) ; consommable non retournable mais remboursements de courtoisie probables. | Moyen : Tigerino 16,49 € la boîte ; granulés Blücare intégrés à une litière Intersand ; Oh Pacha en vente directe. | Réglé par l’envoi trimestriel (< 500 g) ; la litière complète, elle, est écrasée par le port. | Inconnu : aucun fournisseur de granulés seuls ; 32 680 à 39 560 € si seule une litière complète est disponible (MOQ 20 000 sacs). |
| Bouchées glandes anales | Effet en 3 à 5 semaines : une garantie de remboursement est presque obligatoire, et un pot ouvert ne se récupère pas (3,60 € de remboursements nets par pot à 12 %). | Fort : Glandex 22,99 € les 30 et 0,45 € la bouchée en abonnement ([Amazon.fr](https://www.amazon.fr/Vetnique-pour-Chiens-Royaume-Uni-v%C3%A9t%C3%A9rinaires/dp/B0FMFDLMP5)), Treatsy, proGlan ; formule banale (citrouille, psyllium). | Léger : pot sous 500 g ; lot de 2 en tranche de 1 kg. | 1 000 pots ≈ 4 650 € ; péremption ≈ 24 mois contre 29 mois d’écoulement sans réachat (15 avec) ; formule sur mesure ≈ 15 000 $ (anecdote). |
| Boîte-puzzle chat | Chat peu motivé, carton déchiqueté, friandises coincées : retours probables ; boîte montée invendable. | Fort : fonction saturée (labyrinthe carton 2,99 € chez [Action](https://www.action.com/fr-fr/p/3207939/labyrinthe-a-balles-pour-chat-pet-dreamteam/), Trixie 8,30 €, boîtes en bois 19,99–25 €) ; copie facile. | Encombrant : poids volumétrique 1,58 kg ; en prudent, tranche de 2 kg et fret ferroviaire de 3,05 € par boîte. | 500 boîtes ≈ 2 875 € ; stockage au volume. |

## 7. Limites et vérifications qui changeraient les chiffres

1. **Le CPA réel** est le paramètre décisif : aucune donnée Meta propre aux animaux en France. Le test (§5) est la seule façon de le connaître ; les données publicitaires de Pilou sont le meilleur repère disponible.
2. **Les devis** : tous les prix fournisseurs sont des prix d’annonce ; le coût des bouchées UE, des granulés et de la XL sont des hypothèses. Demander au moins deux devis écrits par produit, et deux devis 3PL pour trancher entre « par composants » (≈ 2,30 €) et « coût complet » (3,50 à 7 €).
3. **La rétention** : les repères de réachat et d’attrition viennent de prestataires américains (synthèses de moteur, méthodologies hétérogènes). Les cumuls à 12 mois en dépendent directement.
4. **La douane** : RTC pour le kit (une ou deux lignes), définition de l’« article » pour les frais de 2 €, taux de la position 4016, publication au JO du règlement délégué (UE) 2026/2152 (une seule source).
5. **Le transport** : tarifs pros Mondial Relay et Colissimo non officiels, statut TVA des tarifs Colissimo, hausse 2027.
6. **Le régime de TVA** du porteur de la marque (§2.7) et le taux de change (1 $ = 0,86 €).

## 8. Synthèse

- **Au CPA central de 39,88 €, aucune première commande n’est rentable**, quel que soit le finaliste : les marges contributives intermédiaires des offres principales vont de 10,26 € (jouet, kit L) à 14,26 € (additif), soit −29,62 € à −25,62 € après publicité. Les lots réduisent la perte à −12,48 € au mieux (lot de 2 pots de bouchées ; coffret 6 mois d’additif : −12,74 €). Dans le scénario optimiste complet (CPA de 14,05 €), toutes les premières commandes deviennent positives, de +1,08 € (kit L) à +8,55 € (additif) pour les offres principales.
- **Jouet à lécher** : kit L à 29,90 € = 10,26 € de marge contributive, donc de CPA d’équilibre ; duo à 49,90 € = 18,41 €. Sans recharge alimentaire, le réachat est faible : il faut un **CPA ≤ 11,65 € (kit) ou ≤ 19,80 € (duo)** pour récupérer l’acquisition en 12 mois. 34,90 € rapporte plus par euro de publicité tant que la conversion ne baisse pas de plus de 26 % ; 24,90 € exigerait 53 % de conversion en plus. Stock dans l’UE obligatoire : le dropshipping perd 1,60 € par commande avant publicité (10 € de droit forfaitaire et de frais de traitement). La XL sur mesure exige 39,90 € pour garder la marge du kit L.
- **Valeur client** : seuls les consommables vendus en lot approchent la récupération du CPA central (bouchées par 2 : mois 12 ; additif 6 mois : mois 18), à condition que 40 % des clients se réabonnent et que l’attrition reste à 7,1 % par mois. Les produits durables (jouet, support, boîte chat) ne vivent que de la première commande.
- **Budget de test du jouet** : ≈ 4 700 € (bas, 200 kits génériques), ≈ 14 923 € (central, 1 000 kits L de marque en maritime, 8 vidéos UGC, 2 520 € de publicité ; ≈ 1 950 € de plus en aérien) et ≈ 35 885 € (haut, avec la XL propriétaire). Autres finalistes, budget central : support ≈ 10 406 €, additif ≈ 12 816 € (conditionnel, fournisseur introuvable), bouchées ≈ 13 368 €, boîte chat ≈ 10 321 €.
- **Règle de décision du test** : couper un ensemble après 3 CPA cibles dépensés sans achat ; juger un angle après 15 à 20 achats, un prix ou une offre après 40 à 50 achats par variante ; pour le jouet, poursuivre si le CPA observé reste sous ≈ 18 € à 20 €, arrêter au-delà de ≈ 30 €. Un échec se voit vite et coûte peu ; une réussite coûte plus cher à confirmer.
- **Risques financiers** : le CPA d’abord ; ensuite les remboursements (de 12 % à 24 % : 2,86 € à 4,10 € de marge en moins par commande), la guerre des prix (originaux et copies à 20–35 €, bas de gamme sous 9 €), les seuils de poids (500 g) et la durée d’écoulement du MOQ (≈ 25 mois pour 1 000 kits au rythme actuel du test). Le classement final dépendra surtout du CPA réellement atteint par produit, que seul le test mesurera.
- **Aucun de ces montants n’est un bénéfice net** : coûts fixes et de lancement, impôts, cotisations et rémunération du dirigeant restent à couvrir.

---

*Fichiers de calcul : `/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance/model.py` (paramètres et formules) et `/tmp/claude-0/-home-user-Pilou/a4115cab-5bdb-5d46-9461-6f6c68378b97/scratchpad/finance/report.py` (tableaux). Recherches complémentaires du 28/10/2026 (mode « standard ») : (1) « Recharge State of Subscription Commerce churn rate benchmark pet category monthly churn 2025 » ; (2) « repeat purchase rate benchmark pet ecommerce DTC percentage of first-time customers who make a second purchase within 12 months » ; (3) « cost of REACH PAH and phthalates lab test per sample rubber product price USD testing laboratory 2026 ».*

**Sources des recherches du 28/10 (synthèses de moteur, à ouvrir avant usage)** : [Eightx, attrition par catégorie](https://www.eightx.co/blog/average-subscription-churn-rate-by-category) ; [Eightx, indice 2026](https://eightx.co/blog/dtc-subscription-churn-index-2026) ; [Recharge, données animaux](https://getrecharge.com/blog/pet-food-ma-subscription-data/) ; [Eightx, réachat par secteur 2026](https://eightx.co/blog/average-ecommerce-repeat-purchase-rate-by-vertical-2026) ; [Eightx, réachat par secteur](https://eightx.co/blog/average-repeat-purchase-rate-by-vertical) ; [Mobiloud](https://www.mobiloud.com/blog/repeat-customer-rate-ecommerce) ; [Foundry CRO](https://foundrycro.com/blog/dtc-pet-marketing-benchmarks-2026/) ; [Metricrig](https://metricrig.pages.dev/answers/repeat-purchase-rate-ecommerce-benchmark-2026) ; [Measurlabs, HAP](https://measurlabs.com/products/polycyclic-aromatic-hydrocarbons-pahs-in-plastic-and-rubber-reach) ; [PEPTLAB 2024](https://www.peptlab.unifi.it/upload/sub/1%20versione_Tariffario%20EDCs_PEPTLAB_2024_Inglese.pdf) ; [CAPLINQ](https://caplinq.com/reach-svhc-testing-pricelist.html) ; [ComplianceGate](https://www.compliancegate.com/reach-product-lab-testing/).
