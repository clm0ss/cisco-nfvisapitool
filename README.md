# nfvisapitool
Cisco NFVIS API Tool


Python 3.6 or later required


# Usage

python -m pip install -r requirements.txt

nfviapitool.py --help


```
usage: CISCO NFVIS API TOOL [-h] [-v] [-out FILENAME] [-sys {brief,native}]
                            [-sysrt] [-gvlan BRIDGE] [-guser] [--gettacacs]
                            [--getradius] [--trustedips] [--getbannermotd]
                            [-gsyst] [-gethw] [-gport] [-gwstat] [-glog]
                            [-gpnpip] [-gpnp] [--getvmcpualloc] [-gvmcpuuse]
                            [--checkresources VNFNAME FLAVORNAME LATENCY]
                            [--getbridgeall] [--getnetworkall]
                            [--getimageinfoall]
                            [--getimageinfo IMAGE [IMAGE ...]] [-gdeploy]
                            [-gdeploystat DEPLOYMENTNAME [DEPLOYMENTNAME ...]]
                            [-gflavorall]
                            [-gflavor FLAVORNAME [FLAVORNAME ...]]
                            [--getflavorstatus FLAVORNAME [FLAVORNAME ...]]
                            [--gethostcpuusage] [--gethostcputable]
                            [--gethostdiskstats] [--gethostdiskiops]
                            [--gethostdiskspace] [-ghostmem]
                            [--gethostmemorytable]
                            [--gethostportstats {1min,5min,30min,1h,5d,30d}]
                            [--gethostporttable]
                            [--getvnfcpustatsall {1min,5min,30min,1h,5d,30d}]
                            [--getvnfcpustats DURATION VMNAME]
                            [--getvnfcpuinfoall]
                            [--getcpuvnfinfo VMNAME [VMNAME ...]]
                            [--getvnfdiskstatsall] [--wan_dhcp_renew]
                            [--bridge_dhcp_renew BRIDGENAME] [--reboothost]
                            [--startvm VMNAME [VMNAME ...]]
                            [--stopvm VMNAME [VMNAME ...]]
                            [--rebootvm VMNAME [VMNAME ...]]
                            IPADDRESS USERNAME PASSWORD

positional arguments:
  IPADDRESS             Cisco NFVIS IP Address
  USERNAME              Cisco NFVIS Username
  PASSWORD              Cisco NFVIS Password

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Turn on verbose logging and write logs to file.

Operational data requests:
  -out FILENAME, --output FILENAME
                        Save API request output to a file
  -sys {brief,native}, --system {brief,native}
                        Get NFVIS system settings. 'native' for complete
                        config or 'brief'.
  -sysrt, --sysroutes   Get NFVIS system routes.
  -gvlan BRIDGE, --getvlan BRIDGE
                        Get the configured VLAN info of a bridge
  -guser, --getusers    Get all users info
  --gettacacs           Get TACACS+ configuration
  --getradius           Get RADIUS server configuration.
  --trustedips          Get trused IP source configuration.
  --getbannermotd       Get all banner and MOTD configuration.
  -gsyst, --getsystime  Get the system time information.
  -gethw, --gethardware
                        Get platform hardware information.
  -gport, --getportdetail
                        Get platform port details.
  -gwstat, --getwebstatus
                        Get web portal access status.
  -glog, --getsyslog    Get system log config details.
  -gpnpip, --getpnpipport
                        Get the PnP IP address & port number.
  -gpnp, --getpnpstatus
                        get PnP operational status.
  --getvmcpualloc       Get information on the number of CPUs allocated to
                        VMs, and the CPUs that are already used by VMs.
  -gvmcpuuse, --getvmcpuusage
                        Get the VMs running in each physical CPU in the
                        system.
  --checkresources VNFNAME FLAVORNAME LATENCY
                        Check if there are sufficient resources for the
                        deployment of a VM. (latency: True or False).
  --getbridgeall        Get all bridge configurations.
  --getnetworkall       Get all network configurations.
  --getimageinfoall     Get all VM image information.
  --getimageinfo IMAGE [IMAGE ...]
                        Get VM image information.
  -gdeploy, --getdeployments
                        Get all deployment configuration.
  -gdeploystat DEPLOYMENTNAME [DEPLOYMENTNAME ...], --getdeploymentstatus DEPLOYMENTNAME [DEPLOYMENTNAME ...]
                        Get deployment status & details.
  -gflavorall, --getflavordetailall
                        Get configuration details of all flavors.
  -gflavor FLAVORNAME [FLAVORNAME ...], --getflavordetail FLAVORNAME [FLAVORNAME ...]
                        Get configuration details of a flavor.
  --getflavorstatus FLAVORNAME [FLAVORNAME ...]
                        Get operational status of a flavor.
  --gethostcpuusage     Get host CPU utilization.
  --gethostcputable     Get the host CPU utilization statistics table
                        (minimum, maximum, and average) of all CPU states on
                        each of the CPUs.
  --gethostdiskstats    Get host disk statistics.
  --gethostdiskiops     Get host disk operations.
  --gethostdiskspace    Get host disk space.
  -ghostmem, --gethostmemoryusage
                        Get host memory utilization.
  --gethostmemorytable  Get the host memory utilization in tabular format
                        (minimum, maximum, and average) for each memory type.
  --gethostportstats {1min,5min,30min,1h,5d,30d}
                        Get the packet counts information (error-rx, error-tx,
                        error-total, packets-rx, packets-tx, and packets-
                        total) on all host interfaces.
  --gethostporttable    Get statistics information about all ports.
  --getvnfcpustatsall {1min,5min,30min,1h,5d,30d}
                        Get CPU statistics information of all VMs.
  --getvnfcpustats DURATION VMNAME
                        Get CPU statistics information of specific VMs. (valid
                        durations: '1min','5min','30min','1h','5d','30d)
  --getvnfcpuinfoall    Get CPU information for each VM.
  --getcpuvnfinfo VMNAME [VMNAME ...]
                        Get the CPUs and vCPUs allocated to specific VMs in
                        the system.
  --getvnfdiskstatsall  Get disk statistics of all VNFs

Configuration & Actions requests:
  --wan_dhcp_renew      Renew the DHCP IP address on the WAN bridge (wan-br).
  --bridge_dhcp_renew BRIDGENAME
                        Renew DHCP address of a bridge.
  --reboothost          Reboot host (chassis)
  --startvm VMNAME [VMNAME ...]
                        Start one or more Virtual Machines
  --stopvm VMNAME [VMNAME ...]
                        Stop one or more Virtual Machines
  --rebootvm VMNAME [VMNAME ...]
                        Reboot one or more Virtual Machines

```
