# PDF to Speech Converter

**Hallgató:** Beödők Levente (JGZW76)  

## Feladat leírása  
Ez a Python alkalmazás képes PDF fájlokból szöveget kinyerni, majd az ElevenLabs API segítségével hangformátumba alakítani.  
A grafikus felület **Tkinter**-rel készült, ahol a felhasználó kiválaszthat egy PDF fájlt, majd a play gomb megnyomássával meghallgathatja annak tartalmát.  
A program moduláris felépítésű, tartalmaz saját osztályt és saját függvényt a monogramommal (BL).  

---

## Modulok és függvények

### Modulok
- **tkinter** – grafikus felület (beépített Python modul)  
- **threading** – párhuzamos feladatkezelés (beépített Python modul)  
- **os** – fájl- és környezeti változó kezelés (beépített Python modul)  
- **fitz (PyMuPDF)** – PDF szövegkinyerés  
- **elevenlabs** – szöveg-hang átalakítás  
- **bl_utils.py** – saját segédfüggvények és osztály BL monogrammal  

---

### Fő függvények
- `main()` – a program indítási pontja  
- `bl_show_notification()` – egyedi értesítés megjelenítése (BL monogram)  
- `bl_run_in_thread()` – feladat futtatása külön szálon (BL monogram)  

---

## Osztályok
- `PDFTTSApp` – fő grafikus alkalmazás  
- `PDFReader` – PDF szövegkinyerés kezelése  
- `Speaker` – szöveg-hang konverzió kezelése  
- `BLFileManager` – egyedi fájlkezelő osztály (BL monogram)  

---

## Grafikai modul és eseménykezelés
- **Tkinter** alapú felület gombokkal  
- Események:  
  - „Select PDF” → fájl kiválasztása  
  - „Play” → szöveg felolvasása ElevenLabs API segítségével  
  - Dropdown menu → hang kiválasztása

---

## Telepítés
1. Függőségek telepítése:
   ```bash
   pip install PyMuPDF elevenlabs python-dotenv
   ```
2. `.env` fájl létrehozása az ElevenLabs API kulccsal:
   ```
   ELEVENLABS_API_KEY=your_api_key
   ```
3. Program futtatása:
   ```bash
   python main.py
   ```

---

## Használat
1. Indítsd el a programot a python main.py parancsal
2. Kattints a **Select PDF** gombra és válaszd ki a fájlt  
3. Kattints a **Play** gombra a felolvasáshoz  
