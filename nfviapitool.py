import sys
import json
import requests
import logging
import argparse
import ipaddress
from datetime import datetime
from pprint import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get(option, args):
    PATH = URL + option
    try:
        print(f'\n Sending request to Cisco NFVIS...')
        print(PATH + '\n')
        get_obj = requests.get(PATH, headers=HEADERS, auth=(args.user, args.password), verify=False)
        if get_obj.raise_for_status() is not None:
            print(f'ERROR : {get_obj.raise_for_status()}')
            sys.exit()
        elif get_obj.status_code != requests.codes.ok:
            print(f'WARNING : HTTP Status code - {get_obj.status_code}')
            return
        else:
            result = get_obj.json()
    except requests.ConnectionError as err:
        print(f'ERROR : {err}')
        sys.exit()
    else:
        if args.output:
            with open(f'{args.output[0]}', 'a') as file:
                file.write('\n[' + str(datetime.now()) + '] ' + PATH + '\n')
                json.dump(result, file, ensure_ascii=False, indent=4, sort_keys=True)
                file.close()
        return result


def post(option, args, payload=None):
    PATH = URL + option
    try:
        print(f'\n Sending request to Cisco NFVIS...')
        print(PATH + '\n')
        if payload is not None:
            post_obj = requests.post(PATH, headers=HEADERS, auth=(args.user, args.password), verify=False, data=payload)
        else:
            post_obj = requests.post(PATH, headers=HEADERS, auth=(args.user, args.password), verify=False)
        if post_obj.raise_for_status() is not None:
            print(f'ERROR : {post_obj.raise_for_status()}')
            sys.exit()
        else:
            if post_obj.status_code == 204:
                exit_code = f'INFO : HTTP Status code - {post_obj.status_code}' + ' the request has succeeded!'
            else:
                exit_code = f'INFO : HTTP Status code - {post_obj.status_code}'
            return exit_code
    except requests.ConnectionError as err:
        print(f'ERROR : {err}')
        sys.exit()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='CISCO NFVIS API TOOL')
    parser.add_argument('ipaddr', help='Cisco NFVIS IP Address', metavar='IPADDRESS')
    parser.add_argument('user', help='Cisco NFVIS Username', metavar='USERNAME')
    parser.add_argument('password', help='Cisco NFVIS Password', metavar='PASSWORD')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Turn on verbose logging and write logs to file.')


    get_group = parser.add_argument_group('Operational data requests')
    get_group.add_argument('-out', '--output', nargs=1, help='Save API request output to a file', metavar='FILENAME')
    get_group.add_argument('-sys', '--system',  choices=['brief','native'], help="Get NFVIS system settings. 'native' for complete config or 'brief'.")
    get_group.add_argument('-sysrt', '--sysroutes', action='store_true', default=False, help='Get NFVIS system routes.')
    get_group.add_argument('-gvlan', '--getvlan', help='Get the configured VLAN info of a bridge', nargs=1, metavar='BRIDGE')
    get_group.add_argument('-guser', '--getusers', help='Get all users info', action='store_true', default=False)
    get_group.add_argument('--gettacacs', help='Get TACACS+ configuration', action='store_true', default=False)
    get_group.add_argument('--getradius', action='store_true', default=False, help='Get RADIUS server configuration.')
    get_group.add_argument('--trustedips', action='store_true', default=False, help='Get trused IP source configuration.')
    get_group.add_argument('--getbannermotd', action='store_true', default=False, help='Get all banner and MOTD configuration.')
    get_group.add_argument('-gsyst','--getsystime', action='store_true', default=False, help='Get the system time information.')
    get_group.add_argument('-gethw', '--gethardware', action='store_true', default=False, help='Get platform hardware information.')
    get_group.add_argument('-gport', '--getportdetail', action='store_true', default=False, help='Get platform port details.')
    get_group.add_argument('-gwstat','--getwebstatus', action='store_true', default=False, help='Get web portal access status.')
    get_group.add_argument('-glog', '--getsyslog', action='store_true', default=False, help='Get system log config details.')
    get_group.add_argument('-gpnpip', '--getpnpipport', action='store_true', default=False, help='Get the PnP IP address & port number.')
    get_group.add_argument('-gpnp', '--getpnpstatus', action='store_true', default=False, help='get PnP operational status.')
    get_group.add_argument('--getvmcpualloc', action='store_true', default=False, help='Get information on the number of CPUs allocated to VMs, and the CPUs that are already used by VMs.')
    get_group.add_argument('-gvmcpuuse', '--getvmcpuusage', action='store_true', default=False, help='Get the VMs running in each physical CPU in the system.')
    get_group.add_argument('--checkresources', nargs=3, default=False, help='Check if there are sufficient resources for the deployment of a VM. (latency: True or False).', metavar=('VNFNAME', 'FLAVORNAME', 'LATENCY'))
    get_group.add_argument('--getbridgeall', action='store_true', default=False, help='Get all bridge configurations.')
    get_group.add_argument('--getnetworkall', action='store_true', default=False, help='Get all network configurations.')
    get_group.add_argument('--getimageinfoall', action='store_true', default=False, help='Get all VM image information.')
    get_group.add_argument('--getimageinfo', nargs='+', default=False, help='Get VM image information.', metavar='IMAGE')
    get_group.add_argument('-gdeploy','--getdeployments', action='store_true', default=False, help='Get all deployment configuration.')
    get_group.add_argument('-gdeploystat', '--getdeploymentstatus', nargs='+', default=False, help='Get deployment status & details.', metavar='DEPLOYMENTNAME')
    get_group.add_argument('-gflavorall', '--getflavordetailall', action='store_true', default=False, help='Get configuration details of all flavors.')
    get_group.add_argument('-gflavor', '--getflavordetail', nargs='+', default=False, help='Get configuration details of a flavor.', metavar='FLAVORNAME')
    get_group.add_argument('--getflavorstatus', nargs='+', default=False, help='Get operational status of a flavor.', metavar='FLAVORNAME')
    get_group.add_argument('--gethostcpuusage', action='store_true', default=False, help='Get host CPU utilization.')
    get_group.add_argument('--gethostcputable', action='store_true', default=False, help='Get the host CPU utilization statistics table (minimum, maximum, and average) of all CPU states on each of the CPUs.')
    get_group.add_argument('--gethostdiskstats', action='store_true', default=False, help='Get host disk statistics.')
    get_group.add_argument('--gethostdiskiops', action='store_true', default=False, help='Get host disk operations.')
    get_group.add_argument('--gethostdiskspace', action='store_true', default=False, help='Get host disk space.')
    get_group.add_argument('-ghostmem', '--gethostmemoryusage', action='store_true', default=False, help='Get host memory utilization.')
    get_group.add_argument('--gethostmemorytable', action='store_true', default=False, help='Get the host memory utilization in tabular format (minimum, maximum, and average) for each memory type.')
    get_group.add_argument('--gethostportstats', nargs=1, default=False, choices=['1min','5min','30min','1h','5d','30d'], help='Get the packet counts information (error-rx, error-tx, error-total, packets-rx, packets-tx, and packets-total) on all host interfaces.')
    get_group.add_argument('--gethostporttable', action='store_true', default=False, help='Get statistics information about all ports.')
    get_group.add_argument('--getvnfcpustatsall', nargs=1, default=False, choices=['1min','5min','30min','1h','5d','30d'], help='Get CPU statistics information of all VMs.')
    get_group.add_argument('--getvnfcpustats', nargs=2, default=False, help="Get CPU statistics information of specific VMs. (valid durations: '1min','5min','30min','1h','5d','30d)", metavar=('DURATION', 'VMNAME'))
    get_group.add_argument('--getvnfcpuinfoall', action='store_true', default=False, help='Get CPU information for each VM.')
    get_group.add_argument('--getcpuvnfinfo', nargs='+', default=False, help='Get the CPUs and vCPUs allocated to specific VMs in the system.', metavar='VMNAME')
    get_group.add_argument('--getvnfdiskstatsall', action='store_true', help='Get disk statistics of all VNFs')

    post_group = parser.add_argument_group('Configuration & Actions requests')
    post_group.add_argument('--wan_dhcp_renew', action='store_true', default=False, help='Renew the DHCP IP address on the WAN bridge (wan-br).')
    post_group.add_argument('--bridge_dhcp_renew', nargs=1, default=False, metavar='BRIDGENAME', help='Renew DHCP address of a bridge.')
    post_group.add_argument('--reboothost', action='store_true', default=False, help='Reboot host (chassis)')
    post_group.add_argument('--startvm', nargs='+', default=False, help='Start one or more Virtual Machines', metavar='VMNAME')
    post_group.add_argument('--stopvm', nargs='+', default=False, help='Stop one or more Virtual Machines', metavar='VMNAME')
    post_group.add_argument('--rebootvm', nargs='+', default=False, help='Reboot one or more Virtual Machines', metavar='VMNAME')

    args = parser.parse_args()

    try:
        ipaddress.ip_address(args.ipaddr)   # validate IP address
    except ValueError as err:   # exit if IP validation fails
        print(f'ERROR : {err}')
        sys.exit()
    else:
        HEADERS = {'Accept': 'application/vnd.yang.data+json', 'Content-Type': 'application/vnd.yang.data+json'}    # define HTTP headers for API call
        URL = f'https://{args.ipaddr}/api'  # derive URL from IP address

    if args.verbose:    # Enables verbose logging
        try:
            from http.client import HTTPConnection
        except ImportError:
            from httplib import HTTPConnection
        HTTPConnection.debuglevel = 1
        logging.basicConfig(filename='nfviapitool-http.log', format='%(asctime)s %(message)s')   # you need to initialize logging, otherwise you will not see anything from requests
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    # GET requests section
    if args.system:
        if args.system == 'brief':
            pprint(get('/operational/system/settings', args))
        else:
            pprint(get('/operational/system/settings-native', args))
    if args.sysroutes:
        pprint(get('/operational/system/routes?deep', args))
    if args.getvlan:
        pprint(get(f'/config/bridges/bridge/{args.getvlan[0]}/vlan', args))
    if args.getusers:
        HEADERS = {'Accept': 'application/vnd.yang.collection+json', 'Content-Type': 'application/vnd.yang.collection+json'}
        pprint(get('/config/rbac/authentication/users/user?deep', args))
    if args.gettacacs:
        pprint(get('/config/security_servers/tacacs-server?deep', args))
    if args.getradius:
        pprint(get('/config/security_servers/radius-server/', args))
    if args.trustedips:
        HEADERS = {'Accept': 'application/vnd.yang.collection+json', 'Content-Type': 'application/vnd.yang.collection+json'}
        pprint(get('/operational/system/settings-native/trusted-source', args))
    if args.getbannermotd:
        pprint(get('/operational/banner-motd', args))
        pprint(get('/config/banner-motd', args))
    if args.getsystime:
        pprint(get('/operational/system/time?deep', args))
    if args.gethardware:
        pprint(get('/operational/platform-detail', args))
    if args.getportdetail:
        HEADERS = {'Accept': 'application/vnd.yang.collection+json', 'Content-Type': 'application/vnd.yang.collection+json'}
        pprint(get('/operational/platform-detail/port_detail', args))
    if args.getwebstatus:
        pprint(get('/operational/system/portal/status', args))
    if args.getsyslog:
        pprint(get('/operational/system/logging-level', args))
    if args.getpnpipport:
        pprint(get('/config/pnp?deep', args))
    if args.getpnpstatus:
        pprint(get('/operational/pnp/status', args))
    if args.getvmcpualloc:
        pprint(get('/operational/resources/cpu-info/allocation?deep', args))
    if args.getvmcpuusage:
        pprint(get('/operational/resources/cpu-info/cpus?deep', args))
    if args.checkresources:
        opts = args.checkresources
        pprint(get(f'/operational/resources/precheck/vnf/{opts[0]},{opts[1]},{opts[2]}?deep', args))
    if args.getvnfcpuinfoall:
        pprint(get('/operational/resources/cpu-info/vnfs?deep', args))
    if args.getcpuvnfinfo:
        opts = args.getcpuvnfinfo
        [pprint(get(f'/operational/resources/cpu-info/vnfs/vnf/{x}?deep', args)) for x in opts]
    if args.getbridgeall:
        pprint(get('/config/bridges?deep', args))
    if args.getnetworkall:
        pprint(get('/config/networks?deep', args))
    if args.getimageinfoall:
        pprint(get('/config/vm_lifecycle/images?deep', args))
    if args.getimageinfo:
        opts = args.getimageinfo
        [pprint(get(f'/config/vm_lifecycle/images/image/{x}?deep', args)) for x in opts]
    if args.getdeployments:
        pprint(get('/config/vm_lifecycle/tenants/tenant/admin/deployments?deep', args))
    if args.getdeploymentstatus:
        opts = args.getdeploymentstatus
        [pprint(get(f'/operational/vm_lifecycle/opdata/tenants/tenant/admin/deployments/{x}?deep', args)) for x in opts]
    if args.getflavordetailall:
        pprint(get('/config/vm_lifecycle/flavors?deep', args))
    if args.getflavordetail:
        opts = args.getflavordetail
        [pprint(get(f'/config/vm_lifecycle/flavors/flavor/{x}?deep', args)) for x in opts]
    if args.getflavorstatus:
        opts = args.getflavorstatus
        [pprint(get(f'/operational/vm_lifecycle/opdata/flavors/flavor/{x}?deep', args)) for x in opts]
    if args.gethostcpuusage:
        HEADERS = {'Accept': 'application/vnd.yang.collection+json', 'Content-Type': 'application/vnd.yang.collection+json'}
        pprint(get('/operational/system-monitoring/host/cpu/stats/cpu-usage?deep', args))
    if args.gethostcputable:
        HEADERS = {'Accept': 'application/vnd.yang.collection+json', 'Content-Type': 'application/vnd.yang.collection+json'}
        pprint(get('/operational/system-monitoring/host/cpu/table?deep', args))
    if args.gethostdiskstats:
        pprint(get('/operational/system-monitoring/host/disk/stats?deep', args))
    if args.gethostdiskiops:
        HEADERS = {'Accept': 'application/vnd.yang.collection+json', 'Content-Type': 'application/vnd.yang.collection+json'}
        pprint(get('/operational/system-monitoring/host/disk/stats/disk-operations?deep', args))
    if args.gethostdiskspace:
        HEADERS = {'Accept': 'application/vnd.yang.collection+json', 'Content-Type': 'application/vnd.yang.collection+json'}
        pprint(get('/operational/system-monitoring/host/disk/stats/disk-space?deep', args))
    if args.gethostmemoryusage:
        pprint(get('/operational/system-monitoring/host/memory?deep', args))
    if args.gethostmemorytable:
        pprint(get('/operational/system-monitoring/host/memory/table?deep', args))
    if args.gethostportstats:
        opts = args.gethostportstats
        pprint(get(f'/operational/system-monitoring/host/port/stats/port-usage/{opts[0]}?deep', args))
    if args.gethostporttable:
        opts = args.gethostporttable
        pprint(get(f'/operational/system-monitoring/host/port/table?deep', args))
    if args.getvnfcpustatsall:
        opts = args.getvnfcpustatsall
        pprint(get(f'/operational/system-monitoring/vnf/vcpu/stats/vcpu-usage/{opts[0]}?deep', args))
    if args.getvnfcpustats:
        opts = args.getvnfcpustats
        pprint(get(f'/operational/system-monitoring/vnf/vcpu/stats/vcpu-usage/{opts[0]}/vnf/{opts[1]}?deep', args))
    if args.getvnfdiskstatsall:
        result = get('/operational/system-monitoring/vnf/disk/stats?deep', args)
        print(json.dumps(result))
    if args.bridge_dhcp_renew:
        result = post(f'/operations/hostaction/bridge-dhcp-renew/bridge/{args.bridge_dhcp_renew[0]}', args)
        print(result)
    if args.wan_dhcp_renew:
        result = post(f'/operations/hostaction/wan-dhcp-renew', args)
        print(result)
    if args.reboothost:
        result = post(f'/operations/hostaction/reboot', args)
        print(result)
    if args.startvm:
        HEADERS = {'Accept': 'application/vnd.yang.data+xml', 'Content-Type': 'application/vnd.yang.data+xml'}
        for vm in args.startvm:
            result = post('/operations/vmAction', args, f'<vmAction><actionType>START</actionType><vmName>{vm}</vmName></vmAction>')
            print(result)
    if args.stopvm:
        HEADERS = {'Accept': 'application/vnd.yang.data+xml', 'Content-Type': 'application/vnd.yang.data+xml'}
        for vm in args.stopvm:
            result = post('/operations/vmAction', args, f'<vmAction><actionType>STOP</actionType><vmName>{vm}</vmName></vmAction>')
            print(result)
    if args.rebootvm:
        HEADERS = {'Accept': 'application/vnd.yang.data+xml', 'Content-Type': 'application/vnd.yang.data+xml'}
        for vm in args.rebootvm:
            result = post('/operations/vmAction', args, f'<vmAction><actionType>REBOOT</actionType><vmName>{vm}</vmName></vmAction>')
            print(result)

    # TODO: Left of at 'System Monitoring APIs' - VNF Disk Stats APIs



