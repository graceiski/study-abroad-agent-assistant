#!/usr/bin/env python3
"""
Why School 段生成器

用法：
    python why_school_generator.py <school_name> <program_name> [--student-story <story>]

功能：
    根据学校和项目名称，生成 Why School 段的结构化框架（含占位符）。
    顾问在此基础上填充具体细节。

示例：
    python why_school_generator.py "University of Sydney" "Master of Media and Communications"
    python why_school_generator.py "Monash University" "Master of Cultural & Creative Industries" --student-story "fashion content creator"

输出：
    一个100-150词的 Why School 段框架，包含：
    1. 学校特定资源（课程/实验室/研究中心）
    2. 与学生故事的连接点
    3. 城市/区域文化语境
"""

import sys
from pathlib import Path


# 各校特色资源数据库（澳洲主要院校）
SCHOOL_RESOURCES = {
    "University of Melbourne": {
        "strengths": ["文化管理", "艺术机构生态", "跨学科研究"],
        "keywords": ["cultural management", "arts sector", "interdisciplinary"],
        "city_context": "墨尔本的文化氛围和创意产业生态",
    },
    "University of Sydney": {
        "strengths": ["媒体产业", "亚太传播", " Journalism 实践"],
        "keywords": ["media industry", "Asia-Pacific", "journalism practice"],
        "city_context": "悉尼的媒体产业和亚太传播中心地位",
    },
    "UNSW Sydney": {
        "strengths": ["新闻实践", "行业连接", "媒体技术"],
        "keywords": ["journalism practice", "industry connections", "media tech"],
        "city_context": "悉尼的媒体和科技交汇",
    },
    "Monash University": {
        "strengths": ["文化创意产业", "跨学科", "时尚研究"],
        "keywords": ["cultural and creative industries", "cross-disciplinary", "fashion"],
        "city_context": "墨尔本的创意产业和时尚生态",
    },
    "University of Queensland": {
        "strengths": ["传播学", "旅游/区域研究", "社会科学"],
        "keywords": ["communication studies", "tourism", "regional research"],
        "city_context": "布里斯班的区域研究和旅游产业",
    },
    "RMIT University": {
        "strengths": ["实践导向", "时尚/设计", "行业实习"],
        "keywords": ["practice-oriented", "fashion", "design", "industry internship"],
        "city_context": "墨尔本的设计和时尚中心",
    },
    "University of Technology Sydney": {
        "strengths": ["媒体技术", "行业实习", "创新传播"],
        "keywords": ["media technology", "industry internship", "innovative communication"],
        "city_context": "悉尼的科技和媒体产业",
    },
    "QUT": {
        "strengths": ["传播+技术", "实践应用", "媒体创新"],
        "keywords": ["communication and technology", "applied practice", "media innovation"],
        "city_context": "布里斯班的媒体技术应用环境",
    },
    "Deakin University": {
        "strengths": ["实践导向", "灵活学制", "行业连接"],
        "keywords": ["practice-oriented", "flexible delivery", "industry engagement"],
        "city_context": "墨尔本及维多利亚州的实践学习环境",
    },
    "Macquarie University": {
        "strengths": ["媒体+商科交叉", "传播管理", "亚太研究"],
        "keywords": ["media and business", "communication management", "Asia-Pacific"],
        "city_context": "悉尼的商科和媒体交汇",
    },
    "University of Adelaide": {
        "strengths": ["传播学", "社会科学", " wine 商科"],
        "keywords": ["communication", "social sciences", "industry links"],
        "city_context": "阿德莱德的文化和产业环境",
    },
    "University of Western Australia": {
        "strengths": ["传播学", "商科", "资源产业"],
        "keywords": ["communication", "business", "resource sector"],
        "city_context": "珀斯的资源和媒体产业",
    },
    "ANU": {
        "strengths": ["社会科学", "政策研究", "亚太研究"],
        "keywords": ["social sciences", "policy research", "Asia-Pacific studies"],
        "city_context": "堪培拉的政策和研究环境",
    },
}


def get_school_info(school_name: str) -> dict:
    """Get school resource info, with fallback."""
    # Try exact match first
    if school_name in SCHOOL_RESOURCES:
        return SCHOOL_RESOURCES[school_name]

    # Try partial match
    for key, value in SCHOOL_RESOURCES.items():
        if school_name.lower() in key.lower() or key.lower() in school_name.lower():
            return value

    # Fallback
    return {
        "strengths": ["学术资源", "专业课程"],
        "keywords": ["academic resources", "program curriculum"],
        "city_context": "所在城市",
    }


def generate_why_school(school_name: str, program_name: str, student_story: str = None) -> str:
    """Generate a Why School paragraph framework."""
    info = get_school_info(school_name)
    strengths = info["strengths"]
    keywords = info["keywords"]
    city_context = info["city_context"]

    # Build the paragraph
    lines = []
    lines.append(f"# Why School: {school_name} — {program_name}")
    lines.append("")
    lines.append("## 框架（100-150词）")
    lines.append("")
    lines.append("### 第一部分：学校特定资源（~50词）")
    lines.append("")
    lines.append(f"> [学校名称] 的 [具体课程名称/实验室名称/研究中心名称] "
                 f"在 [相关领域] 具有显著优势，")
    lines.append(f"> 特别是 [与项目最相关的1-2个具体资源]。")
    lines.append(f"> 这些资源与我在 [学生专业/背景] 领域的兴趣高度契合，")
    lines.append(f"> 尤其是 [关键词1: {keywords[0] if keywords else 'N/A'}] "
                 f"和 [关键词2: {keywords[1] if len(keywords) > 1 else 'N/A'}] 方向。")
    lines.append("")
    lines.append("### 第二部分：与学生故事的连接点（~50词）")
    lines.append("")
    if student_story:
        lines.append(f"> 我的背景是 [学生故事: {student_story}]，")
    else:
        lines.append(f"> 我的背景是 [学生故事 — 从通用Body中提取一个核心经历]，")
    lines.append(f"> 这与该项目的 [具体课程/研究方向] 直接相关。")
    lines.append(f"> 我希望在 [学校名称] 的 [具体资源] 深化这一方向，")
    lines.append(f"> 将我的 [现有技能/经验] 提升到 [目标水平]。")
    lines.append("")
    lines.append("### 第三部分：城市/区域文化语境（~30词）")
    lines.append("")
    lines.append(f"> [城市名称] 的 [城市文化/产业特色: {city_context}] ")
    lines.append(f"> 为我提供了独特的学习和实践环境，")
    lines.append(f"> 尤其是在 [具体领域] 的实践机会。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 完整段落示例（填充后）")
    lines.append("")
    lines.append(f"> [在此处写入完整的100-150词段落，")
    lines.append(f"> 包含上述三个部分，语言流畅自然，不要像填空。]")
    lines.append("")
    lines.append("## 该学校的差异化要点")
    lines.append("")
    for s in strengths:
        lines.append(f"- {s}")
    lines.append("")
    lines.append("## 关键词（写PS时参考）")
    lines.append("")
    lines.append(", ".join(keywords))
    lines.append("")

    return "\n".join(lines)


def main():
    if len(sys.argv) < 3:
        print("用法: python why_school_generator.py <school_name> <program_name> [--student-story <story>]")
        print("示例: python why_school_generator.py 'University of Sydney' 'Master of Media and Communications'")
        print("      python why_school_generator.py 'Monash University' 'Master of Cultural & Creative Industries' --student-story 'fashion content creator'")
        sys.exit(1)

    school_name = sys.argv[1]
    program_name = sys.argv[2]
    student_story = None

    if '--student-story' in sys.argv:
        idx = sys.argv.index('--student-story')
        if idx + 1 < len(sys.argv):
            student_story = sys.argv[idx + 1]

    result = generate_why_school(school_name, program_name, student_story)
    print(result)


if __name__ == '__main__':
    main()