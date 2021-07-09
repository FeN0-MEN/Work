#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <>
int main(void)
{
long float x, y, z, a, b, fact, power;
int count, num, det, n, k; 
double product, dec, denom, numer;
float sum;

printf("Enter the variables:\n");
scanf_s("%lf", &x);
scanf_s("%lf", &y);
scanf_s("%lf", &z);


//Вариант №7

//Задание №1
if (1 + ((x*x) / 2) + ((y*y) / 4) == 0)
	{
	printf("The denominator is 0, and you can't divide by 0\n");
	}
if ((z + exp(-(x + 3)) < -1) || (z + exp(-(x + 3)) > 1))
	{
	printf("arcsin cannot contain an expression greater than 1 or less than -1\n");
	}
a = (sqrt(abs(x - 1)) - pow(abs(y), 1.0 / 3)) / (1 + ((x*x) / 2) + ((y*y) / 4));
b = x * (asin(z + exp(-(x + 3))));
printf("%f\n", a);
printf("%f\n", b);

//Задание №2
if (x < -2 || x > 2) 
	{ 
	y = (x*x); 
	}
else 
	{ 
	y = 4;
	}
printf("%lf\n", y);

//Задание №3
printf("Enter number\n");
scanf_s("%d", &num);
printf("Enter the value of the number 'k'\n");
scanf_s("%d", &k);
det = k + 1;
count = 0; 
if (det % 2 == 0)
	{
	det += 1;
	}
while (num >= det)
	{
	if (num % det == 0)
		{
		count += 1;
		}
	det += 2;
	if (num < det) { break; }
	}
printf("Number of odd divisors: %d\n", count);

//Задание №4
printf("Enter count numbers: ");
scanf_s("%d", &n);
count = 0;
for (int i = 1; i <= n; i++)
	{
	k = rand();
	if (k % 2 != 0)
		{
		count++;
		}
	}
printf("%d\n", count);

//Задание №5
sum = 0;
printf("Enter the number A: ");
scanf_s("%lf", &power);
printf("Enter count numbers: ");
scanf_s("%d", &n);
for (int i = 0; i <= n; i++)
	{
	sum += (1. / (pow(power, pow(2,i))));
	}
printf("%f\n", sum);

//Задание №6
printf("Enter the number of iterations and number X: ");
scanf_s("%d", &n);
scanf_s("%lf", &x);
fact = 1;
dec = 1;
for (int i = 1; i <= n; i++)
	{
	if (i == 1 || i == 2) 
		{ fact = 1; 
		}
	else 
		{ 
		fact = fact * (fact + 1); 
		}
	denom = pow((fact + 1), 2);
	numer = pow((1 - x), (k + 1)) + 1;
	product = numer / denom;
	dec = dec * product;
	}
printf("%f", dec);

_getch();

}