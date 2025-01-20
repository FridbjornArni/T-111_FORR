# class Skil4:
#   def __init__(self):
#     self.constituencies = {}
#     self.parties = {}
#     self.election_results = {}
#     self.total_electorates = 0
#     self.constituencies_loaded = False
#     self.parties_loaded = False
#     self.results_loaded = False

#   def load_constituencies(self, filename):
#     if not self.constituencies_loaded:
#       try:
#         with open(filename, 'r') as file:
#           for line in file:
#             constituency_name, electorate_count = line.strip().split(';')
#             self.constituencies[constituency_name] = int(electorate_count)
#             self.total_electorates += int(electorate_count)
#         self.constituencies_loaded = True
#         print("Constituencies data loaded.")
#       except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#     self.display_constituencies()

#   def display_constituencies(self):
#     print(f"{'Constituency':<20} {'Electorates':<10}")
#     print("-" * 30)
#     for constituency_name, electorate_count in self.constituencies.items():
#       print(f"{constituency_name:<20} {electorate_count:<10}")
#     print("-" * 30)
#     print(f"Total: {self.total_electorates}")

#   def load_parties(self, filename):
#     if not self.parties_loaded:
#       try:
#         with open(filename, 'r') as file:
#           for line in file:
#             party_initial, party_name = line.strip().split(';')
#             self.parties[party_initial] = party_name
#         self.parties_loaded = True
#         print("Parties data loaded.")
#       except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")
#     self.display_parties()

#   def display_parties(self):
#     print(f"{'Initial':<6} {'Party':<26}")
#     print("-" * 32)
#     for party_initial, party_name in self.parties.items():
#       print(f"{party_initial:<6} {party_name:<26}")
#     print("-" * 32)

#   def load_election_results(self, filename):
#     if not self.results_loaded:
#       try:
#         with open(filename, 'r') as file:
#           current_constituency = None
#           for line in file:
#             if not ';' in line:
#               current_constituency = line.strip()
#               self.election_results[current_constituency] = []
#             else:
#               party_initial, votes = line.strip().split(';')
#               self.election_results[current_constituency].append((party_initial, int(votes)))
#         self.results_loaded = True
#         print("Election results loaded.")
#       except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")

#   def display_results_for_constituency(self, constituency_name):
#     if constituency_name not in self.election_results:
#       print(f"Error: Constituency '{constituency_name}' not found.")
#       return

#     total_votes = sum(votes for _, votes in self.election_results[constituency_name])
#     electorate_count = self.constituencies.get(constituency_name, 0)
#     print(f"{constituency_name}")
#     print(f"{'Initial':<10} {'Party':<26} {'Votes':<10} {'Percentage':<10}")
#     print("-" * 58)
#     for party_initial, votes in self.election_results[constituency_name]:
#       party_name = self.parties.get(party_initial, "Unknown")
#       percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
#       print(f"{party_initial:<10} {party_name:<26} {votes:<10} {percentage:<10.1f}")
#     print("-" * 58)
#     print(f"Total votes: {total_votes:<10} 100.0")
#     turnout = (total_votes / electorate_count) * 100 if electorate_count > 0 else 0
#     print(f"Turnout: {turnout:.1f}%")

#   def display_menu(self):
#     while True:
#       print("\n1. Show constituencies")
#       print("2. Show parties")
#       print("3. Show election results")
#       print("9. Quit")
#       action = input("Select an action: ")

#       if action == "1":
#         if self.constituencies_loaded == False:
#           filename = input("File name: ")
#           self.load_constituencies(filename)
#       elif action == "2":
#         if self.parties_loaded == False:
#           filename = input("File name: ")
#           self.load_parties(filename)
#       elif action == "3":
#         if self.results_loaded == False:
#           filename = input("File name: ")
#           self.load_election_results(filename)
#         constituency_name = input("Enter constituency name: ")
#         self.display_results_for_constituency(constituency_name)
#       elif action == "9":
#         print("Exiting program.")
#         break
#       else:
#         print("Invalid selection. Please try again.")


# # Example of using the Skil4 class
# if __name__ == "__main__":
#   election_data = Skil4()
#   election_data.display_menu()


class Skil4:
  def __init__(self):
    self.constituencies = {}
    self.parties = {}
    self.election_results = {}
    self.total_electorates = 0
    self.constituencies_loaded = False
    self.parties_loaded = False
    self.results_loaded = False

  def load_constituencies(self, filename):
    if not self.constituencies_loaded:
      try:
        with open(filename, 'r') as file:
          for line in file:
            # Remove any leading/trailing whitespace and split the line
            constituency_name, electorate_count = line.strip().split(';')
            constituency_name = constituency_name.strip()  # Trim any extra spaces
            self.constituencies[constituity_name] = int(electorate_count)
            self.total_electorates += int(electorate_count)
        self.constituencies_loaded = True
        print("Constituencies data loaded.")
      except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    self.display_constituencies()

  def display_constituencies(self):
    print(f"{'Constituency':<20} {'Electorates':<10}")
    print("-" * 30)
    for constituency_name, electorate_count in self.constituencies.items():
      print(f"{constituency_name:<20} {electorate_count:<10}")
    print("-" * 30)
    print(f"Total: {self.total_electorates}")

  def load_parties(self, filename):
    if not self.parties_loaded:
      try:
        with open(filename, 'r') as file:
          for line in file:
            # Remove whitespace and split line into party initials and name
            party_initial, party_name = line.strip().split(';')
            self.parties[party_initial.strip()] = party_name.strip()
        self.parties_loaded = True
        print("Parties data loaded.")
      except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    self.display_parties()

  def display_parties(self):
    print(f"{'Initial':<6} {'Party':<26}")
    print("-" * 32)
    for party_initial, party_name in self.parties.items():
      print(f"{party_initial:<6} {party_name:<26}")
    print("-" * 32)

  def load_election_results(self, filename):
    if not self.results_loaded:
      try:
        with open(filename, 'r') as file:
          current_constituency = None
          for line in file:
            # Check if it's a new constituency line (no semicolon)
            if ';' not in line:
              current_constituency = line.strip()
              self.election_results[current_constituency] = []
            else:
              # Parse votes for each party
              party_initial, votes = line.strip().split(';')
              self.election_results[current_constituency].append((party_initial.strip(), int(votes)))
        self.results_loaded = True
        print("Election results loaded.")
      except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

  def display_results_for_constituency(self, constituency_name):
    constituency_name = constituency_name.strip()  # Ensure no leading/trailing spaces
    if constituency_name not in self.election_results:
      print(f"Error: Constituency '{constituency_name}' not found.")
      return

    total_votes = sum(votes for _, votes in self.election_results[constituency_name])
    electorate_count = self.constituencies.get(constituency_name, 0)
    print(f"{constituency_name}")
    print(f"{'Initial':<10} {'Party':<26} {'Votes':<10} {'Percentage':<10}")
    print("-" * 58)
    for party_initial, votes in self.election_results[constituency_name]:
      party_name = self.parties.get(party_initial, "Unknown")
      percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
      print(f"{party_initial:<10} {party_name:<26} {votes:<10} {percentage:<10.1f}")
    print("-" * 58)
    print(f"Total votes: {total_votes:<10} 100.0")
    turnout = (total_votes / electorate_count) * 100 if electorate_count > 0 else 0
    print(f"Turnout: {turnout:.1f}%")

  def display_menu(self):
    while True:
      print("\n1. Show constituencies")
      print("2. Show parties")
      print("3. Show election results")
      print("9. Quit")
      action = input("Select an action: ")

      if action == "1":
        filename = input("File name: ")
        self.load_constituencies(filename)
      elif action == "2":
        filename = input("File name: ")
        self.load_parties(filename)
      elif action == "3":
        filename = input("File name: ")
        self.load_election_results(filename)
        constituency_name = input("Enter constituency name: ")
        self.display_results_for_constituity(constituency_name)
      elif action == "9":
        print("Exiting program.")
        break
      else:
        print("Invalid selection. Please try again.")


# Example of using the Skil4 class
if __name__ == "__main__":
  election_data = Skil4()
  election_data.display_menu()
