AUTHOR = "Justin Mayer"
SITENAME = "Justin Mayer’s Site"  # noqa: RUF001
SITESUBTITLE = "Digital homestead in the ether"
SITEURL = "https://justinmayer.com"
TIMEZONE = "Europe/Rome"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = "https://github.com/justinmayer"
REVERSE_CATEGORY_ORDER = True
LOCALE = "C"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2012, 3, 2, 14, 1, 1)

FEED_ALL_RSS = "feeds/all.rss.xml"
CATEGORY_FEED_RSS = "feeds/{slug}.rss.xml"

LINKS = (
    ("Hynek Schlawack", "https://hynek.me/"),
    ("Adam Johnson", "https://adamj.eu/tech/"),
    ("Florian Haas", "https://xahteiwi.eu"),
    ("The Desolation of Blog", "https://lapcatsoftware.com/articles/"),
    ("Tyler Hall", "https://tyler.io/"),
    ("Wait But Why", "https://waitbutwhy.com/"),
)

SOCIAL = (
    ("twitter", "https://twitter.com/jmayer"),
    ("github", "http://github.com/justinmayer"),
)

# global metadata to all the contents
DEFAULT_METADATA = {"yeah": "it is"}

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra/robots.txt",
]

# custom page generated with a jinja2 template
TEMPLATE_PAGES = {"pages/jinja2_template.html": "jinja2_template.html"}

# there is no other HTML content
READERS = {"html": None}

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {"linenos": "table"}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
