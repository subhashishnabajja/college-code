#include <iostream>

//F093 / Subhashish Nabajja

using namespace std;

int main()
{
    int a = 5;

    cout << "Default value: "<< a << endl;

    a += 3;
    cout << "a += 3 = " << a << endl;

    a -= 3;
    cout << "a -= 3 = " << a << endl;

    a *= 3;
    cout << "a *= 3 = " << a << endl;

    a /= 3;
    cout << "a /= 3 = " << a << endl;

    a %= 3;
    cout << "a %= 3 = " << a << endl;

    a &= 3;
    cout << "a &= 3 = " << a << endl;

    a |= 3;
    cout << "a |= 3 = " << a << endl;

    a ^= 3;
    cout << "a ^= 3 = " << a << endl;

    a >>= 3;
    cout << "a >>= 3 = " << a << endl;

    a <<= 3;
    cout << "a <<= 3 = " << a << endl;

    return 0;
}
