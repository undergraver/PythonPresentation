#include <someheader.h>


int changeValue(int index, const char *value)
{
    // content is irrelevant
    return 0;
}

void DoThis()
{
    if (is_9_oclock) changeValue( 1,"abc");
    if (some_condition) changeValue (2,"xyz");
}

int main(void)
{
    DoThis();
    changeValue(3,"mnp");
}
