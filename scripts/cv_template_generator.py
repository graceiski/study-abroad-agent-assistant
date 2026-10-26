#!/usr/bin/env python3
"""
CV 模板生成器

用法：
    python cv_template_generator.py [--format markdown|text]

功能：
    生成一个结构化的英文CV模板（留学申请用）。
    顾问根据模板引导学生填写具体内容。

输出：
    一个完整的英文CV模板，包含所有必要部分和占位符。
    格式：Markdown（默认）或纯文本。

示例：
    python cv_template_generator.py
    python cv_template_generator.py --format text
"""

import sys


CV_TEMPLATE_MD = """# CURRICULUM VITAE

---

## PERSONAL INFORMATION

| | |
|---|---|
| **Full Name** | [Your Full Name] |
| **Date of Birth** | [DD Month YYYY] |
| **Nationality** | [Nationality] |
| **Email** | [your.email@example.com] |
| **Phone** | [+86 XXX XXXX XXXX] |
| **LinkedIn** | [linkedin.com/in/yourprofile] (optional) |

---

## EDUCATION

### [Degree Name], [Major]
**[University Name]**, [City, Country]
[Month YYYY] – [Month YYYY]  |  **GPA:** [X.X/4.0]  |  **Rank:** [Top X%] (if applicable)

- Relevant coursework: [Course 1], [Course 2], [Course 3]
- [Honors/Awards/Scholarships related to degree]

---

## PROFESSIONAL EXPERIENCE

### [Job Title]
**[Company Name]**, [City, Country]
[Month YYYY] – [Month YYYY] (X months)

- [Action verb] + [what you did] + [quantifiable result]
  - Example: "Managed a portfolio of 15 client accounts, increasing retention rate by 20%"
- [Second bullet — focus on skills relevant to target program]
- [Third bullet — focus on collaboration or leadership]

### [Internship Title]
**[Company Name]**, [City, Country]
[Month YYYY] – [Month YYYY] (X months)

- [Action verb] + [what you did] + [quantifiable result]
- [Second bullet]

---

## PROJECTS / RESEARCH

### [Project Title]
[Month YYYY] – [Month YYYY]

- **Role:** [Your role — e.g., Team Lead, Research Assistant]
- **Description:** [Brief description of the project]
- **Skills used:** [Skill 1, Skill 2, Skill 3]
- **Outcome:** [Publication, award, deliverable, or quantifiable result]

---

## SKILLS

| Category | Details |
|----------|---------|
| **Languages** | [Language 1] (Native/Bilingual), [Language 2] (Professional), [Language 3] (Intermediate) |
| **Technical** | [Software 1], [Software 2], [Software 3] |
| **Certifications** | [Certification 1], [Certification 2] |

---

## CERTIFICATIONS & HONORS

- [Honor/Award 1] — [Institution], [Year]
- [Honor/Award 2] — [Institution], [Year]
- [Certification 1] — [Issuing Organization], [Year]

---

## EXTRACURRICULAR ACTIVITIES

### [Position], [Organization/Club]
[Month YYYY] – [Month YYYY]

- [Brief description of responsibilities and achievements]
- Example: "Led a 20-member team to organize a community event serving 500+ participants"

---

## REFERENCES

Available upon request
"""


CV_TEMPLATE_TEXT = """CURRICULUM VITAE

PERSONAL INFORMATION
Full Name:          [Your Full Name]
Date of Birth:      [DD Month YYYY]
Nationality:        [Nationality]
Email:              [your.email@example.com]
Phone:              [+86 XXX XXXX XXXX]
LinkedIn:           [linkedin.com/in/yourprofile] (optional)

EDUCATION
[Degree Name], [Major]
[University Name], [City, Country]
[Month YYYY] – [Month YYYY] | GPA: [X.X/4.0] | Rank: [Top X%]
- Relevant coursework: [Course 1], [Course 2], [Course 3]
- [Honors/Awards/Scholarships]

PROFESSIONAL EXPERIENCE
[Job Title]
[Company Name], [City, Country]
[Month YYYY] – [Month YYYY] (X months)
- [Action verb] + [what you did] + [quantifiable result]
- [Second bullet — focus on skills relevant to target program]

PROJECTS / RESEARCH
[Project Title]
[Month YYYY] – [Month YYYY]
- Role: [Your role]
- Description: [Brief description]
- Skills used: [Skill 1, Skill 2, Skill 3]
- Outcome: [Publication, award, deliverable]

SKILLS
Languages:   [Language 1] (Native), [Language 2] (Professional)
Technical:   [Software 1], [Software 2], [Software 3]
Certifications: [Certification 1], [Certification 2]

CERTIFICATIONS & HONORS
- [Honor/Award 1] — [Institution], [Year]
- [Honor/Award 2] — [Institution], [Year]

EXTRACURRICULAR ACTIVITIES
[Position], [Organization/Club]
[Month YYYY] – [Month YYYY]
- [Brief description]

REFERENCES
Available upon request
"""


def generate_cv(format: str = "markdown") -> str:
    """Generate CV template."""
    if format == "text":
        return CV_TEMPLATE_TEXT
    return CV_TEMPLATE_MD


def main():
    format = "markdown"
    if '--format' in sys.argv:
        idx = sys.argv.index('--format')
        if idx + 1 < len(sys.argv):
            format = sys.argv[idx + 1]

    if format not in ("markdown", "text"):
        print(f"❌ Unknown format: {format}. Use 'markdown' or 'text'.")
        sys.exit(1)

    result = generate_cv(format)
    print(result)


if __name__ == '__main__':
    main()