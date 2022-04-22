#include<stdio.h>
typedef unsigned char * byte_pointer;
void show_bytes(byte_pointer start, size_t len) {
	size_t i;
	for (int i = 0; i < len; i++)
		printf("%.2x", start[i]);
	printf("\n");
}

int main() {
	long long a = 0xFFFFFFFF;
	printf("%lld\n", a);
	show_bytes((byte_pointer) &a, sizeof(a));
	 
	int b = 0xf1;
	printf("%d\n", b);
	show_bytes((byte_pointer) &b, sizeof(b));
	return 0;
}