from datetime import datetime
import random

class Patient(object):
    """docstring for Patient."""
    uid = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.bed_number = None
        self.id = Patient.uid
        self.admitted = datetime.now().strftime('%A, %d. %B %Y %I:%M%p')
        self.discharged = None

        Patient.uid += 1


class Hospital(object):
    """docstring for Hospital."""
    def __init__(self):
        self.patient = []
        self.name = 'Memorial Hospital'
        self.capacity = 2
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(1, self.capacity):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patient) >= self.capacity:
            print 'Sorry but the Hospital is full'
        else:
            self.patient.append(patient)
            for i in range(0, len(self.beds)):
                patient.bed_number = self.beds[i]['bed_id']
                self.beds[i]['Available'] = False
                self.capacity -= 1
                break
            print 'The patient #{} has been successfully admitted to bed #{}'.format(patient.uid, patient.bed_number)
        return self

    def discharge(self, find_patient):
        for patient in self.patient:
            if patient.name == find_patient:
                for bed in self.beds:
                    if bed['bed_id'] == patient.bed_number:
                        bed['Available'] = True
                        print 'This is True'
                        break
                self.patient.remove(patient)
                patient.time = datetime.now().strftime('%A, %d. %B %Y %I:%M%p')
                print '{} has been successfully removed'.format(find_patient)
            else:
                print '{} was not in our record'.format(find_patient)
        return self

    def info(self):
        for patient in self.patient:
            print '''Name: {}
Hospital: {}
Alergies: {}
Admitted: {}
Discharge: {}
=============================================='''.format(patient.name, self.name, patient.allergies, patient.admitted, patient.discharged)
        return self

def handle_admission():
    print '''Would you like to admit a patient?
Type [1] for yes, [0] for no and [2] to discharge a patient'''
    ans = raw_input()
    return int(ans)

def admission():
    print "What is the patient's name?"
    name = raw_input()
    print 'What kind of allergies the patient have?'
    allergies = raw_input()
    return Patient(name, allergies)

def discharge_patient():
    print "What is the patient's name?"
    name = raw_input()
    return name

game_on = True
hospital = Hospital()
while game_on:
    new_patient = handle_admission()
    if new_patient == 1:
        hospital.admit(admission())
        print '''====================================

        '''
        print 'Patients Information:'
        hospital.info()
    elif new_patient == 2:
        hospital.discharge(discharge_patient())
    else:
        game_on = False
