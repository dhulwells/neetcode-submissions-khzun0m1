# Agent notes: neetcode-submissions-khzun0m1

<!-- fleet-standard:v1 -->
## Git hosting, rk01 gateway and rk02 (fleet standard)

- **Code lives on self-hosted Forgejo on rk01**, not GitHub: <http://192.168.8.239:3030/dhulwells/neetcode-submissions-khzun0m1> (SSH `ssh://git@192.168.8.239:2222/dhulwells/neetcode-submissions-khzun0m1.git`). GitHub, GitHub Actions and the `gh` CLI are no longer used: do not push to, open PRs on, or read this repo from GitHub. CI is Forgejo Actions on the rk01 runners. Existing workflows stay in `.github/workflows/`, which Forgejo runs only while `.forgejo/workflows/` does not exist: never add `.forgejo/workflows/` to a repo that has `.github/workflows/`, or every `.github` workflow (CI, deploy, publish-docs) silently stops.
- **Every third-party API call goes through rk01-gateway**: LLMs (Anthropic, OpenAI, Gemini, Mistral, DeepSeek), the shared GPU model, Serper, DataForSEO, GoDaddy, Namecheap, USPTO, Slack, domain availability and trademark checks. Never call a provider with a raw key and never put provider keys in this repo, env files or app config; clients hold a gateway token only. On rk01 use `gw METHOD PATH [JSON|@FILE]`; containers on the `fleet` network use `http://rk01-gateway:8790`; the LAN uses `http://192.168.8.239:8790`. Live tool list: `GET /tools` (MCP at `/mcp`). Full reference: agent-workstation `instructions/GATEWAY.md`.
- **rk02 joins as a second gateway node on Saturday 2026-10-31.** Until `instructions/GATEWAY.md` lists rk02's address and it passes its health check, keep using rk01-gateway only. After that either node is valid under the same rules (gateway token only, no raw provider keys, no purchases/transfers/DNS changes/deletes through the gateway); prefer config that can fail over between nodes over hard-coding one host.
- Cloud sessions cannot reach the LAN; work through the linked computer with `ssh rk01`.
<!-- /fleet-standard -->
