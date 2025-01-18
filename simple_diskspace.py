import ansible_runner

# Define the path to your playbook and inventory
playbook_path = 'diskspace.playbook'
inventory_file = 'inventory.ini'  # Use a comma to indicate localhost

# Run the playbook using ansible_runner
runner = ansible_runner.run(
    private_data_dir='.',  # Specify the directory containing the playbook
    playbook=playbook_path,
    inventory=inventory_file
)

# Print the results
print("\n")
print("\n")
print(f"Status: {runner.status}")
print(f"Return Code: {runner.rc}")
print(f"Output: {runner.stdout.read()}")
