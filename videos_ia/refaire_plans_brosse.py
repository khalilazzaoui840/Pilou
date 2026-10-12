#!/usr/bin/env python3
"""Refait les plans où l'homme brosse le chien avec la vraie brosse Pilou (kie.ai).

Plans concernés (vidéo d'origine, 24 i/s) :
  s6 : 14,00 s -> 16,96 s  (« tout le sous-poil mort en douceur sans lui faire mal »)
  s8 : 19,96 s -> 22,67 s  (« et un chien enfin détendu qui adore ça »)

Usage :
    export KIE_API_KEY=...
    python3 refaire_plans_brosse.py s6_clean_720.mp4 brosse_pilou_photo.png [--model MODELE]

Le clip (sans sous-titres) et la photo de la brosse sont envoyés à kie.ai, qui
remplace la brosse en gardant le reste du plan. Le résultat est ensuite recollé
dans la vidéo uniquement autour de la brosse (le reste reste d'origine).
"""
import argparse, json, os, sys, time
from pathlib import Path
import requests

API = "https://api.kie.ai/api/v1"
UPLOAD_API = "https://kieai.redpandaai.co/api/file-stream-upload"

PROMPT = (
    "Replace ONLY the grooming brush held in the man's hand with the exact brush "
    "shown in the reference image: a pet pin brush with an oval light beech-wood "
    "head, a curved ergonomic beech-wood handle, and dense stainless steel pins "
    "with small white rubber ball tips on a white cushion. The pins face the dog's "
    "fur while brushing. Keep everything else exactly identical: same man, same "
    "golden retriever, same hand motion, same framing, same camera, same lighting, "
    "same 3D animated style. No text, no subtitles."
)


def entetes():
    cle = os.environ.get("KIE_API_KEY")
    if not cle:
        sys.exit("Définis d'abord la variable KIE_API_KEY.")
    return {"Authorization": f"Bearer {cle}"}


def verifier(r):
    try:
        j = r.json()
    except ValueError:
        r.raise_for_status()
        raise
    if r.status_code != 200 or j.get("code") != 200:
        raise RuntimeError(f"Erreur kie.ai ({r.status_code}) : {json.dumps(j, ensure_ascii=False)}")
    return j["data"]


def envoyer(fichier):
    p = Path(fichier)
    with p.open("rb") as f:
        r = requests.post(UPLOAD_API, headers=entetes(),
                          files={"file": (p.name, f)},
                          data={"uploadPath": "pilou", "fileName": p.name})
    url = verifier(r)["downloadUrl"]
    print(f"Envoyé : {p.name} -> {url}")
    return url


def lancer(model, video_url, image_url, champ_video, champ_image):
    entree = {"prompt": PROMPT, champ_video: video_url, champ_image: [image_url]}
    r = requests.post(f"{API}/jobs/createTask", headers=entetes(),
                      json={"model": model, "input": entree})
    tache = verifier(r)["taskId"]
    print(f"Tâche lancée ({model}) : {tache}")
    return tache


def attendre(tache):
    while True:
        r = requests.get(f"{API}/jobs/recordInfo", headers=entetes(), params={"taskId": tache})
        d = verifier(r)
        etat = d.get("state")
        if etat == "success":
            return json.loads(d["resultJson"])["resultUrls"][0]
        if etat == "fail":
            raise RuntimeError(f"Échec : {d.get('failMsg') or d}")
        time.sleep(15)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("brosse")
    ap.add_argument("--model", default="wan/2-7-video-edit")
    ap.add_argument("--champ-video", default="video_url")
    ap.add_argument("--champ-image", default="image_urls")
    ap.add_argument("--sortie", default=None)
    a = ap.parse_args()
    url = attendre(lancer(a.model, envoyer(a.clip), envoyer(a.brosse), a.champ_video, a.champ_image))
    sortie = Path(a.sortie or Path(a.clip).with_name(Path(a.clip).stem + "_brosse_pilou.mp4"))
    sortie.write_bytes(requests.get(url).content)
    print(f"Plan refait : {sortie}")


if __name__ == "__main__":
    main()
