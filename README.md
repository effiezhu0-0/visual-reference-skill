# 视觉风格参考收集 Skill

## 基础信息
- 所属业务域：主站营销互动
- 当前状态：进行中 50%

## 用途

从 Pinterest、Behance、站酷等平台自动搜集视觉参考图，整理来源元数据，生成可审阅的确认看板，并在用户确认后输出可编辑的 Figma 视觉风格情绪板，用于设计调研、风格对齐和方案前期探索。

## 适用场景

- 需要快速收集某一视觉方向（如 UI 风格、配色、版式、活动视觉）的参考图
- 需要从多个设计平台横向对比同类视觉案例
- 需要将零散参考图整理成结构化文件夹，并附带来源信息
- 需要在 Figma 中生成统一版式的 16:9 情绪板，供团队评审或二次编辑
- 用户提到「参考图搜集」「情绪板」「moodboard」「Pinterest / Behance / 站酷 搜图」等需求时

## 输入

用户通常需要提供：

| 输入项 | 是否必填 | 说明 |
|--------|----------|------|
| 搜索关键词 / 视觉方向 | 必填 | 如「赛博朋克 UI」「极简品牌海报」 |
| 目标平台 | 必填 | Pinterest、Behance、站酷，默认按用户指定或常用平台 |
| 图片数量 / 分类 | 必填 | 如每类 5 张、共 10 张；或按「版式 / 配色」分类 |
| Figma 输出位置 | 必填 | 已有文件或新建文件 |
| 平台登录状态 | 条件必填 | 如需登录，用户在内置浏览器中手动完成 |

示例提问：

```
帮我从 Pinterest 和 Behance 搜集「赛博朋克 UI」参考图，
按版式和配色两类整理，确认后生成 Figma 情绪板。
```

## 输出

Skill 执行后会产出：

1. **本地参考图文件夹** `reference-images-<关键词>-YYYYMMDD/`
   - 按规范命名的图片文件（如 `001-layout-neon-grid.jpg`）
   - `manifest.json`：记录平台、关键词、分类、描述、来源 URL、作者/项目名、采集方式
   - `confirmation-board.png`：供用户审阅的确认看板

2. **Figma 情绪板**（用户确认后）
   - 16:9 画板（1920×1080）
   - 深色背景、双行分类标题、10 图位网格
   - 可继续在 Figma 中编辑

最终回复应包含：输出文件夹路径、确认看板路径、manifest 路径、Figma 文件/画板状态。

## 依赖资料

| 类型 | 名称 | 说明 |
|------|------|------|
| 设计模板 | [Figma 情绪板模板](https://www.figma.com/design/xYlbfA0qLquW7Ht0PEcpXX/AI%E5%B7%A5%E4%BD%9C%E6%B5%81%E5%B0%9D%E8%AF%95?node-id=88-3&m=dev) | 确认看板与最终幻灯片的视觉规范 |
| 规则文档 | `references/rules.md` | 采集、输出、视觉模板、Figma 与版权边界规则 |
| 流程文档 | `references/workflow.md` | 分阶段执行流程、确认门、异常处理 |
| 背景文档 | `references/overview.md` | Skill 背景、范围、核心概念 |
| 录入标准 | `references/source-docs/skill-entry-standard.md` | 《录入Skill标准.pdf》的结构要求摘要 |
| 验收样例 | `examples/input-01.md` / `examples/output-01.md` | 标准输入输出示例 |
| Agent Skill | 内置浏览器（`browser:browser`） | 打开平台、搜索、点击、截图 |
| Agent Skill | Figma MCP（`figma:figma-use`） | 创建可编辑情绪板 |
| Python 依赖 | Pillow | 生成 `confirmation-board.png` |
| 代码仓库 | [visual-reference-skill](https://github.com/effiezhu0-0/visual-reference-skill) | Skill 源码与脚本 |

安装方式：

```bash
git clone https://github.com/effiezhu0-0/visual-reference-skill.git ~/.codex/skills/reference-image-scraper
pip install pillow
```

## 边界和风险

**不能做：**

- 绕过平台登录、付费墙、私有内容或反爬/反下载限制
- 代替用户输入账号密码
- 声称对导出图片拥有版权；输出仅作视觉调研参考
- 在未获用户确认前直接生成最终 Figma 情绪板

**必须人工审核：**

- 确认看板 `confirmation-board.png` 中的图片筛选与分类是否符合预期
- 平台登录（Pinterest / Behance / 站酷等需登录时）
- 涉及版权敏感或对外发布用途时，需人工核对图片来源与使用权限

**其他风险：**

- 部分平台可能限制直接下载，此时会以截图方式采集并在 `manifest.json` 中标注 `capture_method`
- 内置 helper 脚本布局可能与 Figma 模板不完全一致时，需按 `SKILL.md` 中的视觉模板手动适配

## 目录结构

```text
reference-image-scraper/
├── README.md              # 本文件：给人看的说明
├── SKILL.md               # Agent 执行入口
├── references/            # 知识依据（规则、流程、背景）
│   ├── overview.md
│   ├── rules.md
│   ├── workflow.md
│   └── source-docs/
│       └── skill-entry-standard.md
├── examples/              # 输入输出验收样例
│   ├── input-01.md
│   └── output-01.md
├── scripts/               # 确认看板生成脚本
└── agents/openai.yaml     # Codex 运行配置
```

单次执行输出结构：

```text
reference-images-<关键词>-YYYYMMDD/
├── 001-<分类>-<标题>.jpg
├── manifest.json
└── confirmation-board.png
```

## 作者

- Effie Zhu
- erp：zhuruoyan1

希望这个 skill 可以帮到你。
