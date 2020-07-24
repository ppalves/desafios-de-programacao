#include <stdio.h>
#include <math.h>
int main(){
	int a,b;
	scanf("%d %d",&a, &b);
	int i;
	double c = (double) a;
	double d = (double) b;
	for (i = 1; i < 9; i++){
		printf("%d ",((int)  ceil(((double) i) * 0.1 * c * d)));
	}
	printf("%d\n",((int)  ceil(((double) i) * 0.1 * c * d)));
	return 0;
}
