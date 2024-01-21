from prettytable import PrettyTable
table = PrettyTable()

# print(table)
#Add column to the table we specify

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)
print(table.align)
table.align = "r"
print(table.align)
print(table)

table.border = False
print(table.border)
print(table)
table.border = True

table.add_row(["Bulbasaur", "Grass"])
print(table)
# ["Butterfree", "Pidgey"], ["Bug", "Normal"], ["Golem", "Rock"], ["Snorlax", "Normal"] 
table.add_rows([ ["Butterfree", "Pidgey"], 
                ["Bug", "Normal"], 
                ["Golem", "Rock"], 
                ["Snorlax", "Normal"] 
            ])
print(table)

table.add_autoindex("Index No.")
print(table)

