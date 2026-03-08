login_logs = [
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"},
    {"ip": "192.168.1.15", "user": "root", "status": "failed"},
    {"ip": "172.16.0.5", "user": "ubuntu", "status": "success"},
    {"ip": "192.168.1.15", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "admin", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "root", "status": "failed"},
    {"ip": "203.0.113.8", "user": "admin", "status": "failed"},
    {"ip": "10.0.0.45", "user": "root", "status": "success"}
]

##shows how the IP address is blocked in 3 different firewalls.
def block_ip(ip_address):
    i=1
    while (i<=3):  
        print(f"Blocking {ip_address} on Firewall {i} ...") 
        i+=1
        

get_block_ip=block_ip("10.0.0.45")

##shows how many times each IP has failed.
def analyze_logs(logs):
    failed_counts={}
    for ip in logs:
            if(ip["status"] == "failed"):
                received_id=ip["ip"]
                if received_id in failed_counts:
                    failed_counts[received_id]+=1
                else:
                    failed_counts[received_id]=1
    return failed_counts

##block ips that have 3 or more failed logins
def banned_ips(failed_status_counts):
    banned_ips = {}
    for ip, count in failed_status_counts.items():
        if count >= 3:
            banned_ips[ip] = count  
            block_ip(ip)
    return banned_ips

    

failed_status_counts = analyze_logs(login_logs)
print("Failed counts IP:", failed_status_counts)

get_banned = banned_ips(failed_status_counts)
print("Banned:", get_banned)




def main():
    if __name__ == "__main__":
        analyze_logs(login_logs)
    main()