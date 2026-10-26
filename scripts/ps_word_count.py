#!/usr/bin/env python3
"""
PS/SOP 字数自动检查工具

用法：
    python ps_word_count.py <ps_file.md> [--target <target_words>]

功能：
    1. 统计总字数（英文单词数）
    2. 按段落拆分，显示每段字数
    3. 对照目标字数给出通过/警告/超标判断
    4. 检查是否有P7 Why School段（应为各校独立）
    5. 检查是否有明显的假大空短语

示例：
    python ps_word_count.py my_ps.md --target 1000
    python ps_word_count.py my_ps.md --target 500
"""

import re
import sys
from pathlib import Path


def count_words(text: str) -> int:
    """Count English words in text."""
    # Split on whitespace and count non-empty tokens
    words = text.split()
    return len(words)


def count_words_chinese(text: str) -> int:
    """Count Chinese characters as words (approximate)."""
    # Chinese characters
    chinese = len(re.findall(r'[\u4e00-\u9fff]', text))
    return chinese


def split_paragraphs(text: str) -> list:
    """Split text into paragraphs, skipping empty lines."""
    paragraphs = []
    current = []
    for line in text.split('\n'):
        stripped = line.strip()
        if stripped:
            current.append(stripped)
        else:
            if current:
                paragraphs.append('\n'.join(current))
                current = []
    if current:
        paragraphs.append('\n'.join(current))
    return paragraphs


def check_filler_phrases(text: str) -> list:
    """Check for common filler/vague phrases."""
    fillers = [
        (r'\bpassion(ate)?\b', 'passion'),
        (r'\bdream\b', 'dream'),
        (r'\blife-changing\b', 'life-changing'),
        (r'\bnever stop learning\b', 'cliché'),
        (r'\bI have always wanted to\b', 'generic opener'),
        (r'\bthank you for your time\b', 'closing cliché'),
        (r'\bI believe I am a perfect candidate\b', 'overconfident'),
    ]
    found = []
    for pattern, label in fillers:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            found.append((label, len(matches)))
    return found


def check_why_school(text: str) -> bool:
    """Check if text contains a Why School section."""
    patterns = [
        r'why\s+(i\s+)?choose',
        r'why\s+(this\s+)?school',
        r'why\s+(this\s+)?university',
        r'why\s+(this\s+)?program',
    ]
    for p in patterns:
        if re.search(p, text, re.IGNORECASE):
            return True
    return False


def analyze(ps_file: str, target_words: int = None) -> dict:
    """Analyze a PS/SOP file."""
    path = Path(ps_file)
    if not path.exists():
        print(f"❌ File not found: {ps_file}")
        return {}

    text = path.read_text(encoding='utf-8')
    total_words = count_words(text)
    paragraphs = split_paragraphs(text)
    filler_issues = check_filler_phrases(text)
    has_why_school = check_why_school(text)

    # Per-paragraph word counts
    para_counts = [(i+1, count_words(p)) for i, p in enumerate(paragraphs)]

    result = {
        'file': str(path),
        'total_words': total_words,
        'paragraph_count': len(paragraphs),
        'paragraph_words': para_counts,
        'has_why_school': has_why_school,
        'filler_issues': filler_issues,
        'target': target_words,
    }

    if target_words:
        diff = total_words - target_words
        result['diff'] = diff
        if diff > 100:
            result['status'] = 'OVER'
        elif diff < -100:
            result['status'] = 'UNDER'
        else:
            result['status'] = 'OK'

    return result


def print_report(result: dict):
    """Print analysis report."""
    if not result:
        return

    print(f"\n{'='*50}")
    print(f"📄 {result['file']}")
    print(f"{'='*50}")

    # Total
    total = result['total_words']
    target = result.get('target')
    if target:
        diff = result.get('diff', 0)
        status = result.get('status', 'N/A')
        status_icon = {'OK': '✅', 'OVER': '⚠️', 'UNDER': '⚠️'}.get(status, '')
        print(f"\n📊 总字数: {total} 词 (目标: {target}) {status_icon} {status}")
        if diff > 0:
            print(f"   超出 {diff} 词")
        elif diff < 0:
            print(f"   还差 {-diff} 词")
    else:
        print(f"\n📊 总字数: {total} 词")

    # Per paragraph
    print(f"\n📝 段落拆分 ({result['paragraph_count']} 段):")
    for idx, count in result['paragraph_words']:
        bar = '█' * min(count // 20, 50)
        print(f"   P{idx:>2}: {count:>4}词 {bar}")

    # Why School check
    if result['has_why_school']:
        print(f"\n✅ 包含 Why School 段")
    else:
        print(f"\n⚠️  未找到 Why School 段 — 建议添加")

    # Filler check
    if result['filler_issues']:
        print(f"\n🔍 发现可疑短语:")
        for label, count in result['filler_issues']:
            print(f"   ⚠️  '{label}' 出现 {count} 次 — 建议替换")
    else:
        print(f"\n✅ 未发现明显假大空短语")

    # Recommendations
    print(f"\n💡 建议:")
    if target:
        if result.get('status') == 'OVER':
            print(f"   字数超标，建议压缩 P3-P5 段，保留 P1+P7+P8")
        elif result.get('status') == 'UNDER':
            print(f"   字数不足，建议扩展核心经历段落")
    if not result['has_why_school']:
        print(f"   添加 Why School 段（每校100-150词独立撰写）")
    if result['filler_issues']:
        print(f"   替换假大空短语为具体经历描述")


def main():
    if len(sys.argv) < 2:
        print("用法: python ps_word_count.py <ps_file.md> [--target <target_words>]")
        print("示例: python ps_word_count.py my_ps.md --target 1000")
        sys.exit(1)

    ps_file = sys.argv[1]
    target = None

    if '--target' in sys.argv:
        idx = sys.argv.index('--target')
        if idx + 1 < len(sys.argv):
            target = int(sys.argv[idx + 1])

    result = analyze(ps_file, target)
    print_report(result)


if __name__ == '__main__':
    main()