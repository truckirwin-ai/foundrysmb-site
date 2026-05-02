#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
import textwrap
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

ROOT = Path(__file__).resolve().parents[1]

INK = colors.HexColor("#111411")
PAPER = colors.HexColor("#f7f7f3")
MIST = colors.HexColor("#e8e5dc")
ORANGE = colors.HexColor("#f05a1a")
BLUE = colors.HexColor("#0b5d6b")
MUTED = colors.HexColor("#555b52")
WHITE = colors.white


RESOURCE_SETS = [
    (ROOT / "digital-products", ROOT / "downloads" / "toolkit", "Foundry Toolkit"),
    (ROOT / "support-packs", ROOT / "downloads" / "support-packs", "Foundry Support Pack"),
    (ROOT / "sales-assets", ROOT / "downloads" / "sales-assets", "Foundry Sales Asset"),
    (ROOT / "outbound", ROOT / "downloads" / "outbound", "Foundry Outbound Pack"),
    (ROOT / "content", ROOT / "downloads" / "content", "Foundry Content Asset"),
    (ROOT / "agent-ops", ROOT / "downloads" / "agent-ops", "Foundry Agent Ops"),
]


def slug(path: Path) -> str:
    return path.stem.replace("_", "-")


def clean_title(path: Path, lines: list[str]) -> str:
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def inline(text: str) -> str:
    text = escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r"<u>\1</u>", text)
    return text


def make_styles():
    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle(
            "FoundryTitle",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=28,
            leading=31,
            textColor=WHITE,
            alignment=TA_LEFT,
            spaceAfter=16,
        ),
        "Deck": ParagraphStyle(
            "FoundryDeck",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=12.5,
            leading=18,
            textColor=colors.HexColor("#dfe2db"),
            spaceAfter=10,
        ),
        "Eyebrow": ParagraphStyle(
            "FoundryEyebrow",
            parent=base["BodyText"],
            fontName="Courier-Bold",
            fontSize=8,
            leading=10,
            textColor=ORANGE,
            uppercase=True,
            spaceAfter=18,
        ),
        "H1": ParagraphStyle(
            "FoundryH1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=21,
            leading=25,
            textColor=INK,
            spaceBefore=18,
            spaceAfter=8,
            keepWithNext=True,
        ),
        "H2": ParagraphStyle(
            "FoundryH2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=15,
            leading=18,
            textColor=INK,
            spaceBefore=15,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "H3": ParagraphStyle(
            "FoundryH3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=12.5,
            leading=15,
            textColor=BLUE,
            spaceBefore=11,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "Body": ParagraphStyle(
            "FoundryBody",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.6,
            leading=14,
            textColor=INK,
            spaceAfter=7,
        ),
        "Small": ParagraphStyle(
            "FoundrySmall",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=8,
            leading=11,
            textColor=MUTED,
        ),
        "Bullet": ParagraphStyle(
            "FoundryBullet",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=9.4,
            leading=13.5,
            leftIndent=0,
            bulletIndent=0,
            textColor=INK,
        ),
        "Code": ParagraphStyle(
            "FoundryCode",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.3,
            leading=9.2,
            textColor=INK,
            backColor=colors.HexColor("#fffaf0"),
            borderColor=colors.HexColor("#d7d0c2"),
            borderWidth=0.4,
            borderPadding=7,
            spaceBefore=6,
            spaceAfter=8,
        ),
        "TableCell": ParagraphStyle(
            "FoundryTableCell",
            parent=base["BodyText"],
            fontName="Helvetica",
            fontSize=7.6,
            leading=9.4,
            textColor=INK,
        ),
        "TableHead": ParagraphStyle(
            "FoundryTableHead",
            parent=base["BodyText"],
            fontName="Helvetica-Bold",
            fontSize=7.4,
            leading=9,
            textColor=WHITE,
        ),
    }
    return styles


def page_chrome(kind: str, title: str):
    def draw(canvas, doc):
        canvas.saveState()
        width, height = letter
        canvas.setFillColor(PAPER)
        canvas.rect(0, 0, width, height, stroke=0, fill=1)
        canvas.setStrokeColor(MIST)
        canvas.setLineWidth(0.6)
        canvas.line(doc.leftMargin, height - 0.48 * inch, width - doc.rightMargin, height - 0.48 * inch)
        canvas.setFillColor(INK)
        canvas.setFont("Helvetica-Bold", 8)
        canvas.drawString(doc.leftMargin, height - 0.34 * inch, "Foundry SMB")
        canvas.setFillColor(ORANGE)
        canvas.setFont("Courier-Bold", 7)
        canvas.drawRightString(width - doc.rightMargin, height - 0.34 * inch, kind.upper())
        canvas.setStrokeColor(ORANGE)
        canvas.setLineWidth(1.3)
        canvas.line(doc.leftMargin, 0.52 * inch, width - doc.rightMargin, 0.52 * inch)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7)
        canvas.drawString(doc.leftMargin, 0.34 * inch, title[:70])
        canvas.drawRightString(width - doc.rightMargin, 0.34 * inch, f"Page {doc.page}")
        canvas.restoreState()
    return draw


def cover(canvas, doc, title: str, kind: str, deck: str):
    canvas.saveState()
    width, height = letter
    canvas.setFillColor(INK)
    canvas.rect(0, 0, width, height, stroke=0, fill=1)
    canvas.setFillColor(ORANGE)
    canvas.rect(0.7 * inch, height - 1.25 * inch, 0.12 * inch, 0.12 * inch, stroke=0, fill=1)
    canvas.setFont("Helvetica-Bold", 18)
    canvas.setFillColor(WHITE)
    canvas.drawString(0.9 * inch, height - 1.23 * inch, "Foundry SMB")
    canvas.setFont("Courier-Bold", 8)
    canvas.setFillColor(ORANGE)
    canvas.drawString(0.72 * inch, height - 2.05 * inch, kind.upper())
    text = canvas.beginText(0.72 * inch, height - 2.72 * inch)
    text.setFont("Helvetica-Bold", 30)
    text.setFillColor(WHITE)
    for line in textwrap.wrap(title, width=24):
        text.textLine(line)
    canvas.drawText(text)
    text = canvas.beginText(0.72 * inch, 2.25 * inch)
    text.setFont("Helvetica", 12)
    text.setFillColor(colors.HexColor("#dfe2db"))
    for line in textwrap.wrap(deck, width=62):
        text.textLine(line)
    canvas.drawText(text)
    canvas.setStrokeColor(ORANGE)
    canvas.setLineWidth(2)
    canvas.line(0.72 * inch, 1.1 * inch, width - 0.72 * inch, 1.1 * inch)
    canvas.setFont("Courier-Bold", 8)
    canvas.setFillColor(colors.HexColor("#dfe2db"))
    canvas.drawString(0.72 * inch, 0.78 * inch, "WORKFLOW ASSETS FOR OWNER-LED BUSINESSES")
    canvas.restoreState()


def parse_table(lines: list[str], styles):
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)
    if len(rows) >= 2 and all(re.fullmatch(r":?-{3,}:?", c.replace(" ", "")) for c in rows[1]):
        rows.pop(1)
    width = 7.1 * inch
    max_cols = max(len(r) for r in rows)
    col_widths = [width / max_cols] * max_cols
    data = []
    for r_i, row in enumerate(rows):
        padded = row + [""] * (max_cols - len(row))
        style_name = "TableHead" if r_i == 0 else "TableCell"
        data.append([Paragraph(inline(cell), styles[style_name]) for cell in padded])
    table = Table(data, colWidths=col_widths, hAlign="LEFT", repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), INK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("BACKGROUND", (0, 1), (-1, -1), WHITE),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#c8c2b7")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def code_block(text: str, styles):
    wrapped = []
    for line in text.splitlines():
        if not line:
            wrapped.append("")
            continue
        wrapped.extend(textwrap.wrap(line, width=86, replace_whitespace=False, drop_whitespace=False) or [""])
    return Preformatted("\n".join(wrapped), styles["Code"], maxLineLength=86)


def markdown_story(path: Path, kind: str, styles):
    lines = path.read_text(encoding="utf-8").splitlines()
    title = clean_title(path, lines)
    deck = next((l.strip() for l in lines if l.strip() and not l.startswith("#")), "A Foundry SMB operating resource.")
    story = []
    story.append(PageBreak())
    in_code = False
    code_lines = []
    table_lines = []
    bullets = []

    def flush_bullets():
        nonlocal bullets
        if bullets:
            story.append(ListFlowable(
                [ListItem(Paragraph(inline(item), styles["Bullet"]), leftIndent=12) for item in bullets],
                bulletType="bullet",
                leftIndent=14,
                bulletFontName="Helvetica",
                bulletFontSize=7,
                spaceAfter=6,
            ))
            bullets = []

    def flush_table():
        nonlocal table_lines
        if table_lines:
            flush_bullets()
            story.append(parse_table(table_lines, styles))
            story.append(Spacer(1, 8))
            table_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("```"):
            flush_table()
            flush_bullets()
            if in_code:
                story.append(code_block("\n".join(code_lines), styles))
                code_lines = []
                in_code = False
            else:
                in_code = True
            continue
        if in_code:
            code_lines.append(line)
            continue

        if stripped.startswith("|") and stripped.endswith("|"):
            table_lines.append(stripped)
            continue
        flush_table()

        if not stripped:
            flush_bullets()
            story.append(Spacer(1, 4))
            continue
        if stripped == "---":
            flush_bullets()
            story.append(Spacer(1, 4))
            continue
        if stripped.startswith("# "):
            flush_bullets()
            continue
        if stripped.startswith("## "):
            flush_bullets()
            story.append(Paragraph(inline(stripped[3:]), styles["H1"]))
            continue
        if stripped.startswith("### "):
            flush_bullets()
            story.append(Paragraph(inline(stripped[4:]), styles["H2"]))
            continue
        if stripped.startswith("#### "):
            flush_bullets()
            story.append(Paragraph(inline(stripped[5:]), styles["H3"]))
            continue
        if re.match(r"^- \[[ xX]\] ", stripped):
            bullets.append(stripped[2:])
            continue
        if stripped.startswith("- "):
            bullets.append(stripped[2:])
            continue
        if re.match(r"^\d+\. ", stripped):
            bullets.append(re.sub(r"^\d+\. ", "", stripped))
            continue
        if stripped.startswith(">"):
            flush_bullets()
            story.append(Paragraph(f"<font color='{BLUE.hexval()}'>{inline(stripped.lstrip('> ').strip())}</font>", styles["Body"]))
            continue
        flush_bullets()
        story.append(Paragraph(inline(stripped), styles["Body"]))

    flush_table()
    flush_bullets()
    return title, deck, story


def csv_story(path: Path, styles):
    title = path.stem.replace("-", " ").title()
    rows = list(csv.reader(path.open(newline="", encoding="utf-8")))
    table_lines = ["|" + "|".join(r) + "|" for r in rows]
    return title, "A worksheet for scoring workflow value, risk, readiness, and follow-on potential.", [PageBreak(), parse_table(table_lines, styles)]


def build_pdf(src: Path, out: Path, kind: str):
    styles = make_styles()
    if src.suffix.lower() == ".csv":
        title, deck, story = csv_story(src, styles)
    else:
        title, deck, story = markdown_story(src, kind, styles)

    out.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(out),
        pagesize=letter,
        rightMargin=0.7 * inch,
        leftMargin=0.7 * inch,
        topMargin=0.72 * inch,
        bottomMargin=0.72 * inch,
        title=title,
        author="Foundry SMB",
        subject=kind,
    )

    story_with_cover = [Spacer(1, 0)] + story

    def first_page(canvas, doc):
        cover(canvas, doc, title, kind, deck)

    doc.build(story_with_cover, onFirstPage=first_page, onLaterPages=page_chrome(kind, title))
    print(out.relative_to(ROOT))


def main():
    for src_dir, out_dir, kind in RESOURCE_SETS:
        for src in sorted(src_dir.iterdir()):
            if src.suffix.lower() not in {".md", ".csv"}:
                continue
            out = out_dir / f"{slug(src)}.pdf"
            build_pdf(src, out, kind)


if __name__ == "__main__":
    main()
