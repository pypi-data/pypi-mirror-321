#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include <algorithm>
using namespace std;
namespace math
{
	PyObject* max(PyObject* self, PyObject* args)
	{
		double x, y;
		if (!PyArg_ParseTuple(args, "dd", &x, &y))
		{
			return nullptr;
		}
		return PyFloat_FromDouble(::max(x, y));
	}
	PyObject* min(PyObject* self, PyObject* args)
	{
		double x, y;
		if (!PyArg_ParseTuple(args, "dd", &x, &y))
		{
			return nullptr;
		}
		return PyFloat_FromDouble(::min(x, y));
	}
}
static PyMethodDef functional_methods[] = {
	{ "max", (PyCFunction)math::max, METH_VARARGS, nullptr },
	{ "min", (PyCFunction)math::min, METH_VARARGS, nullptr },
	{ nullptr, nullptr, 0, nullptr }
};
static PyModuleDef functional_module = {
	PyModuleDef_HEAD_INIT,
	"functional",
	nullptr,
	0,
	functional_methods
};
PyMODINIT_FUNC PyInit_functional()
{
	return PyModule_Create(&functional_module);
}

