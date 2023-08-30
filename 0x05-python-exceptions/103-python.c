#include <Python.h>
#include <stdio.h>
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t sze = 0, num = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sze = PyBytes_Size(p);
	printf("  size: %zd\n", sze);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", sze < 10 ? sze + 1 : 10);
	while (num < sze + 1 && num < 10)
	{
		printf(" %02hhx", string[num]);
		num++;
	}
	printf("\n");
}
/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t sze = 0;
	PyObject *item;
	int num = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		sze = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", sze);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (num < sze)
		{
			item = PyList_GET_ITEM(p, num);
			printf("Element %d: %s\n", num, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			num++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
}
/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  val: %s\n", string);
}
