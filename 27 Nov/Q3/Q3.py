class Garage:
    def __init__(self, bikes, cars, trucks):
        self.bikes = bikes
        self.cars = cars
        self.trucks = trucks
        

def MaxRevenue(garages, m):
    if garages is None:
        return -1
        
    max_revenue = 0
    
    for garage in garages:
        revenue = (100 * garage.bikes) + (250 * garage.cars) + (500 * garage.trucks)
        max_revenue = max(max_revenue, revenue)
        
    return max_revenue
    
m = int(input())
garages = []
for _ in range(m):
    bikes, cars, trucks = map(int, input().split())
    garages.append(Garage(bikes, cars, trucks))
    
output = MaxRevenue(garages, m)

print(output)