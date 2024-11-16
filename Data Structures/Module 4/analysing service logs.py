from datetime import datetime

data = [
    {"timestamp": "2024-10-26 07:02:15", "ip": "192.168.1.100", "method": "GET", "endpoint": "/api/users", "status": 200, "response_time": 0.05},
    {"timestamp": "2024-10-26 07:05:46", "ip": "192.168.1.101", "method": "POST", "endpoint": "/api/login", "status": 401, "response_time": 0.08},
    {"timestamp": "2024-10-26 07:08:18", "ip": "192.168.1.102", "method": "GET", "endpoint": "/api/products", "status": 500, "response_time": 1.20},
    {"timestamp": "2024-10-26 07:12:20", "ip": "192.168.1.100", "method": "PUT", "endpoint": "/api/users/1", "status": 200, "response_time": 0.07},
    {"timestamp": "2024-10-26 07:15:25", "ip": "192.168.1.103", "method": "GET", "endpoint": "/api/products", "status": 200, "response_time": 0.04},
    {"timestamp": "2024-10-26 07:18:33", "ip": "192.168.1.104", "method": "POST", "endpoint": "/api/orders", "status": 201, "response_time": 0.15},
    {"timestamp": "2024-10-26 07:22:05", "ip": "192.168.1.101", "method": "GET", "endpoint": "/api/profile", "status": 403, "response_time": 0.03},
    {"timestamp": "2024-10-26 07:25:40", "ip": "192.168.1.105", "method": "DELETE", "endpoint": "/api/cart/1", "status": 204, "response_time": 0.02},
    {"timestamp": "2024-10-26 07:28:15", "ip": "192.168.1.100", "method": "GET", "endpoint": "/api/products/5", "status": 404, "response_time": 0.01},
    {"timestamp": "2024-10-26 07:30:50", "ip": "192.168.1.106", "method": "POST", "endpoint": "/api/login", "status": 200, "response_time": 0.06},
    {"timestamp": "2024-10-26 07:33:22", "ip": "192.168.1.102", "method": "GET", "endpoint": "/api/orders/history", "status": 200, "response_time": 0.25},
    {"timestamp": "2024-10-26 07:35:10", "ip": "192.168.1.107", "method": "PUT", "endpoint": "/api/profile", "status": 400, "response_time": 0.04},
    {"timestamp": "2024-10-26 07:38:45", "ip": "192.168.1.108", "method": "GET", "endpoint": "/api/products", "status": 200, "response_time": 0.08},
    {"timestamp": "2024-10-26 07:41:30", "ip": "192.168.1.109", "method": "POST", "endpoint": "/api/feedback", "status": 201, "response_time": 0.12},
    {"timestamp": "2024-10-26 07:43:20", "ip": "192.168.1.101", "method": "POST", "endpoint": "/api/login", "status": 401, "response_time": 0.07},
    {"timestamp": "2024-10-26 07:45:55", "ip": "192.168.1.110", "method": "GET", "endpoint": "/api/categories", "status": 200, "response_time": 0.03},
    {"timestamp": "2024-10-26 07:48:12", "ip": "192.168.1.100", "method": "GET", "endpoint": "/api/users", "status": 200, "response_time": 0.06},
    {"timestamp": "2024-10-26 07:50:33", "ip": "192.168.1.111", "method": "POST", "endpoint": "/api/orders", "status": 500, "response_time": 2.50},
    {"timestamp": "2024-10-26 07:52:48", "ip": "192.168.1.102", "method": "GET", "endpoint": "/api/products", "status": 502, "response_time": 1.80},
    {"timestamp": "2024-10-26 07:54:15", "ip": "192.168.1.112", "method": "PUT", "endpoint": "/api/cart", "status": 200, "response_time": 0.09},
    {"timestamp": "2024-10-26 07:55:40", "ip": "192.168.1.113", "method": "GET", "endpoint": "/api/search", "status": 200, "response_time": 0.15},
    {"timestamp": "2024-10-26 07:57:22", "ip": "192.168.1.101", "method": "POST", "endpoint": "/api/login", "status": 429, "response_time": 0.02},
    {"timestamp": "2024-10-26 07:58:10", "ip": "192.168.1.114", "method": "GET", "endpoint": "/api/products/featured", "status": 200, "response_time": 0.11},
    {"timestamp": "2024-10-26 07:59:05", "ip": "192.168.1.115", "method": "POST", "endpoint": "/api/newsletter", "status": 201, "response_time": 0.07},
    {"timestamp": "2024-10-26 07:59:45", "ip": "192.168.1.100", "method": "GET", "endpoint": "/api/logout", "status": 200, "response_time": 0.01}
]

#eg data {"timestamp": "2024-10-26 07:02:15", "ip": "192.168.1.100", "method": "GET", "endpoint": "/api/users", "status": 200, "response_time": 0.05}

class ServerLogs:
    fil = []
    def __init__(self, x):
        self.x = x

    def update_logs(self, val):
        curr_time = datetime.now()
        data_time = datetime.strptime(val[0], "%Y-%m-%d %H:%M:%S")
        time_differ = curr_time - data_time
        if time_differ.total_seconds() <= 3600:
            dic = self.service_logs()
            if val[1] in dic.keys():
                dic[val[1]] += 1
                ServerLogs.fil.append([val[1], "added to 1hr mark"])
            else:
                dic[val[1]] = 1
                ServerLogs.fil.append([val[1], "newly added to 1hr mark"])
        ServerLogs.fil.append([val[1], "ignored because time_diff is greater than 1hr"])


    def service_logs(self, ip=None):
        filtered = [[i["timestamp"], i["ip"]] for i in self.x]
        dic = {}

        for i in filtered:
            cur_time = datetime.now()
            data_time = datetime.strptime(i[0], "%Y-%m-%d %H:%M:%S")
            time_differ = cur_time - data_time
            if time_differ.total_seconds() <= 3600:
                if i[1] in dic.keys():
                    dic[i[1]] += 1
                else:
                    dic[i[1]] = 1

        if ip is not None:
            return f'ip:{ip} accessed: {dic[ip]}times in last 1hr'

        return dic

item = ServerLogs(data)
item.update_logs(["2024-10-26 07:02:15", "192.168.1.101"])
print(item.service_logs("192.168.1.101"))
print(item.fil)
