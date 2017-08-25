#include <math.h>

double euclid_dist(double[2] pos1, double[2] pos2){

    return sqrt((pos1[0] - pos2[0])^2 + (pos1[1] - pos2[1])^2)
}
