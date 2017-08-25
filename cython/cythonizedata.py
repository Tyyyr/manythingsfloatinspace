def convert_data(liste_teilchen):
    """
    Converts all variables stated in the global variable "acc_vars" of all
    objects into a list of lists. The order of the variables is alphabeticaly,
    given that, we know that:
    nth list:        variable of the nth object:
    data[n][0]     active[n]
    data[n][1]     force[n]
    data[n][2]     mass[n]
    data[n][3]     momentum[n]
    data[n][4]     radius[n]
    data[n][5]     velocity[n]
    data[n][6]     volume[n]
    data[n][7]     x[n]
    data[n][8]     y[n]
    """
    new_data = []
    for teilchen in liste_teilchen:
        part_data = []
        for attrname in dir(teilchen):
            if attrname in acc_vars:
                part_data.append(teilchen.__getattribute__(attrname))
        new_data.append(part_data)

    return new_data
