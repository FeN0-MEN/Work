#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
	FILE* input, * output;
	// создание динамических массивов
	int size = 5;
	char* text_stack = (char*)malloc(size * sizeof(char));
	char* array = (char*)malloc(size * sizeof(char));
	// копия изначального состояния массива-стека (для дальнейшего сравнения)
	char* start_stack = (char*)malloc(size * sizeof(char));
	start_stack[0] = '\0';
	strcpy(start_stack, array);

	input = fopen("input.txt", "r");
	// если файл пустой - выдать ошибку
	if (input == NULL)
	{
		printf("Error");
	}
	// занесение символов из текстового файла в стек для текста
	while (fscanf(input, "%c", text_stack) != EOF)
	{
		// Алгоритм проверки скобок
		for (int i = 0; i < strlen(text_stack); i++)
		{
			switch (text_stack[i]) 
			{
			case '(':
				for (int right = strlen(array); right >= strlen(array) - 1; right--)
					array[right] = text_stack[i];
				break;
			case '[':
				for (int right = strlen(array); right >= strlen(array) - 1; right--)
					array[right] = text_stack[i];
				break;
			case '{':
				for (int right = strlen(array); right >= strlen(array) - 1; right--)
					array[right] = text_stack[i];
				break;

			case ')':
				for (int left = strlen(array) - 1; left < strlen(array); left++)
					if (array[strlen(array) - 1] == '(')
						array[left] = array[left + 1];
				break;
			case ']':
				for (int left = strlen(array) - 1; left < strlen(array); left++)
					if (array[strlen(array) - 1] == '[')
						array[left] = array[left + 1];
				break;
			case '}':
				for (int left = strlen(array) - 1; left < strlen(array); left++)
					if (array[strlen(array) - 1] == '{')
						array[left] = array[left + 1];
				break;
			}
		}
	}

	
	/*if (strlen(stack) == strlen(start))
	{
		printf("RIGHT\n");
	}
	else
	{
		printf("WRONG\n");
	}
	*/
	
	
	// сравнение количества элементов стека с количеством, которое было при его создании
	output = fopen("output.txt", "w");

	if (strlen(array) == strlen(start_stack))
	{
		fprintf(output, "Right\n");
	}

	else
	{
		fprintf(output, "Wrong\n");
	}
	
	// закрытие файлов и освобождение памяти
	
	fclose(input);
	fclose(output);

	free(array);
	free(start_stack);

	return 0;
}

