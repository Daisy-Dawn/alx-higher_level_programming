#include <stdio.h>
#include <Python.h>
#include <listobject.h>
#include <object.h>

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyListObject *list = (PyListObject *)p;

    size = Py_SIZE(list);

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %zd: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
