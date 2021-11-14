#include <iostream>
using namespace std;

void solve(){
  int A, B, C;
  cin >> A >> B >> C;
  if( ((A == 5) && (B == 5) && (C == 7)) ||
      ((A == 5) && (B == 7) && (C == 5)) ||
      ((A == 7) && (B == 5) && (C == 5)) )
  { cout << "YES" << endl; return; } 

  cout << "NO" << endl; return;

}

int main(){ 
  solve();
  return 0;
}