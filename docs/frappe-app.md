# Installing as a Frappe app

Frappe Cloud and `bench get-app` only accept repositories shaped like a Frappe
app: a `pyproject.toml` at the repository root and a Python package that carries
`hooks.py`, `modules.txt`, and `patches.txt`. Without them Frappe Cloud rejects
the URL with:

> This repository isn't a valid Frappe app. pyproject.toml does not exist in app
> directory.

This repository ships that scaffold (`pyproject.toml` + `mcp_erpnext/`), so the
GitHub URL can be added on Frappe Cloud or installed on a self-hosted bench.

## What the app does — and does not do

The MCP server is a Deno/Node process. It talks to ERPNext from the outside over
the REST API with an API key and secret; it is not Python and does not run
inside the bench. The Frappe app here is therefore deliberately a **no-op**:

- no hooks, no DocTypes, no patches, no scheduled jobs;
- installing it changes nothing on the site;
- installing it does **not** start the MCP server.

Its only job is to make the repository installable so it shows up in the site's
app list. The server itself is still run from
[the Quick Start](../README.md#quick-start) (stdio) or
[`http-deployment.md`](http-deployment.md) (HTTP), pointed at the site with
`ERPNEXT_URL`, `ERPNEXT_API_KEY`, and `ERPNEXT_API_SECRET`.

If all you want is to use the MCP server against a Frappe Cloud site, you do not
need to install this app at all — create an API key on the site and run the
server wherever your MCP client lives.

## Install

On a self-hosted bench:

```bash
bench get-app https://github.com/Casys-AI/mcp-erpnext
bench --site <site-name> install-app mcp_erpnext
```

On Frappe Cloud: **Apps → Add App → From GitHub**, then point it at
`https://github.com/Casys-AI/mcp-erpnext` and add the app to a bench group.

## Maintenance

`mcp_erpnext/__init__.py` carries `__version__` in PEP 440 spelling (`3.1.0b6`
for `3.1.0-beta.6`); it is one of the version locations listed in
[`AGENTS.md`](../AGENTS.md) and must be bumped with `deno.json` and `server.ts`.
