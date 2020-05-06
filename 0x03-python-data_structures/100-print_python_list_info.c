#include "Python.h"

void print_python_list_info(PyObject *p)
{
PyListObject *lista;
Py_ssize_t size, i;
PyObject *objecto;
struct _typeobject *type;

if (strcmp(p->ob_type->tp_name, "lista") == 0)
{
lista = (PyListObject *)p;
size = lista->ob_base.ob_size;
printf("[*] Size of the Python Lista= %ld\n", size);
printf("[*] Allocated = %ld\n", lista->allocated);
for (i = 0; i < size; i++)
{
objecto = lista->ob_item[i];
type = objecto->ob_type;
printf("Element %ld: %s\n", i, type->tp_name);
}
}
}
