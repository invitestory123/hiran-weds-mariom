/**
 * wedding-data.js — Customer-facing editable data layer for noor-e-zahra
 * Edit this file to update couple names, parents, dates, venue, Islamic dua, music, and photos.
 */

window.WEDDING_DATA = {
  order: "groom-first",
  coupleDisplay: "Hiran & Mariom",
  hidePhotos: true,

  couple: {
    groom: {
      first: "Md.",
      last: "Hiran",
      script: "",
      parents: "Son of Md. Samsuddin Mia & Sahila Bibi",
      note: "Son of Md. Samsuddin Mia & Sahila Bibi — steady, kind, and embarking on this blessed new journey.",
      photo: "./editable/assets/groom.jpg",
    },
    bride: {
      first: "Mariom",
      last: "Ferdousi",
      script: "",
      parents: "Daughter of S.K. Mustaque Ali & Sabnam Ferdousi",
      note: "Daughter of S.K. Mustaque Ali & Sabnam Ferdousi — a heart full of grace, warmth, and quiet light.",
      photo: "./editable/assets/bride.jpg",
    },
  },

  wedding: {
    eventName: "Reception Ceremony",
    countdownTitle: "Until The Reception",
    dateISO: "2027-01-17T12:00:00+05:30",
    dateLabel: "January",
    day: "17",
    year: "2027",
    weekday: "Sunday",
    time: "12:00 Noon",
    blessing: "With the blessings of Allah and our families, we cordially invite you, our dear friends, to share in the joy and celebrations of the Wedding Reception of Md. Hiran & Mariom Ferdousi.",
  },

  religious: {
    eyebrow: "Bismillah",
    duaArabic: "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
    duaTranslit: "In the name of Allah, the Most Gracious, the Most Merciful",
  },

  venue: {
    name: "\"Binapani\" Anusthan Bhaban",
    line2: "Near Yatrik Club, Police Line, Suri, Birbhum",
    address: "\"Binapani\" Anusthan Bhaban, Near Yatrik Club, Birbhum Police Line, Suri, West Bengal 731101",
    plusCode: "WG2J+HQ6, Birbhum Police Line, Suri, West Bengal 731101",
    mapUrl: "https://www.google.com/maps/search/?api=1&query=WG2J%2BHQ6%2C+Birbhum+Police+Line%2C+Suri%2C+West+Bengal+731101",
    mapEmbedUrl: "https://maps.google.com/maps?q=23.9014125,87.531890625+(Binapani+Anusthan+Bhaban)&t=&z=16&ie=UTF8&iwloc=B&output=embed",
    hosts: "Md. Samsuddin Mia & Sahila Bibi",
  },

  music: {
    src: "./editable/assets/bgm.mp3",
    title: "Wedding BGM",
    youtubeUrl: "https://youtube.com/shorts/KVPFa8Z7dic?si=8RLheq5MHoPvbBTX",
  },

  images: {
    bride: "./editable/assets/bride.jpg",
    groom: "./editable/assets/groom.jpg",
    floralCorner: "./editable/assets/floral-corner.png",
    goldFlourish: "./editable/assets/gold-flourish.png",
    masjid: "./editable/assets/masjid.png",
    mandala: "",
    paperTexture: "./editable/assets/paper-texture.jpg",
    map: "./images/map.jpg",
  },
};
