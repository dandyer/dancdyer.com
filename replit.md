# Dan Dyer Portfolio Website

## Project Overview
A personal portfolio website for Dan Dyer — AI entrepreneur and builder. A clean, modern, single-page static site showcasing his background, AI/SaaS projects (Jobkeepr, AnalyticLunch), and contact information.

## Tech Stack
- **HTML5** — semantic markup (`index.html`)
- **CSS3** — custom styles, Flexbox/Grid layout, animations (`styles.css`)
- **Google Fonts** — Inter font family via CDN
- **No build system or package manager** — pure static files

## Project Structure
```
index.html      # Main entry point
styles.css      # All styling
images/
  dan.jpg       # Profile photo
```

## Development
The site is served using Python's built-in HTTP server on port 5000:
```
python3 -m http.server 5000 --bind 0.0.0.0
```

The workflow "Start application" is configured to run this command automatically.

## Deployment
Configured as a **static** deployment with `publicDir: "."` — the root directory is served directly.
