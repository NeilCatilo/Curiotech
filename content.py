"""Curated offline content. External resources open in the user's browser."""

TERMS = [
    {"term": term, "meaning": meaning, "category": category}
    for term, meaning, category in [
        ("Account", "Your personal profile on an app or website, usually protected by a password.", "Technology"),
        ("App", "A program on a phone, tablet, or computer that helps you do a task.", "Technology"),
        ("Avatar", "A picture or character that represents you online.", "Technology"),
        ("BAE", "An affectionate word for a partner or someone special.", "Slang"),
        ("BRB", "Be right back. A quick way to say you are stepping away briefly.", "Abbreviations"),
        ("Browser", "An app for visiting websites, such as Chrome, Edge, or Firefox.", "Technology"),
        ("Cloud", "Files stored on internet-connected servers so you can access them from different devices.", "Technology"),
        ("Data", "Information such as text, photos, numbers, or records.", "Technology"),
        ("DM", "Direct message. A private message to another person on a platform.", "Abbreviations"),
        ("Download", "Copy a file from the internet to your device.", "Technology"),
        ("Follower", "Someone who subscribes to see an account's posts.", "Technology"),
        ("FOMO", "Fear of missing out: worry that others are having experiences you are missing.", "Abbreviations"),
        ("IDK", "I don't know.", "Abbreviations"),
        ("Influencer", "Someone whose online audience may be influenced by their posts or recommendations.", "Technology"),
        ("LOL", "Laugh out loud. Often used to show that something is funny.", "Abbreviations"),
        ("Phishing", "A scam that imitates a trusted person or service to steal your details.", "Technology"),
        ("Python", "A programming language people use to create software and work with data.", "Technology"),
        ("QR code", "A square pattern you can scan with a camera to open information. Check the destination before continuing.", "Technology"),
        ("SMH", "Shaking my head. Used to express disbelief or disappointment.", "Abbreviations"),
        ("SUS", "Suspicious. Slang used when something seems untrustworthy.", "Slang"),
        ("Two-step verification", "An extra sign-in check after your password, such as a code or an authenticator prompt.", "Technology"),
        ("Upload", "Send a file from your device to an online service.", "Technology"),
        ("Wi-Fi", "A wireless connection between your device and a local network.", "Technology"),
        ("Yeet", "Slang for throwing something with force; sometimes an expression of excitement.", "Slang"),
        ("YOLO", "You only live once. Used to express taking a chance or enjoying life.", "Abbreviations"),
    ]
]

QUESTIONS = [
    {"topic": "Trustworthy information", "question": "A news story looks surprising. How can you check it before sharing?",
     "choices": ["Share it if it has many likes.", "Compare it with independent, reputable sources and check the date.", "Trust it because a friend shared it.", "Read only the headline."], "answer": 1,
     "explanation": "Check the source, author, date, and supporting evidence. Independent coverage helps you spot misleading or outdated claims."},
    {"topic": "Learning a new app", "question": "You are trying an unfamiliar app. What is a helpful first step?",
     "choices": ["Tap random buttons until something happens.", "Avoid the app entirely.", "Follow its getting-started guide and practise one task at a time.", "Share your password so someone else can do it."], "answer": 2,
     "explanation": "Small steps make learning manageable. Use the app's official help and ask someone you trust when you need support."},
    {"topic": "Safer passwords", "question": "Which approach gives a new account stronger protection?",
     "choices": ["Reuse the password from your email.", "Use your name and birthday.", "Choose a long, unique password and enable two-step verification.", "Use a short word so it is easy to type."], "answer": 2,
     "explanation": "A unique password limits the damage if another service is breached. A password manager can help, and two-step verification adds protection."},
    {"topic": "Spotting scams", "question": "An unexpected message says you won a prize and asks you to open a link. What should you do?",
     "choices": ["Open it quickly before the prize expires.", "Reply with your personal details.", "Forward it to everyone you know.", "Avoid the link; verify through the organisation's official website or phone number."], "answer": 3,
     "explanation": "Urgency and unexpected prizes are common scam tactics. Use contact details you find independently, rather than those inside the message."},
    {"topic": "Digital balance", "question": "Social media is taking time away from things you enjoy. What could help?",
     "choices": ["Set a daily limit and plan time away from the screen.", "Keep scrolling until you feel tired.", "Turn on every notification.", "Ignore how much time you spend."], "answer": 0,
     "explanation": "Small boundaries, fewer notifications, and regular breaks can help you stay in control of your time online."},
    {"topic": "Working together", "question": "A friend shares a document in a collaboration tool you have never used. How can you begin?",
     "choices": ["Give everyone full access to your account.", "Use the official help and ask your friend to show you the first steps.", "Download an unknown tool from a pop-up.", "Share your sign-in code in the document."], "answer": 1,
     "explanation": "Learn through the tool's official guidance. Check sharing permissions and keep passwords and sign-in codes private."},
    {"topic": "Personal information", "question": "A free app asks for access to your contacts, location, and photos. What should you do first?",
     "choices": ["Allow everything automatically.", "Post your details publicly.", "Check why each permission is needed and decline unnecessary access.", "Assume every free app is safe."], "answer": 2,
     "explanation": "Only grant access that is needed for the task. Review the privacy policy and consider another app if the request seems excessive."},
    {"topic": "Checking viral content", "question": "A viral video claims a scientific breakthrough. What is a useful way to evaluate it?",
     "choices": ["Believe it because it has many views.", "Assume every viral video is false.", "Share it to ask for likes.", "Find the original research and compare it with explanations from qualified sources."], "answer": 3,
     "explanation": "Popularity is not evidence. Look for original sources, relevant expertise, and whether the claim matches what the research actually found."},
]

ARTICLES = [
    ("Internet basics", "What can you do online?", "Everyday ways to use the internet, explained step by step.", "GCFGlobal", "https://edu.gcfglobal.org/en/internetbasics/what-can-you-do-online/1/"),
    ("Internet basics", "A brief history of the internet", "Understand how the connected world began.", "Internet Society", "https://www.internetsociety.org/internet/history-internet/"),
    ("App guides", "Install apps on Android", "Learn how to find and install apps from Google Play.", "Google Help", "https://support.google.com/android/answer/9457058?hl=en"),
    ("App guides", "Getting started with Facebook", "A guide to profiles, posts, and connecting with people.", "HubSpot", "https://blog.hubspot.com/marketing/how-to-use-facebook"),
    ("App guides", "Using Messenger", "Learn the basics of sending messages and making calls.", "wikiHow", "https://www.wikihow.com/Use-Facebook-Messenger"),
    ("App guides", "Using YouTube", "Find and watch videos at your own pace.", "Lifewire", "https://www.lifewire.com/how-to-use-youtube-2655498"),
    ("News & radio", "Manila Bulletin", "Browse the newspaper's digital edition; a subscription may be required.", "PressReader", "https://manilabulletin.pressreader.com/"),
    ("News & radio", "Philippine Daily Inquirer", "Browse the digital newspaper; a subscription may be required.", "PressReader", "https://philippinedailyinquirerplus.pressreader.com/"),
    ("News & radio", "The Manila Times", "Find print-edition information and news.", "The Manila Times", "https://www.manilatimes.net/print-edition"),
    ("News & radio", "Listen to Philippine radio", "Explore radio stations available online.", "Radio Philippines", "https://www.radio-philippines.com/"),
]

VIDEOS = [
    ("Online safety", "Being safe on the internet", "Start with the basics of staying safer online.", "HxySrSbSY7o", "Images/img.png"),
    ("Online safety", "11 internet safety tips", "Practical habits for protecting yourself and your accounts.", "aO858HyFbKI", "Images/img_1.png"),
    ("Online safety", "Online safety for grown ups", "A friendly introduction to common online risks.", "iCs3aJYXLwo", "Images/img_2.png"),
    ("Online safety", "Digital literacy: staying safe", "Build awareness as you explore the digital world.", "EyQeUwqCDWg", "Images/img_3.png"),
    ("Everyday language", "Internet slang explained", "Get familiar with expressions you may see online.", "PVnrDHHJwHM", "Images/img_4.png"),
]

TEAM = [
    ("Annessa Acar", "Project manager · Researcher · Programmer", "Images/ACAR.jpg"),
    ("Neil Catilo", "Project lead · UI/UX developer · Programmer", "Images/Neil.jpg"),
    ("John Delen", "Data analyst · Researcher · Programmer", "Images/Delen.jpg"),
    ("Kelly Gonzalez", "Researcher · Programmer · Documentation", "Images/Gonzalez.jpg"),
    ("Djohn Jared Larios", "Data analyst · Project manager · Programmer", "Images/Jared.jpg"),
]
