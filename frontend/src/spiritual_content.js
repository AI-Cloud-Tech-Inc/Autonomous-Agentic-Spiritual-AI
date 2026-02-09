// Telugu Bhakti Content - Public Domain / Traditional Stotras

// Vishnu Sahasranamam - Public Domain (from Mahabharata)
export const VISHNU_SAHASRANAMAM = {
  id: 'vishnu-sahasranamam',
  title: 'విష్ణు సహస్రనామమ్',
  titleEnglish: 'Vishnu Sahasranamam',
  category: 'Public Domain Stotram',
  totalNames: 1000,
  keyNames: [
    { name: 'విష్ణు', meaning: 'The all-pervading one' },
    { name: 'నారాయణ', meaning: 'The abode of cosmic consciousness' },
    { name: 'వాసుదేవ', meaning: 'The indwelling divine' },
    { name: 'సంకర్షణ', meaning: 'The source of all beings' },
    { name: 'ప్రద్యుమ్న', meaning: 'The son of Vasudeva' },
    { name: 'అనిరుద్ధ', meaning: 'The unconquered lord' },
    { name: 'పురుషోత్తమ', meaning: 'The supreme being' },
    { name: 'అవ్యయ', meaning: 'The imperishable one' },
    { name: 'పరమేశ్వర', meaning: 'The supreme lord' },
    { name: 'ఓంకార', meaning: 'The sacred Om' }
  ],
  significance: 'The thousand names of Lord Vishnu from the Mahabharata, revealing divine qualities.',
  sanskrit: 'విష్ణుః పరమంపద్మవక్షః శ్రీవత్సాక్షః గరుడోత్థుతః।',
  telugu: 'విష్ణువు పరమోత్తముడు, పద్మవక్షుడు, శ్రీవత్సాక్షుడు, గరుడవాహనుడు.',
  audioUrl: '/stotras/vishnu-sahasranamam.mp3'
};

// Lalitha Sahasranamam - Public Domain
export const LALITHA_SAHASRANAMAM = {
  id: 'lalitha-sahasranamam',
  title: 'లలితా సహస్రనామమ్',
  titleEnglish: 'Lalitha Sahasranamam',
  category: 'Public Domain Stotram',
  keyNames: [
    { name: 'శ్రీమతి', meaning: 'The auspicious one' },
    { name: 'భగవతీ', meaning: 'The divine goddess' },
    { name: 'లలిత', meaning: 'The gentle one' },
    { name: 'కామేశ్వరీ', meaning: 'Lord of desires' },
    { name: 'రత్నావళి', meaning: 'Jeweled garland' },
    { name: 'వందరువు', meaning: 'The infinite one' },
    { name: 'జగదంబ', meaning: 'Mother of the universe' },
    { name: 'శివదేవీ', meaning: 'Consort of Shiva' }
  ],
  significance: 'Thousand names of Goddess Lalitha Tripura Sundari, from the Lalitha Sahasranamam.',
  audioUrl: '/stotras/lalitha-sahasranamam.mp3'
};

// Hanuman Chalisa - Public Domain
export const HANUMAN_CHALISA = {
  id: 'hanuman-chalisa',
  title: 'హనుమాన్ చాలీసా',
  titleEnglish: 'Hanuman Chalisa',
  category: 'Public Domain Prayer',
  verses: [
    {
      telugu: 'శ్రీగురు చరణ కరుణామృతం, జయ హనుమాన్!',
      meaning: 'Salutations to the guru\'s feet, victory to Hanuman!'
    },
    {
      telugu: 'హనుమాన్! జయ రామకుమారా!',
      meaning: 'Hanuman! Victory to Rama\'s servant!'
    },
    {
      telugu: 'అంజనేయ మహావీర! కపి తిరస్కర!',
      meaning: 'Mighty Anjaneya! Vanquisher of demons!'
    },
    {
      telugu: 'సుగ్రీవ సేవకోధ్యక్ష! భీమ సేనాపతి!',
      meaning: 'Humble servant of Sugreeva! Commander of mighty forces!'
    }
  ],
  significance: '40 verses praising Lord Hanuman\'s strength and devotion to Rama.',
  audioUrl: '/stotras/hanuman-chalisa.mp3'
};

// Aditya Hrudayam - Public Domain (from Yuddha Kanda)
export const ADITYA_HRUDAYAM = {
  id: 'aditya-hrudayam',
  title: 'ఆదిత్య హృదయమ్',
  titleEnglish: 'Aditya Hridayam',
  category: 'Public Domain Stotram',
  meaning: 'Heart of the Sun God',
  keyVerse: {
    sanskrit: 'ఆదిత్యమహర్మ్యం శ్రీకరం విభువం, జగత్సముద్ధారణమ్।',
    telugu: 'సూర్యదేవుని మహిమను, ప్రకాశమానమైన, విశ్వమంత నింపు.',
    english: 'The glory of the Sun God, the beautiful one who illuminates the world.'
  },
  significance: 'Revealed by sage Agastya to Rama before the battle with Ravana.',
  audioUrl: '/stotras/aditya-hrudayam.mp3'
};

// Telugu Bhajans - Traditional Public Domain
export const TELUGU_BHAJANS = [
  {
    id: 'tiruppavai',
    title: 'తిరుప్పావై',
    titleEnglish: 'Tiruppavai',
    deity: 'Vishnu',
    poet: 'Andal',
    verse: 'ఓం నమాల్వార్‌కు పావై పాటలు। దేవదేవుని స్తుతి.',
    meaning: 'Sacred hymns sung by the divine saint Andal.',
    audioUrl: '/bhajans/tiruppavai.mp3'
  },
  {
    id: 'divvi-saptagati',
    title: 'దివ్వి సప్తగతి',
    titleEnglish: 'Divvi Saptagati',
    deity: 'Vishnu',
    poet: 'Tallapaka Annamacharya',
    verse: 'ఓం నమో వేంకటేశాయ। దివ్వి సప్తగతి యోగి.',
    meaning: 'Seven steps to the divine, ascending to Vaikuntha.',
    audioUrl: '/bhajans/divvi-saptagati.mp3'
  },
  {
    id: 'kala-bhairava',
    title: 'కాలభైరవ',
    titleEnglish: 'Kala Bhairava',
    deity: 'Shiva',
    verse: 'భైరవాది మంత్రం, శివస్తుతి.',
    meaning: 'Sacred mantra of Lord Bhairava, destroyer of time.',
    audioUrl: '/bhajans/kala-bhairava.mp3'
  },
  {
    id: 'maha-lakshmi',
    title: 'మహా లక్ష్మి',
    titleEnglish: 'Maha Lakshmi',
    deity: 'Lakshmi',
    verse: 'శ్రీలక్ష్మి దేవి, సరస్వతీ సమేత.',
    meaning: 'Goddess of wealth, prosperity and wisdom.',
    audioUrl: '/bhajans/maha-lakshmi.mp3'
  }
];

// Daily Mantras - Public Domain
export const DAILY_MANTRAS = [
  {
    id: 'gayatri',
    name: 'గాయత్రీ మంత్రం',
    englishName: 'Gayatri Mantra',
    sanskrit: 'ॐ भूर्भुवः स्वः। तत्सवितुर्वरेण्यं। भर्गो देवस्य धीमहि। धियो यो नः प्रचोदयात्॥',
    telugu: 'ఓం భూర్భువః స్వః। తత్సవితుర్వరేణ్యం। భర్గో దేవస్య ధీమహి। ధియో యో నః ప్రచోదయాత్॥',
    english: 'We meditate on the glory of the divine light.',
    benefit: 'Knowledge, wisdom, spiritual illumination'
  },
  {
    id: 'om-namah-shivaya',
    name: 'ఓం నమః శివాయ',
    englishName: 'Om Namah Shivaya',
    sanskrit: 'ॐ नमः शिवाय',
    telugu: 'ఓం నమః శివాయ',
    english: 'I bow to Shiva',
    benefit: 'Inner peace, transformation, removal of obstacles'
  },
  {
    id: 'om-narayanaya',
    name: 'ఓం నారాయణాయ నమః',
    englishName: 'Om Narayanaya Namah',
    sanskrit: 'ॐ नारायणाय नमः',
    telugu: 'ఓం నారాయణాయ నమః',
    english: 'I bow to Narayana',
    benefit: 'Devotion, protection, spiritual growth'
  },
  {
    id: 'om-hanumate',
    name: 'ఓం హనుమతే నమః',
    englishName: 'Om Hanumate Namah',
    sanskrit: 'ॐ हनुमते नमः',
    telugu: 'ఓం హనుమతే నమః',
    english: 'I bow to Hanuman',
    benefit: 'Strength, courage, protection from harm'
  }
];

// Morning/Evening Practices
export const SPIRITUAL_ROUTINES = {
  morning: [
    {
      practice: 'గాయత్రీ మంత్రం',
      english: 'Gayatri Mantra',
      duration: '5 minutes',
      benefit: 'Mental clarity and spiritual growth'
    },
    {
      practice: 'సూర్య నమస్కారం',
      english: 'Sun Salutations',
      duration: '10 minutes',
      benefit: 'Physical and mental energy'
    },
    {
      practice: 'ప్రాతః స్మరణం',
      english: 'Morning Remembrance',
      duration: '3 minutes',
      benefit: 'Grounding and gratitude'
    }
  ],
  evening: [
    {
      practice: 'భజనం',
      english: 'Devotional Singing',
      duration: '15 minutes',
      benefit: 'Emotional peace and devotion'
    },
    {
      practice: 'ధ్యానం',
      english: 'Meditation',
      duration: '10 minutes',
      benefit: 'Inner calm and self-realization'
    },
    {
      practice: 'శయన స్మరణం',
      english: 'Bedtime Reflection',
      duration: '5 minutes',
      benefit: 'Peaceful sleep and self-awareness'
    }
  ]
};
