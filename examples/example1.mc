n = 10;
a = 0;
b = 1;

while (n > 0) {
    print(a);
    temp = a + b;
    a = b;
    b = temp;
    n = n - 1;
}
