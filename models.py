from pydantic import BaseModel, Field
from typing import List, Dict


class Meta(BaseModel):
	description: str = Field("", description="Meta description")
	keywords: str = Field("", description="Meta keywords")


class HeadingTexts(BaseModel):
	count: int = Field(0, description="Number of headings")
	texts: List[str] = Field(default_factory=list, description="Heading texts")


class Headings(BaseModel):
	h1: HeadingTexts = Field(default_factory=HeadingTexts)
	h2: HeadingTexts = Field(default_factory=HeadingTexts)


class Links(BaseModel):
	internal: List[str] = Field(default_factory=list)
	external: List[str] = Field(default_factory=list)


class Images(BaseModel):
	total: int = 0
	with_alt: int = 0
	without_alt: int = 0


class AnalyzeResult(BaseModel):
	url: str
	title: str
	meta: Meta
	headings: Headings
	links: Links
	images: Images
	word_count: int
	word_density_percent: Dict[str, float] = Field(default_factory=dict)
	load_time_ms: int
	seo_warnings: List[str] = Field(default_factory=list)
	seo_score: int


class QuickScoreResult(BaseModel):
	url: str
	seo_score: int
	seo_warnings: List[str] = Field(default_factory=list)


class MetadataResult(BaseModel):
	url: str
	title: str
	meta: Meta
	headings: Headings


class HealthCheck(BaseModel):
	status: str
	message: str
	endpoints: List[str] = Field(default_factory=list)


__all__ = [
	"Meta",
	"HeadingTexts",
	"Headings",
	"Links",
	"Images",
	"AnalyzeResult",
	"QuickScoreResult",
	"MetadataResult",
	"HealthCheck",
]
