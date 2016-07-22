class patientRecord:
    # values shared amoung all instances of the class
    patientCount = 0;

    # constructor called to initialize new instance
    def __init__(self, name, healthCardNumber, age, gender):
        self.name = name
        self.healthCardNumber = healthCardNumber
        self.age = age
        self.gender = gender
        patientRecord.patientCount += 1

    # functions
    def displayPatientCount(self):
        print("The total number of patients is: ", patientRecord.patientCount)

    def displayPatient(self):
        print("")
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender:", self.gender)
        print("health card number: ", self.healthCardNumber)
        print("")

# creating objects
patient1 = patientRecord("Arrchana", 12345678, 19, "M")
patient2 = patientRecord("Bhavya", 87654321, 19, "F")

patient1.displayPatient()
patient2.displayPatient()
print("The total number of patients is: ", patientRecord.patientCount)

# modifying attributes of objects
patient2.age = 18

# special functions
hasattr(patient1, "name") # returns true if name exists
getattr(patient1, "name") # returns names
setattr(patient1, "gender", "F") # sets gender to F
# delattr(patient1, "healthCardNumber") # deletes healthCardNumber
