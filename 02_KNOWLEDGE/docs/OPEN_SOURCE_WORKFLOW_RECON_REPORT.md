# Executive Summary

Research date: 2026-05-22.

This reconnaissance looked for production-grade open-source or source-available workflow ecosystems that can be harvested into ALLURE's future business automation layer without creating agents yet. GitHub star, issue, and commit data were captured from the GitHub API on 2026-05-22. Note: GitHub `open_issues_count` includes both issues and pull requests.

The strongest shortlist is not a single "marketing agent" repository. The harvestable stack is a layered system:

1. **OpenAI Agents SDK** as the native agent runtime and compatibility target.
2. **LangGraph** for durable graph/state patterns where workflows need explicit branching, checkpoints, or long-running state.
3. **n8n or Activepieces** as the integration/workflow catalog layer, especially for CRM, email, lead routing, forms, webhooks, and lightweight business automation.
4. **Mautic or Dittofeed** as reusable marketing/lifecycle automation references.
5. **Twenty** as a CRM data/workflow reference.
6. **PostHog + GrowthBook** as analytics, funnel, experimentation, conversion, and optimization references.
7. **Robyn** only for paid acquisition budget modeling, not general automation.

The best harvest strategy for ALLURE is to extract workflow patterns, schemas, lifecycle concepts, templates, and approval/measurement loops rather than adopt one platform whole. Most "autonomous marketing agent" repos are shallow demos; the production value is in mature workflow products plus agent orchestration frameworks.

# Top Candidate Matrix

| Repo | Category | Stars | What it does | Workflow categories | Agent decomposition | OpenAI fit | Harvestability | Risks | Verdict |
|---|---:|---:|---|---|---|---|---|---|---|
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Agent runtime | 26,575 | Lightweight multi-agent workflow framework with tools, handoffs, guardrails, tracing, MCP, memory, realtime, and voice modules. | Agent orchestration, approvals, tool use, handoffs. | Native agents, tools, handoffs, runners, guardrails. | Native. Official OpenAI target. | Very high for ALLURE agent architecture. | Young project; not a business workflow library. | **Use as runtime baseline.** |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Agent workflow graph | 32,694 | Resilient agent graphs with checkpointing, SDKs, prebuilt modules. | Durable workflows, branching, multi-agent state, retries. | Graph nodes, state, edges, checkpointers, prebuilt agents. | High; OpenAI via model adapters, mappable to Agents SDK concepts. | Very high for explicit workflow modeling. | LangChain ecosystem coupling; abstraction overhead. | **Use for graph patterns, maybe not as runtime dependency.** |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Multi-agent framework | 51,963 | Role/task/crew orchestration for collaborative agents. | Content production, research, planning, delegation. | Agents, tasks, crews, flows, tools. | High; OpenAI-supported, concepts map to Agents SDK. | High for role/task templates. | Less explicit durable workflow state than LangGraph; hype surface. | **Harvest role/task decomposition.** |
| [n8n-io/n8n](https://github.com/n8n-io/n8n) | Workflow automation / iPaaS | 189,244 | Visual automation platform with 400+ integrations and AI/MCP capabilities. | Marketing ops, CRM sync, form capture, lead routing, lifecycle triggers, reporting. | Not agent-native; workflows are nodes and credentials. | Medium-high; AI/MCP nodes can bridge, workflows can call OpenAI agents. | Very high for integration catalog and workflow UX. | License is source-available/fair-code, not pure OSS; large platform. | **Best integration/workflow reference.** |
| [activepieces/activepieces](https://github.com/activepieces/activepieces) | AI workflow automation | 22,344 | Automation platform focused on AI agents, MCPs, and workflow pieces. | Marketing ops, lead workflows, content ops, CRM ops. | Pieces/actions/triggers; MCP servers can become agent tools. | High; MCP orientation maps well to OpenAI tool architecture. | Very high for reusable tool/piece packaging. | License/commercial boundaries need review before reuse. | **Strong n8n alternative, better MCP fit.** |
| [mautic/mautic](https://github.com/mautic/mautic) | Marketing automation | 9,726 | Mature marketing automation suite. | Campaigns, email, forms, landing pages, scoring, segments, channels. | Not agent-native; domain services and bundles. | Medium; agents can operate campaign objects via APIs. | Very high for lifecycle campaign model. | PHP monolith, heavy legacy surface. | **Harvest domain model, not platform.** |
| [dittofeed/dittofeed](https://github.com/dittofeed/dittofeed) | Customer engagement | 2,775 | Open-source customer messaging across email, SMS, push, WhatsApp, Slack. | Lifecycle journeys, onboarding, transactional + marketing messages. | Not agent-native; journeys, workers, API/dashboard packages. | Medium-high; agents can generate/approve lifecycle assets. | High for journey/message architecture. | Smaller community than Mautic; less proven at large scale. | **Use as modern lifecycle reference.** |
| [twentyhq/twenty](https://github.com/twentyhq/twenty) | CRM | 46,029 | Open Salesforce alternative, designed for AI. | CRM records, sales pipeline, customer lifecycle, integrations. | Not agent-native; CRM objects and apps. | Medium-high; AI/design positioning, APIs and SDK packages. | High for CRM data model and lifecycle workspace. | Source-available license boundaries; not marketing-specific. | **Use as CRM reference.** |
| [PostHog/posthog](https://github.com/PostHog/posthog) | Analytics/CDP/experimentation | 34,642 | Product/web analytics, session replay, feature flags, surveys, warehouse, CDP, AI assistant. | Funnel analytics, conversion, cohorts, surveys, session analysis, CDP. | Not agent-native; analytics products and event pipelines. | Medium-high; agents can query/interpret analytics. | Very high for measurement loops. | Large platform; license/commercial boundaries. | **Use for analytics/optimization patterns.** |
| [growthbook/growthbook](https://github.com/growthbook/growthbook) | Experimentation | 7,799 | Feature flags, experimentation, product analytics. | A/B tests, conversion experiments, decisioning, metrics. | Not agent-native; experiment objects and SDKs. | Medium; agents can propose tests and read results. | High for funnel optimization governance. | Not a full marketing automation platform. | **Use for test/experiment architecture.** |
| [facebookexperimental/Robyn](https://github.com/facebookexperimental/Robyn) | Paid acquisition / MMM | 1,464 | Marketing mix modeling and budget allocation package from Meta Marketing Science. | Paid media attribution, spend response, budget allocation. | Not agent-native; statistical modeling workflows. | Medium; agents can prepare inputs/explain outputs. | Medium-high for paid acquisition optimization. | Specialized R/Jupyter workflow; not an automation engine. | **Use narrowly for paid media modeling.** |
| [FoundationAgents/MetaGPT](https://github.com/FoundationAgents/MetaGPT) | Multi-agent framework | 68,212 | Multi-agent "software company" framework. | Software/product generation, research, planning. | Roles, actions, team, environment, memory. | Medium; can call OpenAI, but not OpenAI-native. | Medium for org/role patterns. | Less revenue-workflow aligned; abstraction is software-company-centric. | **Do not use as core; mine ideas only.** |
| [OpenHands/OpenHands](https://github.com/OpenHands/OpenHands) | Dev agent platform | 74,512 | AI-driven software development agent platform. | Coding, debugging, repo operations. | Developer agent, runtime, frontend/server, skills. | Medium-high for coding agents. | Low for revenue workflows. | Not marketing/CRM/funnel focused. | **Exclude from business workflow core.** |

# Deep Dives

## openai/openai-agents-python

Evidence: [repo](https://github.com/openai/openai-agents-python), [docs](https://openai.github.io/openai-agents-python/). GitHub API: 26,575 stars, 4,075 forks, 107 open issues/PRs, pushed 2026-05-22, MIT.

Architecture:

- Top-level folders: `docs`, `examples`, `src`, `tests`.
- Core package: `src/agents`.
- Important modules inspected: `agent.py`, `run.py`, `tool.py`, `handoffs`, `guardrail.py`, `mcp`, `memory`, `tracing`, `realtime`, `voice`, `run_state.py`.

Workflow design:

- Best suited as ALLURE's future agent execution layer.
- Supports a clean mapping from business roles to agents, business capabilities to tools, and approval gates to guardrails/handoffs.
- Does not provide marketing workflow packs. It provides the runtime primitives for building them.

Agent model:

- Agent = instructions + tools + model settings + output model + handoffs.
- Tools can wrap business APIs.
- Handoffs provide delegation between specialist agents.
- Guardrails and tracing provide operational control.

Reuse potential for ALLURE:

- Use as the compatibility baseline.
- Encode ALLURE agents as thin wrappers around harvested workflows.
- Avoid building directly against non-OpenAI abstractions unless they add durable workflow capability.

## langchain-ai/langgraph

Evidence: [repo](https://github.com/langchain-ai/langgraph), [docs homepage in repo metadata](https://docs.langchain.com/oss/python/langgraph/). GitHub API: 32,694 stars, 5,532 forks, 553 open issues/PRs, pushed 2026-05-21, MIT.

Architecture:

- Top-level folders: `docs`, `examples`, `libs`.
- `libs` includes `langgraph`, `prebuilt`, `sdk-js`, `sdk-py`, `checkpoint`, `checkpoint-postgres`, `checkpoint-sqlite`, and `cli`.

Workflow design:

- Explicit graph/state model is the main asset.
- Strong for branching workflows such as "lead captured -> qualify -> segment -> generate follow-up -> approval -> send -> measure -> optimize".
- Checkpointing modules are directly relevant to durable business workflows.

Agent model:

- Agents are graph nodes with state transitions.
- Workflows expose explicit control flow instead of hidden autonomous loops.
- Prebuilt components can accelerate common agent patterns.

Reuse potential for ALLURE:

- Harvest graph schemas, checkpoint/replay patterns, and state machine structure.
- Good fit for revenue workflows where every step must be observable and auditable.
- If ALLURE stays OpenAI-native, LangGraph can be a design reference or selective dependency, with nodes mapped to OpenAI Agents SDK runs/tools.

## crewAIInc/crewAI

Evidence: [repo](https://github.com/crewAIInc/crewAI), [homepage](https://crewai.com). GitHub API: 51,963 stars, 7,204 forks, 356 open issues/PRs, pushed 2026-05-22, MIT.

Architecture:

- Top-level folders: `docs`, `lib`, tests/config files.
- `lib` includes `crewai-core`, `crewai-tools`, `crewai-files`, `cli`, `devtools`.

Workflow design:

- Useful abstraction for revenue-first work decomposition: strategist, copywriter, campaign planner, CRM operator, analyst, QA/approval.
- Crew/task flows are readable for non-engineering workflow owners.
- Less attractive for durable state and governance than LangGraph.

Agent model:

- Role-oriented agents execute tasks inside crews/flows.
- Strong mental model for content production pipelines and research workflows.

Reuse potential for ALLURE:

- Harvest role/task templates for content, marketing, and funnel workflows.
- Reimplement or map those templates into OpenAI Agents SDK when productionizing.
- Avoid copying broad framework assumptions before ALLURE's own workflow boundaries are clearer.

## n8n-io/n8n

Evidence: [repo](https://github.com/n8n-io/n8n), [homepage](https://n8n.io). GitHub API: 189,244 stars, 57,906 forks, 1,462 open issues/PRs, pushed 2026-05-22.

Architecture:

- TypeScript monorepo.
- Top-level `packages` includes `cli`, `core`, `workflow`, `nodes-base`, `frontend`, `testing`, `node-dev`, `extensions`, `@n8n`.
- Repo metadata describes visual workflow automation, native AI capabilities, self-hosting, MCP client/server, and 400+ integrations.

Workflow design:

- Visual node graph with triggers, actions, credentials, execution history, retries, and integrations.
- Strong source of reusable operational workflows: lead capture, CRM sync, email notifications, Slack/WhatsApp alerts, webhook ingestion, spreadsheet/database updates.

Agent model:

- Not agent-native.
- Best mapped as an integration layer: each n8n node or workflow can become an OpenAI tool endpoint or a callable business process.

Reuse potential for ALLURE:

- Very high for integration catalog design and workflow UX.
- Use as benchmark for workflow visibility, execution logs, credentials, and operator control.
- Do not embed n8n by default until license/commercial constraints are reviewed.

## activepieces/activepieces

Evidence: [repo](https://github.com/activepieces/activepieces), [homepage](https://www.activepieces.com). GitHub API: 22,344 stars, 3,683 forks, 495 open issues/PRs, pushed 2026-05-22.

Architecture:

- TypeScript monorepo.
- Top-level `packages` includes `pieces`, `server`, `web`, `shared`, `cli`, `ee`, `tests-e2e`.
- Metadata emphasizes AI agents, MCP servers, workflow automation, and n8n alternative positioning.

Workflow design:

- Trigger/action pieces are modular and harvestable.
- More directly aligned with OpenAI-native tool architecture than older workflow products because MCP is a first-class concept in repo metadata.

Agent model:

- Not a pure agent runtime.
- Pieces can map cleanly to OpenAI tools; MCP servers can provide agent-accessible capabilities.

Reuse potential for ALLURE:

- Strong reference for packaging reusable business capabilities.
- Potential template for "ALLURE pieces": waitlist, investor CRM, content publishing, lead scoring, campaign QA, approval routing.
- Review licensing before copying code.

## mautic/mautic

Evidence: [repo](https://github.com/mautic/mautic), [homepage](https://www.mautic.org). GitHub API: 9,726 stars, 3,299 forks, 310 open issues/PRs, pushed 2026-05-22.

Architecture:

- PHP/Symfony-style monolith.
- Important bundles: `CampaignBundle`, `EmailBundle`, `FormBundle`, `LeadBundle`, `PageBundle`, `PointBundle`, `ReportBundle`, `SmsBundle`, `StageBundle`, `WebhookBundle`, `IntegrationsBundle`.

Workflow design:

- Directly aligned with marketing automation: contacts/leads, scoring, campaigns, landing pages, forms, channels, reports.
- Mature domain decomposition for lifecycle automation.

Agent model:

- No native agent model.
- Agents could generate segments, propose campaign branches, write copy, produce test variants, and request approval before publishing through APIs.

Reuse potential for ALLURE:

- Harvest the marketing domain model, not the PHP platform.
- Particularly useful for waitlist nurturing, invitation stages, investor communications, and venue-launch lifecycle flows.

## dittofeed/dittofeed

Evidence: [repo](https://github.com/dittofeed/dittofeed), [homepage](https://dittofeed.com/). GitHub API: 2,775 stars, 346 forks, 43 open issues/PRs, pushed 2026-03-28, MIT.

Architecture:

- TypeScript/Node monorepo.
- Top-level `packages` includes `api`, `backend-lib`, `dashboard`, `worker`, `isomorphic-lib`, `admin-cli`, `docs`, `lite`, `emailo`.
- Deployment assets include Docker Compose, Helm charts, Prometheus/Grafana config, and OpenTelemetry collector config.

Workflow design:

- Focused customer engagement: lifecycle journeys and messages across email, SMS, push, WhatsApp, Slack.
- More modern and narrower than Mautic, with a clearer messaging-product boundary.

Agent model:

- No native agent decomposition.
- Good substrate for lifecycle-message agents, approval agents, and analytics feedback agents.

Reuse potential for ALLURE:

- Strong for invitation, waitlist, post-visit, VIP, investor, and venue-opening journeys.
- Useful modern reference for worker separation and messaging infrastructure.

## twentyhq/twenty

Evidence: [repo](https://github.com/twentyhq/twenty), [homepage](https://twenty.com). GitHub API: 46,029 stars, 6,485 forks, 118 open issues/PRs, pushed 2026-05-22.

Architecture:

- TypeScript/Nx-style monorepo.
- Top-level `packages` includes `twenty-server`, `twenty-front`, `twenty-ui`, `twenty-shared`, `twenty-sdk`, `twenty-client-sdk`, `twenty-cli`, `twenty-apps`, `twenty-zapier`, `twenty-emails`, `twenty-docs`, and `twenty-claude-skills`.

Workflow design:

- CRM object model and workflow surface are directly useful for ALLURE's private waitlist, investors, partners, venues, operators, and high-intent customers.
- Less directly useful for content/ad workflows.

Agent model:

- Not agent-native, but repo is AI-positioned and includes SDK/app packages.
- OpenAI agents can act on CRM objects through APIs/tools.

Reuse potential for ALLURE:

- High for CRM schema inspiration and operational workspace patterns.
- Use as reference for records, relationships, activity history, pipeline stages, and app integrations.

## PostHog/posthog

Evidence: [repo](https://github.com/PostHog/posthog), [homepage](https://posthog.com). GitHub API: 34,642 stars, 2,746 forks, 4,233 open issues/PRs, pushed 2026-05-22.

Architecture:

- Large Python/TypeScript product platform.
- Relevant folders include `posthog/cdp`, `posthog/feature_flags`, `posthog/session_recordings`, `posthog/hogql`, `posthog/queries`, `posthog/plugins`, `frontend`, `ee`, `funnel-udf`.
- Repo metadata covers product analytics, web analytics, session replay, feature flags, experimentation, surveys, CDP, data warehouse, and AI assistant.

Workflow design:

- Strongest reference for analytics feedback loops: events -> cohorts -> funnels -> surveys/session replay -> insight -> experiment -> rollout.
- Relevant to ALLURE funnel conversion from landing page, waitlist, qualification, booking, referral, and retention.

Agent model:

- Not agent-native.
- Agents can query metrics, summarize sessions, detect drop-off, propose experiments, and create weekly optimization briefs.

Reuse potential for ALLURE:

- Very high for measurement and optimization design.
- Avoid copying platform internals; harvest concepts, event schemas, funnel reports, cohort definitions, and experiment review workflows.

## growthbook/growthbook

Evidence: [repo](https://github.com/growthbook/growthbook), [homepage](https://www.growthbook.io). GitHub API: 7,799 stars, 750 forks, 834 open issues/PRs, pushed 2026-05-22.

Architecture:

- TypeScript monorepo.
- Top-level `packages` includes `back-end`, `front-end`, `sdk-js`, `sdk-react`, `shared`, `stats`.
- Repo metadata emphasizes feature flags, experimentation, analytics, statistics, and warehouse-native workflows.

Workflow design:

- Strong for test lifecycle: hypothesis, metric, variant, exposure, result, decision.
- Useful for funnel/conversion workflows on landing pages and email journeys.

Agent model:

- No native agents.
- OpenAI agents can propose tests, generate variants, monitor results, and prepare decision memos.

Reuse potential for ALLURE:

- High as a governance model for experiments.
- Combine with PostHog-style analytics and OpenAI approval agents.

## facebookexperimental/Robyn

Evidence: [repo](https://github.com/facebookexperimental/Robyn), [docs](https://facebookexperimental.github.io/Robyn/). GitHub API: 1,464 stars, 427 forks, 113 open issues/PRs, pushed 2026-01-26, MIT.

Architecture:

- R/Jupyter-oriented marketing science package.
- Repo metadata identifies Marketing Mix Modeling, adstocking, budget allocation, cost-response curves, and hyperparameter optimization.

Workflow design:

- Narrow but valuable paid acquisition workflow: historical spend/performance -> model -> response curves -> budget recommendation.

Agent model:

- No agent model.
- Agents can prepare datasets, run modeling scripts, explain recommendations, and route budget changes for approval.

Reuse potential for ALLURE:

- Medium-high once paid acquisition spend is meaningful.
- Not useful before channel data exists.

## FoundationAgents/MetaGPT

Evidence: [repo](https://github.com/FoundationAgents/MetaGPT), [homepage](https://atoms.dev/). GitHub API: 68,212 stars, 8,691 forks, 125 open issues/PRs, pushed 2026-01-21, MIT.

Architecture:

- Python framework with `metagpt/actions`, `roles`, `team.py`, `environment`, `memory`, `tools`, `skills`, `strategy`, `provider`, `rag`, `document_store`.

Workflow design:

- Well-known multi-agent pattern library, mostly centered on software-company simulation and natural-language programming.
- Less directly useful for marketing, funnel, CRM, and analytics workflows.

Agent model:

- Roles perform actions inside teams/environments with memory and tools.

Reuse potential for ALLURE:

- Mine role/action/team concepts only.
- Do not adopt as ALLURE's core runtime because OpenAI Agents SDK is a better native target and LangGraph provides clearer durable workflow semantics.

## OpenHands/OpenHands

Evidence: [repo](https://github.com/OpenHands/OpenHands), [homepage](https://openhands.dev). GitHub API: 74,512 stars, 9,439 forks, 401 open issues/PRs, pushed 2026-05-22.

Architecture:

- Large Python/TypeScript dev-agent platform.
- Top-level includes `openhands`, `frontend`, `openhands-ui`, `server`, `containers`, `skills`, `enterprise`, `tests`.

Workflow design:

- Strong for coding/development workflows, not revenue operations.

Agent model:

- Developer agent with runtime/container control and UI/server architecture.

Reuse potential for ALLURE:

- Low for this mission.
- Could inspire future internal software-maintenance agents, but it is not a marketing/content/funnel/CRM workflow ecosystem.

# Recommended Harvest Stack

## 1. OpenAI-native agent layer

Use **OpenAI Agents SDK** as the primary runtime model:

- Agent = business role.
- Tool = callable business capability.
- Handoff = delegation between roles.
- Guardrail = approval/compliance/brand-safety gate.
- Trace = audit trail.

Initial ALLURE agent categories to design later:

- Brand strategist.
- Content producer.
- Funnel analyst.
- CRM lifecycle operator.
- Paid acquisition analyst.
- Approval/governance agent.
- Founder/investor communications assistant.

## 2. Durable workflow design layer

Harvest from **LangGraph**:

- Explicit state machines.
- Checkpointing.
- Branching.
- Human-in-the-loop pauses.
- Retry/resume semantics.

Use where workflows are not simple one-shot agent runs.

## 3. Business integration layer

Harvest from **n8n** and **Activepieces**:

- Trigger/action packaging.
- Credential separation.
- Integration catalog organization.
- Workflow execution history.
- Node/piece metadata.
- MCP/tool exposure concepts.

For ALLURE, the highest-value future workflow packs are:

- Waitlist intake and enrichment.
- Lead scoring and segmentation.
- Investor CRM updates.
- Content calendar production.
- Email/SMS/WhatsApp lifecycle journeys.
- Founder approval queue.
- Landing page conversion alerts.
- Weekly growth analytics digest.

## 4. Marketing and lifecycle domain model

Harvest from **Mautic** and **Dittofeed**:

- Campaigns.
- Segments.
- Forms.
- Landing pages.
- Lead/contact records.
- Scoring/points.
- Journey stages.
- Channel messaging.
- Reports.
- Webhooks.

Use Mautic for breadth and maturity; use Dittofeed for modern messaging/journey architecture.

## 5. CRM operational model

Harvest from **Twenty**:

- Objects and relationships.
- Activity timeline.
- Pipeline stages.
- Apps/integrations.
- SDK boundaries.
- Email/CRM workspace patterns.

ALLURE-specific CRM objects should likely include:

- Waitlist person.
- Couple profile.
- Investor.
- Partner.
- Venue.
- Operator.
- Campaign.
- Booking intent.
- Experience session.

## 6. Measurement and optimization layer

Harvest from **PostHog** and **GrowthBook**:

- Event taxonomy.
- Funnels.
- Cohorts.
- Session review.
- Surveys.
- Feature flags.
- Experiment lifecycle.
- Metrics and statistical decisioning.

ALLURE should eventually structure optimization as:

1. Capture event.
2. Detect funnel drop-off.
3. Generate insight.
4. Propose experiment.
5. Generate variants.
6. Human approve.
7. Launch.
8. Measure.
9. Decide.
10. Archive learning.

## 7. Paid acquisition modeling

Harvest narrowly from **Robyn**:

- Marketing mix modeling concepts.
- Spend-response curves.
- Budget allocation outputs.
- Channel-level scenario planning.

Only useful after ALLURE has enough paid acquisition data.

# What NOT to use

## Do not build around "autonomous marketing agent" demos

Search terms such as "marketing agent", "growth automation agent", "funnel automation agent", and "autonomous business workflow" produce many small repositories and demos. Most are not production-grade because they lack:

- Active issue/commit activity.
- Durable workflow state.
- Real integrations.
- Approval models.
- Observability.
- Repeatable workflow packs.
- Domain-rich marketing/CRM objects.

Use mature workflow products and agent frameworks instead.

## Do not use MetaGPT as the core ALLURE runtime

MetaGPT is popular and useful conceptually, but it is not revenue-workflow-first and its strongest patterns are software-company roles/actions. For ALLURE, OpenAI Agents SDK plus LangGraph-style explicit workflows is cleaner.

## Do not use OpenHands for this mission

OpenHands is high-quality for software development agents, but it does not solve marketing, content, funnel, CRM, lifecycle automation, or analytics workflows.

## Do not adopt n8n, Activepieces, PostHog, Twenty, or GrowthBook blindly

Several strong candidates are source-available or have enterprise/commercial licensing boundaries. They are still excellent architecture references, but code reuse must wait for license review.

## Do not start with Robyn

Robyn is a serious paid acquisition modeling package, but it needs spend/history data. It should not be part of the first ALLURE workflow layer.

# Source Notes

- GitHub API metadata captured 2026-05-22 for all repos listed in the matrix.
- Repository structures were inspected through GitHub API `contents` endpoints.
- Primary repo sources:
  - https://github.com/openai/openai-agents-python
  - https://openai.github.io/openai-agents-python/
  - https://github.com/langchain-ai/langgraph
  - https://docs.langchain.com/oss/python/langgraph/
  - https://github.com/crewAIInc/crewAI
  - https://github.com/n8n-io/n8n
  - https://github.com/activepieces/activepieces
  - https://github.com/mautic/mautic
  - https://github.com/dittofeed/dittofeed
  - https://github.com/twentyhq/twenty
  - https://github.com/PostHog/posthog
  - https://github.com/growthbook/growthbook
  - https://github.com/facebookexperimental/Robyn
  - https://github.com/FoundationAgents/MetaGPT
  - https://github.com/OpenHands/OpenHands
