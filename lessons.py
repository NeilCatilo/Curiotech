"""Original, offline step-by-step guides. Links are optional further reading."""

from content import ARTICLES

# Each pair is (English, Tagalog); URLs and publisher names come from the catalogue.
_TEXT = {
    "What can you do online?": {
        "intro": ("Use the internet to find information, keep in touch, and learn something new. Start with one small task.", "Gamitin ang internet para maghanap ng impormasyon, makipag-ugnayan, at matuto. Magsimula sa isang maliit na gawain."),
        "steps": [
            ("Connect your phone to a trusted Wi-Fi network or turn on mobile data. Mobile data may have charges.", "Ikonekta ang telepono sa pinagkakatiwalaang Wi-Fi o buksan ang mobile data. Maaaring may bayad ang mobile data."),
            ("Open your browser, such as Chrome, and type a question into its search field.", "Buksan ang browser, tulad ng Chrome, at i-type ang tanong sa search field."),
            ("Read the website name before opening a result. Prefer an official organisation or a source you recognise.", "Basahin ang pangalan ng website bago buksan ang resulta. Piliin ang opisyal na organisasyon o sangguniang kilala mo."),
            ("Check the author and date. Compare important information with another reliable source before acting on it.", "Suriin ang may-akda at petsa. Ihambing ang mahalagang impormasyon sa isa pang maaasahang sanggunian bago kumilos."),
        ],
        "tip": ("Practise by searching for tomorrow's weather. You do not need to give a website your password to read a weather forecast.", "Magsanay sa paghahanap ng lagay ng panahon bukas. Hindi mo kailangang ibigay ang password para magbasa ng ulat-panahon."),
    },
    "A brief history of the internet": {
        "intro": ("The internet connects networks around the world. The web is one service on it, used to visit websites through a browser.", "Pinag-uugnay ng internet ang mga network sa buong mundo. Ang web ay isang serbisyo rito para bumisita sa mga website gamit ang browser."),
        "steps": [
            ("Find the browser app on your phone. Its job is to open websites; it is different from your Wi-Fi connection.", "Hanapin ang browser app sa iyong telepono. Nagbubukas ito ng website at iba ito sa koneksiyon mong Wi-Fi."),
            ("Look at the address field when you open a page. The website address identifies the site you are visiting.", "Tingnan ang address field kapag nagbukas ng pahina. Ipinapakita ng web address kung aling site ang binibisita mo."),
            ("Try opening a trusted website. If it does not load, check your connection before changing account settings.", "Subukang magbukas ng pinagkakatiwalaang website. Kung hindi ito mag-load, suriin muna ang koneksiyon bago baguhin ang account settings."),
        ],
        "tip": ("Wi-Fi, the internet, and a browser do different jobs. The optional link explains how the internet developed.", "Magkakaiba ang gawain ng Wi-Fi, internet, at browser. Ipinapaliwanag ng opsiyonal na link kung paano nabuo ang internet."),
    },
    "Install apps on Android": {
        "intro": ("Use Google Play to find an app and review it before installation. Buttons may differ slightly by phone.", "Gamitin ang Google Play para maghanap at suriin ang app bago i-install. Maaaring bahagyang mag-iba ang mga button sa bawat telepono."),
        "steps": [
            ("Open Google Play and search for the app's name.", "Buksan ang Google Play at hanapin ang pangalan ng app."),
            ("Check the developer, description, ratings, and any price. Similar names do not always mean the same app.", "Tingnan ang developer, paglalarawan, rating, at presyo. Hindi lahat ng magkapangalan ay iisang app."),
            ("If it is the app you want, choose Install. If there is a price, review it before confirming a purchase.", "Kung ito ang gusto mong app, piliin ang Install. Kung may presyo, suriin muna bago kumpirmahin ang pagbili."),
            ("Open the app after installation. Allow only permissions that make sense for what you want to do.", "Buksan ang app pagkatapos ma-install. Payagan lang ang mga pahintulot na kailangan sa nais mong gawin."),
        ],
        "tip": ("Do not install an unfamiliar app just because a pop-up says your phone is infected.", "Huwag mag-install ng di-kilalang app dahil lang may pop-up na nagsasabing may virus ang telepono."),
    },
    "Getting started with Facebook": {
        "intro": ("Practise reading and sharing while choosing who can see your information.", "Magsanay sa pagbabasa at pagbabahagi habang pinipili kung sino ang makakakita ng iyong impormasyon."),
        "steps": [
            ("Open the official Facebook app or website and sign in to your own account.", "Buksan ang opisyal na Facebook app o website at mag-sign in sa sarili mong account."),
            ("Read a post from someone you know. Check the source before sharing information from it.", "Magbasa ng post mula sa kakilala. Suriin ang pinagmulan bago ibahagi ang impormasyon rito."),
            ("Before posting, review the audience setting and choose the people you want to share with.", "Bago mag-post, suriin ang audience setting at piliin kung kanino mo ito ibabahagi."),
            ("Review privacy settings and keep passwords, sign-in codes, and personal documents out of public posts.", "Suriin ang privacy settings at huwag ilagay sa pampublikong post ang password, sign-in code, at personal na dokumento."),
        ],
        "tip": ("A familiar profile photo does not prove who is messaging you. Verify unusual requests using another contact method.", "Hindi sapat ang pamilyar na profile picture para makilala ang kausap. Tiyakin ang kakaibang kahilingan gamit ang ibang paraan ng pakikipag-ugnayan."),
    },
    "Using Messenger": {
        "intro": ("Start with a short message to someone you already know.", "Magsimula sa maikling mensahe para sa taong kilala mo na."),
        "steps": [
            ("Open Messenger and find the conversation with your contact, or search for their name.", "Buksan ang Messenger at hanapin ang usapan sa iyong kakilala, o hanapin ang kaniyang pangalan."),
            ("Check that you selected the correct person, especially if several profiles have the same name.", "Tiyaking tamang tao ang napili, lalo na kung maraming magkapangalan."),
            ("Type a short greeting, read it once, then use the send button.", "Mag-type ng maikling pagbati, basahin muna ito, saka pindutin ang send."),
            ("For a call, use the voice or video call control in the conversation. End the call when you are finished.", "Para tumawag, gamitin ang voice o video call control sa usapan. Tapusin ang tawag kapag tapos na."),
        ],
        "tip": ("Never send a sign-in code or password in a message, even if someone claims to be support staff.", "Huwag magpadala ng sign-in code o password sa mensahe, kahit may magpakilalang support staff."),
    },
    "Using YouTube": {
        "intro": ("Find a useful video, then pause or repeat any part you want to practise.", "Maghanap ng kapaki-pakinabang na video, saka i-pause o ulitin ang bahaging gusto mong pag-aralan."),
        "steps": [
            ("Open YouTube and search for a topic, such as how to use your phone's camera.", "Buksan ang YouTube at maghanap ng paksa, tulad ng paggamit ng camera ng telepono."),
            ("Check the channel and title, then choose a video that matches your task.", "Suriin ang channel at pamagat, saka pumili ng video na tugma sa gawain."),
            ("Tap the video to show playback controls. Pause before trying a step on your own device.", "Pindutin ang video para makita ang mga control. I-pause muna bago subukan ang hakbang sa sarili mong device."),
            ("Look for captions in the player controls or settings. Available languages depend on the publisher.", "Hanapin ang mga caption sa player controls o settings. Nakasalalay sa gumawa ang mga magagamit na wika."),
        ],
        "tip": ("A video can be popular and still be misleading. Compare important advice with an official source.", "Maaaring sikat ang video pero mali pa rin ang impormasyon. Ihambing ang mahalagang payo sa opisyal na sanggunian."),
    },
    "Manila Bulletin": {
        "intro": ("A digital newspaper lets you browse an edition on your device. Access to some editions may require payment.", "Mababasa sa device ang digital na pahayagan. Maaaring may bayad ang ilang edisyon."),
        "steps": [
            ("Open the newspaper's official digital-edition service when you are connected to the internet.", "Buksan ang opisyal na serbisyo ng digital na edisyon kapag may internet."),
            ("Check the issue date so you know whether you are reading today's news or an older edition.", "Tingnan ang petsa ng edisyon para malaman kung bago o lumang balita ang binabasa."),
            ("Select a headline to read. Review any subscription price before entering payment details.", "Pumili ng pamagat na babasahin. Suriin muna ang presyo ng subscription bago magbigay ng detalye sa pagbabayad."),
        ],
        "tip": ("You can read these app instructions for free; an external newspaper may have its own subscription.", "Libre ang mga gabay sa app na ito; maaaring may sariling subscription ang panlabas na pahayagan."),
    },
    "Philippine Daily Inquirer": {
        "intro": ("Use the digital edition to browse newspaper pages, with attention to dates and access charges.", "Gamitin ang digital na edisyon para magbasa ng pahayagan, habang sinusuri ang petsa at posibleng bayarin."),
        "steps": [
            ("Visit the official digital-edition page using the optional link below.", "Bisitahin ang opisyal na pahina ng digital na edisyon gamit ang opsiyonal na link sa ibaba."),
            ("Choose the edition you want and check its date before reading.", "Piliin ang nais na edisyon at tingnan ang petsa bago basahin."),
            ("Review any sign-in or subscription requirement. Stop if you do not want to create an account or pay.", "Suriin kung kailangan ng sign-in o subscription. Huminto kung ayaw mong gumawa ng account o magbayad."),
        ],
        "tip": ("A screenshot of a headline may leave out important context. Read the full story and check the date.", "Maaaring kulang ang konteksto sa screenshot ng pamagat. Basahin ang buong balita at tingnan ang petsa."),
    },
    "The Manila Times": {
        "intro": ("Read news with attention to the source, date, and distinction between reporting and opinion.", "Magbasa ng balita habang sinusuri ang pinagmulan, petsa, at pagkakaiba ng ulat at opinyon."),
        "steps": [
            ("Open the newspaper's official website and find a section or story of interest.", "Buksan ang opisyal na website ng pahayagan at pumili ng seksiyon o balita."),
            ("Check the publication date, author, and whether the article is labelled opinion.", "Tingnan ang petsa, may-akda, at kung may tatak na opinyon ang artikulo."),
            ("Read beyond the headline. Compare important claims with another reliable report before sharing.", "Basahin ang higit pa sa pamagat. Ihambing ang mahahalagang pahayag sa isa pang maaasahang ulat bago ibahagi."),
        ],
        "tip": ("If a payment or subscription prompt appears, review its terms before agreeing.", "Kung may hiling na bayad o subscription, suriin muna ang mga kondisyon bago pumayag."),
    },
    "Listen to Philippine radio": {
        "intro": ("Listen to an online station through its player. Streaming uses an internet connection.", "Makinig sa online na estasyon gamit ang player nito. Kailangan ng internet sa streaming."),
        "steps": [
            ("Choose a station you recognise from the radio directory or the station's own website.", "Pumili ng estasyong kilala mo sa listahan ng radyo o sa sariling website ng estasyon."),
            ("Use the station's play control and adjust your phone's media volume to a comfortable level.", "Gamitin ang play control ng estasyon at ayusin ang media volume sa komportableng lakas."),
            ("Pause or stop the stream when finished, especially if you are using paid mobile data.", "I-pause o ihinto ang stream kapag tapos na, lalo na kung may bayad ang mobile data."),
        ],
        "tip": ("Avoid download buttons in advertisements. A browser-based radio player usually does not need a separate app.", "Iwasan ang download button sa mga patalastas. Karaniwang hindi kailangan ng hiwalay na app para sa radio player sa browser."),
    },
}

GUIDES = []
LESSON_TRANSLATIONS = {}
for index, (category, title, summary, publisher, url) in enumerate(ARTICLES):
    text = _TEXT[title]
    for english, tagalog in [text["intro"], text["tip"], *text["steps"]]:
        LESSON_TRANSLATIONS[english] = tagalog
    GUIDES.append({"id": f"guide-{index + 1}", "category": category, "title": title,
                   "summary": summary, "publisher": publisher, "url": url,
                   "intro": text["intro"][0], "steps": [pair[0] for pair in text["steps"]],
                   "tip": text["tip"][0]})


def get_guide(guide_id):
    return next((guide for guide in GUIDES if guide["id"] == guide_id), None)
