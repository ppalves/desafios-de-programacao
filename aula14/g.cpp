#include <iostream>
#include <cmath>
#include <cstring>

using namespace std;


int main(){
	int T;
	cin >> T;


	int i;
	double current, root;

	long long values[T];
	long long maior = 0;
	for (i = 0; i < T; i++){
		cin>>values[i];
		if (values[i] > maior) maior = values[i];
			
	}
	long long root_maior = sqrt(maior);
	root_maior += 10;
	bool prime[root_maior+1];
	memset(prime, true, sizeof(prime)); 
  
	for (int p=2; p*p<=root_maior; p++) 
	{ 
		// If prime[p] is not changed, then it is a prime 
		if (prime[p] == true) 
		{ 
		    // Update all multiples of p greater than or  
		    // equal to the square of it 
		    // numbers which are multiple of p and are 
		    // less than p^2 are already been marked.  
		    for (int i=p*p; i<=root_maior; i += p) 
			prime[i] = false; 
		} 
	} 
	for (i = 0; i < T; i++){
		long long tmp;
		tmp = sqrt(values[i]);	
		if (tmp*tmp != values[i] || values[i] == 1 || values[i] == 0){
			cout<<"NO"<<endl;	
		}else{
			if (prime[tmp]){
				cout<<"YES"<<endl;
			}else{
				cout<<"NO"<<endl;
			
			}

		}
		

	} 

	return 0;
}
