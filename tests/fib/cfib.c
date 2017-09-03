double cfib(int n){
    double a = 0;
    double b = 1;
    double tmp;
    int i;
    for(i = 0; i < n; i++){
        tmp = a;
        a = a + b;
        b = tmp;
    }
    return a;
}
