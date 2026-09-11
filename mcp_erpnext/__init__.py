"""Frappe app wrapper for the @casys/mcp-erpnext MCP server.

The MCP server itself is a Deno/Node process that talks to this site over the
REST API; installing this app on a bench or on Frappe Cloud does not start it.
See README.md for how to run the server and point it at your site.
"""

__version__ = "3.1.0b6"
