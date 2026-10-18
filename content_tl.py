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
    "You are reading a news article online, but you’re unsure if the website is trustworthy. What should you do?": {
        "topic": "Pagkilala sa mapagkakatiwalaang impormasyon online",
        "question": "Nagbabasa ka ng balita online, pero hindi ka sigurado kung mapagkakatiwalaan ang website. Ano ang dapat mong gawin?",
        "choices": [
            "Ibahagi agad ang balita sa social media nang hindi sinusuri.",
            "Tingnan ang pahinang \"About Us\" at ang impormasyon tungkol sa mga may-akda.",
            "Maghanap ng kaparehong balita sa mga mapagkakatiwalaang plataporma ng balita.",
            "Gamitin ang dami ng like at komento para malaman kung kapani-paniwala ito."
        ],
        "explanation": "Suriin ang pinagmulan, may-akda, petsa, at ebidensiya. Makatutulong ang mga hiwalay na ulat para matukoy ang mali o lumang impormasyon."
    },
    "Your workplace has introduced new project management software, but you are unfamiliar with it. How should you approach learning it?": {
        "topic": "Pag-aaral ng bagong software",
        "question": "May bagong software para sa pamamahala ng proyekto sa trabaho, pero hindi mo pa ito alam gamitin. Paano mo ito pag-aaralan?",
        "choices": [
            "Pindutin ang kahit anong button hanggang matutuhan mo ito.",
            "Manood ng mga tutorial at basahin ang gabay ng software.",
            "Hintaying may ibang magturo sa iyo kung paano ito gamitin.",
            "Iwasan ang software at gamitin na lang ang dating paraan."
        ],
        "explanation": "Mas madaling matuto sa maliliit na hakbang. Gamitin ang opisyal na gabay ng app at humingi ng tulong sa taong pinagkakatiwalaan mo."
    },
    "You need to create a new password for your online bank account. What is the most secure approach?": {
        "topic": "Pagpapalakas ng seguridad ng password",
        "question": "Kailangan mong gumawa ng bagong password para sa iyong online bank account. Alin ang pinakaligtas na paraan?",
        "choices": [
            "Gamitin ang pangalan at kaarawan mo para madaling tandaan.",
            "Pumili ng mahaba at random na kombinasyon ng mga letra, numero, at espesyal na karakter.",
            "Gamitin ang password na ginagamit mo sa ibang website.",
            "Isulat ang password sa sticky note at idikit sa monitor ng computer."
        ],
        "explanation": "Nalilimitahan ng natatanging password ang pinsala kung malantad ang datos ng ibang serbisyo. Makatutulong ang password manager, at may dagdag na proteksiyon ang two-step verification."
    },
    "You receive an email claiming you’ve won a cash prize but need to provide personal information to claim it. What should you do?": {
        "topic": "Pag-iwas sa panloloko online",
        "question": "Nakatanggap ka ng email na nagsasabing nanalo ka ng pera, pero kailangan mong magbigay ng personal na impormasyon para makuha ito. Ano ang dapat mong gawin?",
        "choices": [
            "Ibigay agad ang hinihinging impormasyon.",
            "Burahin ang email at i-block ang nagpadala.",
            "Pindutin ang link para mag-imbestiga.",
            "Sumagot at humingi ng dagdag na detalye tungkol sa premyo."
        ],
        "explanation": "Karaniwang panlilinlang ang pagmamadali at di-inaasahang premyo. Gumamit ng impormasyong pangkontak na ikaw mismo ang nakahanap, hindi ng nasa mensahe."
    },
    "You notice you are spending too much time on social media, affecting your productivity. What would be the best course of action?": {
        "topic": "Balanse sa paggamit ng teknolohiya",
        "question": "Napapansin mong sobra ang oras mo sa social media at naaapektuhan ang iyong mga gawain. Ano ang pinakamainam mong gawin?",
        "choices": [
            "Patayin nang tuluyan ang telepono habang nagtatrabaho.",
            "Magtakda ng tiyak na limitasyon sa oras ng paggamit ng mga social media app.",
            "Permanenteng alisin ang lahat ng social media app.",
            "Huwag pansinin ang problema at umasang kusa itong mawawala."
        ],
        "explanation": "Makatutulong ang mga limitasyon, mas kaunting notification, at regular na pahinga para makontrol ang oras online."
    },
    "You’re working on a group project, and a teammate shares a document for collaboration on a platform you’ve never used before. How do you handle this?": {
        "topic": "Pag-unawa sa pagtutulungan online",
        "question": "May pangkatang proyekto kayo at nagbahagi ang kasama mo ng dokumento sa platapormang hindi mo pa nagagamit. Paano ka kikilos?",
        "choices": [
            "Hilingin sa kasama na gumamit ng platapormang alam mo na.",
            "Tuklasin ang plataporma, gamitin ang tulong nito, at humingi ng tip sa mga kasama.",
            "Huwag munang makilahok hanggang may mag-upload ng pinal na bersiyon.",
            "I-print ang dokumento at magbigay na lang ng puna nang personal."
        ],
        "explanation": "Matuto gamit ang opisyal na gabay ng tool. Suriin ang mga pahintulot sa pagbabahagi at panatilihing pribado ang password at sign-in code."
    },
    "You are signing up for a free online service, and it asks for extensive personal information, including your address and phone number. What is the best response?": {
        "topic": "Pagprotekta sa personal na datos",
        "question": "Nagsa-sign up ka sa libreng serbisyong online at humihingi ito ng maraming personal na impormasyon, pati address at numero ng telepono. Ano ang pinakamainam na tugon?",
        "choices": [
            "Ibigay ang lahat ng impormasyon para magamit ang serbisyo.",
            "Huwag ituloy ang pag-sign up at maghanap ng ibang plataporma.",
            "Basahin ang patakaran sa pagkapribado para malaman kung paano gagamitin ang iyong datos.",
            "Gumamit ng pekeng impormasyon sa paggawa ng account."
        ],
        "explanation": "Ibigay lang ang access na kailangan sa gawain. Basahin ang patakaran sa pagkapribado at isaalang-alang ang ibang app kung sobra ang hinihingi."
    },
    "A video on social media is going viral, claiming a groundbreaking scientific discovery. How do you verify its authenticity?": {
        "topic": "Pagsusuri ng nilalaman sa media",
        "question": "May viral na video sa social media na nagsasabing may malaking bagong tuklas sa agham. Paano mo susuriin kung totoo ito?",
        "choices": [
            "Paniwalaan dahil marami itong panonood at pagbabahagi.",
            "Suriin ang kredensiyal ng pinagmulan at maghanap ng mga artikulong sinuri ng kapwa eksperto.",
            "Isiping peke dahil hindi mapagkakatiwalaan ang karamihan sa viral na nilalaman.",
            "Ibahagi sa mga kaibigan para makuha ang kanilang opinyon."
        ],
        "explanation": "Hindi ebidensiya ang kasikatan. Hanapin ang orihinal na sanggunian at tamang kaalaman, at tingnan kung tugma ang sinasabi sa totoong resulta ng pananaliksik."
    }
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
