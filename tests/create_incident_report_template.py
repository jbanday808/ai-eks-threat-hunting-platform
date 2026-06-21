from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.pdfbase.acroform import AcroForm

OUTPUT_PDF = '/mnt/data/incident_report_template_fillable.pdf'

PAGE_W, PAGE_H = letter
LEFT = 0.55 * inch
RIGHT = PAGE_W - 0.55 * inch
TOP = PAGE_H - 0.55 * inch
BOTTOM = 0.55 * inch
FIELD_BG = colors.Color(0.96, 0.98, 1.0)
HEADER = colors.Color(0.11, 0.22, 0.38)
LIGHT = colors.Color(0.90, 0.93, 0.96)
BORDER = colors.Color(0.55, 0.60, 0.65)


def draw_header(c, title, subtitle=None, page_num=1):
    c.setFillColor(HEADER)
    c.rect(0, PAGE_H - 0.42 * inch, PAGE_W, 0.42 * inch, fill=True, stroke=False)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(LEFT, PAGE_H - 0.26 * inch, title)
    if subtitle:
        c.setFont('Helvetica', 8)
        c.drawRightString(RIGHT, PAGE_H - 0.26 * inch, subtitle)
    c.setFillColor(colors.grey)
    c.setFont('Helvetica', 8)
    c.drawCentredString(PAGE_W/2, 0.28 * inch, f'Incident Report Template | Page {page_num}')
    c.setFillColor(colors.black)


def section_title(c, y, text):
    c.setFillColor(LIGHT)
    c.rect(LEFT, y - 0.16*inch, RIGHT-LEFT, 0.24*inch, fill=True, stroke=False)
    c.setFillColor(HEADER)
    c.setFont('Helvetica-Bold', 10)
    c.drawString(LEFT + 6, y - 0.07*inch, text)
    c.setFillColor(colors.black)
    return y - 0.45*inch


def label(c, x, y, text, size=8):
    c.setFont('Helvetica-Bold', size)
    c.setFillColor(colors.black)
    c.drawString(x, y, text)


def text_field(c, name, x, y, w, h, tooltip='', multiline=False, maxlen=5000, value=''):
    flags = 'multiline' if multiline else ''
    c.acroForm.textfield(
        name=name,
        tooltip=tooltip or name,
        x=x, y=y, width=w, height=h,
        borderColor=BORDER, fillColor=FIELD_BG, textColor=colors.black,
        borderWidth=0.6, forceBorder=True,
        fieldFlags=flags, maxlen=maxlen, fontName='Helvetica', fontSize=8, value=value
    )


def checkbox(c, name, x, y, text):
    c.acroForm.checkbox(
        name=name, x=x, y=y, size=9, borderColor=BORDER, fillColor=colors.white,
        textColor=HEADER, buttonStyle='check', forceBorder=True, fieldFlags=''
    )
    c.setFont('Helvetica', 8)
    c.setFillColor(colors.black)
    c.drawString(x + 13, y + 1, text)


def two_col_fields(c, y, rows, prefix):
    col_w = (RIGHT - LEFT - 12) / 2
    field_h = 0.22 * inch
    gap = 0.34 * inch
    for i, (left_label, right_label) in enumerate(rows):
        yy = y - i*gap
        label(c, LEFT, yy + field_h + 2, left_label)
        text_field(c, f'{prefix}_{i}_left', LEFT, yy, col_w, field_h, left_label)
        x2 = LEFT + col_w + 12
        label(c, x2, yy + field_h + 2, right_label)
        text_field(c, f'{prefix}_{i}_right', x2, yy, col_w, field_h, right_label)
    return y - len(rows)*gap


def multi_box(c, name, x, y, w, h, title, hint=''):
    label(c, x, y + h + 4, title)
    if hint:
        c.setFont('Helvetica-Oblique', 7)
        c.setFillColor(colors.darkgray)
        c.drawString(x, y + h - 10, hint)
    text_field(c, name, x, y, w, h, title, multiline=True)


def table_lines(c, x, y, w, row_h, cols, rows, field_prefix):
    # cols: list of (heading, width_fraction)
    total = sum(frac for _, frac in cols)
    widths = [w * frac/total for _, frac in cols]
    c.setFillColor(HEADER)
    c.rect(x, y, w, row_h, fill=True, stroke=False)
    c.setFillColor(colors.white)
    c.setFont('Helvetica-Bold', 7)
    xx = x
    for (heading, _), cw in zip(cols, widths):
        c.drawString(xx + 2, y + 4, heading)
        xx += cw
    y0 = y - row_h
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.3)
    for r in range(rows):
        xx = x
        for ci, cw in enumerate(widths):
            text_field(c, f'{field_prefix}_{r}_{ci}', xx, y0 - r*row_h, cw, row_h, f'{field_prefix}_{r}_{ci}', maxlen=1000)
            xx += cw
    return y0 - rows*row_h


def add_page_1(c):
    draw_header(c, 'Fillable Cybersecurity Incident Report Template', 'Designed to reduce analyst reporting time', 1)
    y = TOP - 0.25*inch
    c.setFillColor(HEADER)
    c.setFont('Helvetica-Bold', 18)
    c.drawString(LEFT, y, 'Cybersecurity Incident Report')
    c.setFont('Helvetica', 9)
    c.setFillColor(colors.black)
    c.drawString(LEFT, y - 0.18*inch, 'Purpose: Give analysts a complete, repeatable report format for faster incident documentation.')
    y -= 0.55*inch

    y = section_title(c, y, '1. Incident Summary')
    rows = [
        ('Incident Title', 'Case / Ticket Number'),
        ('Incident Type', 'Severity'),
        ('Status', 'Detection Date / Time'),
        ('Primary Analyst', 'Reporting Team / Unit'),
        ('Affected Hostname(s)', 'Affected IP Address(es)'),
        ('Affected User(s)', 'Business / Mission Impact'),
    ]
    y = two_col_fields(c, y, rows, 'summary')

    y -= 0.1*inch
    label(c, LEFT, y + 0.2*inch, 'Severity Checklist')
    x = LEFT
    for name in ['Critical', 'High', 'Medium', 'Low', 'Informational']:
        checkbox(c, f'severity_{name}', x, y, name)
        x += 1.05*inch
    y -= 0.35*inch
    label(c, LEFT, y + 0.2*inch, 'Incident Type Checklist')
    x = LEFT
    for name in ['Phishing', 'Malware', 'Unauthorized Access', 'C2', 'Data Exfiltration']:
        checkbox(c, f'type_{name.replace(" ", "_")}', x, y, name)
        x += 1.27*inch

    y -= 0.65*inch
    y = section_title(c, y, '2. Executive Summary')
    multi_box(c, 'executive_summary', LEFT, y - 1.0*inch, RIGHT-LEFT, 0.95*inch, 'Brief Summary', 'Summarize what happened, impact, current status, and response actions in 3-5 sentences.')
    y -= 1.25*inch
    y = section_title(c, y, '3. Incident Overview')
    multi_box(c, 'incident_overview', LEFT, y - 0.85*inch, RIGHT-LEFT, 0.8*inch, 'What Happened?', 'Explain the incident in plain language for technical and non-technical readers.')


def add_page_2(c):
    draw_header(c, 'Detection and Initial Analysis', page_num=2)
    y = TOP - 0.25*inch
    y = section_title(c, y, '4. Detection Source')
    label(c, LEFT, y + 0.18*inch, 'Detection Sources Used')
    x = LEFT
    sources = ['Splunk ES', 'Microsoft Sentinel', 'Suricata', 'Zeek', 'Trellix EDR', 'Defender', 'ACAS', 'User Report']
    for i, name in enumerate(sources):
        checkbox(c, f'source_{i}', x, y - (i//4)*0.25*inch, name)
        x += 1.35*inch
        if (i+1)%4 == 0:
            x = LEFT
    y -= 0.75*inch
    rows = [
        ('Alert Name', 'Alert ID'),
        ('Alert Timestamp', 'Detection Tool'),
        ('Source IP / Host', 'Destination IP / Domain'),
        ('Username / Account', 'Initial Severity'),
    ]
    y = two_col_fields(c, y, rows, 'detect')
    y -= 0.1*inch
    y = section_title(c, y, '5. Analyst Triage')
    multi_box(c, 'triage_notes', LEFT, y - 1.0*inch, RIGHT-LEFT, 0.95*inch, 'Triage Notes', 'Validate the alert, identify true positive or false positive, and summarize first findings.')
    y -= 1.25*inch
    y = section_title(c, y, '6. Scope and Impact')
    cols = [('Asset / User', 1.2), ('Observed Activity', 2.0), ('Impact', 1.3), ('Status', 1.0)]
    table_lines(c, LEFT, y - 0.2*inch, RIGHT-LEFT, 0.24*inch, cols, 5, 'scope')


def add_page_3(c):
    draw_header(c, 'Indicators of Compromise and Timeline', page_num=3)
    y = TOP - 0.25*inch
    y = section_title(c, y, '7. Indicators of Compromise (IOCs)')
    cols = [('Type', .75), ('Indicator', 2.0), ('Description', 2.1), ('Confidence', .85)]
    y = table_lines(c, LEFT, y - 0.2*inch, RIGHT-LEFT, 0.24*inch, cols, 10, 'ioc')
    y -= 0.35*inch
    y = section_title(c, y, '8. Timeline of Events')
    cols = [('Date / Time', 1.15), ('Event', 2.7), ('Evidence Source', 1.35), ('Analyst Notes', 1.3)]
    table_lines(c, LEFT, y - 0.2*inch, RIGHT-LEFT, 0.24*inch, cols, 8, 'timeline')


def add_page_4(c):
    draw_header(c, 'Technical Analysis', page_num=4)
    y = TOP - 0.25*inch
    y = section_title(c, y, '9. Network Analysis')
    multi_box(c, 'network_findings', LEFT, y - 0.95*inch, RIGHT-LEFT, 0.9*inch, 'Network Findings', 'Document DNS, HTTP/HTTPS, C2, beaconing, NetFlow, PCAP, or IDS findings.')
    y -= 1.2*inch
    y = section_title(c, y, '10. Endpoint Analysis')
    multi_box(c, 'endpoint_findings', LEFT, y - 0.95*inch, RIGHT-LEFT, 0.9*inch, 'Endpoint Findings', 'Document process activity, file activity, registry changes, persistence, and user activity.')
    y -= 1.2*inch
    y = section_title(c, y, '11. Malware / File Analysis')
    rows = [('Malware Family', 'File Name'), ('SHA256', 'File Type'), ('Observed Behavior', 'Detection Result')]
    y = two_col_fields(c, y, rows, 'malware')
    y -= 0.1*inch
    multi_box(c, 'malware_summary', LEFT, y - 0.7*inch, RIGHT-LEFT, 0.65*inch, 'Malware Summary', 'Summarize static or dynamic analysis findings in plain English.')


def add_page_5(c):
    draw_header(c, 'MITRE ATT&CK and Detection Engineering', page_num=5)
    y = TOP - 0.25*inch
    y = section_title(c, y, '12. MITRE ATT&CK Mapping')
    cols = [('Tactic', 1.3), ('Technique', 1.9), ('ID', .8), ('Evidence', 2.3)]
    y = table_lines(c, LEFT, y - 0.2*inch, RIGHT-LEFT, 0.24*inch, cols, 8, 'mitre')
    y -= 0.35*inch
    y = section_title(c, y, '13. Detection Content Created or Updated')
    cols = [('Tool', 1.0), ('Detection / Query / Rule', 2.4), ('Purpose', 2.0), ('Status', .9)]
    y = table_lines(c, LEFT, y - 0.2*inch, RIGHT-LEFT, 0.24*inch, cols, 6, 'detection')
    y -= 0.35*inch
    y = section_title(c, y, '14. Evidence Sources')
    multi_box(c, 'evidence_sources', LEFT, y - 0.75*inch, RIGHT-LEFT, 0.7*inch, 'Evidence Sources', 'List screenshots, logs, PCAPs, ticket numbers, SIEM searches, EDR events, or malware analysis reports.')


def add_page_6(c):
    draw_header(c, 'Incident Response Actions', page_num=6)
    y = TOP - 0.25*inch
    y = section_title(c, y, '15. Incident Response Lifecycle')
    items = [
        ('Preparation', 'Tools, SOPs, escalation paths, logging, and contacts were available.'),
        ('Detection', 'Alert, user report, IDS/IPS, SIEM, EDR, or threat intelligence identified suspicious activity.'),
        ('Analysis', 'Analyst validated the alert, identified IOCs/TTPs, and determined scope and impact.'),
        ('Containment', 'Affected systems, accounts, network paths, or indicators were isolated or blocked.'),
        ('Eradication', 'Malware, persistence, unauthorized accounts, and malicious content were removed.'),
        ('Recovery', 'Systems were restored, validated, patched, and monitored for reinfection.'),
        ('Lessons Learned', 'Findings, gaps, detections, procedures, and improvements were documented.'),
    ]
    for i, (phase, hint) in enumerate(items):
        h = 0.48*inch
        label(c, LEFT, y, phase)
        text_field(c, f'ir_{phase.lower().replace(" ", "_")}', LEFT + 1.15*inch, y - 0.12*inch, RIGHT-LEFT-1.15*inch, h, phase, multiline=True)
        c.setFont('Helvetica-Oblique', 6.5)
        c.setFillColor(colors.darkgray)
        c.drawString(LEFT + 1.18*inch, y + h - 0.18*inch, hint[:120])
        c.setFillColor(colors.black)
        y -= 0.62*inch


def add_page_7(c):
    draw_header(c, 'Recommendations and Closure', page_num=7)
    y = TOP - 0.25*inch
    y = section_title(c, y, '16. Recommendations')
    multi_box(c, 'immediate_actions', LEFT, y - 0.85*inch, RIGHT-LEFT, 0.8*inch, 'Immediate Actions', 'Examples: block IOCs, reset passwords, isolate systems, disable accounts, update detections.')
    y -= 1.1*inch
    multi_box(c, 'long_term_actions', LEFT, y - 0.85*inch, RIGHT-LEFT, 0.8*inch, 'Long-Term Improvements', 'Examples: tune detections, improve logging, user training, patching, segmentation, new playbooks.')
    y -= 1.15*inch
    y = section_title(c, y, '17. Analyst Conclusion')
    multi_box(c, 'analyst_conclusion', LEFT, y - 0.9*inch, RIGHT-LEFT, 0.85*inch, 'Conclusion', 'State whether the incident was confirmed, contained, remediated, and what improvements were made.')
    y -= 1.15*inch
    y = section_title(c, y, '18. Approval and Closure')
    rows = [('Prepared By', 'Date'), ('Reviewed By', 'Date'), ('Final Status', 'Closure Notes')]
    two_col_fields(c, y, rows, 'closure')


def build_pdf(output=OUTPUT_PDF):
    c = canvas.Canvas(output, pagesize=letter)
    c.setTitle('Fillable Cybersecurity Incident Report Template')
    c.setAuthor('Generated by Python ReportLab')
    pages = [add_page_1, add_page_2, add_page_3, add_page_4, add_page_5, add_page_6, add_page_7]
    for i, fn in enumerate(pages):
        fn(c)
        if i != len(pages)-1:
            c.showPage()
    c.save()
    return output


if __name__ == '__main__':
    print(f'Created: {build_pdf()}')
