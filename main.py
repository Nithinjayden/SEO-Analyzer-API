from fastapi import FastAPI, HTTPException, Query
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from collections import Counter
import time
import re

app = FastAPI(title="Ultimate SEO Analyzer API", version="5.0")

cache = {}
CACHE_EXPIRY = 300


def get_links(soup, base_url):
    internal_links, external_links = [], []
    for link in soup.find_all("a", href=True):
        href = link['href']
        if href.startswith('#'):
            continue
        full_url = urljoin(base_url, href)
        if urlparse(full_url).netloc == urlparse(base_url).netloc:
            internal_links.append(full_url)
        else:
            external_links.append(full_url)
    return {"internal": list(set(internal_links)), "external": list(set(external_links))}


def get_img_alt_stats(soup):
    images = soup.find_all("img")
    total = len(images)
    with_alt = len([img for img in images if img.get("alt")])
    without_alt = total - with_alt
    return {"total": total, "with_alt": with_alt, "without_alt": without_alt}


def get_word_density(text):
    words = re.findall(r'\w+', text.lower())
    counter = Counter(words)
    total_words = len(words)
    density = {word: round(count / total_words * 100, 2) for word, count in counter.items()} if total_words else {}
    return density


def seo_warnings(title, meta_desc, h1, h2, images):
    warnings = []
    if not title:
        warnings.append("Title is missing")
    elif len(title) > 60:
        warnings.append("Title is too long (>60 characters)")
    if not meta_desc:
        warnings.append("Meta description is missing")
    elif len(meta_desc) > 160:
        warnings.append("Meta description is too long (>160 characters)")
    if len(h1) == 0:
        warnings.append("H1 is missing")
    if len(h2) == 0:
        warnings.append("H2 is missing")
    if images["without_alt"] > 0:
        warnings.append(f"{images['without_alt']} images are missing alt attribute")
    return warnings


def seo_score(warnings):
    score = 100 - len(warnings) * 15
    return max(score, 0)


def fetch_page(url):
    start = time.time()
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error fetching page: {e}")
    load_time = int((time.time() - start) * 1000)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup, load_time


def analyze_page(url):
    current_time = time.time()
    if url in cache and current_time - cache[url]["time"] < CACHE_EXPIRY:
        return cache[url]["data"]

    soup, load_time = fetch_page(url)

    title = soup.title.string.strip() if soup.title else ""
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    meta_keywords_tag = soup.find("meta", attrs={"name": "keywords"})
    meta_desc = meta_desc_tag["content"] if meta_desc_tag else ""
    meta_keywords = meta_keywords_tag["content"] if meta_keywords_tag else ""
    h1 = [h.get_text(strip=True) for h in soup.find_all("h1")]
    h2 = [h.get_text(strip=True) for h in soup.find_all("h2")]

    text_content = soup.get_text(separator=" ", strip=True)
    word_count = len(text_content.split())
    word_density = get_word_density(text_content)
    images = get_img_alt_stats(soup)
    links = get_links(soup, url)

    warnings = seo_warnings(title, meta_desc, h1, h2, images)
    score = seo_score(warnings)

    result = {
        "url": url,
        "title": title,
        "meta": {"description": meta_desc, "keywords": meta_keywords},
        "headings": {
            "h1": {"count": len(h1), "texts": h1},
            "h2": {"count": len(h2), "texts": h2},
        },
        "links": links,
        "images": images,
        "word_count": word_count,
        "word_density_percent": word_density,
        "load_time_ms": load_time,
        "seo_warnings": warnings,
        "seo_score": score,
    }

    cache[url] = {"data": result, "time": current_time}
    return result


@app.get("/analyze")
def analyze(url: str = Query(..., description="URL of the page to analyze")):
    """Full SEO analysis (metadata, headings, links, images, keyword density, load time, score)"""
    return analyze_page(url)


@app.get("/quick-score")
def quick_score(url: str = Query(..., description="URL of the page to analyze")):
    """Quick SEO score + warnings only"""
    data = analyze_page(url)
    return {
        "url": data["url"],
        "seo_score": data["seo_score"],
        "seo_warnings": data["seo_warnings"],
    }


@app.get("/metadata")
def metadata(url: str = Query(..., description="URL of the page to analyze")):
    """Extract metadata and headings only"""
    data = analyze_page(url)
    return {
        "url": data["url"],
        "title": data["title"],
        "meta": data["meta"],
        "headings": data["headings"],
    }