# 🚀 Ultimate SEO Analyzer API

[![RapidAPI](https://img.shields.io/badge/View%20on-RapidAPI-00bfff?logo=cloudflare&logoColor=white)](https://rapidapi.com/KovalDenys1/api/ultimate-seo-analyzer)  
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)  
[![License](https://img.shields.io/badge/License-Proprietary-red)](#-license)

**Ultimate SEO Analyzer API** is a web API built with FastAPI that provides SEO-related analysis of any given webpage.  
It extracts metadata, headings, links, images, keyword density, page load time, SEO warnings, and calculates an overall SEO score.

![SEO Analyzer Logo](Logo.png)

---

## 🔍 Key Features
- Extract **page metadata** (title, description, keywords)  
- Analyze **H1/H2 headings**  
- Separate **internal & external links**  
- Audit **images with/without alt**  
- Measure **keyword density**  
- Count **words** on the page  
- Measure **page load time (ms)**  
- Detect **SEO warnings** (common issues)  
- Calculate an **SEO score (0–100)**  

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
- SEO auditing tools  
- Marketing dashboards  
- Content optimization  
- Automated SEO monitoring  

---

## 📦 Availability
The API is accessible via [RapidAPI](https://rapidapi.com/KovalDenys1/api/ultimate-seo-analyzer), where Free, Basic, and Pro usage tiers are provided.

---

## ⚠️ License
This repository is for **documentation purposes only**.  
The API source code is **proprietary** and not open-source.  
Usage is available through the RapidAPI platform.  
