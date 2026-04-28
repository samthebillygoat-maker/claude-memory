---
title: Abandoned Place Finder
date: 2026-04-26
tags: [project, tool, urbex, abandoned-places, python, streamlit]
type: project
status: active
---

# Abandoned Place Finder

**Location:** `C:\Users\samth\abandoned-finder\`  
**Run:** `streamlit run C:\Users\samth\abandoned-finder\app.py` → http://localhost:8501  
**Or:** Double-click `run.bat`

---

## What It Does

Search any city and it aggregates abandoned places from 10+ sources, shows them on an interactive map, scores them with Claude Vision AI, and exports to Obsidian or Google My Maps.

---

## Data Sources

| Source | What It Finds | Free? |
|--------|--------------|-------|
| OpenStreetMap | Community-tagged abandoned/disused/ruins globally | ✅ |
| HIFLD (DHS Federal) | Closed hospitals with `STATUS=CLOSED` | ✅ |
| USGS National Structures | Hospitals, schools, prisons, courthouses from gov topo maps | ✅ |
| City Open Data (Socrata) | Vacant building registries — Chicago, Detroit, Baltimore, LA, Sacramento, Cleveland, New Orleans | ✅ |
| County Parcel Records | County assessor vacant property GIS data | ✅ |
| Wikipedia GeoSearch | Geo-tagged articles about derelict sites | ✅ |
| Atlas Obscura | Curated obscure & hidden places | ✅ |
| EPA ECHO | Inactive industrial/chemical facilities (slow ~30s) | ✅ |
| Reddit Urbex | r/urbanexploration, r/abandoned posts | ✅ |
| Google Places | Permanently closed businesses | 🔑 API key |

---

## API Keys

- **Google API Key** — enables Google Places + Street View thumbnails. Set up at console.cloud.google.com → enable Places API (New) + Street View Static API + Maps Static API
- **Anthropic API Key** — enables Claude Vision AI scoring (1–10). Get at console.anthropic.com

---

## File Structure

```
C:\Users\samth\abandoned-finder\
├── app.py
├── run.bat
├── client_secrets.json       ← Google OAuth (add for My Maps)
├── google_token.pkl          ← auto-saved after first Google login
├── requirements.txt
└── sources/
    ├── overpass.py           ← OSM (3 mirror fallbacks)
    ├── hifld.py              ← DHS federal closed hospitals
    ├── epa_echo.py           ← EPA inactive facilities
    ├── usgs_structures.py    ← USGS structure layers
    ├── socrata.py            ← City open data portals
    ├── county_parcels.py     ← County assessor GIS
    ├── atlas_obscura.py      ← Atlas Obscura scraper
    ├── wikimedia.py          ← Wikipedia GeoSearch
    ├── reddit.py             ← Reddit urbex communities
    ├── google_places.py      ← Permanently closed via Places API
    ├── google_mymaps.py      ← Auto-save to Google My Maps
    ├── obsidian_export.py    ← Export to Obsidian vault
    ├── coord_resolver.py     ← Auto-geocode missing coordinates
    ├── geocoder.py           ← Nominatim location search
    └── ai_scorer.py          ← Claude Vision abandonment scoring
```

---

## Obsidian Export

Each search creates:
- One `.md` note per location (coordinates, links, AI score)
- One `_Index` note linking all results
- Saved to `Abandoned Places/{city}/` in the Obsidian vault
- Compatible with **Map View plugin** (pins on map inside Obsidian)

Abandoned places are exported here: [[Abandoned Places/Sacramento, CA/_Index — Sacramento, CA]]

---

## Google My Maps

Results auto-upload to a layer called **"Possible Abandoned Places"**.

**One-time setup:**
1. console.cloud.google.com → Credentials → OAuth 2.0 Client ID → Desktop App
2. Download JSON → rename to `client_secrets.json` → place in `abandoned-finder/`
3. Enable Google Drive API in Cloud Console
4. Click "Save to Google My Maps" in Export tab → browser opens for login once, then auto-saves

---

## Tips

- **Best cities:** Detroit, Chicago, Baltimore, Cleveland, Philadelphia (most OSM tagging + city data)
- **Sacramento:** Enable USGS Structures + bump radius to 50km
- **EPA ECHO:** Leave off unless hunting industrial sites (slow)
- **AI Scoring:** Sort by "AI Score high→low" to find most likely abandoned first
- **Export:** Save to Obsidian, Google My Maps, CSV, or KML (Google Earth)

---

## Categories

🏠 Abandoned House · 🏥 Hospital/Medical · ⛪ Church/Worship · 🏫 School/Education  
🏛 Government · 🪖 Military/Bunker · 🏭 Industrial/Factory · 👻 Ghost Town · 🏚 General
