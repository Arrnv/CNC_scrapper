import pandas as pd
import numpy as np
import random
import math
df = pd.read_csv('suplyer.csv')
df = df.drop('Unnamed: 0', axis=1)



def estimate_cnc_part_cost_range(material, material_usage, part_size, complexity):

    material_costs = {
        'Aluminum': 2.5,
        'Steel': 3.0,
        'Plastic': 1.5,
        'MS/SS': 4.0,
        'Stainless Steel': 3.25,
        'Carbon Steel': 2.5,
        'Mild Steel': 1.75,
        'MS': 2.0,
        'Cast Iron': 2.25,
        'Alloy Steel': 3.0,
        'En - 36': 5.0,
    }

    machine_time_costs = {
        'Small': {'Simple': 10, 'Moderate': 15, 'Complex': 20},
        'Medium': {'Simple': 20, 'Moderate': 30, 'Complex': 40},
        'Large': {'Simple': 30, 'Moderate': 45, 'Complex': 60}
    }

    setup_costs = {
        'Simple': 50,
        'Moderate': 75,
        'Complex': 100
    }

    tool_costs_per_hour = {
        'Simple': (5, 10),  
        'Moderate': (10, 15),  
        'Complex': (15, 25)   
    }


    tool_usage_hours = {
        'Simple': (1, 5),  
        'Moderate': (5, 10),  
        'Complex': (10, 20)   
    }


    labor_cost_per_hour = 20

    overhead_cost_percentage = 0.1

    if material not in material_costs:
        raise ValueError("Invalid material type.")
    if part_size not in machine_time_costs:
        raise ValueError("Invalid part size.")
    if complexity not in machine_time_costs[part_size]:
        raise ValueError("Invalid complexity level.")


    material_cost = material_costs[material] * material_usage
    machine_time_cost = machine_time_costs[part_size][complexity]
    setup_cost = setup_costs[complexity]

    tool_cost_per_hour_min = tool_costs_per_hour[complexity][0]
    tool_usage_hours_min = tool_usage_hours[complexity][0]
    tool_cost_min = tool_usage_hours_min * tool_cost_per_hour_min

    tool_cost_per_hour_max = tool_costs_per_hour[complexity][1]
    tool_usage_hours_max = tool_usage_hours[complexity][1]
    tool_cost_max = tool_usage_hours_max * tool_cost_per_hour_max

    labor_cost = machine_time_cost

    overhead_cost_min = overhead_cost_percentage * (material_cost + machine_time_cost + setup_cost + tool_cost_min + labor_cost)
    overhead_cost_max = overhead_cost_percentage * (material_cost + machine_time_cost + setup_cost + tool_cost_max + labor_cost)

    total_cost_min = material_cost + machine_time_cost + setup_cost + tool_cost_min + labor_cost + overhead_cost_min
    total_cost_max = material_cost + machine_time_cost + setup_cost + tool_cost_max + labor_cost + overhead_cost_max

    
    return total_cost_min, total_cost_max

print("""
        Materials:
        'Aluminum', 
        'Steel', 
        'Plastic', 
        'MS/SS',
        'Stainless Steel',
        'Carbon Steel',
        'Mild Steel',
        'MS',
        'Cast Iron',
        'Alloy Steel',
        'En - 36'
        -----------
        size:
        'Small, Medium, Large'
        -----------
        complexity: 
        'Simple'
        'Moderate'
        'Complex'
        """)

material = input('\nEnter the Material: ')
material_usage = int(input("\nUnit Of material: ") )
part_size = input("\nSize of the part: ")
complexity = input("\nComplexity : ")

total_cost_min, total_cost_max = estimate_cnc_part_cost_range(material, material_usage, part_size, complexity)
print(f"\nEstimated total cost range: ${total_cost_min:.2f} - ${total_cost_max:.2f}")


def calculate_distance(base_location, supplier_location):
    return random.randint(10, 500)  # Assuming distance in kilometers

def match_suppliers(part_specifications, min_cost, max_cost, suppliers, base_location='Pune, Maharashtra'):
    material = part_specifications['Materials']
    size = part_specifications['size']
    complexity = part_specifications['complexity']
    matched = {}

    for index, row in suppliers.iterrows():
        if material == row['Materials'] and max_cost > row['price'] and min_cost < row['price']:
            supplier_location = row['Location']
            distance = calculate_distance(base_location, supplier_location)
            matched.update({row['Supplier_Name']: {'Location': supplier_location, 'Distance (km)': distance, 'Material': row['Materials'], 'price': row['price']}})
    return matched

part_specifications = {'Materials': 'Stainless Steel', 'size':'Small','complexity':'Moderate' }  # Example part specifications

matched_suppliers = match_suppliers(part_specifications, total_cost_min, total_cost_max, df)

print("\nMatching suppliers:")
for supplier_name, info in matched_suppliers.items():
    print(f"\nSupplier: {supplier_name}, Location: {info['Location']}, Material: {info['Material']}, Distance: {info['Distance (km)']} km")
