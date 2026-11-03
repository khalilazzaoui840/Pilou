// Illustrations vectorielles originales (Falcon 9, Dragon, atterrissage) rendues en PNG
const sharp = require("sharp");

function rng(seed) { let s = seed; return () => (s = (s * 16807) % 2147483647) / 2147483647; }
function stars(W, H, n, seed, maxY = H) {
  const r = rng(seed); let o = "";
  for (let i = 0; i < n; i++) {
    const x = r() * W, y = r() * maxY, rad = 0.6 + r() * 1.6, op = 0.25 + r() * 0.65;
    o += `<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="${rad.toFixed(2)}" fill="#fff" opacity="${op.toFixed(2)}"/>`;
  }
  return o;
}
const defs = `
<linearGradient id="body" x1="0" x2="1"><stop offset="0" stop-color="#9EA3AA"/><stop offset="0.35" stop-color="#FFFFFF"/><stop offset="0.7" stop-color="#E4E6E9"/><stop offset="1" stop-color="#7D838B"/></linearGradient>
<linearGradient id="dark" x1="0" x2="1"><stop offset="0" stop-color="#050505"/><stop offset="0.4" stop-color="#3A3D42"/><stop offset="1" stop-color="#050505"/></linearGradient>
<linearGradient id="soot" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2B2620" stop-opacity="0"/><stop offset="0.45" stop-color="#2B2620" stop-opacity="0.55"/><stop offset="1" stop-color="#15120E" stop-opacity="0.9"/></linearGradient>
<radialGradient id="flame" cx="0.5" cy="0.1" r="0.9"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.18" stop-color="#FFF3C4"/><stop offset="0.45" stop-color="#FFB347"/><stop offset="0.75" stop-color="#E8541E" stop-opacity="0.7"/><stop offset="1" stop-color="#C8102E" stop-opacity="0"/></radialGradient>
<radialGradient id="glow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#FFB347" stop-opacity="0.55"/><stop offset="1" stop-color="#FFB347" stop-opacity="0"/></radialGradient>
<radialGradient id="smoke" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#D9D4CC" stop-opacity="0.9"/><stop offset="0.6" stop-color="#8E8880" stop-opacity="0.5"/><stop offset="1" stop-color="#5A5650" stop-opacity="0"/></radialGradient>
<linearGradient id="night" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#03040A"/><stop offset="0.65" stop-color="#0E1420"/><stop offset="1" stop-color="#2A2A30"/></linearGradient>
<linearGradient id="dusk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#05070D"/><stop offset="0.55" stop-color="#1A2236"/><stop offset="0.85" stop-color="#4A3B44"/><stop offset="1" stop-color="#8A5A4A"/></linearGradient>
<linearGradient id="sea" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#18222E"/><stop offset="1" stop-color="#05080C"/></linearGradient>
<radialGradient id="earth" cx="0.5" cy="0.15" r="0.75"><stop offset="0" stop-color="#4C8BC8"/><stop offset="0.55" stop-color="#1D4E89"/><stop offset="1" stop-color="#0A1F3D"/></radialGradient>
<linearGradient id="atmo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8EC5FF" stop-opacity="0.9"/><stop offset="1" stop-color="#8EC5FF" stop-opacity="0"/></linearGradient>
<linearGradient id="panel" x1="0" x2="1"><stop offset="0" stop-color="#2A3550"/><stop offset="0.5" stop-color="#4A5A80"/><stop offset="1" stop-color="#22304A"/></linearGradient>
<linearGradient id="trunk" x1="0" x2="1"><stop offset="0" stop-color="#8C9097"/><stop offset="0.4" stop-color="#F4F5F6"/><stop offset="1" stop-color="#70757C"/></linearGradient>
`;

// Fusée complète (vue verticale). cx = axe, top = sommet, d = diamètre (px)
function fullRocket(cx, top, d, payload = "fairing") {
  const x = cx - d / 2;
  const fairH = d * 3.6, s2H = d * 3.4, interH = d * 1.4, s1H = d * 11.5;
  let y = top, o = "";
  if (payload === "fairing") {
    o += `<path d="M ${x} ${y + fairH} L ${x} ${y + fairH * 0.45} Q ${x} ${y + fairH * 0.05} ${cx} ${y} Q ${x + d} ${y + fairH * 0.05} ${x + d} ${y + fairH * 0.45} L ${x + d} ${y + fairH} Z" fill="url(#body)"/>`;
    o += `<line x1="${cx}" y1="${y + d * 0.3}" x2="${cx}" y2="${y + fairH}" stroke="#9EA3AA" stroke-width="${d * 0.02}"/>`;
    y += fairH;
  } else {
    const capH = d * 1.6, trunkH = d * 1.5;
    o += `<path d="M ${x + d * 0.12} ${y + capH} L ${x + d * 0.3} ${y + d * 0.25} Q ${cx} ${y - d * 0.05} ${x + d * 0.7} ${y + d * 0.25} L ${x + d * 0.88} ${y + capH} Z" fill="url(#body)"/>`;
    o += `<rect x="${x + d * 0.42}" y="${y - d * 0.2}" width="${d * 0.16}" height="${d * 0.3}" fill="#C9CCD1"/>`;
    o += `<rect x="${x}" y="${y + capH}" width="${d}" height="${trunkH}" fill="url(#trunk)"/>`;
    o += `<rect x="${x}" y="${y + capH + trunkH * 0.2}" width="${d}" height="${trunkH * 0.55}" fill="url(#dark)" opacity="0.85"/>`;
    y += capH + trunkH;
    o += `<rect x="${x}" y="${y}" width="${d}" height="${fairH - capH - trunkH > 0 ? 0 : 0}" fill="none"/>`;
  }
  o += `<rect x="${x}" y="${y}" width="${d}" height="${s2H}" fill="url(#body)"/>`;
  y += s2H;
  o += `<rect x="${x}" y="${y}" width="${d}" height="${interH}" fill="url(#dark)"/>`;
  // grid fins (repliées)
  o += gridFin(x - d * 0.12, y + interH * 0.55, d * 0.14, d * 0.32) + gridFin(x + d * 0.98, y + interH * 0.55, d * 0.14, d * 0.32);
  y += interH;
  o += `<rect x="${x}" y="${y}" width="${d}" height="${s1H}" fill="url(#body)"/>`;
  o += `<text x="${cx}" y="${y + s1H * 0.25}" fill="#1B1B1B" font-family="Arial" font-weight="700" font-size="${d * 0.42}" text-anchor="middle" letter-spacing="${d * 0.05}" transform="rotate(-90 ${cx} ${y + s1H * 0.25})" dominant-baseline="middle">FALCON 9</text>`;
  // drapeau stylisé
  o += `<rect x="${cx - d * 0.18}" y="${y + s1H * 0.52}" width="${d * 0.36}" height="${d * 0.5}" fill="#C8102E" opacity="0.85"/>`;
  // jambes repliées
  o += `<path d="M ${x - d * 0.06} ${y + s1H} L ${x - d * 0.06} ${y + s1H * 0.78} L ${x + d * 0.1} ${y + s1H * 0.78} L ${x + d * 0.1} ${y + s1H} Z" fill="#111"/>`;
  o += `<path d="M ${x + d * 1.06} ${y + s1H} L ${x + d * 1.06} ${y + s1H * 0.78} L ${x + d * 0.9} ${y + s1H * 0.78} L ${x + d * 0.9} ${y + s1H} Z" fill="#111"/>`;
  y += s1H;
  o += `<path d="M ${x + d * 0.08} ${y} L ${x + d * 0.92} ${y} L ${x + d * 0.85} ${y + d * 0.35} L ${x + d * 0.15} ${y + d * 0.35} Z" fill="#2C2E33"/>`;
  return { svg: o, bottom: y + d * 0.35 };
}
function gridFin(x, y, w, h) {
  let o = `<rect x="${x}" y="${y}" width="${w}" height="${h}" fill="#1A1A1A"/>`;
  for (let i = 1; i < 4; i++) o += `<line x1="${x}" y1="${y + (h * i) / 4}" x2="${x + w}" y2="${y + (h * i) / 4}" stroke="#555" stroke-width="${w * 0.08}"/>`;
  return o;
}
function flame(cx, y, w, h) {
  return `<ellipse cx="${cx}" cy="${y + h * 0.15}" rx="${w * 2.2}" ry="${h * 0.6}" fill="url(#glow)"/>
  <path d="M ${cx - w / 2} ${y} Q ${cx - w * 0.9} ${y + h * 0.5} ${cx} ${y + h} Q ${cx + w * 0.9} ${y + h * 0.5} ${cx + w / 2} ${y} Z" fill="url(#flame)"/>`;
}

// 1. Décollage (titre)
function liftoff(W, H) {
  const d = H * 0.56 / 20.3, cx = W * 0.5;
  const r = fullRocket(cx, H * 0.06, d, "fairing");
  const fl = flame(cx, r.bottom, d * 0.9, H * 0.26);
  let smoke = "";
  const rr = rng(7);
  for (let i = 0; i < 26; i++) {
    const sx = cx + (rr() - 0.5) * W * 1.1, sy = H * 0.93 + rr() * H * 0.08, sr = W * (0.08 + rr() * 0.14);
    smoke += `<circle cx="${sx}" cy="${sy}" r="${sr}" fill="url(#smoke)"/>`;
  }
  return `<rect width="${W}" height="${H}" fill="url(#night)"/>${stars(W, H, 140, 3, H * 0.6)}
  <ellipse cx="${cx}" cy="${H * 0.9}" rx="${W * 0.7}" ry="${H * 0.2}" fill="url(#glow)"/>
  ${r.svg}${fl}${smoke}`;
}

// 2. Fusée sur le pas de tir, avec tour
function onPad(W, H) {
  const d = H * 0.8 / 20.3, cx = W * 0.56, top = H * 0.07;
  const r = fullRocket(cx, top, d, "fairing");
  const groundY = r.bottom + H * 0.02;
  const tx = cx - d * 2.6, tw = d * 1.3;
  let tower = `<rect x="${tx}" y="${top + d * 2}" width="${tw}" height="${groundY - top - d * 2}" fill="none" stroke="#3A3F47" stroke-width="${d * 0.08}"/>`;
  for (let yy = top + d * 2; yy < groundY; yy += tw) tower += `<path d="M ${tx} ${yy} L ${tx + tw} ${yy + tw} M ${tx + tw} ${yy} L ${tx} ${yy + tw} M ${tx} ${yy} L ${tx + tw} ${yy}" stroke="#3A3F47" stroke-width="${d * 0.05}"/>`;
  tower += `<rect x="${tx + tw}" y="${top + d * 6}" width="${cx - d / 2 - tx - tw}" height="${d * 0.25}" fill="#3A3F47"/>`;
  const lights = [0.2, 0.45, 0.7].map((f) => `<circle cx="${tx + tw / 2}" cy="${top + d * 2 + f * (groundY - top - d * 2)}" r="${d * 0.09}" fill="#C8102E"/>`).join("");
  return `<rect width="${W}" height="${H}" fill="url(#dusk)"/>${stars(W, H, 90, 11, H * 0.45)}
  ${tower}${lights}${r.svg}
  <rect x="0" y="${groundY}" width="${W}" height="${H - groundY}" fill="#0B0C0E"/>
  <rect x="${cx - d * 2}" y="${groundY - d * 0.25}" width="${d * 4}" height="${d * 0.25}" fill="#2A2D31"/>
  <ellipse cx="${cx}" cy="${groundY}" rx="${W * 0.45}" ry="${d * 0.6}" fill="#FFB347" opacity="0.08"/>`;
}

// 3. Dragon près de l'ISS, au-dessus de la Terre
function dragonIss(W, H) {
  const cx = W * 0.42, cy = H * 0.42, s = W * 0.16;
  // ISS stylisée en haut à droite
  const ix = W * 0.78, iy = H * 0.16, k = W * 0.06;
  let iss = `<rect x="${ix - k * 3.2}" y="${iy - k * 0.12}" width="${k * 6.4}" height="${k * 0.24}" fill="#B9BDC3"/>`;
  for (const dx of [-2.9, -2.1, 1.3, 2.1]) for (const dy of [-1, 1]) iss += `<rect x="${ix + dx * k}" y="${dy < 0 ? iy - k * 1.6 : iy + k * 0.2}" width="${k * 0.7}" height="${k * 1.4}" fill="url(#panel)" stroke="#8C96AA" stroke-width="1"/>`;
  iss += `<rect x="${ix - k * 0.25}" y="${iy - k * 0.6}" width="${k * 0.5}" height="${k * 2.2}" fill="#D7DADF"/>`;
  // Dragon (vue de côté, incliné)
  const dragon = `<g transform="translate(${cx} ${cy}) rotate(-28)">
    <rect x="${-s * 0.62}" y="${s * 0.55}" width="${s * 1.24}" height="${s * 1.0}" fill="url(#trunk)"/>
    <rect x="${-s * 0.62}" y="${s * 0.75}" width="${s * 1.24}" height="${s * 0.55}" fill="url(#dark)"/>
    <path d="M ${-s * 0.62} ${s * 0.55} L ${-s * 0.42} ${-s * 0.55} Q 0 ${-s * 0.75} ${s * 0.42} ${-s * 0.55} L ${s * 0.62} ${s * 0.55} Z" fill="url(#body)"/>
    <path d="M ${-s * 0.3} ${-s * 0.62} Q 0 ${-s * 0.95} ${s * 0.3} ${-s * 0.62} Z" fill="#E9EBEE"/>
    <rect x="${-s * 0.12}" y="${-s * 0.15}" width="${s * 0.24}" height="${s * 0.16}" rx="${s * 0.04}" fill="#1C2433"/>
    <rect x="${-s * 0.66}" y="${s * 0.5}" width="${s * 1.32}" height="${s * 0.08}" fill="#2A2D31"/>
  </g>`;
  return `<rect width="${W}" height="${H}" fill="#020306"/>${stars(W, H, 160, 21, H * 0.75)}
  <ellipse cx="${W * 0.5}" cy="${H * 1.55}" rx="${W * 1.6}" ry="${H * 0.8}" fill="url(#atmo)" opacity="0.5"/>
  <ellipse cx="${W * 0.5}" cy="${H * 1.58}" rx="${W * 1.55}" ry="${H * 0.78}" fill="url(#earth)"/>
  <ellipse cx="${W * 0.3}" cy="${H * 0.9}" rx="${W * 0.35}" ry="${H * 0.03}" fill="#FFFFFF" opacity="0.18"/>
  <ellipse cx="${W * 0.75}" cy="${H * 0.95}" rx="${W * 0.25}" ry="${H * 0.025}" fill="#FFFFFF" opacity="0.14"/>
  ${iss}${dragon}`;
}

// 4. Atterrissage du premier étage sur une barge
function landing(W, H) {
  const d = H * 0.72 / 13, cx = W * 0.5, top = H * 0.08, L = d * 10.5, x = cx - d / 2;
  let o = "";
  // corps sali par la rentrée
  o += `<rect x="${x}" y="${top}" width="${d}" height="${L}" fill="url(#body)"/>`;
  o += `<rect x="${x}" y="${top + L * 0.25}" width="${d}" height="${L * 0.75}" fill="url(#soot)"/>`;
  o += `<rect x="${x}" y="${top}" width="${d}" height="${d * 1.1}" fill="url(#dark)"/>`;
  o += `<path d="M ${x} ${top} L ${x + d} ${top} L ${x + d * 0.9} ${top - d * 0.15} L ${x + d * 0.1} ${top - d * 0.15} Z" fill="#111"/>`;
  // grid fins déployées
  o += gridFin(x - d * 0.55, top + d * 0.25, d * 0.5, d * 0.55) + gridFin(x + d * 1.05, top + d * 0.25, d * 0.5, d * 0.55);
  o += `<text x="${cx}" y="${top + L * 0.32}" fill="#1B1B1B" font-family="Arial" font-weight="700" font-size="${d * 0.38}" text-anchor="middle" letter-spacing="${d * 0.04}" transform="rotate(-90 ${cx} ${top + L * 0.32})" dominant-baseline="middle">FALCON 9</text>`;
  const by = top + L;
  // jambes déployées
  const leg = (sx, ex) => `<path d="M ${sx} ${by - d * 1.6} L ${ex} ${by + d * 1.3}" stroke="#111" stroke-width="${d * 0.16}" stroke-linecap="round"/><path d="M ${sx} ${by - d * 0.1} L ${ex} ${by + d * 1.3}" stroke="#222" stroke-width="${d * 0.07}"/><rect x="${ex - d * 0.2}" y="${by + d * 1.25}" width="${d * 0.4}" height="${d * 0.1}" fill="#111"/>`;
  o += leg(x + d * 0.05, x - d * 1.15) + leg(x + d * 0.95, x + d * 2.15);
  o += `<path d="M ${x + d * 0.1} ${by} L ${x + d * 0.9} ${by} L ${x + d * 0.82} ${by + d * 0.3} L ${x + d * 0.18} ${by + d * 0.3} Z" fill="#2C2E33"/>`;
  const fl = flame(cx, by + d * 0.3, d * 0.55, d * 1.0);
  const deckY = by + d * 1.45;
  const rr = rng(5); let smoke = "";
  for (let i = 0; i < 14; i++) smoke += `<circle cx="${cx + (rr() - 0.5) * W * 0.9}" cy="${deckY - rr() * d * 0.6}" r="${d * (0.6 + rr() * 1.1)}" fill="url(#smoke)" opacity="0.7"/>`;
  return `<rect width="${W}" height="${H}" fill="url(#dusk)"/>${stars(W, H, 70, 33, H * 0.4)}
  <rect x="0" y="${deckY}" width="${W}" height="${H - deckY}" fill="url(#sea)"/>
  <rect x="${W * 0.08}" y="${deckY - d * 0.1}" width="${W * 0.84}" height="${d * 0.55}" fill="#2A2D31"/>
  <rect x="${W * 0.08}" y="${deckY - d * 0.1}" width="${W * 0.84}" height="${d * 0.08}" fill="#4A4E55"/>
  <circle cx="${cx}" cy="${deckY}" r="${d * 0.9}" fill="none" stroke="#C8C8C8" stroke-width="${d * 0.05}" opacity="0.45" transform="scale(1 0.18) translate(0 ${deckY * (1 / 0.18 - 1)})"/>
  <ellipse cx="${cx}" cy="${deckY}" rx="${W * 0.5}" ry="${d * 0.9}" fill="url(#glow)"/>
  ${o}${fl}${smoke}`;
}

const SCENES = { liftoff, onPad, dragonIss, landing };
async function render(scene, wIn, hIn) {
  const W = Math.round(wIn * 220), H = Math.round(hIn * 220);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><defs>${defs}</defs>${SCENES[scene](W, H)}</svg>`;
  return await sharp(Buffer.from(svg)).png().toBuffer();
}
module.exports = { render };
