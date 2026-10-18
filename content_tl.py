"""Tagalog learning content. Choice order matches each English source question."""

TERM_MEANINGS_TL = {
    "Account": "Iyong personal na profile sa app o website, na karaniwang protektado ng password.",
    "App": "Isang programa sa telepono, tablet, o computer na tumutulong sa paggawa ng isang gawain.",
    "Avatar": "Larawan o karakter na kumakatawan sa iyo online.",
    "BAE": "Malambing na tawag sa kapareha o taong mahalaga sa iyo.",
    "BRB": "Be right back, o babalik agad. Ginagamit kapag pansamantala kang aalis sa usapan.",
    "Browser": "App para bumisita sa mga website, tulad ng Chrome, Edge, o Firefox.",
    "Cloud": "Imbakan ng mga file sa mga server na nakakonekta sa internet, para mabuksan ang mga ito sa iba't ibang device.",
    "Data": "Impormasyon tulad ng teksto, larawan, numero, o mga tala.",
    "DM": "Direct message, o pribadong mensahe sa isang tao sa isang platform.",
    "Download": "Pagkopya ng file mula sa internet papunta sa iyong device.",
    "Follower": "Taong sumusubaybay sa mga post ng isang account.",
    "FOMO": "Fear of missing out: pag-aalala na may magagandang karanasan ang iba na hindi mo nararanasan.",
    "IDK": "I don't know, o hindi ko alam.",
    "Influencer": "Taong may mga tagasubaybay online na maaaring maimpluwensiyahan ng kaniyang mga post o rekomendasyon.",
    "LOL": "Laugh out loud. Ginagamit upang ipakitang nakakatawa ang isang bagay.",
    "Phishing": "Panlolokong nagpapanggap na mapagkakatiwalaang tao o serbisyo upang nakawin ang iyong impormasyon.",
    "Python": "Isang programming language na ginagamit sa paggawa ng software at pagproseso ng data.",
    "QR code": "Parisukat na pattern na ini-scan gamit ang camera upang magbukas ng impormasyon. Suriin muna ang pupuntahang link.",
    "SMH": "Shaking my head. Nagpapahiwatig ng hindi makapaniwala o pagkadismaya.",
    "SUS": "Suspicious, o kahina-hinala. Balbal na tawag kapag tila hindi mapagkakatiwalaan ang isang bagay.",
    "Two-step verification": "Karagdagang pagsusuri sa pag-sign in pagkatapos ng password, tulad ng code o paalala mula sa authenticator app.",
    "Upload": "Pagpapadala ng file mula sa iyong device papunta sa isang online na serbisyo.",
    "Wi-Fi": "Wireless na koneksiyon sa pagitan ng iyong device at isang lokal na network.",
    "Yeet": "Balbal na salita para sa malakas na paghagis; ginagamit din minsan bilang pagpapahayag ng tuwa.",
    "YOLO": "You only live once, o minsan ka lang mabubuhay. Ginagamit sa pagsubok ng pagkakataon o pag-enjoy sa buhay.",
}

QUIZ_TL = {
    "A news story looks surprising. How can you check it before sharing?": {
        "topic": "Mapagkakatiwalaang impormasyon",
        "question": "Nakakagulat ang isang balita. Paano mo ito masusuri bago ibahagi?",
        "choices": ["Ibahagi kung marami itong like.", "Ihambing sa mga hiwalay at mapagkakatiwalaang sanggunian at tingnan ang petsa.", "Paniwalaan dahil ibinahagi ito ng kaibigan.", "Basahin lang ang pamagat."],
        "explanation": "Suriin ang pinagmulan, may-akda, petsa, at ebidensiya. Makatutulong ang mga hiwalay na ulat para matukoy ang mali o lumang impormasyon.",
    },
    "You are trying an unfamiliar app. What is a helpful first step?": {
        "topic": "Pag-aaral ng bagong app",
        "question": "Gumagamit ka ng app na hindi mo pa kilala. Ano ang makatutulong na unang hakbang?",
        "choices": ["Pindutin ang kahit anong button hanggang may mangyari.", "Iwasang gamitin ang app.", "Sundin ang panimulang gabay at magsanay sa paisa-isang gawain.", "Ibigay ang password para iba na ang gumawa."],
        "explanation": "Mas madaling matuto sa maliliit na hakbang. Gamitin ang opisyal na gabay ng app at humingi ng tulong sa taong pinagkakatiwalaan mo.",
    },
    "Which approach gives a new account stronger protection?": {
        "topic": "Mas ligtas na password",
        "question": "Alin ang mas makapagpoprotekta sa isang bagong account?",
        "choices": ["Gamitin muli ang password ng iyong email.", "Gamitin ang pangalan at kaarawan mo.", "Pumili ng mahaba at natatanging password at paganahin ang two-step verification.", "Gumamit ng maikling salita para madaling i-type."],
        "explanation": "Nalilimitahan ng natatanging password ang pinsala kung malantad ang datos ng ibang serbisyo. Makatutulong ang password manager, at may dagdag na proteksiyon ang two-step verification.",
    },
    "An unexpected message says you won a prize and asks you to open a link. What should you do?": {
        "topic": "Pagkilala sa panloloko",
        "question": "May di-inaasahang mensaheng nagsasabing nanalo ka at pinapabuksan ang isang link. Ano ang dapat mong gawin?",
        "choices": ["Buksan agad bago mawalan ng bisa ang premyo.", "Ipadala ang iyong personal na impormasyon.", "Ipasa sa lahat ng kakilala mo.", "Huwag buksan ang link; tiyakin sa opisyal na website o numero ng organisasyon."],
        "explanation": "Karaniwang panlilinlang ang pagmamadali at di-inaasahang premyo. Gumamit ng impormasyong pangkontak na ikaw mismo ang nakahanap, hindi ng nasa mensahe.",
    },
    "Social media is taking time away from things you enjoy. What could help?": {
        "topic": "Balanse sa paggamit ng teknolohiya",
        "question": "Nauubos sa social media ang oras para sa mga bagay na gusto mo. Ano ang makatutulong?",
        "choices": ["Magtakda ng araw-araw na limitasyon at oras na malayo sa screen.", "Patuloy na mag-scroll hanggang mapagod.", "Buksan ang lahat ng notification.", "Huwag pansinin ang oras na ginugugol dito."],
        "explanation": "Makatutulong ang mga limitasyon, mas kaunting notification, at regular na pahinga para makontrol ang oras online.",
    },
    "A friend shares a document in a collaboration tool you have never used. How can you begin?": {
        "topic": "Pagtutulungan online",
        "question": "May kaibigang nagbahagi ng dokumento sa tool na hindi mo pa nagagamit. Paano ka magsisimula?",
        "choices": ["Bigyan ang lahat ng buong access sa iyong account.", "Gamitin ang opisyal na gabay at magpaturo sa kaibigan ng mga unang hakbang.", "Mag-download ng di-kilalang tool mula sa pop-up.", "Ilagay ang iyong sign-in code sa dokumento."],
        "explanation": "Matuto gamit ang opisyal na gabay ng tool. Suriin ang mga pahintulot sa pagbabahagi at panatilihing pribado ang password at sign-in code.",
    },
    "A free app asks for access to your contacts, location, and photos. What should you do first?": {
        "topic": "Personal na impormasyon",
        "question": "Humihingi ang libreng app ng access sa contacts, lokasyon, at mga larawan mo. Ano ang una mong dapat gawin?",
        "choices": ["Awtomatikong payagan ang lahat.", "I-post sa publiko ang iyong impormasyon.", "Suriin kung bakit kailangan ang bawat pahintulot at tanggihan ang hindi kailangan.", "Isiping ligtas ang lahat ng libreng app."],
        "explanation": "Ibigay lang ang access na kailangan sa gawain. Basahin ang patakaran sa pagkapribado at isaalang-alang ang ibang app kung sobra ang hinihingi.",
    },
    "A viral video claims a scientific breakthrough. What is a useful way to evaluate it?": {
        "topic": "Pagsusuri ng viral na nilalaman",
        "question": "May viral na video tungkol sa malaking tuklas sa agham. Paano mo ito masusuri?",
        "choices": ["Paniwalaan dahil maraming nanood.", "Isiping peke ang lahat ng viral na video.", "Ibahagi para makakuha ng like.", "Hanapin ang orihinal na pananaliksik at ihambing sa paliwanag ng mga kwalipikadong sanggunian."],
        "explanation": "Hindi ebidensiya ang kasikatan. Hanapin ang orihinal na sanggunian at tamang kaalaman, at tingnan kung tugma ang sinasabi sa totoong resulta ng pananaliksik.",
    },
}

RESOURCES_TL = {
    "What can you do online?": ("Ano ang magagawa online?", "Mga pang-araw-araw na gamit ng internet, na ipinaliliwanag nang paisa-isang hakbang."),
    "A brief history of the internet": ("Maikling kasaysayan ng internet", "Alamin kung paano nagsimula ang mundong magkakaugnay online."),
    "Install apps on Android": ("Mag-install ng app sa Android", "Alamin kung paano maghanap at mag-install ng app mula sa Google Play."),
    "Getting started with Facebook": ("Pagsisimula sa Facebook", "Gabay sa profile, mga post, at pakikipag-ugnayan sa iba."),
    "Using Messenger": ("Paggamit ng Messenger", "Alamin ang mga batayan ng pagpapadala ng mensahe at pagtawag."),
    "Using YouTube": ("Paggamit ng YouTube", "Maghanap at manood ng mga video sa sarili mong bilis."),
    "Manila Bulletin": ("Manila Bulletin", "Basahin ang digital na edisyon ng pahayagan; maaaring kailangan ng subscription."),
    "Philippine Daily Inquirer": ("Philippine Daily Inquirer", "Basahin ang digital na pahayagan; maaaring kailangan ng subscription."),
    "The Manila Times": ("The Manila Times", "Tingnan ang mga balita at impormasyon sa nakalimbag na edisyon."),
    "Listen to Philippine radio": ("Makinig sa radyo sa Pilipinas", "Tuklasin ang mga estasyon ng radyo na mapakikinggan online."),
    "Being safe on the internet": ("Pagiging ligtas sa internet", "Magsimula sa mga batayan ng mas ligtas na paggamit ng internet."),
    "11 internet safety tips": ("11 tip sa kaligtasan sa internet", "Mga praktikal na paraan upang protektahan ang sarili at mga account."),
    "Online safety for grown ups": ("Kaligtasan online para sa matatanda", "Madaling panimula sa karaniwang mga panganib online."),
    "Digital literacy: staying safe": ("Kaalamang digital: manatiling ligtas", "Maging mas mapagmatyag habang ginagalugad ang digital na mundo."),
    "Internet slang explained": ("Paliwanag sa mga balbal sa internet", "Kilalanin ang mga ekspresyong maaari mong makita online."),
}

ROLES_TL = {
    "Project manager · Researcher · Programmer": "Tagapamahala ng proyekto · Mananaliksik · Programmer",
    "Project lead · UI/UX developer · Programmer": "Pinuno ng proyekto · UI/UX developer · Programmer",
    "Data analyst · Researcher · Programmer": "Tagasuri ng datos · Mananaliksik · Programmer",
    "Researcher · Programmer · Documentation": "Mananaliksik · Programmer · Tagapagtala",
    "Data analyst · Project manager · Programmer": "Tagasuri ng datos · Tagapamahala ng proyekto · Programmer",
}
