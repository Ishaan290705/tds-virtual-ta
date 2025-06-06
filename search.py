from bs4 import BeautifulSoup

# Load and parse course content
def load_course_content(path="tds-content.xml"):
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "xml")
    docs = []
    for doc in soup.find_all("document"):
        source = doc.find("source").text
        text = doc.find("document_content").text
        docs.append((source, text))
    return docs

# Search for best matching document
def search_content(question: str, docs):
    q_words = question.lower().split()
    best = None
    for source, text in docs:
        if any(q in text.lower() for q in q_words):
            lines = text.strip().split("\n")
            for line in lines:
                if any(q in line.lower() for q in q_words):
                    return line.strip(), [{"url": source, "text": "From course content"}]
    return "Sorry, I couldn't find a match.", []
