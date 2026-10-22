# AI Engineer Roadmap: Zero to Advanced

> A practical, project-driven roadmap for web/mobile developers who want to become **AI Application Engineers** — building chatbots, RAG systems, and AI agents that run in production.
>
> Study time: **10 hours/week** · Duration: **6–12 months** · Cost: **free** (official docs + free courses)

If you can build a web app with a backend and a database, you can follow this roadmap. If you can't yet, start at **Phase 0**.

---

## Table of Contents

1. [Who this is for](#who-this-is-for)
2. [Core strategy](#core-strategy)
3. [The stack](#the-stack)
4. [Roadmap overview](#roadmap-overview)
5. [Weekly routine](#weekly-routine-10-hours)
6. [Phase 0 – Prerequisites](#phase-0-prerequisites)
7. [Phase 1 – LLM fundamentals](#phase-1-ai-and-llm-fundamentals)
8. [Phase 2 – LLM application engineering](#phase-2-llm-application-engineering)
9. [Phase 3 – Embeddings and RAG](#phase-3-embeddings-and-rag)
10. [Phase 4 – AI agents, tool calling and MCP](#phase-4-ai-agents-tool-calling-and-mcp)
11. [Phase 5 – Production AI engineering](#phase-5-production-ai-engineering)
12. [Phase 6 – ML fundamentals (parallel)](#phase-6-machine-learning-fundamentals-parallel-track)
13. [Phase 7 – Advanced AI engineering](#phase-7-advanced-ai-engineering)
14. [Phase 8 – Career: jobs, freelancing, SaaS](#phase-8-career-jobs-freelancing-saas)
15. [Repository structure](#repository-structure)
16. [What to skip](#what-to-skip-for-now)
17. [Glossary](#glossary)
18. [Progress tracker](#progress-tracker)

---

## Who this is for

| You are... | Start at |
|---|---|
| New to programming or only know HTML/CSS/basic JS | Phase 0 (full) |
| Junior web dev (can build a CRUD app with a DB) | Phase 0 checklist → Phase 1 |
| Full-stack web/mobile dev (Node/TypeScript or Python, SQL) | Phase 1 |

Target roles after this roadmap:

- **AI Application Engineer / Generative AI Engineer / LLM Engineer** – main target
- **Full-Stack or Backend Engineer on AI-enabled products** – the safety net
- **AI Platform / AI Backend Engineer** – longer-term growth
- **Machine Learning Engineer** – later option, after Phase 6–7

---

## Core strategy

1. **Software engineering is the foundation.** Nobody hires an "AI engineer" who can't ship a reliable API with auth, tests and a database. Keep these skills sharp.
2. **One language first.** This roadmap is **TypeScript-first** (Node.js + Next.js/NestJS). Python is added later, only where it is genuinely needed (ML fundamentals, some agent frameworks). Learning two stacks in parallel at 10 hours/week kills your speed.
3. **Build on real systems.** Every project in this roadmap has two options: a *generic* version (for learning) and a *real* version (plug AI into an app you or your company already have — an ERP, an accounting app, a shop). The real version is always worth more in interviews.
4. **Measure from day one.** Evaluation (test cases for your AI features) starts in Phase 2, not at the end. If you can't measure it, you can't improve it.
5. **Ship, then apply.** Start applying for jobs/clients after Project 3, not after finishing the whole roadmap.
6. **ML theory runs in parallel, never blocks.** Understanding transformers and embeddings matters; training models from scratch does not (yet).

---

## The stack

| Layer | Technology | Why |
|---|---|---|
| Web frontend | Next.js + TypeScript | Streaming UIs, server actions, what most teams use |
| Backend | NestJS or Next.js API routes (TypeScript) | Your existing skills; keep one language |
| AI SDK | Vercel AI SDK + official OpenAI / Anthropic SDKs | Provider-agnostic streaming, tool calling, structured output |
| Model providers | OpenAI **and** one more (Anthropic Claude / Google Gemini / open models via Ollama) | Never depend on one vendor |
| Validation | Zod | Schemas for tool inputs and structured outputs |
| Database | PostgreSQL + **pgvector** | One DB for users, chats, and embeddings |
| Background jobs | Redis + BullMQ | Document ingestion, long-running agents |
| Agent tooling | Direct SDK calls → Vercel AI SDK agents → LangGraph (Phase 7) | Learn the loop by hand before using a framework |
| Tool interface | **Model Context Protocol (MCP)** | The standard way agents talk to your systems |
| Evaluation | Vitest/Jest + a golden test set + Langfuse (or Promptfoo) | Regression testing for prompts and retrieval |
| Observability | Langfuse (open source) | Trace every model + tool call, cost, latency |
| Deployment | Docker + Railway / Fly.io / VPS | Simple first, cloud-native later |
| Python (Phase 6+) | Python, uv, scikit-learn, PyTorch basics, FastAPI | ML fundamentals and the Python agent ecosystem |

**Rule:** one model API, one retrieval approach, one agent approach. Add tools only when a project demands them.

---

## Roadmap overview

| Phase | Duration | Goal | Deliverable |
|---|---|---|---|
| 0. Prerequisites | 0–8 weeks (as needed) | Solid TypeScript, Node, SQL, Git, HTTP | Deployed CRUD app with auth |
| 1. LLM fundamentals | Weeks 1–2 | Understand LLMs and model APIs | CLI AI assistant |
| 2. LLM application engineering | Weeks 3–4 | Full-stack chatbot + first evals | Deployed chatbot with eval set |
| 3. Embeddings and RAG | Weeks 5–7 | Chat with your own documents | Document assistant with citations |
| 4. Agents, tools, MCP | Weeks 8–11 | Agents that use APIs safely | Business agent + MCP server |
| 5. Production AI | Weeks 12–16 | Reliable, tested, monitored systems | Hardened flagship project |
| 6. ML fundamentals | Parallel, months 3–6 | Understand the models you use | Notes + 2 mini ML projects |
| 7. Advanced AI engineering | Months 7–9 | Orchestration, advanced RAG, system design | Research/task-execution agent |
| 8. Career | From week 8 onward | Jobs, freelancing, SaaS | Portfolio, applications, first contract |

Weeks are planning targets, not deadlines. Take longer when something isn't clear; don't skip ahead when it isn't working.

### What you can do after each milestone

- **After Phase 1:** make an AI call from your own code and explain what happened.
- **After Phase 2:** ship a real chatbot with login, history, and streaming.
- **After Phase 3:** build "chat with your documents" for any business. **→ Start applying.**
- **After Phase 4:** build agents that read your systems and take approved actions.
- **After Phase 5:** call yourself an AI Application Engineer with evidence.
- **After Phase 7:** design AI systems, not just build features.

---

## Weekly routine (10 hours)

| Activity | Hours |
|---|---|
| Learn: docs, one lesson, one video | 2–3 |
| Build: your current project | 4–5 |
| Verify: tests, evals, notes, README | 1–2 |
| Career: DSA, system design, CV, applications | 1 |

**The learning loop for every topic:**

1. Read/watch **one** lesson.
2. Write the concept in your own words in `notes/concepts.md`.
3. Implement a small example **without copy-pasting**.
4. Break it on purpose: bad input, API failure, model mistake. See what happens.
5. Commit it. Write one line in `notes/weekly-log.md`.

Every Sunday: review the week, plan the next 10 hours.

---

# Phase 0: Prerequisites

**Duration:** 0–8 weeks, depending on where you start. Experienced devs: just tick the checklist and move on.

You don't need everything to be perfect, but AI engineering sits on top of normal backend engineering. Weak foundations here will block you in Phase 2–4.

### Checklist

**Programming**
- [ ] JavaScript: async/await, Promises, modules, error handling
- [ ] TypeScript: types, interfaces, generics, `unknown` vs `any`, narrowing
- [ ] Node.js: npm/pnpm, environment variables, `fetch`, streams basics
- [ ] OOP basics and clean code (functions, modules, naming)
- [ ] DSA basics: arrays, hash maps, recursion, Big-O (interview level)

**Web**
- [ ] HTTP: methods, status codes, headers, JSON, REST
- [ ] Build a REST API (Express/NestJS/Next.js routes) with validation (Zod)
- [ ] React/Next.js: components, state, data fetching, forms
- [ ] Authentication: sessions/JWT, password hashing, protected routes

**Data**
- [ ] SQL: SELECT/JOIN/GROUP BY, indexes, transactions
- [ ] PostgreSQL + an ORM/query builder (Prisma or Drizzle)
- [ ] Database design: tables, relations, migrations

**Tooling**
- [ ] Git & GitHub: branches, PRs, good commit messages, `.gitignore`
- [ ] Docker basics: Dockerfile, docker compose, running Postgres locally
- [ ] Deploy something publicly (Railway, Fly.io, Vercel, or a VPS)
- [ ] Write a README that another person can follow

### Resources

- JavaScript/TypeScript: https://javascript.info · https://www.totaltypescript.com (free tutorials)
- Node.js docs: https://nodejs.org/en/learn
- Next.js Learn course: https://nextjs.org/learn
- NestJS docs: https://docs.nestjs.com
- SQL: https://sqlbolt.com · PostgreSQL docs: https://www.postgresql.org/docs/
- Prisma: https://www.prisma.io/docs · Drizzle: https://orm.drizzle.team/docs
- Git: https://git-scm.com/book
- Docker: https://docs.docker.com/get-started/
- DSA: https://neetcode.io (roadmap) · https://leetcode.com

### Project 0: Deployed CRUD app

A task manager, inventory list, or notes app with: login, a PostgreSQL database, a REST API with validation, a Next.js UI, Docker, deployed with a public URL, and a README.

**Milestone:** You can ship a full-stack app end-to-end on your own.

---

# Phase 1: AI and LLM Fundamentals

**Duration:** Weeks 1–2

### Learn

- [ ] AI vs Machine Learning vs Deep Learning vs Generative AI (one-paragraph definitions)
- [ ] What is a Large Language Model (LLM)?
- [ ] Tokens and tokenization — try a tokenizer playground
- [ ] Context windows and why they matter
- [ ] How LLMs generate text: next-token prediction, temperature, sampling
- [ ] Prompt roles: system / user / assistant
- [ ] Hallucinations and model limitations
- [ ] Model APIs, API keys, environment variables
- [ ] Input vs output tokens and pricing
- [ ] Structured outputs (validated JSON with Zod)
- [ ] Hosted APIs vs open models (run one locally with Ollama)

### Resources

| Resource | Use it for |
|---|---|
| Andrej Karpathy – *Intro to Large Language Models* (YouTube, 1 hr) | Best single overview of what an LLM is |
| 3Blue1Brown – *But what is a GPT?* and the neural network series: https://www.3blue1brown.com/topics/neural-networks | Visual intuition |
| OpenAI API docs: https://platform.openai.com/docs | Reference while building |
| Anthropic docs: https://docs.anthropic.com | Second provider; excellent prompting guide |
| Anthropic free courses (prompting, tool use): https://github.com/anthropics/courses | Hands-on prompt engineering |
| Vercel AI SDK docs: https://sdk.vercel.ai/docs | TypeScript AI integration |
| OpenAI tokenizer: https://platform.openai.com/tokenizer | See tokens with your own eyes |
| Ollama: https://ollama.com | Run an open model locally |

### Week 1 — day by day

| Day | Task | Time |
|---|---|---|
| 1 | LLMs, tokens, context windows (Karpathy video + notes) | 1.5 h |
| 2 | First API request with the official SDK; print the response and token usage | 1.5 h |
| 3 | Prompt experiments: system instructions, examples, output formats | 1.5 h |
| 4 | Structured output: extract `{name, price, category}` from messy text, validate with Zod | 1.5 h |
| 5–6 | Build the CLI assistant | 3 h |
| 7 | Review, notes, list open questions | 1 h |

### Project 1: Command-line AI assistant

- [ ] Accept user questions in a loop
- [ ] Send requests to an LLM API (try two providers)
- [ ] Keep conversation history in memory
- [ ] `--json` mode: structured, validated output
- [ ] Handle API errors, timeouts, rate limits
- [ ] Secrets in `.env`, `.env` in `.gitignore`
- [ ] README: setup, how it works, what you learned

**Milestone:** You can draw and explain the full request lifecycle: your code → model API → response → your code.

---

# Phase 2: LLM Application Engineering

**Duration:** Weeks 3–4

### Learn

- [ ] Conversation state: storing and replaying history
- [ ] Streaming responses end-to-end (server → UI)
- [ ] System prompts and prompt templates
- [ ] Structured output validation and retries on invalid output
- [ ] Function calling basics (one tool, e.g. "get current time" or "lookup product")
- [ ] Token counting, context trimming, summarizing old history
- [ ] Authentication and per-user chat history
- [ ] Input validation, output sanitization
- [ ] Error handling, retries with backoff, timeouts, fallback model
- [ ] Rate limiting and per-user usage/cost tracking
- [ ] Prompt caching basics
- [ ] **Evaluation basics:** a golden test set, pass/fail checks, LLM-as-judge (simple)

### Resources

- Vercel AI SDK: streaming, `generateObject`, tools — https://sdk.vercel.ai/docs
- OpenAI guides: streaming, structured outputs, function calling
- Anthropic guide: tool use, prompt caching
- Promptfoo (prompt/eval testing): https://www.promptfoo.dev/docs/
- Langfuse (tracing, free self-host/cloud tier): https://langfuse.com/docs

### Project 2: Full-stack AI chatbot

```
Next.js (chat UI, streaming)
        │
        ▼
API layer (auth, rate limits, history)
        │               │
        ▼               ▼
   PostgreSQL        LLM API(s)
        │
        ▼
   Langfuse (traces)
```

- [ ] Chat UI with streaming tokens and stop button
- [ ] Persistent history: `users`, `conversations`, `messages`
- [ ] Authentication
- [ ] Per-user usage limits; token and cost logging
- [ ] Auto-generated conversation titles
- [ ] One tool call (e.g. weather, product lookup)
- [ ] Error states in the UI (retry, offline, limit reached)
- [ ] **Eval set:** 20–30 prompts with expected behaviour; a script that runs them and reports pass rate
- [ ] Tracing with Langfuse
- [ ] Dockerized and deployed; README with architecture diagram and screenshots

**Real-project option:** add an AI assistant inside an app you already own or maintain (an ERP, an accounting app, a shop admin).

**Milestone:** A deployed chatbot with login, history, streaming — and a test set that tells you when you break it.

---

# Phase 3: Embeddings and RAG

**Duration:** Weeks 5–7

**RAG (Retrieval-Augmented Generation):** before the model answers, your app searches your own data for relevant passages and gives them to the model. The model answers *from your data* instead of guessing.

### Learn

- [ ] Embeddings: text → vectors; why similar meaning = nearby vectors
- [ ] Cosine similarity and nearest-neighbour search
- [ ] Document ingestion: PDF, DOCX, HTML, plain text extraction
- [ ] Chunking strategies, chunk size and overlap
- [ ] Embedding models (hosted and open-source)
- [ ] pgvector: tables, HNSW vs IVFFlat indexes, filtering
- [ ] Metadata filtering and multi-tenant isolation (user A never sees user B's docs)
- [ ] Hybrid search: vector + keyword (Postgres full-text / BM25)
- [ ] Reranking basics
- [ ] Context construction and prompt budgeting
- [ ] Citations; answering "I don't know" when the docs don't cover it
- [ ] **Retrieval evaluation:** recall@k, groundedness, answer correctness

### Resources

- pgvector: https://github.com/pgvector/pgvector
- Vercel AI SDK RAG guide: https://sdk.vercel.ai/docs/guides/rag-chatbot
- DeepLearning.AI short courses on embeddings / RAG (free): https://www.deeplearning.ai/short-courses/
- Hugging Face Learn: https://huggingface.co/learn
- LlamaIndex docs (ingestion patterns reference): https://docs.llamaindex.ai
- Eugene Yan – *Patterns for Building LLM-based Systems*: https://eugeneyan.com/writing/llm-patterns/

### Project 3: Document intelligence assistant

- [ ] Upload PDFs/documents (background ingestion with BullMQ)
- [ ] Extract, clean, chunk text
- [ ] Generate embeddings; store in pgvector with metadata
- [ ] Retrieve top-k chunks with filters; add hybrid search
- [ ] Generate grounded answers with citations (document + page/section)
- [ ] Refuse or flag when documents don't contain the answer
- [ ] Document-level permissions
- [ ] **Eval set:** 30+ question/answer pairs; measure retrieval recall and answer accuracy; compare two chunk sizes and two embedding models
- [ ] Deployed; README with architecture and eval results

**Real-project option:** invoices/receipts/contracts assistant for an accounting app; policy/SOP assistant for a company; product-manual assistant for a shop.

**Milestone:** A deployed document chatbot that cites sources, admits what it doesn't know, and has measured accuracy. **Start applying for jobs and small client projects now.**

---

# Phase 4: AI Agents, Tool Calling and MCP

**Duration:** Weeks 8–11

An **agent** is a loop: the model decides which tool to call → your code executes it → the model sees the result → it decides again, until the task is done or a limit is hit. **You** define the tools, **your backend** executes them, and the model never gets raw database or shell access.

### Learn

- [ ] Chatbot vs workflow vs agent — and when a plain workflow is better
- [ ] Tool calling and JSON schemas (Zod → schema)
- [ ] The agent loop, written by hand (no framework)
- [ ] Parallel tool calls
- [ ] State management and persistence (pause / resume a run)
- [ ] Short-term memory (conversation) vs long-term memory (stored facts)
- [ ] Conditional branching, sequential steps, loops with limits
- [ ] Retries, timeouts, max-step guards, cost caps
- [ ] **Human-in-the-loop approval** for anything that changes data or sends messages
- [ ] Permissions: tenant-scoped tools, least privilege
- [ ] Tracing and logging every tool call
- [ ] **Model Context Protocol (MCP):** what it is, building an MCP server for your own system, connecting it to a client
- [ ] Multi-agent concepts (supervisor, handoffs) — awareness only
- [ ] **Agent evaluation:** task success rate, tool-call correctness, unnecessary calls

### Resources

- Anthropic – *Building Effective Agents* (article): https://www.anthropic.com/research/building-effective-agents
- Vercel AI SDK – tools and agents: https://sdk.vercel.ai/docs/foundations/agents
- OpenAI function calling guide · Anthropic tool use guide
- MCP: https://modelcontextprotocol.io (spec, TypeScript SDK, examples)
- Hugging Face Agents Course (free): https://huggingface.co/learn/agents-course
- LangGraph concepts (read only for now; use in Phase 7): https://langchain-ai.github.io/langgraph/

### Project 4: Business automation agent + MCP server

Example: an operations/support agent for an ERP, CRM, or shop.

The agent should:
1. Understand the user's request
2. Search authorized records (customers, providers, orders) via tools
3. Check status / inventory / invoices via tools
4. Summarize findings
5. Draft an email or response
6. **Ask for approval** before any write or send
7. Log every tool call, result and failure

- [ ] Define 4–6 tools with strict Zod schemas
- [ ] Wrap your existing REST APIs as tools (your backend is the tool layer)
- [ ] Validate tool arguments before execution
- [ ] Permission checks per user/tenant
- [ ] State persistence: resume an interrupted run
- [ ] Human approval step with a UI
- [ ] Max steps, timeout, cost cap
- [ ] **Expose the same tools as an MCP server**; connect it to an MCP client (e.g. Claude Desktop or your own)
- [ ] Failure-scenario tests: tool errors, bad arguments, infinite loops, prompt injection via tool output
- [ ] Execution trace viewer in the UI
- [ ] **Eval set:** 20+ tasks with expected tool sequences and outcomes

**Real-project option:** an agent on top of your company's ERP/CRM module (e.g. service providers, invoices, support tickets). This is the strongest interview story you can have.

**Milestone:** A working agent with controlled, traceable tool execution and an MCP server for your system.

---

# Phase 5: Production AI Engineering

**Duration:** Weeks 12–16

This is what separates a demo from something a company will pay for.

### Learn

- [ ] Unit and integration tests for LLM features and tools
- [ ] Regression testing with golden sets in CI
- [ ] LLM-as-judge and human review workflows
- [ ] Retrieval and answer-quality metrics (from Phase 3) in dashboards
- [ ] Hallucination analysis and root-causing failures
- [ ] Observability: tracing model + tool calls, latency, token cost per user/feature
- [ ] Caching: responses, embeddings, prompt caching
- [ ] Rate limiting, retries, graceful degradation, fallback models
- [ ] **Security:** prompt injection, untrusted document and tool output, OWASP LLM Top 10
- [ ] Secrets management, RBAC, tenant isolation
- [ ] PII handling, data retention, audit logs
- [ ] Cost optimization: model routing, smaller models, batching
- [ ] Deployment: Docker, CI/CD, environment config, health checks
- [ ] Load testing basics

### Resources

- OWASP Top 10 for LLM Applications: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- Langfuse docs: https://langfuse.com/docs
- Promptfoo (red-teaming + evals): https://www.promptfoo.dev/docs/
- Hugging Face evaluation cookbook: https://huggingface.co/learn/cookbook
- Chip Huyen – *AI Engineering* (book, highly recommended)

### Project 5: Flagship production project

Take Project 3 or 4 and harden it:

- [ ] Test suite (unit + integration + eval set) running in CI
- [ ] Tracing dashboard with cost and latency per request
- [ ] Prompt-injection defenses and red-team tests
- [ ] RBAC and tenant isolation, audit log
- [ ] Caching and fallback model
- [ ] Documented architecture: diagram + short decision records (ADRs)
- [ ] 2–3 minute demo video
- [ ] Public live demo with usage limits

**Milestone:** A production-grade AI application you can show employers and clients — with tests, traces, and security.

---

# Phase 6: Machine Learning Fundamentals (parallel track)

**Duration:** Months 3–6, ~2 hours/week alongside Phases 3–5. Does **not** block the main track.

Goal: understand the models you use well enough to explain them in interviews and make good trade-offs (prompting vs RAG vs fine-tuning). Not research, not training LLMs.

### Learn

- [ ] Linear algebra for ML: vectors, matrices, dot products, why embeddings work
- [ ] Probability and statistics; evaluation metrics (precision, recall, F1)
- [ ] Supervised vs unsupervised learning
- [ ] Linear/logistic regression, overfitting, train/val/test splits
- [ ] Gradient descent and loss functions
- [ ] Neural networks: layers, activations, backpropagation
- [ ] Transformers and attention (conceptual, then one code walkthrough)
- [ ] How LLMs are trained: pretraining → SFT → RLHF
- [ ] Prompting vs RAG vs fine-tuning: when to use which
- [ ] Inference basics: quantization, batching, latency
- [ ] Python essentials: uv, virtual envs, NumPy, pandas, notebooks

### Resources

- Google ML Crash Course: https://developers.google.com/machine-learning/crash-course
- Andrej Karpathy – *Neural Networks: Zero to Hero* (YouTube playlist)
- 3Blue1Brown – linear algebra + neural networks series
- fast.ai – Practical Deep Learning: https://course.fast.ai
- Hugging Face LLM Course: https://huggingface.co/learn/llm-course
- Book: *Hands-On Machine Learning* (Géron) — selected chapters

### Project 6: ML mini-projects (pick two)

- [ ] Train a small classifier (e.g. support-ticket categorization) with scikit-learn and measure it properly
- [ ] Implement a tiny neural network from scratch in NumPy
- [ ] Compare two embedding models on your Phase 3 eval set and write up the results
- [ ] (Optional, only with a real use case) LoRA fine-tune a small open model and compare with prompting

**Milestone:** You can explain embeddings, attention, and fine-tuning clearly in an interview — and know when *not* to fine-tune.

---

# Phase 7: Advanced AI Engineering

**Duration:** Months 7–9

### Learn

- [ ] Agent orchestration patterns: supervisor, planner–executor, handoffs
- [ ] Durable execution and long-running workflows (LangGraph, or Temporal/Inngest with the AI SDK)
- [ ] Advanced RAG: query rewriting, multi-hop, reranking models, GraphRAG awareness
- [ ] Structured extraction pipelines at scale
- [ ] Building and securing MCP servers for production
- [ ] Multimodal basics: images in, speech-to-text, text-to-speech
- [ ] System design for AI products: queues, streaming, caching, multi-tenancy, cost
- [ ] Guardrails and policy enforcement
- [ ] A/B testing prompts and models in production
- [ ] Python agent ecosystem (LangGraph, OpenAI Agents SDK) — now it's worth it

### Resources

- LangGraph docs: https://langchain-ai.github.io/langgraph/
- OpenAI Agents SDK: https://openai.github.io/openai-agents-python/
- Hugging Face Agents Course (advanced units)
- System design: *Designing Data-Intensive Applications* (Kleppmann) — selected chapters

### Project 7: Research and task-execution agent

- [ ] Break a user goal into subtasks (planner)
- [ ] Search approved sources (web and/or internal docs)
- [ ] Execute bounded workflows and save progress durably
- [ ] Cite sources and record every tool call
- [ ] Recover from failures and resume
- [ ] Evaluation harness comparing agent versions

**Milestone:** Three portfolio projects (beginner → intermediate → advanced), each with live demo, code, architecture diagram and video. You can design AI systems, not just build features.

---

# Phase 8: Career — Jobs, Freelancing, SaaS

**Starts at week 8 (after Project 3) and runs in parallel.**

### Job titles to target (priority order)

1. **Full-Stack / Backend Engineer on AI-enabled products** — safety net, most openings
2. **AI Application Engineer / Generative AI Engineer / LLM Engineer** — main target
3. **AI Platform / AI Backend Engineer** — growth path
4. **Machine Learning Engineer** — later, after Phase 6–7 and real ML work

### Checklist

- [ ] Portfolio: 3 projects, each with README, diagram, demo video, live link
- [ ] GitHub profile cleaned up; best repos pinned
- [ ] CV rewritten: full-stack **+** AI; quantify results; name the stack
- [ ] LinkedIn headline and summary updated
- [ ] DSA: 2 problems/week (never stop)
- [ ] System design: 1 case study/week (design a RAG platform, a chat product, an agent platform)
- [ ] AI engineering interview prep: prompting, RAG, agents, evals, security, cost — explain every decision in your projects out loud
- [ ] Apply weekly: local market, remote international, product companies
- [ ] Track applications in a simple sheet

### Freelance offers (sell outcomes, not "a chatbot")

| Offer | Built on | Pitch |
|---|---|---|
| Customer-support assistant trained on company docs | Projects 2 + 3 | "Cut repeat support questions" |
| Internal document / policy / SOP assistant | Project 3 | "Staff find answers in seconds" |
| Lead qualification / CRM agent | Project 4 | "Draft follow-ups, flag hot leads" |
| Workflow automation agent | Projects 4 + 5 | "Automate the boring back-office steps, with approval" |

### SaaS track

1. Pick one narrow problem you've seen in client work or your own company.
2. Talk to 5 potential customers before building.
3. Build the smallest paid version (one AI feature, not an "AI platform").
4. Measure usage, reliability, and inference cost before adding agents.

---

## Repository structure

```
ai-engineering-journey/
├── README.md                ← this roadmap
├── 00-prerequisites/        ← Project 0 (CRUD app)
├── 01-llm-fundamentals/     ← Project 1 (CLI assistant) + experiments
├── 02-chatbot/              ← Project 2
├── 03-rag/                  ← Project 3
├── 04-agents-mcp/           ← Project 4 (agent + MCP server)
├── 05-production/           ← Project 5 (hardened flagship)
├── 06-ml-fundamentals/      ← notebooks + mini projects
├── 07-advanced/             ← Project 7
└── notes/
    ├── concepts.md          ← every concept in your own words
    ├── weekly-log.md        ← what you did, what broke, next week
    └── interview-questions.md
```

Rules:
- Never commit API keys or secrets. `.env` goes in `.gitignore`.
- Every project folder has its own README: setup, architecture, what you learned, eval results.
- Weekly log every Sunday.

---

## What to skip (for now)

- Training an LLM from scratch
- Research-level math before building anything
- Fine-tuning before you have a clear use case **and** an eval set
- Multi-agent systems when a simple workflow works
- Learning five agent frameworks at once
- Learning Python *and* TypeScript AI stacks in parallel (TypeScript first)
- Paid bootcamps — the free resources above are enough to start; pay only for a specific gap

---

## Glossary

| Term | Meaning |
|---|---|
| **LLM** | Large Language Model — the model behind ChatGPT/Claude; predicts the next token |
| **Token** | A piece of text (≈ 3/4 of a word) that the model reads and writes; pricing is per token |
| **Context window** | The maximum tokens a model can see at once (prompt + history + response) |
| **Prompt** | The instructions and input you send to the model |
| **System prompt** | The standing instructions that define how the assistant should behave |
| **Hallucination** | A confident but false answer |
| **Structured output** | Forcing the model to return validated JSON instead of free text |
| **Embedding** | A list of numbers representing meaning; similar texts have nearby vectors |
| **Vector database** | Storage that can find the nearest vectors fast (pgvector, Qdrant, Pinecone) |
| **RAG** | Retrieval-Augmented Generation — fetch relevant data, then let the model answer from it |
| **Chunking** | Splitting documents into pieces before embedding them |
| **Tool / function calling** | The model asks your code to run a function and returns the result to it |
| **Agent** | A loop where the model picks tools, sees results, and keeps going until done |
| **Human-in-the-loop** | A person approves sensitive actions before they execute |
| **MCP** | Model Context Protocol — a standard for exposing tools/data to AI models |
| **Eval** | A test set that measures whether your AI feature works and catches regressions |
| **Tracing / observability** | Recording every model and tool call with latency and cost |
| **Prompt injection** | Malicious text (in a document, web page, or tool result) that tries to hijack the model |
| **Fine-tuning** | Training an existing model further on your own data |

---

## Progress tracker

| Phase | Status | Started | Completed | Project link |
|---|---|---|---|---|
| 0. Prerequisites | ☐ | | | |
| 1. LLM fundamentals | ☐ | | | |
| 2. Chatbot | ☐ | | | |
| 3. RAG | ☐ | | | |
| 4. Agents + MCP | ☐ | | | |
| 5. Production | ☐ | | | |
| 6. ML fundamentals | ☐ | | | |
| 7. Advanced | ☐ | | | |
| 8. Career | ☐ | | | |

---

**First milestone:** finish Phase 1 and ship the CLI assistant. Don't touch agents until Project 2 is deployed. Build first, learn as you build.

*Fork this repo, tick the boxes, and share your progress. If you find a better free resource, open a PR.*
