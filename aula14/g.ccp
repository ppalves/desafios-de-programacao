#include <iostream>
#include <cmath>

using namespace std;

void SieveOfEratosthenes(int n) 
{ 
    // Create a boolean array "prime[0..n]" and initialize 
    // all entries it as true. A value in prime[i] will 
    // finally be false if i is Not a prime, else true. 
	bool prime[n+1]; 
	memset(prime, true, sizeof(prime)); 
  
    for (int p=2; p*p<=n; p++) 
    { 
        // If prime[p] is not changed, then it is a prime 
        if (prime[p] == true) 
        { 
            // Update all multiples of p greater than or  
            // equal to the square of it 
            // numbers which are multiple of p and are 
            // less than p^2 are already been marked.  
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
  
    // Print all prime numbers 
    for (int p=2; p<=n; p++) 
       if (prime[p]) 
          cout << p << " "; 
} 

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
	long long root_maior = sqrt(sqrt(maior));
	root_maior += 10;
	int sieve[root_maior];
	for (i = 0; i< root_maior; i++){
		sieve[i] = 0;
	}
	for (i = 2;  i*i < root_maior;i++){
		if (sieve[i] == 0){
			int p;
			for (p = i*i; p < root_maior; p+=i){
				sieve[p] = 1;	
			}
		}
	}
	for (i = 0; i < T; i++){
		long long tmp;
		tmp = sqrt(values[i]);	
		if (tmp*tmp != values[i]){
			cout<<"NO"<<endl;	
		}else{
			bool is_prime = true;
			for (int k = 2; k < tmp; k++){
				if (sieve[k] == 0 && tmp%k == 0){
					cout<<"penis";
					cout<<"NO"<<endl;
					is_prime = false;
					break;
				}
			}
			if (is_prime){
				cout<<"YES"<<endl;
			}

		}
		

	} 

	return 0;
}
