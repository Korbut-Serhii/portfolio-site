# My Portfolio

A personal portfolio website built with **Flask** (Python) to showcase GitHub projects, organized by category. Features a clean responsive design with light/dark theme switching.

## Preview

The site displays project categories on the main page. Each category links to a detail page listing individual projects with direct GitHub links.

## Tech Stack

- **Backend:** Python / Flask
- **Frontend:** HTML, CSS, JavaScript (Vanilla)
- **Icons:** Font Awesome 6

## Project Structure

```
portfolio/
├── app.py                  # Flask app & routes
├── templates/
│   ├── base.html           # Base layout with navbar
│   ├── index.html          # Main page (category grid)
│   └── category.html       # Category detail page
└── static/
    ├── css/
    │   └── style.css       # Styles + dark/light theme
    └── js/
        └── script.js       # Theme toggle logic
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Korbut-Serhii/portfolio-site
cd portfolio-site
```

**2. Create and activate a virtual environment** (recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install flask
```

**4. Run the development server**

```bash
python app.py
```

**5. Open in your browser**

```
http://127.0.0.1:5000
```

The site will hot-reload automatically on code changes since debug mode is enabled.

## Features

- Categorized project showcase (Python, Web, Other, Main Project)
- Direct links to GitHub repositories
- Light / Dark theme toggle — preference is saved in `localStorage`
- Fully responsive layout (desktop, tablet, mobile)
- Clean card-based UI with hover animations

## Adding New Projects

Open `app.py` and find the `content` dictionary inside the `category_page` route. Add a new entry to the relevant category's `projects` list:

```python
{"name": "Your Project Name", "link": "https://github.com/your-username/your-repo"}
```

To add an entirely new category, add it to both the `categories` list in the `index()` route and the `content` dictionary in `category_page()`.

## License

This project is open source and available under the [MIT License](LICENSE).
