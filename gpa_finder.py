from __future__ import print_function
# Let's define some grade things.
cp_gpa = []
h_gpa = []
ap_gpa = []
average = 40
for whattonamethis in range(0, 41):
    cp_gpa.append(whattonamethis * .1)
    h_gpa.append(whattonamethis * .1 + .5)
    ap_gpa.append(whattonamethis * .1 + 1)

# Not every student takes the same amount of classes.
number_of_classes = int(input('How many classes were you enrolled in this year? '))
cp_classes = int(input('And how many of those classes were weighted CP (standard)? '))
h_classes = int(input('And how many of those classes were weighted Honors? '))
# To confirm.  That way, the user can just cancel.
print('So that means you were enrolled in', (number_of_classes - cp_classes) - h_classes, 'AP classes.')
correct = raw_input('Is that correct (y/n)? ')
correct.upper()
correct.lower()

if correct.lower() == 'y':
    print('I\'m going to have to ask you some questions now. Unfortunately, I would make this',
       'sound a little smarter, but Python\'s way of getting input from you from the console is a little annoying. Bear with me though.')

    gpas = []
    for cp_class_grade in range(0, cp_classes):
        num_grade = int(input('What was your grade for one of your CP classes? '))
        gpa = cp_gpa[num_grade - 59]
        print(gpa)
        gpas.append(gpa)

    for h_class_grade in range(0, h_classes):
        num_grade = int(input('What was your grade for one of your Honors classes? '))
        gpa = h_gpa[num_grade - 59]
        gpas.append(gpa)
        print(gpa)

    for ap_class_grade in range(0, (number_of_classes - cp_classes) - h_classes):
        num_grade = int(input('What was your grade for one of your AP classes? '))
        gpa = ap_gpa[num_grade - 59]
        gpas.append(gpa)
        print(gpa)

        total_gpa = 0.0    
    def get_average_gpa(gpalist):
        gpasum = 0
        for gpa in gpalist:
            gpasum += gpa
        return gpasum / len(gpalist)
    avg_gpa = get_average_gpa(gpas)
    print('Your average weighted South Carolina GPA is ', avg_gpa, '!', sep='')
else:
    print('Well, you screwed up, not me.')