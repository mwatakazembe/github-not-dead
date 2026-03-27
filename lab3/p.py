#растение: название, светолюбивое/тенелюбивое, любит/не любит влагу. наследники: комнатное, клумбовое, для огорода. 
#переопределение, свои исключнеия, пользовательский ввод: добавить, удалить растение, магич методы кроме инит

class PlantException(Exception):
    pass

class WrongPlantTypeInputError(PlantException):
    pass

class PlantNotFound(PlantException):
    pass

plants = {}
class Plant:
    plant_counter = 1
    
    def __init__(self):
        self.plant_id = Plant.plant_counter
        Plant.plant_counter += 1

    def __str__(self):
        plant_str = ""
        for t in plants:
            plant_str += f"{t}: {plants[t]}\n"
        return plant_str
        
    def create_plant(self):
        print("create your plant.")
        name = input("input plants' name: ")
        while True:
            light_input = input("\ntype by light love:\n 1. light-loving\n 2. shadow-loving\n")
            try: 
                if light_input== "1":
                    light_type = "light-loving"
                    break
                    
                elif light_input == "2":
                    light_type = "shadow-loving"
                    break
                else: raise WrongPlantTypeInputError("wrong type try again")
            except WrongPlantTypeInputError as e:
                print(f"error: {e}")

        while True:
            water_input = input("\ntype by humidity love:\n 1. humidity-loving\n 2. dry-loving\n")
            try: 
                if water_input== "1":
                    water_type = "humidity-loving"
                    break
                elif water_input == "2":
                    water_type = "dry-loving"
                    break
                else: raise WrongPlantTypeInputError("wrong type try again")
            except WrongPlantTypeInputError as e:
                print(f"error: {e}")
    
        data = {self.plant_id: {"name": name, "light loving type": light_type, "water loving type": water_type}}
        plants.update(data)
        
            
class Room(Plant):
    def create_plant(self):
        super(Room, self).create_plant()
        print(f"plant created. plant id: {self.plant_id}")

class Street(Plant):
    def create_plant(self):
        super(Street, self).create_plant()
        print(f"plant created. plant id: {self.plant_id}")

class Garden(Plant):
    def create_plant(self):
        super(Garden, self).create_plant()
        print(f"plant created. plant id: {self.plant_id}")

        
while True:
    choice = input("\nmenu:\n 1. create plant\n 2. delete plant\n 3. show plants\n")
    if choice == "1":
        pl = input("choose your plant:\n 1. room\n 2. street\n 3. garden\n")
        if pl == "1":
            room_plant = Room()
            room_plant.create_plant()
        elif pl == "2":
            street_plant = Street()
            street_plant.create_plant()
        elif pl == "3": 
            garden_plant = Garden()
            garden_plant.create_plant()
    

    elif choice == "2":
        try:
            del_id = int(input("what plant do you want to delete?\n"))
            if del_id not in plants.keys():
                raise PlantNotFound("plant not found")
            del(plants[del_id])
               
        except PlantNotFound as e: 
            print(f"error: {e}")
        

    elif choice == "3":
        print(str(room_plant))