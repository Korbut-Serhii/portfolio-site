from flask import Flask, render_template

app = Flask(__name__)

# Main Page Route
@app.route('/')
def index():
    # Data for the main page
    categories = [
        {"id": "python", "title": "Python Projects", "desc": "Small scripts and experiments.", "icon": "fab fa-python"},
        {"id": "web", "title": "Full Stack Dev", "desc": "Web sites and applications.", "icon": "fas fa-code"},
        {"id": "other", "title": "Other Projects", "desc": "Other, uncategorized projects.", "icon": "fas fa-rocket"},
        {"id": "main", "title": "Main Global Project", "desc": "My main project is Project-Chatt", "icon": "fas fa-globe"}
    ]
    return render_template('index.html', categories=categories)

# Category Page Route
@app.route('/category/<cat_id>')
def category_page(cat_id):
    # Data for category pages
    content = {
        "python": {
            "title": "Python projects",
            "text": "I create small scripts and experiments to learn new libraries and concepts. These projects are not polished, but show my learning process.",
            "projects": [
                {"name": "Uncategorized Projects", "link": "https://github.com/Korbut-Serhii/Python-Projects"},
                {"name": "Tamagotchi - Small Game", "link": "https://github.com/Korbut-Serhii/Tamagotchi"},
                {"name": "ClipboardManager", "link": "https://github.com/Korbut-Serhii/ClipboardManager"},
                {"name": "MinLang Interpreter", "link": "https://github.com/Korbut-Serhii/MinLang"}
            ]
        },
        "web": {
            "title": "Full Stack Development",
            "text": "Creating different sites, apps on electron, games, interfaces and server logic (Node.js).",
            "projects": [
                {"name": "Pi-Monitor", "link": "https://github.com/Korbut-Serhii/pi-monitor"},
                {"name": "Site Showcase", "link": "https://github.com/Korbut-Serhii/Site-Showcase"},
                {"name": "File-Converter", "link": "https://github.com/Korbut-Serhii/File-Converter"},
                {"name": "Infinity-Puzzle", "link": "https://github.com/Korbut-Serhii/Infinity-Puzzle"},
                {"name": "SoftPad", "link": "https://github.com/Korbut-Serhii/SoftPad"},
                {"name": "Chroma App", "link": "https://github.com/Korbut-Serhii/Chroma"},
                {"name": "Wallpaper Manager", "link": "https://github.com/Korbut-Serhii/wallpaper-manager"}
            ]
        },
        "other": {
            "title": "Other Projects",
            "text": "Other, uncategorized projects that I have worked on. These projects may not fit into the other categories, but they are still important to me and show my versatility as a developer.",
            "projects": [
                {"name": "Arduino Projects", "link": "https://github.com/Korbut-Serhii/Arduino-Projects"},
                {"name": "Rust-Server", "link": "https://github.com/Korbut-Serhii/rust-server"},
                {"name": "Rust-P2P_Chat", "link": "https://github.com/Korbut-Serhii/p2p_Chat"}
            ]
        }
        ,
        "main": {
            "title": "Main Global Project",
            "text": "Project-Chatt - is a project that I am currently working on. It is a chat application that allows users to communicate with each other in real-time. The project is still in development, but I am excited to share it with the world once it is complete. It uses "
            "electron for app. Server on Node.js. I am learning a lot from this project and I am looking forward to seeing it come to life.",
            "projects": [
                {"name": "Youtube Video", "link": "https://www.youtube.com/"},
                {"name": "Main Page", "link": "https://weksar.duckdns.org/"}
            ]
        }
    }
    
    data = content.get(cat_id)
    if not data:
        return "Page not Found", 404
        
    return render_template('category.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
