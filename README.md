[README.md](https://github.com/user-attachments/files/33956427/README.md)
# 留学申请中介助理 Skill

> 留学申请中介助理 Skill · 完整方法论封装。适配 DIY 与找中介两类客户，覆盖定校（冲刺/主申/保底）→ AI 评估 → 模块化文书写作 → 超哥视角润色 → 纳什均衡策略优化 → 投递监控全链路。内置首次对话脚本（小红书风格）、通用申请材料清单（5大类）、甘特图时间线+AI提醒Prompt、32个文书素材挖掘问题、模块化文书架构（P1-P8）、纳什均衡四维分析框架（DYNAMics/Tradeoffs/Risks/Hidden Players）、3个可执行Python脚本（PS字数自动检查 / Why School段生成器 / CV模板生成器）。基于真实案例打磨，已完全脱敏，可直接上传 GitHub 开源。核心理念：既然留学了，一定要冲，不然浪费时间。—— 拿到你的 offer呀！

---

## 这是什么

一个给 AI 助手用的**留学申请方法论 Skill**。你把它装进 WorkBuddy（或任何兼容 Skill 格式的 AI 助手），它就变成你的留学申请中介助理——能陪你从第一次聊天走到拿到 offer。


## 适配人群

- **DIY 申请党**：自己搞全部流程，需要方法论 + 工具 + 时间线
- **找中介的**：已经签了中介，需要评估、监督、文书把关
- ** borderline 型选手**：均分刚好卡线、没有实习——这套方法论依旧适用

## 核心流程

```
首次对话 → 定校策略 → AI 评估 → 模块化文书 → 超哥视角润色 → 纳什均衡优化 → 投递监控
```

### 首次对话

开场先判断客户是 DIY 还是找中介，走不同路径。脚本参考 `references/first-conversation-script.md`。

### 定校策略

三档分层：**冲刺档**（QS Top 50，20-40% 录取率）→ **主申档**（QS 50-200，40-70%）→ **保底档**（QS 200+，70-90%）。从冲刺档开始倒推。

### 模块化文书

通用 Body 写一遍（P1-P8 八段式），各校只换 Why School 段（100-150 词）。详见 `references/modular-document-approach.md`。

### 超哥视角润色

完成初稿后，用超哥的判断框架（ROI、信息不对称、逆向筛选、反中介）审视文书，给出麻辣修改意见。

### 纳什均衡策略优化

用四维分析框架（DYNAMics / Tradeoffs / Risks / Hidden Players）优化投递顺序、风险对冲、家庭约束。详见 `references/nash-equilibrium-framework.md`。

## 目录结构

```
study-abroad-agent-assistant/
├── SKILL.md                          # 主文件：YAML 元信息 + 7 个章节
├── README.md                         # 本文件
├── references/
│   ├── first-conversation-script.md  # 首次对话脚本（小红书风格）
│   ├── document-checklist.md         # 通用申请材料清单（5 大类）
│   ├── timeline-template.md          # 甘特图时间线 + AI 提醒 Prompt
│   ├── ps-reference-example.md       # 文书叙事策略参考（脱敏案例）
│   ├── document-mining-questions.md  # 32 个文书素材挖掘问题
│   ├── modular-document-approach.md  # 模块化文书架构（P1-P8）
│   └── nash-equilibrium-framework.md # 纳什均衡四维分析框架
└── scripts/
    ├── ps_word_count.py              # PS 字数自动检查 + 填充词检测
    ├── why_school_generator.py       # 各校 Why School 段生成器
    └── cv_template_generator.py      # CV 模板生成器（Markdown / 纯文本）
```

## 可执行脚本

### PS 字数检查

```bash
python scripts/ps_word_count.py your_ps.md --target 1000
```

输出：总字数、分段字数、填充词检测、Why School 段识别。

### Why School 段生成器

```bash
python scripts/why_school_generator.py "University of Sydney" "Master of Media and Communications" --student-story "fashion content creator"
```

内置 13 所澳洲大学资源，生成三段式 Why School 框架：学校资源 → 学生故事连接 → 城市/区域语境。

### CV 模板生成器

```bash
python scripts/cv_template_generator.py --format markdown
```

生成英文 CV 模板，Markdown 或纯文本格式。

## 安装方式

Skill 文件夹直接放入 WorkBuddy 的 skills 目录即可：

```
~/.workbuddy/skills/study-abroad-agent-assistant/
```

或项目级：

```
{workspace}/.workbuddy/skills/study-abroad-agent-assistant/
```

## 隐私说明

所有案例已完全脱敏——真实姓名、具体学校、精确分数、日期均已移除或泛化。

## 更新日志

- **v1.0** — 初始版本：核心方法论 + 7 个参考文档 + 3 个可执行脚本
