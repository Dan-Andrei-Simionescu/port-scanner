import argparse

parser = argparse.ArgumentParser(description="DasDuke Port Scanner")
parser.add_argument("-t", "--target", dest="target", required=True, help="Target IP address")
parser.add_argument("-p", "--port", dest="ports", default="1-1024", help="Port range to scan")
parser.add_argument("-o", "--output", dest="output", default=None, help="Save results to a file")
parser.add_argument("-T", "--timeout", dest="timeout", default=0.5, type=float, help="Set TIMEOUT for current scan")
parser.add_argument("-w", "--workers", dest="workers", default=100, type=int, help="Tune performance based on your machine/network power - Set numbers of port to be scanned simultaneously")
parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="Show closed ports too")

args = parser.parse_args()

parts = args.ports.split("-")
start_port = int(parts[0])
end_port = int(parts[1])

