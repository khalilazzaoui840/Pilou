// Génère le diaporama « Falcon 9 – Management de l'innovation » (.pptx modifiable)
// Usage : node build_deck.js <speech.txt> <dossier_sortie>
const fs = require("fs");
const path = require("path");
const pptxgen = require("pptxgenjs");
const sharp = require("sharp");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const fa = require("react-icons/fa");

const SPEECH = process.argv[2];
const OUT_DIR = process.argv[3] || ".";
const SKILL = process.env.PPTX_SKILL;
const { applyTheme } = require(path.join(SKILL, "scripts/apply_theme.js"));

// ---------- Thème ----------
const HEX = {
  black: "0B0B0C", white: "FFFFFF", graphite: "2A2D31", light: "F1F2F4",
  red: "C8102E", grey: "6B7078", silver: "A9ADB3", steel: "3D4147", mist: "D9DBDE", darkred: "8A0B1F",
};
const THEME = {
  name: "Falcon 9 – Aérospatial",
  headFontFace: "Arial",
  bodyFontFace: "Arial",
  colors: {
    dk1: HEX.black, lt1: HEX.white, dk2: HEX.graphite, lt2: HEX.light,
    accent1: HEX.red, accent2: HEX.grey, accent3: HEX.silver, accent4: HEX.steel,
    accent5: HEX.mist, accent6: HEX.darkred, hlink: HEX.red, folHlink: HEX.grey,
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5 in
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Falcon 9 – Management de l'innovation";
pres.subject = "Réutilisation du premier étage et écosystème d'innovation";
pres.author = "Master 1 AES – Avignon Université";
pres.company = "Avignon Université";
const C = pres.SchemeColor;
const RED = C.accent1, GREY = C.accent2, SILVER = C.accent3, MIST = C.accent5, BLACK = C.text1, WHITE = C.background1, LIGHT = C.background2, GRAPHITE = C.text2;

const W = 13.333, H = 7.5, M = 0.6;

// ---------- Notes (speech) ----------
const speech = fs.readFileSync(SPEECH, "utf8").replace(/\r/g, "");
function between(a, b) {
  const i = speech.indexOf(a);
  const j = b ? speech.indexOf(b, i + 1) : speech.length;
  if (i < 0 || j < 0) throw new Error("Repère introuvable dans le speech : " + a + " / " + b);
  return speech.slice(i, j).replace(/\n(?!\n)/g, " ").replace(/ +/g, " ").replace(/\n\s*/g, "\n").trim();
}
const NOTES = {
  1: between("« Bonjour à tous", "Pour comprendre cette innovation"),
  2: between("Pour comprendre cette innovation", "PERSONNE 2 – Diapositive 3"),
  3: between("« Maintenant, voyons", "PERSONNE 3 – Diapositives 4"),
  4: between("« Falcon 9 permet également", "Pour comprendre cet écosystème"),
  5: between("Pour comprendre cet écosystème", "PERSONNE 1 – Diapositive 6"),
  6: between("« Falcon 9 crée de la valeur", "PERSONNE 2 – Diapositive 7"),
  7: between("Sur cette diapositive, nous allons distinguer", "PERSONNE 3 – Diapositives 8"),
  8: between("« Pour qu'une innovation fonctionne", "Falcon 9 présente aussi"),
  9: between("Falcon 9 présente aussi", "Pour terminer notre analyse"),
  10: between("Pour terminer notre analyse", "PERSONNE 1 – Diapositive 11"),
  11: between("« Pour conclure", null),
};
const SPEAKER = { 1: "Intervenant 1", 2: "Intervenant 1", 3: "Intervenant 2", 4: "Intervenant 3", 5: "Intervenant 3", 6: "Intervenant 1", 7: "Intervenant 2", 8: "Intervenant 3", 9: "Intervenant 3", 10: "Intervenant 3", 11: "Intervenant 1" };
function notes(slide, n, extra) {
  slide.addNotes(`[${SPEAKER[n]}]\n\n${NOTES[n]}${extra ? "\n\n" + extra : ""}`);
}

// ---------- Images : icônes et cadres photo ----------
async function icon(Comp, color, size = 256) {
  const svg = ReactDOMServer.renderToStaticMarkup(React.createElement(Comp, { color: "#" + color, size: String(size) }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}
function esc(s) { return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;"); }
// Cadre photo provisoire : à remplacer dans PowerPoint par clic droit › Changer l'image
async function photoFrame(w, h, label) {
  const pw = Math.round(w * 200), ph = Math.round(h * 200);
  const fs1 = Math.round(Math.min(pw, ph) * 0.045);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${pw}" height="${ph}">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2E3135"/><stop offset="1" stop-color="#0E0F11"/></linearGradient>
  <pattern id="p" width="${pw / 12}" height="${pw / 12}" patternUnits="userSpaceOnUse"><path d="M ${pw / 12} 0 L 0 0 0 ${pw / 12}" fill="none" stroke="#FFFFFF" stroke-opacity="0.05" stroke-width="2"/></pattern></defs>
  <rect width="100%" height="100%" fill="url(#g)"/><rect width="100%" height="100%" fill="url(#p)"/>
  <g fill="none" stroke="#FFFFFF" stroke-opacity="0.35" stroke-width="4">
    <path d="M 40 110 L 40 40 L 110 40"/><path d="M ${pw - 110} 40 L ${pw - 40} 40 L ${pw - 40} 110"/>
    <path d="M 40 ${ph - 110} L 40 ${ph - 40} L 110 ${ph - 40}"/><path d="M ${pw - 110} ${ph - 40} L ${pw - 40} ${ph - 40} L ${pw - 40} ${ph - 110}"/>
  </g>
  <text x="50%" y="47%" text-anchor="middle" font-family="Arial" font-size="${fs1}" font-weight="700" fill="#FFFFFF" fill-opacity="0.85" letter-spacing="${fs1 * 0.15}">PHOTO</text>
  <text x="50%" y="${0.47 * ph + fs1 * 1.4}" text-anchor="middle" font-family="Arial" font-size="${Math.round(fs1 * 0.62)}" fill="#FFFFFF" fill-opacity="0.65">${esc(label)}</text>
  <text x="50%" y="${0.47 * ph + fs1 * 2.4}" text-anchor="middle" font-family="Arial" font-size="${Math.round(fs1 * 0.5)}" fill="#C8102E" fill-opacity="0.9">Clic droit › Changer l'image</text>
</svg>`;
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}
async function addPhoto(slide, x, y, w, h, label, name) {
  slide.addImage({ data: await photoFrame(w, h, label), x, y, w, h, altText: "Photo : " + label, objectName: name || "Photo" });
}

// ---------- Layouts ----------
const footerOpts = (color) => ({ fontSize: 9, color, charSpacing: 2, margin: 0, valign: "middle" });
pres.defineSlideMaster({
  title: "Titre (sombre)",
  background: { color: HEX.black },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: M + 0.1, y: 1.55, w: 6.2, h: 1.3, fontSize: 72, bold: true, color: WHITE, align: "left", valign: "bottom", margin: 0, charSpacing: 2 }, text: "" } },
    { placeholder: { options: { name: "body", type: "body", x: M + 0.1, y: 3.0, w: 6.0, h: 1.0, fontSize: 20, color: SILVER, valign: "top", margin: 0 }, text: "" } },
  ],
});
function contentLayout(name, dark) {
  pres.defineSlideMaster({
    title: name,
    background: { color: dark ? HEX.black : HEX.white },
    margin: [0.5, M, 0.6, M],
    slideNumber: { x: W - M - 0.5, y: 7.0, w: 0.5, h: 0.25, fontSize: 9, color: dark ? SILVER : GREY, align: "right", margin: 0 },
    objects: [
      { text: { text: "FALCON 9  ·  MANAGEMENT DE L'INNOVATION", options: { x: M, y: 7.0, w: 5, h: 0.25, ...footerOpts(dark ? SILVER : GREY) } } },
      { placeholder: { options: { name: "kicker", type: "body", x: M, y: 0.45, w: 9, h: 0.3, fontSize: 12, bold: true, color: RED, charSpacing: 3, margin: 0, valign: "middle" }, text: "" } },
      { placeholder: { options: { name: "title", type: "title", x: M, y: 0.78, w: W - 2 * M, h: 0.75, fontSize: 32, bold: true, color: dark ? WHITE : BLACK, align: "left", margin: 0, valign: "middle" }, text: "" } },
      { placeholder: { options: { name: "speaker", type: "body", x: W - M - 4.0, y: 7.0, w: 3.3, h: 0.25, fontSize: 9, color: dark ? SILVER : GREY, align: "right", margin: 0, valign: "middle", charSpacing: 2 }, text: "" } },
    ],
  });
}
contentLayout("Contenu", false);
pres.defineSlideMaster({
  title: "Conclusion (sombre, photo à gauche)",
  background: { color: HEX.black },
  slideNumber: { x: W - M - 0.5, y: 7.0, w: 0.5, h: 0.25, fontSize: 9, color: SILVER, align: "right", margin: 0 },
  objects: [
    { placeholder: { options: { name: "kicker", type: "body", x: 5.75, y: 0.6, w: 6.9, h: 0.3, fontSize: 12, bold: true, color: RED, charSpacing: 3, margin: 0, valign: "middle" }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: 5.75, y: 0.95, w: 6.98, h: 1.2, fontSize: 32, bold: true, color: WHITE, align: "left", margin: 0, valign: "top" }, text: "" } },
    { placeholder: { options: { name: "speaker", type: "body", x: W - M - 4.0, y: 7.0, w: 3.3, h: 0.25, fontSize: 9, color: SILVER, align: "right", margin: 0, valign: "middle", charSpacing: 2 }, text: "" } },
  ],
});

function contentSlide(n, section, kicker, title, master = "Contenu") {
  const s = pres.addSlide({ masterName: master, sectionTitle: section });
  s.addText(kicker, { placeholder: "kicker" });
  s.addText(title, { placeholder: "title" });
  if (SPEAKER[n]) s.addText(SPEAKER[n].toUpperCase(), { placeholder: "speaker" });
  return s;
}
function T(slide, text, o) { slide.addText(text, { isTextBox: true, margin: 0, fontSize: 14, color: BLACK, valign: "top", ...o }); }
function card(slide, x, y, w, h, fill, name) {
  slide.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: fill || LIGHT }, line: { type: "none" }, objectName: name });
}
async function iconCircle(slide, Comp, x, y, d, bg, fg) {
  slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: bg }, line: { type: "none" } });
  const p = d * 0.25;
  slide.addImage({ data: await icon(Comp, fg), x: x + p, y: y + p, w: d - 2 * p, h: d - 2 * p, altText: "" });
}
const sep = (t) => t.join("  ·  ");

(async () => {
  // =============== 1. TITRE ===============
  pres.addSection({ title: "Introduction" });
  {
    const s = pres.addSlide({ masterName: "Titre (sombre)", sectionTitle: "Introduction" });
    await addPhoto(s, 7.45, 0, W - 7.45, H, "Décollage de Falcon 9", "Photo titre");
    T(s, "MANAGEMENT DE L'INNOVATION", { x: M + 0.1, y: 1.05, w: 6.4, h: 0.3, fontSize: 12, bold: true, color: RED, charSpacing: 3 });
    s.addText("FALCON 9", { placeholder: "title" });
    s.addText("Réutiliser le premier étage : l'innovation qui a transformé l'accès à l'espace", { placeholder: "body" });
    T(s, "PROBLÉMATIQUE", { x: M + 0.1, y: 4.3, w: 6.2, h: 0.25, fontSize: 11, bold: true, color: GREY, charSpacing: 3 });
    T(s, "Comment Falcon 9 a-t-elle transformé les lancements spatiaux grâce à la réutilisation de son premier étage, et quel rôle les différents acteurs ont-ils joué dans cette réussite ?",
      { x: M + 0.1, y: 4.6, w: 6.2, h: 1.0, fontSize: 14, italic: true, color: WHITE });
    T(s, "Prénom NOM  ·  Prénom NOM  ·  Prénom NOM", { x: M + 0.1, y: 6.15, w: 6.4, h: 0.3, fontSize: 13, bold: true, color: WHITE });
    T(s, "Master 1 AES – Management de l'Innovation et de la Transformation Numérique\nAvignon Université  ·  2026-2027", { x: M + 0.1, y: 6.5, w: 6.6, h: 0.5, fontSize: 10, color: SILVER });
    notes(s, 1);
  }

  // =============== 2. CONTEXTE (A) ===============
  {
    const s = contentSlide(2, "Introduction", "A  ·  INNOVATION ET CONTEXTE", "Un secteur fondé sur des fusées à usage unique");
    await addPhoto(s, M, 1.8, 4.6, 4.85, "Falcon 9 sur le pas de tir", "Photo contexte");
    const rows = [
      [fa.FaBuilding, "Entreprise", "SpaceX, fondée en 2002 par Elon Musk (Californie)"],
      [fa.FaSatellite, "Secteur", "Lancement spatial : satellites, cargo et équipages"],
      [fa.FaTrashAlt, "Constat", "Une fusée = un seul vol, le lanceur est perdu"],
      [fa.FaRecycle, "Ambition", "Récupérer et réutiliser pour réduire les coûts"],
    ];
    let y = 1.8;
    for (const [ic, lab, txt] of rows) {
      await iconCircle(s, ic, 5.65, y, 0.55, LIGHT, HEX.black);
      T(s, lab.toUpperCase(), { x: 6.4, y: y - 0.02, w: 6.3, h: 0.25, fontSize: 11, bold: true, color: GREY, charSpacing: 2 });
      T(s, txt, { x: 6.4, y: y + 0.24, w: 6.3, h: 0.35, fontSize: 16, color: BLACK });
      y += 0.78;
    }
    const dates = [["2002", "Création de SpaceX"], ["2010", "1er vol de Falcon 9"], ["2015", "Premier atterrissage du 1er étage"], ["2017", "Premier étage réutilisé"]];
    s.addShape(pres.shapes.LINE, { x: 5.65, y: 5.15, w: 7.08, h: 0, line: { color: MIST, width: 1 } });
    dates.forEach(([d, t], i) => {
      const x = 5.65 + i * 1.8;
      T(s, d, { x, y: 5.35, w: 1.7, h: 0.55, fontSize: 30, bold: true, color: i >= 2 ? RED : BLACK });
      T(s, t, { x, y: 5.95, w: 1.65, h: 0.7, fontSize: 12, color: GREY });
    });
    notes(s, 2);
  }

  // =============== 3. NATURE (B) ===============
  pres.addSection({ title: "Analyse de l'innovation" });
  {
    const s = contentSlide(3, "Analyse de l'innovation", "B  ·  NATURE, TYPES ET DEGRÉ", "Une innovation de produit et de procédé");
    const types = [
      [fa.FaRocket, "Produit", ["Un nouveau lanceur", "Premier étage récupérable"]],
      [fa.FaSyncAlt, "Procédé", ["Récupérer · reconditionner · relancer", "Nouvelle façon de lancer"]],
      [fa.FaChartLine, "Modèle économique", ["Coût par vol réduit", "Cadence de lancement accrue"]],
    ];
    for (let i = 0; i < 3; i++) {
      const [ic, lab, kws] = types[i];
      const x = M + i * 4.15;
      card(s, x, 1.8, 3.85, 2.25, i < 2 ? LIGHT : WHITE, "Type " + lab);
      if (i === 2) s.addShape(pres.shapes.RECTANGLE, { x, y: 1.8, w: 3.85, h: 2.25, fill: { type: "none" }, line: { color: MIST, width: 1, dashType: "dash" } });
      await iconCircle(s, ic, x + 0.3, 2.05, 0.6, i < 2 ? HEX.black : HEX.light, i < 2 ? HEX.white : HEX.grey);
      T(s, lab, { x: x + 1.05, y: 2.1, w: 2.7, h: 0.5, fontSize: 20, bold: true, color: i < 2 ? BLACK : GREY, valign: "middle" });
      T(s, kws.map((k, j) => ({ text: k, options: { breakLine: j < kws.length - 1 } })), { x: x + 0.3, y: 2.85, w: 3.35, h: 1.0, fontSize: 15, color: i < 2 ? BLACK : GREY, paraSpaceAfter: 4 });
    }
    T(s, "Le Manuel d'Oslo distingue innovation de produit et innovation de processus d'affaires (procédé, organisation, modèle économique).", { x: M, y: 4.15, w: 12.1, h: 0.3, fontSize: 11, italic: true, color: GREY });

    T(s, "DEGRÉ D'INNOVATION", { x: M, y: 4.55, w: 6, h: 0.3, fontSize: 12, bold: true, color: GREY, charSpacing: 3 });
    const x0 = 1.4, x1 = 11.95, ly = 5.65;
    s.addShape(pres.shapes.LINE, { x: x0, y: ly, w: x1 - x0, h: 0, line: { color: SILVER, width: 2, endArrowType: "triangle" } });
    const stops = [
      [2.2, "Incrémentale", "Block 1 → Block 5 : améliorations successives", BLACK, true],
      [6.67, "Radicale", "Réutilisation du 1er étage : rupture avec la fusée jetable", RED, true],
      [11.1, "Disruptive ?", "Effet sur le marché : prix en baisse, nouvelles règles", GREY, false],
    ];
    for (const [cx, lab, txt, col, on] of stops) {
      s.addShape(pres.shapes.OVAL, { x: cx - 0.13, y: ly - 0.13, w: 0.26, h: 0.26, fill: { color: on ? col : WHITE }, line: { color: col, width: 2 } });
      T(s, lab, { x: cx - 1.9, y: ly - 0.62, w: 3.8, h: 0.4, fontSize: 18, bold: true, color: col, align: "center" });
      T(s, txt, { x: cx - 1.9, y: ly + 0.28, w: 3.8, h: 0.7, fontSize: 14, color: on ? BLACK : GREY, align: "center" });
    }
    notes(s, 3, "Pistes si question : le modèle économique change aussi (coût par vol, cadence) ; le caractère « disruptif » se discute (baisse des prix du marché, nouveaux usages comme les constellations).");
  }

  // =============== 4. ACTEURS (C) ===============
  {
    const s = contentSlide(4, "Analyse de l'innovation", "C  ·  ACTEURS ET COLLABORATIONS", "SpaceX n'innove pas seule");
    const cx = W / 2, cy = 3.55, d = 2.1;
    const cards = [
      [M, 1.85, "NASA", "Contrats · financements · connaissances", fa.FaUserAstronaut],
      [M, 3.6, "FAA", "Autorité américaine : autorisations · sécurité", fa.FaBalanceScale],
      [W - M - 3.9, 1.85, "Clients commerciaux", "Opérateurs de satellites", fa.FaSatelliteDish],
      [W - M - 3.9, 3.6, "Fournisseurs", "Composants et matériaux", fa.FaCogs],
      [cx - 1.95, 5.05, "Infrastructures", "Pas de tir · barges d'atterrissage", fa.FaIndustry],
    ];
    // liens
    for (const [x, y] of cards.slice(0, 4)) {
      const left = x < cx;
      const ex = left ? x + 3.9 : x, ey = y + 0.62;
      s.addShape(pres.shapes.LINE, { x: Math.min(cx, ex), y: Math.min(cy, ey), w: Math.abs(cx - ex), h: Math.abs(cy - ey), flipV: (left && ey > cy) || (!left && ey < cy), line: { color: SILVER, width: 1.25 } });
    }
    s.addShape(pres.shapes.LINE, { x: cx, y: cy + d / 2, w: 0, h: 5.05 - (cy + d / 2), line: { color: SILVER, width: 1.25 } });
    s.addShape(pres.shapes.OVAL, { x: cx - d / 2, y: cy - d / 2, w: d, h: d, fill: { color: BLACK }, line: { type: "none" }, objectName: "SpaceX" });
    T(s, [{ text: "SpaceX", options: { fontSize: 22, bold: true, breakLine: true } }, { text: "Conçoit · fabrique · lance · récupère", options: { fontSize: 12, color: SILVER } }],
      { x: cx - d / 2 + 0.15, y: cy - 0.55, w: d - 0.3, h: 1.1, color: WHITE, align: "center", valign: "middle" });
    for (const [x, y, lab, txt, ic] of cards) {
      card(s, x, y, 3.9, 1.25, LIGHT, lab);
      await iconCircle(s, ic, x + 0.25, y + 0.3, 0.6, HEX.white, HEX.black);
      T(s, lab, { x: x + 1.05, y: y + 0.2, w: 2.75, h: 0.4, fontSize: 16, bold: true, valign: "middle" });
      T(s, txt, { x: x + 1.05, y: y + 0.62, w: 2.75, h: 0.5, fontSize: 13, color: GRAPHITE });
    }
    T(s, [{ text: "Innovation ouverte ", options: { bold: true, color: RED } }, { text: "(contrats, savoirs, données partagés)  +  " }, { text: "forte intégration verticale ", options: { bold: true } }, { text: "(moteurs, structures et logiciels conçus en interne)" }],
      { x: M, y: 6.45, w: W - 2 * M, h: 0.35, fontSize: 14, color: GRAPHITE, align: "center" });
    notes(s, 4);
  }

  // =============== 5. ÉCOSYSTÈME – ADNER ===============
  {
    const s = contentSlide(5, "Analyse de l'innovation", "C  ·  ÉCOSYSTÈME D'INNOVATION – GRILLE D'ADNER", "Un écosystème bâti autour d'une proposition de valeur");
    s.addShape(pres.shapes.RECTANGLE, { x: M, y: 1.75, w: W - 2 * M, h: 0.95, fill: { color: BLACK }, line: { type: "none" } });
    T(s, [{ text: "PROPOSITION DE VALEUR", options: { fontSize: 11, bold: true, color: RED, charSpacing: 3, breakLine: true } }, { text: "Accéder à l'orbite de façon fiable, fréquente et moins coûteuse", options: { fontSize: 20, bold: true, color: WHITE } }],
      { x: M + 0.35, y: 1.75, w: W - 2 * M - 0.7, h: 0.95, valign: "middle" });
    const cols = [
      ["01", "Activités", "Que faut-il faire ?", ["Concevoir", "Fabriquer", "Tester", "Lancer", "Récupérer"]],
      ["02", "Acteurs", "Qui le fait ?", ["SpaceX", "NASA", "Fournisseurs", "FAA", "Clients"]],
      ["03", "Positions", "Où intervient chacun ?", ["SpaceX : pivot, intégrateur", "NASA : client et financeur", "FAA : régulateur", "Fournisseurs : en amont"]],
      ["04", "Liens", "Qu'échangent-ils ?", ["Argent (contrats)", "Connaissances", "Données de vol", "Services de lancement"]],
    ];
    const cw = 2.86, gap = (W - 2 * M - 4 * cw) / 3;
    cols.forEach(([num, lab, q, items], i) => {
      const x = M + i * (cw + gap);
      card(s, x, 2.9, cw, 2.9, LIGHT, "Adner " + lab);
      T(s, num, { x: x + 0.25, y: 3.05, w: 0.8, h: 0.45, fontSize: 24, bold: true, color: RED });
      T(s, lab, { x: x + 0.95, y: 3.08, w: cw - 1.1, h: 0.4, fontSize: 18, bold: true, valign: "middle" });
      T(s, q, { x: x + 0.25, y: 3.55, w: cw - 0.5, h: 0.3, fontSize: 12, italic: true, color: GREY });
      T(s, items.map((t, j) => ({ text: t, options: { bullet: { indent: 12 }, breakLine: j < items.length - 1 } })), { x: x + 0.25, y: 3.95, w: cw - 0.4, h: 1.75, fontSize: 14, paraSpaceAfter: 3 });
    });
    T(s, "ALIGNEMENT DES ACTEURS", { x: M, y: 6.05, w: 3.2, h: 0.5, fontSize: 12, bold: true, color: GREY, charSpacing: 3, valign: "middle" });
    ["Capacités : pouvoir agir", "Intérêt à participer", "Compréhension des rôles"].forEach((t, i) => {
      const x = 3.85 + i * 2.98;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 6.05, w: 2.78, h: 0.5, rectRadius: 0.25, fill: { color: WHITE }, line: { color: BLACK, width: 1 } });
      T(s, t, { x, y: 6.05, w: 2.78, h: 0.5, fontSize: 13, bold: true, align: "center", valign: "middle" });
    });
    notes(s, 5);
  }

  // =============== 6. CRÉATION DE VALEUR (D) ===============
  {
    const s = contentSlide(6, "Analyse de l'innovation", "D  ·  CRÉATION DE VALEUR", "Une valeur créée pour plusieurs acteurs");
    await addPhoto(s, M, 1.8, 4.3, 4.85, "Capsule Dragon / ISS", "Photo valeur");
    const cards = [
      [fa.FaSatellite, "Clients", ["Prix plus compétitifs", "Meilleure disponibilité"]],
      [fa.FaUserAstronaut, "NASA", ["Transport spatial", "Cargo et équipages (Dragon)"]],
      [fa.FaRocket, "SpaceX", ["Revenus · expérience", "Avantage concurrentiel"]],
      [fa.FaGlobeEurope, "Secteur spatial", ["Essor du marché", "spatial commercial"]],
    ];
    const x0 = 5.3, cw = (W - M - x0 - 0.3) / 2, ch = 2.28;
    for (let i = 0; i < 4; i++) {
      const [ic, lab, kws] = cards[i];
      const x = x0 + (i % 2) * (cw + 0.3), y = 1.8 + Math.floor(i / 2) * (ch + 0.3);
      card(s, x, y, cw, ch, LIGHT, "Valeur " + lab);
      await iconCircle(s, ic, x + 0.3, y + 0.3, 0.65, i === 2 ? HEX.red : HEX.black, HEX.white);
      T(s, lab, { x: x + 0.3, y: y + 1.08, w: cw - 0.6, h: 0.4, fontSize: 18, bold: true });
      T(s, kws.map((k, j) => ({ text: k, options: { breakLine: j < kws.length - 1 } })), { x: x + 0.3, y: y + 1.48, w: cw - 0.6, h: 0.7, fontSize: 14, color: GRAPHITE });
    }
    notes(s, 6);
  }

  // =============== 7. CRÉATION vs CAPTURE ===============
  {
    const s = contentSlide(7, "Analyse de l'innovation", "D  ·  CRÉATION ET CAPTURE DE VALEUR", "Créer la valeur ensemble, la capter différemment");
    const half = (W - 2 * M - 0.3) / 2;
    [["CRÉATION DE VALEUR", "Les bénéfices produits grâce à l'innovation", LIGHT, BLACK, GRAPHITE],
     ["CAPTURE DE VALEUR", "Ce que chaque acteur récupère : revenus, savoirs, réputation", BLACK, WHITE, SILVER]].forEach(([h, t, bg, c1, c2], i) => {
      const x = M + i * (half + 0.3);
      s.addShape(pres.shapes.RECTANGLE, { x, y: 1.75, w: half, h: 0.85, fill: { color: bg }, line: { type: "none" } });
      T(s, h, { x: x + 0.3, y: 1.85, w: half - 0.6, h: 0.3, fontSize: 13, bold: true, color: i ? RED : c1, charSpacing: 3 });
      T(s, t, { x: x + 0.3, y: 2.17, w: half - 0.6, h: 0.35, fontSize: 14, color: c2 });
    });
    const rows = [
      ["SpaceX", "Coûts réduits · cadence accrue · offre compétitive", "Revenus · avantage concurrentiel"],
      ["NASA", "Contrats · financements · connaissances", "Services de transport spatial"],
      ["Clients", "Commandes · confiance accordée", "Accès à l'espace à meilleur prix"],
      ["Fournisseurs", "Composants · savoir-faire", "Nouveaux contrats"],
    ];
    const lx = M, lw = 2.0, c1x = M + 2.15, c1w = half - 2.15, c2x = M + half + 0.3, c2w = half;
    T(s, "Ce que l'acteur apporte / permet", { x: c1x + 0.2, y: 2.8, w: c1w, h: 0.3, fontSize: 11, bold: true, color: GREY, charSpacing: 2 });
    T(s, "Ce que l'acteur récupère", { x: c2x + 0.2, y: 2.8, w: c2w, h: 0.3, fontSize: 11, bold: true, color: GREY, charSpacing: 2 });
    rows.forEach(([a, cr, ca], i) => {
      const y = 3.18 + i * 0.78, rh = 0.66;
      T(s, a, { x: lx, y, w: lw, h: rh, fontSize: 16, bold: true, valign: "middle" });
      s.addShape(pres.shapes.RECTANGLE, { x: c1x, y, w: c1w, h: rh, fill: { color: LIGHT }, line: { type: "none" } });
      T(s, cr, { x: c1x + 0.2, y, w: c1w - 0.4, h: rh, fontSize: 14, valign: "middle", color: GRAPHITE });
      s.addShape(pres.shapes.RIGHT_ARROW, { x: c2x - 0.27, y: y + rh / 2 - 0.12, w: 0.24, h: 0.24, fill: { color: RED }, line: { type: "none" } });
      s.addShape(pres.shapes.RECTANGLE, { x: c2x, y, w: c2w, h: rh, fill: { color: WHITE }, line: { color: BLACK, width: 1 } });
      T(s, ca, { x: c2x + 0.2, y, w: c2w - 0.4, h: rh, fontSize: 14, bold: true, valign: "middle" });
    });
    T(s, [{ text: "→  ", options: { color: RED } }, { text: "Une valeur créée collectivement, mais captée de façon différente par chaque acteur" }],
      { x: M, y: 6.38, w: W - 2 * M, h: 0.4, fontSize: 16, bold: true, align: "center" });
    notes(s, 7, "Rappel du cours : la capture de valeur n'est pas uniquement financière (revenus, connaissances, réputation, accès à des ressources, possibilités de croissance).");
  }

  // =============== 8. DIFFUSION (E) ===============
  pres.addSection({ title: "Diffusion, risques et processus" });
  {
    const s = contentSlide(8, "Diffusion, risques et processus", "E  ·  DIFFUSION ET ADOPTION", "De la NASA aux opérateurs commerciaux");
    // Courbe de Rogers (géométrie personnalisée)
    const gx = 0.75, gw = 6.6, base = 5.35, gh = 2.55;
    const X = (z) => gx + ((z + 3) / 6) * gw;
    const f = (z) => Math.exp(-z * z / 2);
    const segs = [[-3, -2, RED, "Innovateurs", "2,5 %"], [-2, -1, GRAPHITE, "Adopteurs précoces", "13,5 %"], [-1, 0, SILVER, "Majorité précoce", "34 %"], [0, 1, MIST, "Majorité tardive", "34 %"], [1, 3, LIGHT, "Retardataires", "16 %"]];
    for (const [a, b, col, lab, pct] of segs) {
      const sx = X(a), sw = X(b) - X(a), top = base - gh;
      const pts = [{ x: 0, y: gh }];
      for (let k = 0; k <= 24; k++) { const z = a + (b - a) * k / 24; pts.push({ x: X(z) - sx, y: gh - gh * f(z) }); }
      pts.push({ x: sw, y: gh }); pts.push({ close: true });
      s.addShape(pres.shapes.CUSTOM_GEOMETRY, { x: sx, y: top, w: sw, h: gh, points: pts, fill: { color: col }, line: { color: WHITE, width: 1.5 }, objectName: "Rogers " + lab });
      T(s, [{ text: lab, options: { bold: true, breakLine: true } }, { text: pct, options: { color: GREY } }], { x: sx + 0.02, y: base + 0.1, w: sw - 0.04, h: 0.65, fontSize: 11, align: "center" });
    }
    s.addShape(pres.shapes.LINE, { x: gx, y: base, w: gw, h: 0, line: { color: GREY, width: 1 } });
    // gouffre
    s.addShape(pres.shapes.LINE, { x: X(-1), y: 2.3, w: 0, h: base - 2.3, line: { color: RED, width: 1.5, dashType: "dash" } });
    T(s, "Gouffre (Moore)", { x: X(-1) + 0.1, y: 2.25, w: 1.8, h: 0.3, fontSize: 11, italic: true, color: RED });
    // premiers utilisateurs
    T(s, [{ text: "Premiers utilisateurs", options: { bold: true, breakLine: true, color: RED } }, { text: "NASA (cargo vers l'ISS)", options: { breakLine: true } }, { text: "Opérateurs de satellites" }],
      { x: gx, y: 1.85, w: 2.6, h: 0.95, fontSize: 13 });
    s.addShape(pres.shapes.LINE, { x: X(-2.2), y: 2.85, w: 0, h: base - 0.25 - 2.85, line: { color: RED, width: 1, endArrowType: "oval" } });
    T(s, "Théorie de la diffusion – Rogers (2003)", { x: gx, y: 6.2, w: gw, h: 0.3, fontSize: 11, italic: true, color: GREY });

    // Facteurs
    const px = 7.95, pw = W - M - px;
    const block = async (y, h, title, Ic, col, items) => {
      card(s, px, y, pw, h, LIGHT, title);
      await iconCircle(s, Ic, px + 0.3, y + 0.25, 0.45, col, HEX.white);
      T(s, title, { x: px + 0.9, y: y + 0.25, w: pw - 1.1, h: 0.45, fontSize: 13, bold: true, charSpacing: 2, valign: "middle", color: BLACK });
      T(s, items.map((t, j) => ({ text: t, options: { bullet: { indent: 12 }, breakLine: j < items.length - 1 } })), { x: px + 0.3, y: y + 0.85, w: pw - 0.6, h: h - 1.0, fontSize: 14, paraSpaceAfter: 3 });
    };
    await block(1.8, 2.3, "FACTEURS FAVORABLES", fa.FaPlus, HEX.black, ["Prix compétitifs", "Disponibilité des lancements", "Performances et fiabilité", "Certifications des autorités"]);
    await block(4.35, 2.3, "FREINS", fa.FaMinus, HEX.red, ["Échecs : CRS-7 (2015), Amos-6 (2016)", "Méfiance envers le « réutilisé »", "Autorisations réglementaires"]);
    notes(s, 8, "Repère : SES est le premier client à accepter un premier étage déjà utilisé (mission SES-10, mars 2017). Le « gouffre » (Moore) sépare les adopteurs précoces, prêts à prendre des risques, de la majorité précoce qui attend des preuves de fiabilité.");
  }

  // =============== 9. RISQUES (F) ===============
  {
    const s = contentSlide(9, "Diffusion, risques et processus", "F  ·  DIFFICULTÉS ET RISQUES", "Des risques élevés à chaque étape");
    const risks = [
      [fa.FaCoins, "Coûts", ["Développement très coûteux", "Aucune garantie de succès"]],
      [fa.FaExclamationTriangle, "Risque technique", ["Échec = pertes financières", "Atteinte à la réputation"]],
      [fa.FaBalanceScale, "Réglementation", ["Licences de lancement (FAA)", "Règles de sécurité"]],
      [fa.FaProjectDiagram, "Coordination", ["Équipes internes", "Partenaires et clients"]],
      [fa.FaLock, "Propriété intellectuelle", ["Protéger savoirs et technologies", "Secret industriel"]],
      [fa.FaLink, "Dépendance", ["Contrats publics (NASA)", "Autorités et sites de lancement"]],
    ];
    const cw = (W - 2 * M - 0.6) / 3, ch = 2.3;
    for (let i = 0; i < 6; i++) {
      const [ic, lab, kws] = risks[i];
      const x = M + (i % 3) * (cw + 0.3), y = 1.8 + Math.floor(i / 3) * (ch + 0.3);
      card(s, x, y, cw, ch, LIGHT, "Risque " + lab);
      await iconCircle(s, ic, x + 0.3, y + 0.3, 0.6, i === 1 ? HEX.red : HEX.black, HEX.white);
      T(s, lab, { x: x + 1.1, y: y + 0.3, w: cw - 1.3, h: 0.6, fontSize: 18, bold: true, valign: "middle" });
      T(s, kws.map((k, j) => ({ text: k, options: { bullet: { indent: 12 }, breakLine: j < kws.length - 1 } })), { x: x + 0.3, y: y + 1.15, w: cw - 0.5, h: 1.0, fontSize: 14, color: GRAPHITE, paraSpaceAfter: 3 });
    }
    notes(s, 9);
  }

  // =============== 10. PROCESSUS (G) ===============
  {
    const s = contentSlide(10, "Diffusion, risques et processus", "G  ·  PROCESSUS D'INNOVATION RECONSTITUÉ", "Un processus expérimental, fait d'essais et d'erreurs");
    const steps = [
      ["2002", "Objectif : réduire le coût des lancements", 0],
      ["2010", "Premier vol de Falcon 9", 0],
      ["2012-2014", "Essais du prototype Grasshopper", 0],
      ["2015", "Atterrissages manqués · échec CRS-7", 1],
      ["Déc. 2015", "Premier atterrissage du 1er étage", 2],
      ["2016", "Explosion d'Amos-6 au sol", 1],
      ["Mars 2017", "1er étage réutilisé (SES-10)", 2],
      ["2018", "Block 5, conçu pour la réutilisation", 0],
    ];
    const lx0 = 1.85, lx1 = W - 1.85, ly = 3.85, stepW = (lx1 - lx0) / (steps.length - 1);
    s.addShape(pres.shapes.LINE, { x: M, y: ly, w: W - 2 * M, h: 0, line: { color: SILVER, width: 2, endArrowType: "triangle" } });
    steps.forEach(([d, t, kind], i) => {
      const cx = lx0 + i * stepW, up = i % 2 === 0;
      const col = kind === 1 ? RED : BLACK;
      const r = kind === 2 ? 0.17 : 0.13;
      s.addShape(pres.shapes.OVAL, { x: cx - r, y: ly - r, w: 2 * r, h: 2 * r, fill: { color: kind === 1 ? WHITE : col }, line: { color: col, width: 2.5 } });
      s.addShape(pres.shapes.LINE, { x: cx, y: up ? ly - 0.75 : ly + r + 0.05, w: 0, h: up ? 0.75 - r - 0.05 : 0.7 - r - 0.05, line: { color: MIST, width: 1 } });
      const by = up ? 1.8 : ly + 0.75, bw = 2.4;
      T(s, [{ text: d, options: { fontSize: 16, bold: true, color: col, breakLine: true } }, { text: t, options: { fontSize: 13, color: GRAPHITE } }],
        { x: cx - bw / 2, y: by, w: bw, h: 1.25, align: "center", valign: up ? "bottom" : "top" });
    });
    // légende
    s.addShape(pres.shapes.OVAL, { x: M, y: 5.95, w: 0.2, h: 0.2, fill: { color: BLACK }, line: { type: "none" } });
    T(s, "Étape franchie", { x: M + 0.3, y: 5.9, w: 1.6, h: 0.3, fontSize: 11, color: GREY, valign: "middle" });
    s.addShape(pres.shapes.OVAL, { x: M + 1.95, y: 5.95, w: 0.2, h: 0.2, fill: { color: WHITE }, line: { color: RED, width: 2 } });
    T(s, "Échec", { x: M + 2.25, y: 5.9, w: 1.0, h: 0.3, fontSize: 11, color: GREY, valign: "middle" });
    // boucle d'apprentissage
    const loop = ["Essai", "Échec", "Apprentissage", "Amélioration"];
    const bx = 4.0, bw = 1.75, bg = 0.38;
    T(s, "≠ modèle linéaire", { x: bx - 0.3 - 1.6, y: 6.25, w: 1.6, h: 0.45, fontSize: 12, italic: true, color: GREY, align: "right", valign: "middle" });
    loop.forEach((t, i) => {
      const x = bx + i * (bw + bg);
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 6.25, w: bw, h: 0.45, rectRadius: 0.22, fill: { color: i === 1 ? RED : BLACK }, line: { type: "none" } });
      T(s, t, { x, y: 6.25, w: bw, h: 0.45, fontSize: 13, bold: true, color: WHITE, align: "center", valign: "middle" });
      const ax = x + bw + 0.07;
      if (i < 3) s.addShape(pres.shapes.RIGHT_ARROW, { x: ax, y: 6.36, w: bg - 0.14, h: 0.23, fill: { color: SILVER }, line: { type: "none" } });
    });
    s.addImage({ data: await icon(fa.FaRedoAlt, HEX.red), x: bx + 4 * (bw + bg) - 0.25, y: 6.3, w: 0.35, h: 0.35, altText: "Boucle itérative" });
    notes(s, 10, "Repères : tentatives d'atterrissage sur barge manquées en janvier et avril 2015 ; échec de la mission CRS-7 (juin 2015) ; premier atterrissage réussi le 21 décembre 2015 (Orbcomm-2) ; explosion d'Amos-6 sur le pas de tir (septembre 2016) ; premier étage réutilisé le 30 mars 2017 (SES-10) ; Block 5 en mai 2018.");
  }

  // =============== 11. CONCLUSION ===============
  pres.addSection({ title: "Conclusion" });
  {
    const s = pres.addSlide({ masterName: "Conclusion (sombre, photo à gauche)", sectionTitle: "Conclusion" });
    await addPhoto(s, 0, 0, 5.15, H, "Atterrissage du premier étage", "Photo conclusion");
    s.addText("CONCLUSION", { placeholder: "kicker" });
    s.addText("Une réussite technologique et organisationnelle", { placeholder: "title" });
    s.addText(SPEAKER[11].toUpperCase(), { placeholder: "speaker" });
    const pts = [
      ["01", "Une innovation complète", "Produit · procédé · modèle économique"],
      ["02", "Un écosystème aligné", "NASA · fournisseurs · clients · autorités"],
      ["03", "Un processus itératif", "Essais · erreurs · améliorations successives"],
    ];
    pts.forEach(([n, h, t], i) => {
      const y = 2.6 + i * 0.95;
      T(s, n, { x: 5.75, y, w: 0.9, h: 0.7, fontSize: 30, bold: true, color: RED, valign: "middle" });
      T(s, [{ text: h, options: { fontSize: 18, bold: true, color: WHITE, breakLine: true } }, { text: t, options: { fontSize: 14, color: SILVER } }], { x: 6.7, y: y - 0.02, w: 6.0, h: 0.75, valign: "middle" });
    });
    s.addShape(pres.shapes.LINE, { x: 5.75, y: 5.6, w: 0, h: 0.75, line: { color: RED, width: 3 } });
    T(s, "« La réussite de Falcon 9 repose autant sur la technologie que sur la capacité à coordonner les acteurs. »", { x: 6.0, y: 5.55, w: 6.7, h: 0.85, fontSize: 16, italic: true, color: WHITE, valign: "middle" });
    T(s, "Merci pour votre attention", { x: 5.75, y: 6.95, w: 4.5, h: 0.3, fontSize: 12, bold: true, color: SILVER, charSpacing: 2, valign: "middle" });
    notes(s, 11);
  }

  // =============== 12. RÉFÉRENCES ===============
  {
    const s = contentSlide(12, "Conclusion", "SOURCES", "Références");
    const colW = (W - 2 * M - 0.5) / 2;
    const list = (x, y, h, title, items) => {
      T(s, title, { x, y, w: colW, h: 0.3, fontSize: 12, bold: true, color: RED, charSpacing: 3 });
      T(s, items.map((t, j) => ({ text: t, options: { breakLine: j < items.length - 1 } })), { x, y: y + 0.4, w: colW, h, fontSize: 12, color: GRAPHITE, paraSpaceAfter: 7 });
    };
    list(M, 1.8, 4.6, "CADRES THÉORIQUES (COURS)", [
      "Adner, R. (2017). Ecosystem as Structure: An Actionable Construct for Strategy. Journal of Management, 43(1), 39-58.",
      "Granstrand, O. & Holgersson, M. (2020). Innovation ecosystems: A conceptual review and a new definition. Technovation, 90-91.",
      "OCDE / Eurostat (2018). Manuel d'Oslo, 4e édition.",
      "Rogers, E. M. (2003). Diffusion of Innovations, 5e édition. Free Press.",
      "Moore, G. A. (1991). Crossing the Chasm. HarperBusiness.",
      "Cours « Management de l'innovation : acteurs et écosystèmes », séance 1, Master 1 AES, Avignon Université.",
    ]);
    list(M + colW + 0.5, 1.8, 3.2, "SOURCES SUR FALCON 9", [
      "SpaceX – Falcon 9 : spacex.com/vehicles/falcon-9",
      "NASA (2014). Commercial Orbital Transportation Services: A New Era in Spaceflight. NASA/SP-2014-617.",
      "FAA – Office of Commercial Space Transportation : faa.gov/space",
    ]);
    list(M + colW + 0.5, 4.7, 1.6, "CRÉDITS PHOTOS", [
      "Photos : SpaceX / NASA – à compléter selon les images insérées (licence indiquée sur Wikimedia Commons).",
    ]);
    s.addNotes("Diapositive de références : non commentée à l'oral.");
  }

  const out = path.join(OUT_DIR, "Falcon9_Management_Innovation.pptx");
  await pres.writeFile({ fileName: out });
  await applyTheme(out, THEME);
  console.log("OK", out);
})().catch((e) => { console.error(e); process.exit(1); });
