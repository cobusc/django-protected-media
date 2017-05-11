# These are the known headers used by some servers.
DEFAULT_X_SENDFILE_HEADER = "X-Sendfile"

_SERVER_HEADER_MAP = {
    "nginx": "X-Accel-Redirect",
}


def server_header(server):
    return _SERVER_HEADER_MAP.get(server, DEFAULT_X_SENDFILE_HEADER)