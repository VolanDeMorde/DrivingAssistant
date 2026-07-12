import fitz

files = ['Road-Signs-Europe.pdf', 'Signs-pdf-English-.pdf']

for fname in files:
    doc = fitz.open(fname)
    meta = doc.metadata
    print('=== ' + fname + ' ===')
    print('Pages: ' + str(doc.page_count))
    print('Title: ' + str(meta.get('title', '')))
    print('Author: ' + str(meta.get('author', '')))
    print('Creator: ' + str(meta.get('creator', '')))
    print('Subject: ' + str(meta.get('subject', '')))
    total_images = sum(len(doc[i].get_images()) for i in range(min(5, doc.page_count)))
    print('Images in first 5 pages: ' + str(total_images))
    page0_text = doc[0].get_text()[:500]
    print('First page text snippet:')
    print(page0_text)
    doc.close()
    print()
