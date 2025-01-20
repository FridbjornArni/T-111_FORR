# Friðbjörn 
# problem E
# Secture Doors

def main():
	log_length = int(input())  # Read the number of log entries
	access_log = {}

	for _ in range(log_length):
		action, name = input().split()  # Split the action and name
		
		if action == 'entry':
			if access_log.get(name, False):  # Check if the person is already inside
				print(f"{name} entered (ANOMALY)")
			else:
				print(f"{name} entered")
			access_log[name] = True  # Mark the person as inside
		
		elif action == 'exit':
			if not access_log.get(name, False):  # Check if the person is already outside
				print(f"{name} exited (ANOMALY)")
			else:
				print(f"{name} exited")
			access_log[name] = False  # Mark the person as outside

main()