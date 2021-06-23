from ipaddress import ip_network, ip_address
from flask import Flask,request,jsonify

class solution():

    def log_parser(self,filepath):
        ip_map={}
        with open(filepath,"r") as infile:
            for row in infile:                                   # Iterate through each line in the log file and extract the IP address
                if row=="":
                    continue
                ip=row.split(" ")[0]
                try:                                            # only filter valid IP's
                    ip_address(ip)
                except Exception as e:
                    print("invalid IP {}, skipping this log line ".format(ip) + row )
                    continue
                if ip in ip_map.keys():                         # if an ip is already present in the result object, increment the counter for that IP
                    ip_map[ip]+=1
                else:
                    ip_map[ip]=1
        return ip_map

    def classify_ip(self,incoming_ips,buckets):
        res={}
        for i in buckets:                               # iterate through each CIDR range
            try:
                net = ip_network(i)
                for j in incoming_ips:                  # for each CIDR range, iterate through the IP list
                    try:
                        if (ip_address(j) in net) :     # Adjust the counter for each CIDR if a match is found
                            if i in res.keys():
                                res[i]+=1
                            else:
                                res[i]=1
                    except Exception as f:              # validate the incoming IP's
                        print("invalid IP")
                        continue
            except Exception as g:                      # Validate the CIDR Range
                print(i+" is not a valid subnet")
                continue
        return res

    def display(self,ip_list,res):
        for i in ip_list:
            print("Address {0} was encountered {1} time(s)".format(i,ip_list[i]))
        print("===========================================================================")
        for j in res:
            print("The bucket {0} contains {1} addresses".format(j,res[j]))
        return

    def web_output(self,combined_result):
        app = Flask(__name__)

        @app.route('/',methods=['GET'])
        def index():
            return jsonify(combined_result)

        app.run(debug=True, host='0.0.0.0', port=5100)

def main():
    buckets = ["108.162.0.0/16", "212.129.32.223/32", "173.245.56.0/23"]
    s=solution()
    ip_list=s.log_parser('nginx')
    res=s.classify_ip(ip_list,buckets)
    s.display(ip_list,res)
    combined_result={'buckets':res,'ip_list':ip_list}
    s.web_output(combined_result)

if __name__ == "__main__":
    main()



