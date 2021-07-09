#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

	struct aeroflot
	{
	char name[100];
	char number;
	char type[100];
	};

	struct knot
	{
	struct aeroflot flights;
	struct knot* next;
	};

	struct knot* first = NULL;
	struct knot* newElement;

	int main(void)
	{
		int i = 0, counter = 0, n = 0;
		char breaker[5] = {'\0'};
		char typeOfAirplane[100];

		printf("Enter name, number and type of airplane: \n");
		do
		{
			char AirplanesBuffer[100];
			printf("Name of airplane: ");
			scanf_s("%s", AirplanesBuffer, 100);
				
			int numberOfFlight;	
			printf("Number of flight: ");
			scanf_s("%d", &numberOfFlight);

			char str[100];
			printf("Type of airplane: ");
			scanf_s("%s", str, 100);

			printf("Do you want to continue? (Press f to stop)\n");
			scanf_s("%s", breaker, 5);

			if (first == NULL)
			{
				first = malloc(sizeof(struct knot));
	
				first -> next = NULL;

				strcpy(first -> flights.name, AirplanesBuffer);
				strcpy(first -> flights.type, str);
				first -> flights.number = numberOfFlight;
				continue;
			}

			newElement = malloc(sizeof(struct knot));
			strcpy(newElement -> flights.name, AirplanesBuffer);
			strcpy(newElement -> flights.type, str);
			newElement -> flights.number = numberOfFlight;

			struct knot* current;
			current = first;

			if (strcmp(first -> flights.name, newElement -> flights.name) > 0)
			{
				newElement -> next = first;
				first = newElement;
			}

			else
			{
				while (current -> next != NULL && strcmp(current -> next -> flights.name, newElement -> flights.name) < 0) current = current -> next;
				newElement -> next = current -> next;
				current -> next = newElement;
			}

	} while (strcmp(breaker, "f"));

		struct knot* tmp = first;

		printf("Input type of airplane to know its name of city and his number race. Or print exit to end: \n");
		scanf_s("%s", typeOfAirplane, 100);
 
		while (tmp != NULL)
		{
			if (strcmp(typeOfAirplane, tmp -> flights.type) == 0)
			{
				n++;
				printf("%s\n", tmp -> flights.name);
				printf("%d\n", tmp -> flights.number);
			}

			if (n == 0) printf("Unknown type of airplane \n");
			tmp = tmp -> next;
		}

		while (first != NULL)
		{
			struct knot* mnp = first;
			first = first -> next;
			free(mnp);
		}

		newElement = NULL;

		return 0;


	/*struct node* mnp = first;
	while (mnp != NULL)
	{
		printf("%s\n", mnp->flightData.name);
		mnp = mnp->next;
	}
	*/
}