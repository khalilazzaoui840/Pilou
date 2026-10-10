#!/usr/bin/env python3
"""Génère des vidéos publicitaires de la brosse Pilou avec kie.ai (Veo 3).

Usage :
    export KIE_API_KEY=...            # ne jamais committer la clé
    python3 generer_videos.py         # génère toutes les scènes
    python3 generer_videos.py chien   # une seule scène

Les vidéos sont téléchargées dans videos_ia/sorties/.
"""
import os
import sys
import time
from pathlib import Path

import requests

API = "https://api.kie.ai/api/v1"
UPLOAD_API = "https://kieai.redpandaai.co/api/file-stream-upload"
ICI = Path(__file__).parent
IMAGE = ICI / "brosse.jpg"
SORTIES = ICI / "sorties"
MODELE = "veo3_fast"  # "veo3" pour la qualité maximale (plus cher)

PRODUIT = ("a premium pet grooming pin brush with a natural light beech wood "
           "oval head, a curved ergonomic beech wood handle, and dense "
           "stainless steel pins with white rounded tips on a white cushion")

SCENES = {
    "packshot": (
        "16:9",
        f"Elegant product commercial of {PRODUIT}. Slow 360-degree orbit around "
        "the brush floating on a warm cream background, soft studio light, "
        "gentle shadows, light glinting on the steel pins, macro detail of the "
        "wood grain. Minimalist, calm, luxury Scandinavian aesthetic. No text."),
    "chien": (
        "9:16",
        f"Cozy lifestyle video: a hand gently brushes a fluffy golden retriever "
        f"lying on a linen sofa with {PRODUIT}. The dog closes its eyes, relaxed "
        "and happy. Warm natural window light, soft focus background, slow "
        "motion fur movement. Calm acoustic music, natural ambient sound."),
    "chat": (
        "9:16",
        f"Close-up of a long-haired fluffy cat being gently brushed with "
        f"{PRODUIT} on a cream wool blanket. The cat purrs and stretches with "
        "pleasure. Soft morning light, shallow depth of field, warm tones, "
        "ASMR brushing sound and soft purring."),
    "avant_apres": (
        "9:16",
        f"Satisfying grooming video: {PRODUIT} glides through a tangled, "
        "matted dog coat in one smooth stroke, leaving it silky, shiny and "
        "detangled. Macro shot of the pins passing through the fur, then the "
        "brush is set down on a wooden table. Bright natural light, satisfying "
        "ASMR sound."),
}


def entetes():
    cle = os.environ.get("KIE_API_KEY")
    if not cle:
        sys.exit("Définis d'abord la variable KIE_API_KEY.")
    return {"Authorization": f"Bearer {cle}"}


def verifier(r):
    r.raise_for_status()
    j = r.json()
    if j.get("code") != 200:
        raise RuntimeError(f"Erreur kie.ai : {j}")
    return j["data"]


def envoyer_image():
    with IMAGE.open("rb") as f:
        r = requests.post(UPLOAD_API, headers=entetes(),
                          files={"file": (IMAGE.name, f, "image/jpeg")},
                          data={"uploadPath": "pilou", "fileName": IMAGE.name})
    url = verifier(r)["downloadUrl"]
    print(f"Image envoyée : {url}")
    return url


def lancer(nom, format_, prompt, image_url):
    r = requests.post(f"{API}/veo/generate", headers=entetes(), json={
        "prompt": prompt,
        "imageUrls": [image_url],
        "model": MODELE,
        "aspectRatio": format_,
        "generationType": "REFERENCE_2_VIDEO" if MODELE == "veo3_fast" else "FIRST_AND_LAST_FRAMES_2_VIDEO",
        "enableTranslation": False,
    })
    tache = verifier(r)["taskId"]
    print(f"[{nom}] tâche lancée : {tache}")
    return tache


def attendre(nom, tache):
    while True:
        r = requests.get(f"{API}/veo/record-info", headers=entetes(),
                         params={"taskId": tache})
        d = verifier(r)
        etat = d.get("successFlag")
        if etat == 1:
            return d["response"]["resultUrls"][0]
        if etat in (2, 3):
            raise RuntimeError(f"[{nom}] échec : {d.get('errorMessage') or d}")
        time.sleep(15)


def main():
    choix = sys.argv[1:] or list(SCENES)
    SORTIES.mkdir(exist_ok=True)
    image_url = envoyer_image()
    taches = {n: lancer(n, *SCENES[n], image_url) for n in choix}
    for nom, tache in taches.items():
        try:
            url = attendre(nom, tache)
        except RuntimeError as e:
            print(e)
            continue
        fichier = SORTIES / f"{nom}.mp4"
        fichier.write_bytes(requests.get(url).content)
        print(f"[{nom}] vidéo prête : {fichier}  ({url})")


if __name__ == "__main__":
    main()
