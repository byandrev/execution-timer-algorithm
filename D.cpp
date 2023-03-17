#include <bits/stdc++.h>

using namespace std;

void solve() {
    int a, b; cin >> a >> b;

    for (int i = 0; i < a; i++) {
        for (int j = 0; j < b; j++) {
            int number; cin >> number;

            if (i % 2 == 0) number += 1;
            if (j % 2 == 0) number += 2;
            if (i % 2 != 0 && j % 2 != 0) number -= 3;

            if (j < b-1) cout << number << " ";
            else cout << number;
        }

        cout << "\n";
    }
}

int main() {
    solve();

    return 0;
}