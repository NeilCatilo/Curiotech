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
    {
        "topic": "Identifying Reliable Information Online",
        "question": "You are reading a news article online, but you’re unsure if the website is trustworthy. What should you do?",
        "choices": [
            "Share the article on social media without verifying it.",
            "Check the website’s 'About Us' page and look for information about the authors.",
            "Search for similar articles on reputable news platforms.",
            "Rely on the number of likes and comments to judge its credibility."
        ],
        "answer": 1,
        "explanation": "Check the source, author, date, and supporting evidence. Independent coverage helps you spot misleading or outdated claims."
    },
    {
        "topic": "Using New Software Tools",
        "question": "Your workplace has introduced new project management software, but you are unfamiliar with it. How should you approach learning it?",
        "choices": [
            "Experiment with random buttons until you figure it out.",
            "Watch tutorials and review the software's user guide.",
            "Wait for someone else to teach you how to use it.",
            "Avoid using the software and stick to old methods."
        ],
        "answer": 1,
        "explanation": "Small steps make learning manageable. Use the app's official help and ask someone you trust when you need support."
    },
    {
        "topic": "Strengthening Password Security",
        "question": "You need to create a new password for your online bank account. What is the most secure approach?",
        "choices": [
            "Use your name and birthdate so it’s easy to remember.",
            "Choose a long, random combination of letters, numbers, and special characters.",
            "Use the same password you’ve used on other websites.",
            "Write the password on a sticky note and attach it to your computer monitor."
        ],
        "answer": 1,
        "explanation": "A unique password limits the damage if another service is breached. A password manager can help, and two-step verification adds protection."
    },
    {
        "topic": "Avoiding Online Scams",
        "question": "You receive an email claiming you’ve won a cash prize but need to provide personal information to claim it. What should you do?",
        "choices": [
            "Immediately provide the requested information.",
            "Delete the email and block the sender.",
            "Click on the link to investigate further.",
            "Reply asking for more details about the prize."
        ],
        "answer": 1,
        "explanation": "Urgency and unexpected prizes are common scam tactics. Use contact details you find independently, rather than those inside the message."
    },
    {
        "topic": "Managing Digital Well-being",
        "question": "You notice you are spending too much time on social media, affecting your productivity. What would be the best course of action?",
        "choices": [
            "Turn off your phone completely during work hours.",
            "Set specific time limits for using social media apps.",
            "Uninstall all social media apps permanently.",
            "Ignore the problem and hope it resolves itself."
        ],
        "answer": 1,
        "explanation": "Small boundaries, fewer notifications, and regular breaks can help you stay in control of your time online."
    },
    {
        "topic": "Understanding Digital Collaboration",
        "question": "You’re working on a group project, and a teammate shares a document for collaboration on a platform you’ve never used before. How do you handle this?",
        "choices": [
            "Request the teammate to use a platform you’re comfortable with.",
            "Explore the platform, use its help feature, and ask teammates for tips.",
            "Avoid participating until someone else uploads the final version.",
            "Print the document and provide feedback in person instead."
        ],
        "answer": 1,
        "explanation": "Learn through the tool's official guidance. Check sharing permissions and keep passwords and sign-in codes private."
    },
    {
        "topic": "Protecting Personal Data",
        "question": "You are signing up for a free online service, and it asks for extensive personal information, including your address and phone number. What is the best response?",
        "choices": [
            "Provide all the information to access the service.",
            "Skip signing up and look for alternative platforms.",
            "Read the privacy policy to understand how your data will be used.",
            "Use false information to create the account."
        ],
        "answer": 2,
        "explanation": "Only grant access that is needed for the task. Review the privacy policy and consider another app if the request seems excessive."
    },
    {
        "topic": "Evaluating Media Content",
        "question": "A video on social media is going viral, claiming a groundbreaking scientific discovery. How do you verify its authenticity?",
        "choices": [
            "Believe it because it has many views and shares.",
            "Check the credentials of the source and look for peer-reviewed articles.",
            "Assume it's fake because most viral content is unreliable.",
            "Share it with friends to get their opinions."
        ],
        "answer": 1,
        "explanation": "Popularity is not evidence. Look for original sources, relevant expertise, and whether the claim matches what the research actually found."
    }
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
