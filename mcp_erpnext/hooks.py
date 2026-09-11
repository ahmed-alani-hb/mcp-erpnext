app_name = "mcp_erpnext"
app_title = "MCP ERPNext"
app_publisher = "Casys AI"
app_description = "Frappe app wrapper for the @casys/mcp-erpnext MCP server"
app_email = "contact@casys.ai"
app_license = "MIT"

# The MCP server runs outside the bench and reaches this site over the REST
# API, so this app intentionally registers no hooks: installing it neither
# patches the site nor starts the server.
