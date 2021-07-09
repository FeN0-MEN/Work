#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

struct aeroflot {

    char name[60];
    char number[60];
    char type[20];
};

int complare(void const* a, void const* b) {

    struct aeroflot* airplaneA = (struct aeroflot*)a;
    struct aeroflot* airplaneB = (struct aeroflot*)b;

    return strcmp(airplaneA->name, airplaneB->name);
}

int main(void) 
{
    SetConsoleCP(1251);
    SetConsoleOutputCP(1251);
    char c, com[20];
    int counter = 0, check = 0, z = 0;

    struct aeroflot d[7];
    for (int s = 0; s < 7; s++) {

        printf("Enter name, number and type of airplane: "); 
        scanf("%s %s %s[^\n]", d[s].name, d[s].number, d[s].type);
        counter++;
        if (s != 6) { printf("You want to continue? y/n: "); 
        scanf("%s", &c); }
        if (c == 'n') { s = 7; break; }
    }

    qsort(d, counter, sizeof(struct aeroflot), complare);

    for (int i = 0; i < counter; i++) printf("%s %s %s \n", d[i].name, d[i].number, d[i].type);

    printf("Input type of airplane to know its name of city and his number race. Or print exit to end: ");
    while (1)
    {
        scanf("%s", com);
        if (strcmp("exit", com) == 0) 
            return 0;
        for (int i = 0; i < counter; i++) {

            if (strcmp(d[i].type, com) == 0)
            {
                printf("%s \n", d[i].name); 
                printf("%s \n", d[i].number);
            }
            else { z++; }
        }
        if (counter == z) printf("Unknown type of airplane \n");
    }

}
