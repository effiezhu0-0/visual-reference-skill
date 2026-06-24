# Visual Reference Skill

从 Pinterest、Behance 自动搜集视觉参考图，生成确认看板，并在用户确认后输出 Figma 演示幻灯片。

## 功能

- 在浏览器中搜索关键词，浏览并筛选相关图片
- 将参考图保存到本地文件夹，并记录来源信息
- 生成 PNG 确认看板，供你审阅后再继续
- 确认后自动在 Figma 中创建 16:9 演示页

## 安装

### 1. 克隆到技能目录

**Cursor：**

```bash
git clone https://github.com/effiezhu0-0/visual-reference-skill.git ~/.cursor/skills/reference-image-scraper
```

**Codex：**

```bash
git clone https://github.com/effiezhu0-0/visual-reference-skill.git ~/.codex/skills/reference-image-scraper
```

### 2. 安装依赖

确认看板脚本需要 Pillow：

```bash
pip install pillow
```

### 3. 前置条件

- 已启用 **浏览器** 技能（用于打开 Pinterest / Behance）
- 已启用 **Figma MCP**（用于生成最终幻灯片）
- Pinterest / Behance 如需登录，请在浏览器内手动登录

## 使用

在对话中直接描述你的需求，例如：

```
帮我从 Pinterest 和 Behance 搜集「赛博朋克 UI」的参考图，
做成确认看板，确认后再生成 Figma 幻灯片。
```

### 推荐流程

1. **说明需求** — 提供搜索关键词、平台（Pinterest / Behance）、大致图片数量或分类
2. **自动搜集** — Agent 搜索、点进详情页并保存参考图
3. **审看看板** — 查看生成的 `confirmation-board.png`，确认是否满意
4. **生成 Figma** — 确认后，Agent 按模板创建 16:9 演示页

### 输出结构

```
reference-images-<关键词>-YYYYMMDD/
├── 001-<分类>-<标题>.jpg
├── 002-<分类>-<标题>.png
├── manifest.json          # 图片来源与元数据
└── confirmation-board.png # 确认看板
```

### 手动生成确认看板

```bash
python3 scripts/build_confirmation_board.py <输出文件夹>/manifest.json
```

## 文件说明

| 文件 | 说明 |
|------|------|
| `SKILL.md` | Agent 工作流与规范 |
| `agents/openai.yaml` | 技能展示名称与默认提示 |
| `scripts/build_confirmation_board.py` | 从 manifest 生成 PNG 看板 |

## 注意事项

- 仅保存浏览会话中可见的图片，不绕过登录或付费限制
- 参考图仅供设计调研，版权归原作者所有
- 详细来源信息保存在 `manifest.json`，不会全部显示在看板上

## License

MIT
