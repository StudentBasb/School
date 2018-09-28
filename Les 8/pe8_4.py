studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
   student0 = sum(studentencijfers[0])/3
   student1 = sum(studentencijfers[1])/3
   student2 = sum(studentencijfers[2])/3
   student3 = sum(studentencijfers[3])/3
   antw = 'De gemiddelde cijfers zijn respectivelijk {}, {}, {} en {}'.format(student0, student1, student2, student3)
   return antw

def gemiddelde_van_alle_studenten(studentencijfers):
   student0 = sum(studentencijfers[0])
   student1 = sum(studentencijfers[1])
   student2 = sum(studentencijfers[2])
   student3 = sum(studentencijfers[3])
   gemiddelde = (student0+student1+student2+student3)/12
   antw ='Het gemiddelde van alle studenten is {}'.format(gemiddelde)
   return antw

print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
