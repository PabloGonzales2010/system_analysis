#include <iostream>
#include <vector>

using namespace std;

double task(vector<string> a, vector<string> b, vector<string> c) {
    vector<int> a1{ 0,1,2 };
    vector<int> b1(3, 0);
    vector<int> c1(3, 0);

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (b[j] == a[i]) {
                b1[j] = i;
                break;
            }
        }
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (c[j] == a[i]) {
                c1[j] = i;
                break;
            }
        }
    }
    for (int i = 0; i < 3; i++) {
        a1[i]++;
        b1[i]++;
        c1[i]++;
    }
    vector<int> x(3, 0);
    for (int i = 0; i < 3; i++) {
        x[i] += a1[i] + b1[i] + c1[i];
    }
    double m = (x[0] + x[1] + x[2]) / 3;
    for (int i = 0; i < 3; i++) {
        x[i] = (x[i] - m) * (x[i] - m);
    }
    double summ = 0;
    for (int i = 0; i < 3; i++) {
        summ += x[i];
    }
    double d = summ / (3 - 1);

    vector<int> x0(3, 0);
    for (int i = 0; i < 3; i++) {
        x0[i] = 3 * a1[i];
    }
    double m0 = (x0[0] + x0[1] + x0[2]) / 3;
    double summ0 = 0;
    for (int i = 0; i < 3; i++) {
        summ0 += x0[i];
    }
    double d0 = summ0 / (3 - 1);
    return d / d0;
}

int main(){   
}
