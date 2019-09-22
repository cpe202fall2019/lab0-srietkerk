# Student: Sarah Rietkerk
# Instructor: Paul Hatalsky
# Class: CPE 202
# Term: Fall 2019


def weight_on_planets():
    #get someone's weight and make it into a float for multiplication
    earth_weight = float(input("What do you weigh on earth? "))
    #calculate weight on mars by multiplying Earth weight by 0.38
    mars = earth_weight * 0.38
    #calculate weight on jupiter by multiplying Earth weight by 2.34
    jupiter = earth_weight * 2.34
    #display the results and place the float value of both weights at the 
    # location of the curly brackets, limited to 2 decimal places
    print("\nOn Mars you would weigh {:.2f} pounds.".format(mars) +
        "\nOn Jupiter you would weigh {:.2f} pounds.".format(jupiter))
   
   
if __name__ == '__main__':
    weight_on_planets()
