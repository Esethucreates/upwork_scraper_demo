import httpx


class ProxyManager:
    def __init__(self):
        self.proxy_server = httpx.get(
            "https://proxylist.geonode.com/api/proxy-list?protocols=http&limit=500&page=1&sort_by=speed&sort_type=asc")
        self.proxies_used = set()

    def get_proxy(self, current_ip_id: str = "111111111111111111111111") -> dict[str, str]:
        proxy_index = 0
        proxy_list = self.proxy_server.json()["data"][proxy_index]  # This is a list now

        if current_ip_id in self.proxies_used:
            proxy_index = proxy_index + 1

        self.proxies_used.add(proxy_list["_id"])
        return {"proxy_id": proxy_list["_id"], "ip_address": proxy_list["ip"],
                "port": proxy_list["port"], "protocols": proxy_list["protocols"]}

    def get_proxies_used(self) -> set[str]:
        return self.proxies_used
