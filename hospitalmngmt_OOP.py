from cryptography.fernet import Fernet


# Encryption Helper Class
class EncryptionHelper:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, data):
        return self.cipher.decrypt(data.encode()).decode()


# Base Person Class
class Person:
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}, Age: {self.age}, ID: {self.id_number}"


# Doctor Class (inherits from Person)
class Doctor(Person):
    def __init__(self, name, age, id_number, speciality):
        super().__init__(name, age, id_number)
        self.speciality = speciality

    def diagnose(self, patient_name):
        return f"Doctor {self.name} has diagnosed {patient_name}."


# Nurse Class (inherits from Person)
class Nurse(Person):
    def __init__(self, name, age, id_number, department):
        super().__init__(name, age, id_number)
        self.department = department

    def assist(self, doctor_name):
        return f"Nurse {self.name} is assisting Doctor {doctor_name}."


# Patient Class (inherits from Person)
class Patient(Person):
    def __init__(self, name, age, id_number, ailment):
        super().__init__(name, age, id_number)
        self.ailment = ailment

    def request_treatment(self):
        return f"Patient {self.name} is requesting treatment for {self.ailment}."


# Admission Class
class Admission:
    def __init__(self, patient, admission_date):
        self.patient = patient
        self.admission_date = admission_date

    def __str__(self):
        return (
            f"Admission Record: {self.patient.name} admitted on {self.admission_date}"
        )


# Treatment Class (with polymorphism)
class Treatment:
    def __init__(self, patient, doctor, treatment_details):
        self.patient = patient
        self.doctor = doctor
        self.treatment_details = treatment_details

    def execute_treatment(self):
        return f"Patient {self.patient.name} is receiving treatment from Doctor {self.doctor.name} for {self.treatment_details}"


# Billing Class
class Billing(EncryptionHelper):
    def __init__(self, patient, amount):
        super().__init__()
        self.patient = patient
        self.amount = amount
        self.encrypted_amount = self.encrypt(str(amount))

    def get_bill(self):
        return f"Bill for {self.patient.name}: {self.decrypt(self.encrypted_amount)} KES. (Encrypted: {self.encrypted_amount})"


# Demonstrating the System
if __name__ == "__main__":
    # Create instances
    dr_smith = Doctor("Smith", 45, "D001", "Cardiology")
    nurse_mary = Nurse("Mary", 30, "N101", "ICU")
    patient_john = Patient("John Doe", 60, "P5001", "Heart Disease")

    # Admission
    admission = Admission(patient_john, "2024-12-02")
    print(admission)

    # Treatment
    treatment = Treatment(patient_john, dr_smith, "Heart Surgery")

    # Billing
    bill = Billing(patient_john, 15000)
    print(bill.get_bill())

    # Demonstrating Nurse assisting Doctor
    print(nurse_mary.assist(dr_smith.name))

    # Demonstrating Patient requesting treatment
    print(patient_john.request_treatment())
