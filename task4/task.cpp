#include <iostream>
#include <vector>
#include<algorithm>
using namespace std;

vector<double> task() {
    vector<double> ret;
    
    return ret;
}

int main()
{
    vector<int> v;
    for (int i = 1; i <= 6; i++) {
        for (int j = 1; j <= 6; j++) {
            v.push_back(i * j);
        }
    }
    sort(v.begin(), v.end());
    for (int i = 0; i < v.size() - 1; i++) {
        if (v[i] == v[i + 1]) {
            v.erase(v.begin() + i);
            i--;
        }
    }

    vector<int> vv;
    for (int i = 1; i <= 6; i++) {
        for (int j = 1; j <= 6; j++) {
            vv.push_back(i + j);
        }
    }
    sort(vv.begin(), vv.end());
    for (int i = 0; i < vv.size() - 1; i++) {
        if (vv[i] == vv[i + 1]) {
            vv.erase(vv.begin() + i);
            i--;
        }
    }

    vector<vector<double>> m;
    for (int i = 0; i < vv.size(); i++) {
        vector<double> t(v.size(), 0);
        m.push_back(t);
    }

    vector<int> index(v[v.size() - 1] + 1, 0);
    int t = 0;
    for (int i = 0; i < v.size(); i++) {
        index[v[i]] = t;
        t++;
    }

    vector<int> indexv(vv[vv.size() - 1] + 1, 0);
    t = 0;
    for (int i = 0; i < vv.size(); i++) {
        indexv[vv[i]] = t;
        t++;
    }

    for (int i = 1; i <= 6; i++) {
        for (int j = 1; j <= 6; j++) {
            if (i == j) {
                m[indexv[i + j]][index[i * j]] = 1;
            }
            else {
                m[indexv[i + j]][index[i * j]] = 2;
            }
        }
    }

    for (int i = 0; i < m.size(); i++) {
        for (int j = 0; j < m[i].size(); j++) {
            m[i][j] /= 36;
        }
    }



    //for (int i = 0; i < indexv.size(); i++) cout << indexv[i] << " ";
    for (int i = 0; i < m.size(); i++) {for (int j = 0; j < m[i].size(); j++) cout << m[i][j] << " "; cout << "\n";}

}
