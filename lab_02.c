#include <stdio.h>
#include <stdlib.h>
long main(void)
{
	int max, n, amount, tmp, range, count;
	float x, maxnum, maxi, border, maximal, minimal_1, minimal_2;
	double sum, mult;
	#define size 100
		//Вариант №7

		//Задание №1

	float a[size];
	printf("input range of array: \n");
	scanf_s("%d", &n);
	sum = 0;
	mult = 1;
	if ((n <= 0) || (n > size))
	{
		printf("array out of range!\n");
		return 0;
	}
	for (int i = 0; i < n; i++)
	{
		x = -25 + rand() % 100;
		a[i] = x;
	}
	maxnum = a[0];
	for (int i = 0; i < n; i++)
	{
		if (a[i] >= maxnum)
		{
			maxnum = a[i];
			max = i;
		}		
	}
	printf("number of max num %d\n", max);
	printf("max num %f\n", maxnum);
	count = 0;
	for (int i = max; i < n; i++)
	{
		if (a[i] >= 0)
		{
			sum +=  a[i];
		}
		else
		{
			mult = mult * a[i];
			count += 1;
		}
	}
	if (count == 0)
	{
		printf("Negitive numbers is not find");
		mult = 0;
	}
	printf("sum = %f\n", sum);
	printf("multiply = %f\n", mult);
	
		//задание №2

	/*float b[] = { 11, 17, 3, 22, 6, 5, 19, 4, 8, 10, 15, 13, 20, 18, 7, 12, 14, 16, 1, 9, 21 };
	maxi = b[0];
	for (int i = 0; i < 22; i++)
	{
		if (b[i] > maxi)
		{
			maxi = b[i];
			max = i;
		}
	}
	for (int i = 2; i < max; i = i + 2)
		{
		b[i] = b[i] * maxi;
		printf("%f\n", b[i]);
		}*/

		// Задание №3

	int c[size];
	printf("input range of array: \n");
	scanf_s("%d", &amount);
	if ((amount <= 0) || (amount > size))
	{
		printf("array out of range!\n");
		return 0;
	}
	printf("input values of array\n");
	for (int i = 0; i < amount; i++)
	{
		scanf_s("%d", &c[i]);
	}
	for (int i = 0; i < amount - 1; i++)
	{
		if (c[i] % 2 != 0 && c[i + 1] % 2 == 0)
		{
			for (int j = 0; j < amount - 1; j++)
			{
				{
					tmp = c[i];
					c[i + 2] = tmp;
				}
			}
		}
	}
	for (int i = 0; i <= amount; i++)
	{
		if ((i == amount) & (c[amount] == -858993460))
		{
			break;
		}
		printf("%d ", c[i]);
	}

		// Задание №4

	/*int range_matrix = 4;

	float matrix[4][4] = {
		{2, 1, -4, 3},
		{5, 16, 7, 8},
		{9, 1, 20, 4},
		{6, 5, -6.3, 0}
	};
	border = 0;
	minimal_1 = matrix[0][0];
	minimal_2 = matrix[0][range_matrix - 1];
	border = (range_matrix % 2) ? (range_matrix / 2) + 1 : (range_matrix / 2);
	maximal = matrix[0][range_matrix - 1];
	for (int i = 0; i < border; i++)
	{
		for (int j = 0; j + i < range_matrix - 2; j++)
		{
			if (minimal_1 > matrix[i][j])
			{
				minimal_1 = matrix[i][j];
			}
		}
	}
	for (int i = border; i < range_matrix; i++)
	{
		for (int j = range_matrix - 1; j + i > range_matrix; j--)
		{
			if (minimal_2 > matrix[i][j])
			{
				minimal_2 = matrix[i][j];
			}
		}
	}
	for (int i = 0; i < range_matrix; i++)
	{
		for (int j = 0; j < range_matrix; j++)
		{
			if (maximal < matrix[i][j] && j + i < range_matrix + 1 && j + i >= range_matrix - 2)
			{
				maximal = matrix[i][j];
			}
		}
	}
	if (minimal_1 < minimal_2)
		{
		printf("Minimal: %f\n", minimal_1);
		}
	else
		{
		printf("Minimal: %f\n", minimal_2);
		}
	printf("Maximal: %f\n", maximal);
	
	/* float matrix[size][size];
	printf("Input range of matrix: \n");
	scanf_s("%d", &range);
	if ((range <= 0) || (range > size))
	{
		printf("Array out of range!\n");
		return 0;
	}
	printf("Input values of array\n");
	for (int i = 0; i < range; i++)
	{
		for (int j = 0; j < range; j++)
		{
			scanf_s("%f", &matrix[i][j]);
		}
	}
	for (int i = 0; i < range; i++)
	{
		for (int j = 0; j < range; j++)
		{
			print("%f", matrix[range - i][range - j]);
		}
	}*/
}