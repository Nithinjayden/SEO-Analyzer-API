# 🚀 Ultimate SEO Analyzer API

[![RapidAPI](https://img.shields.io/badge/Get%20on-RapidAPI-00bfff?logo=cloudflare&logoColor=white)](https://rapidapi.com/KovalDenys1/api/ultimate-seo-analyzer)  
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)  
[![License](https://img.shields.io/badge/License-Proprietary-red)](#-license)

A professional **SEO analysis API** that helps developers, marketers, and businesses analyze any website in seconds.  
Get insights about titles, meta tags, headings, links, images, keyword density, page load time, SEO warnings, and an overall SEO score.

![SEO Analyzer Banner](Logo.png)

---

## 🔍 Key Features
- Extract **page metadata** (title, description, keywords)  
- Analyze **H1/H2 headings**  
- Separate **internal & external links**  
- Audit **images with/without alt**  
- Measure **keyword density**  
- Count **words** on the page  
- Measure **page load time (ms)**  
- Get **SEO warnings** (common issues)  
- Overall **SEO score (0–100)**  

---

## 🌐 Example Request

```http
GET /analyze?url=https://example.com
```

---

## ✅ Example Response

```json
{
  "url": "https://example.com",
  "title": "Example Page",
  "meta": {
    "description": "This is an example page for SEO analysis.",
    "keywords": ""
  },
  "headings": {
    "h1": {"count": 1, "texts": ["Main Heading"]},
    "h2": {"count": 2, "texts": ["Subheading 1", "Subheading 2"]}
  },
  "links": {
    "internal": ["https://example.com/about"],
    "external": ["https://google.com"]
  },
  "images": {"total": 5, "with_alt": 4, "without_alt": 1},
  "word_count": 350,
  "word_density_percent": {
    "example": 3.5,
    "page": 2.0
  },
  "load_time_ms": 123,
  "seo_warnings": ["1 image missing alt attribute"],
  "seo_score": 85
}
```

---

## 📌 Use Cases
- 🔎 SEO auditing tools  
- 📊 Marketing dashboards  
- 📝 Blog & content optimization  
- ⏱ Automated SEO monitoring  

---

## 💳 Pricing
- **Free** → 50 requests/day  
- **Basic** → 500 requests/day – $5/month  
- **Pro** → 2000 requests/day – $20/month  

👉 [Subscribe on RapidAPI]([https://rapidapi.com/](https://rapidapi.com/KovalDenys1/api/ultimate-seo-analyzer))

---

## ⚠️ License
This repository is for **documentation purposes only**.  
The API source code is **proprietary** and not open-source.  
To use the API, please subscribe via **RapidAPI**.
