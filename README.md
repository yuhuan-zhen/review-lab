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

## 分支保护的实际配置（2026-10-20 实测）

| 项 | 值 |
| --- | --- |
| 必需状态检查 | `test`（strict：合并前必须先对齐最新 main） |
| enforce_admins | 开（管理员也拦） |
| 必需讨论 resolved | 开 |
| 必需批准 | 未开（单人仓库会死锁，理由见上） |
| force push / 删除分支 | 禁止 |

### 踩到的坑：必需检查的名字

填 `CI / test`（工作流名 / job 名）会让 PR **永远 BLOCKED**——GitHub 在等一个永远不会上报的检查名。
正确做法是**只填 job 名**：本仓库是 `test`。

判定方法（比看 UI 可靠）：检查全绿时读 `mergeStateStatus`。

```
gh pr view <PR号> -R yuhuan-zhen/review-lab --json mergeStateStatus -q .mergeStateStatus
# CLEAN            -> 配置正确
# BLOCKED + 全绿   -> 检查名填错，或还有未 resolved 的讨论
```
