0x08. Networking basics #1

What is localhost. 

Localhost is a hostname that refers to the current computer used used to access it. The name localhost is reserverd for loopback purposes. Its used to access network services that are running on the host via the loopback network interface. 

What is 0.0.0.0

IANA(Internet Assigned Numbers Authority) who allocates IP addresses globally have allocated the single  IP 0.0.0.0 to RFC 1122 section 3.2.1.3. Its named as This host on this network.

RFC 1122 refers to 0.0.0.0 using the notation {0,0}. It prohibits this as a destination address in IPV4 and only allows it as sourse address under specific circumtances. 

How to Modify and Manage the Hosts File on Linux

There is a single file on your computer that serves as a small gateway between you and  the web. Its called the hosts file. If you need to block websites or use personalised web shortcuts on Linux, you can adjust or tweak a few lines in the file. 


What is the Linux Hosts File?

The hosts file is a plain text file that all operating systems use to translate hostnames into IP addresses. When you type the hostname, the system will into the hosts file to get the IP addresses needed to connect tp connect to the appropriate server. 

Turns out that the system will look for hostfile first before looking up a site on the DNS.

This means that you can use he hosts file to on what the DNS server can't provide(such as aliases for locations on your local network)

The Linux Hosts Files Location

On linux to can find the hosts file under /etc/hosts


Practical Linux Netcat NC Command Examples

Netcat or nc is a networking utility for debugging and investigating network. This utility can be used for creating TCP/UDP connections and investigating them. The biggest use of this utility is in the scripts where we need to deal with TCP/UDP sockets. 

Netcat in a Server-Client Architecture

The netcat utility can be run in the server mode on a specified port for listening for incoming connections.
$ nc -l 2389
