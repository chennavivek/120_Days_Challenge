# create a vehicle class and perform method overloading

class vehicle:
    def start_engine(self, fuel_type=None): # Method overloading with default parameter
        """Start the engine with a specific fuel type."""
        if fuel_type is None: # Default case when no fuel type is provided
            return "Engine started with default fuel"
        elif fuel_type == "electric": # Electric fuel type
            return "Engine started with electric power"
        elif fuel_type == "diesel": # Diesel fuel type
            return "Engine started with diesel fuel"
        else: # Any other fuel type
            return "Unknown fuel type"

# create an object
v = vehicle()
# call the method with different fuel types
print(v.start_engine()) # No fuel type provided
print(v.start_engine("electric")) # Electric fuel type
print(v.start_engine("diesel")) # Diesel fuel type
print(v.start_engine("gasoline")) # Unknown fuel type
        
