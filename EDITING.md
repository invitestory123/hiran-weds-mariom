# Customer Editing Guide — noor-e-zahra

This template is an Islamic Nikkah invitation featuring rich gold, parchment styling, Arabic calligraphy (Dua), couple introduction cards, live countdown timer, and venue card with Google Maps and calendar export.

---

## Normal Customer Changes

All routine customer edits are configured in:
→ [editable/wedding-data.js](file:///Users/amnas/Desktop/h2track/noor-e-zahra/editable/wedding-data.js)

### Couple Profiles
Edit `couple.bride` and `couple.groom` in `editable/wedding-data.js`:
- `first` & `last`: First and last names (e.g. `"Aaliya"`, `"Zohra"`)
- `script`: Traditional Arabic/Urdu family script designation (e.g. `"Noorani"`, `"Rahmani"`)
- `parents`: Parents lineage line
- `note`: Personal biographical description
- `photo`: Path to photo (e.g. `"./editable/assets/bride.jpg"`)

### Nikkah Event & Countdown
Edit `wedding` in `editable/wedding-data.js`:
- `eventName`: Event title (e.g. `"Nikkah Ceremony"`)
- `dateISO`: Event timestamp in ISO 8601 (`"YYYY-MM-DDTHH:MM:SS+05:30"`). Directly drives the live countdown timer and Google Calendar export.
- `dateLabel`: Month name (e.g. `"February"`)
- `day`: Day number string (e.g. `"19"`)
- `year`: Year string (e.g. `"2027"`)
- `weekday`: Day of the week (e.g. `"Friday"`)
- `time`: Formatted time string (e.g. `"6:00 PM onwards"`)
- `blessing`: Opening invitation message

### Islamic Blessings
Edit `religious` in `editable/wedding-data.js`:
- `duaArabic`: Arabic Nikkah blessing calligraphy
- `duaTranslit`: English translation / transliteration of the dua

### Venue & Location
Edit `venue` in `editable/wedding-data.js`:
- `name`: Masjid or venue name (e.g. `"Noor-e-Zahra Grand Masjid"`)
- `line2`: Sub-area / city (e.g. `"Banjara Hills, Hyderabad"`)
- `address`: Complete physical address string (used for Google Maps query)
- `hosts`: Family host sign-off (e.g. `"Best wishes from Zohra Manzil"`)

### Photos & Accents
Replace files directly in `editable/assets/` or update `images`:
- Bride photo: `editable/assets/bride.jpg`
- Groom photo: `editable/assets/groom.jpg`
- Decorative graphics: `masjid.png`, `floral-corner.png`, `gold-flourish.png`, `mandala.png`, `paper-texture.jpg`

---

## Rules for Future Agents

1. Make customer content edits in `editable/wedding-data.js` and replace photos in `editable/assets/`.
2. Do not modify bundled code in `assets/` unless requested.
3. Keep ISO date strings with proper timezone offsets (e.g. `+05:30`).
4. Validate changes with `node --check editable/wedding-data.js`.
