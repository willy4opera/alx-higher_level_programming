#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
	int d_size, allocat, num;
	PyObject *objec;

	d_size = Py_SIZE(p);
	allocat = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", d_size);
	printf("[*] Allocated = %d\n", allocat);

	for (num = 0; num < d_size; num++)
	{
		printf("Element %d: ", num);

		objec = PyList_GetItem(p, num);
		printf("%s\n", Py_TYPE(objec)->tp_name);
	}
}
