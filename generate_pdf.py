from markdown_pdf import MarkdownPdf, Section

pdf = MarkdownPdf(toc_level=0)
pdf.meta["title"] = "Ved Project Report"
pdf.meta["author"] = "AI Setup"

with open("Ved_Project_Report.md", "r", encoding="utf-8") as f:
    text = f.read()

pdf.add_section(Section(text))
pdf.save("Ved_Project_Report.pdf")
