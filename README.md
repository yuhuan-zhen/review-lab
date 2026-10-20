# review-lab

用来练 **PR 流程与审查纪律** 的最小项目。不是产品，是一个沙盒：故意小、故意能跑、故意能被弄坏。

对应《Claude Code 代码审查工作流·学习资料》的第 6、7、8 课。

## 这里的规则（练的就是这些）

| # | 规则 | 在哪生效 |
| --- | --- | --- |
| 1 | 任何改动都必须走 PR，不能直推 main | 分支保护（已开，enforce_admins=true） |
| 2 | CI 必须绿 | 必需状态检查 `CI / test` |
| 3 | 所有审查讨论必须 resolved | conversation resolution |
| 4 | PR 正文四节：怎么测的 / 风险 / 怎么撤 / 签字 | `pull_request_template.md` |
| 5 | 一个分支一个 PR | 人工纪律，`gh pr list --head <branch>` 先查 |
| 6 | 审查轮数上限 3 轮，第 4 轮只审增量 | 人工纪律 |

## 单人仓库的已知限制（重要）

GitHub **不允许作者批准自己的 PR**，所以"必须 1 人批准"在单人仓库里会死锁。这里的做法是：

- 沙盒**不要求**审批，但要求 CI + 讨论 resolved；
- 团队里再打开 "Require approvals: 1"，并且把作者排除在审批要求外（或用可绕过的 ruleset）。

**这不需要花钱**：公开仓库的分支保护在免费套餐上就能用。

## 跑起来

```bash
python -m unittest -v
```

## 目录

```
app.py                     被审查的代码（很小，故意留了边界）
test_app.py                验证（CI 跑的就是它）
.github/workflows/ci.yml   CI
.github/pull_request_template.md
.github/CODEOWNERS
CLAUDE.md                  项目是什么（每次审查都会读）
REVIEW.md                  这个仓库里什么算失败（审查器的过滤器）
```
