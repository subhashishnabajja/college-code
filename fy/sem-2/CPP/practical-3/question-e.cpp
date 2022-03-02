#include <iostream>

//F093 / Subhashish Nabajja

using namespace std;

int main()
{
    int a = 5, b = 6 ;

    cout << "The default values are " << a << "\t"<< b << endl;

    cout << "(a == b && a < b) = " << (a == b && a < b) << endl;
    cout << "(a == b || a < b) = " << (a == b || a < b) << endl;
    cout << "!(a == b) = " << !(a == b) << endl;
    return 0;
}
