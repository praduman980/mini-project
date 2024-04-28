class VotingSystem:
    def __init__(self):
        self.candidates = {}

    def menu(self):
        while True:
            print("\nVoting System Menu:")
            print("1. Add Candidate")
            print("2. Vote")
            print("3. Display Results")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter candidate name: ")
                if name not in self.candidates:
                    self.candidates[name] = 0
                    print(f"{name} added successfully.")
                else:
                    print(f"{name} is already a candidate.")
            elif choice == '2':
                name = input("Enter candidate name you want to vote for: ")
                if name in self.candidates:
                    self.candidates[name] += 1
                    print(f"Vote for {name} recorded successfully.")
                else:
                    print(f"{name} is not a valid candidate.")
            elif choice == '3':
                print("\nVoting Results:")
                for candidate, votes in self.candidates.items():
                    print(f"{candidate}: {votes} votes")
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    voting_system = VotingSystem()
    voting_system.menu()
